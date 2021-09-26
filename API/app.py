import numpy as np
from flask import Flask,Blueprint, request, jsonify, render_template,flash, redirect, url_for, session, logging
import pickle
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
import os
import pandas as pd
import numpy as np
from os.path import join as join_dir
from os.path import isfile, join, isdir
from androguard.core.bytecodes.apk import APK
import shutil

app=Flask(__name__)
url='localhost:5000/apk/'
modelo= pickle.load(open('sigpid.pkl','rb'))
#print(model)
def sigpid(path):
   try:
    global lista_permissoes
    global nome
    global target_sdk_version
    global minSdkVersion
    a = APK(path)
    app = a.get_permissions()
    nome = a.get_app_name()
    target_sdk_version = a.get_effective_target_sdk_version()
    minSdkVersion = a.get_min_sdk_version()
    if path.endswith(".apk"):
        lista_permissoes = []
        for i in app:
            print(i)
            lista_permissoes.append(i)
        df_perm = pd.read_csv("DrebinDatasetPermissoes.csv")
        malapp = {i: 0 for i in df_perm.columns}
        del malapp["class"]
        for i in lista_permissoes:
            for j in malapp:
                if i == j:
                    malapp[j] = 1
        y_testapp = list(malapp.values())
        y_test = np.array([np.array(y_testapp)])
        modelo = pickle.load(open("sigpid.pkl", "rb"))
        teste = modelo.predict(y_test)
        if teste == False:
            teste = "Benigno"
        else:
            teste = "Malware"
        return teste

   except:
   	os.remove(path)
   	print("Erro no arquivo")
    
    
@app.route('/<string:name>/')
def hello(name):
    return "Hello " + name  
    
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict' ,methods=['POST'])
def predict():
   
    if request.method == 'POST':
        if 'file' not in request.files:
           return "Erro"
      
        user_file = request.files['file']
        temp = request.files['file']
        if user_file.filename == '':
            #print("Arquivo não encontrado")
            return render_template('index.html')
        if user_file.filename.endswith(".apk")==False:
            #print("Arquivo não encontrado")
            return render_template('index.html')            


        else:
            path=os.path.join(os.getcwd()+'/apk/'+user_file.filename)
            #print(contador(os.getcwd()+'/apk/Malwares/',".apk")) #Melhoria contador de Melwares
            user_file.save(path)
            result=sigpid(path)
            if result =="Malware":
                shutil.move(path, os.getcwd()+'/apk/Malwares/'+user_file.filename)
                return jsonify(result, nome, str(target_sdk_version), minSdkVersion, lista_permissoes)
            if result =="Benigno":
                shutil.move(path, os.getcwd()+'/apk/Benignos/'+user_file.filename)
                return jsonify(result, nome, str(target_sdk_version), minSdkVersion, lista_permissoes)
            
def contador(path,extension):
  list_dir = []
  list_dir = os.listdir(path)
  count = 0
  for file in list_dir:
    if file.endswith(extension): # eg: '.txt'
      count += 1
  return count

if __name__ == "__main__":
    app.run(debug=True)
