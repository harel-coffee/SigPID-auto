# Overview

Neste trabalho, apresentamos a realização da reprodução dos 3 níveis de corte de permissões SigPID, implementação e avaliação dos principais métodos de aprendizagem do SigPID, utilizando um conjunto de dados publicamente disponível. Nós comparamos as permissões em cada nível de corte com as 32 permissões identificadas como mais recorrentes; as 113 do conjunto de dados público escolhido e as 22 permissões (contidas no conjunto de dados), consideradas perigosas pela Google. Nosso estudo inicial indica que o número de permissões impacta o tempo de treinamento e execução, bem como a acurácia dos modelos. Entretanto, o tempo de execução pode não ser significativo a ponto de justificar um número menor de permissões para detecção de malwares.

## Metodologia
**MLDP: Remoção Multinível de Dados**

MLDP Multi-Level Data Pruning é um método multinível (de 3 níveis) de remoção de dados cujo objetivo é reduzir o número de permissões de um conjunto de dados para o treino dos modelos de aprendizado de máquina. A ideia por trás do método é diminuir significativamente o número de permissões e, consequentemente, o tempo de execução dos modelos. O MLDP assume como ponto de corte uma taxa de acurácia de no mínimo 90%, considerada uma taxa ótima. O MLDP opera nos seguintes três níveis de corte: 
1. Classificação de permissão com taxa negativa (Permission Ranking Negative Rate ou PRNR)
2.  Classificação de permissão baseada em suporte (Support Based Permission Ranking ou SPR)
3. Mineração de permissões com regras de associação (Permission Mining with Association Rules ou PMAR )

##  Tecnologias utilizadas
- Jupyter Notebook (IPython 7.12.0, Python 3.7.6 (default, Jan 8 2020)
- Google Chrome Versão 91.0.4472.124 (Versão oficial) 64 bits
- Weka versão 3.8.5
##  Bibliotecas utilizadas
- Pandas versão 1.2.4
- Matplotlib 3.4.0
- Numpy 1.20.1
- Scikit-learn versão 0.22.1
- Apyori 1.1.2
- Mlxtend 0.19.0

## **Algoritmos de Machine Learning**
- Random forest
- Decision tree
- Support vector machines (SVM)
- Functional Trees

Os hiper-parâmetros são variáveis que controlam o próprio processo de treinamento e foram definidos como **padrão** referente a versão 0.22.1 da biblioteca Scikit-learn. Por exemplo:

|    Algoritmos  |hiper-parâmetros             |
|----------------|-----------------------------|
|Random forest   |_n_estimators=100_, _*_, _criterion='gini'_, _max_depth=None_, _min_samples_split=2_, _min_samples_leaf=1_, _min_weight_fraction_leaf=0.0_, _max_features='auto'_, _max_leaf_nodes=None_, _min_impurity_decrease=0.0_, _min_impurity_split=None_, _bootstrap=True_, _oob_score=False_, _n_jobs=None_, _random_state=None_, _verbose=0_, _warm_start=False_, _class_weight=None_, _ccp_alpha=0.0_, _max_samples=None_           |
|Decision tree         |_criterion='gini'_, _splitter='best'_, _max_depth=None_, _min_samples_split=2_, _min_samples_leaf=1_, _min_weight_fraction_leaf=0.0_, _max_features=None_, _random_state=None_, _max_leaf_nodes=None_, _min_impurity_decrease=0.0_, _min_impurity_split=None_, _class_weight=None_, _ccp_alpha=0.0_ |
|SVM|_C=1.0_, _kernel='linear'_, _degree=3_, _gamma='scale'_, _coef0=0.0_, _shrinking=True_, _probability=False_, _tol=0.001_, _cache_size=200_, _class_weight=None_, _verbose=False_, _max_iter=- 1_, _decision_function_shape='ovr'_, _break_ties=False_, _random_state=None_|

**Obs:** Functional Tree  foi implementado utilizando a proposta de [Gama-2004](https://link.springer.com/content/pdf/10.1023/B:MACH.0000027782.67192.13.pdf) utilizando a ferramenta Weka versão 3.8.5, pois não possui biblioteca em Scikit-learn.

##  Ambientes de execução
Para execução foi utilizado um notebook com processador Intel Celeron 1007U (1.5GHz, Dual Core, 2MB L2), 4GB DDR3 1.600MHz, disco rígido de 320GB (SATA - 5.400rpm), Windows 10 Home Single Language, compilação 19042.1110.

## 108 Permissões selecionadas após PRNR 
| |                             |
|:---------------------------------:|:---------------------------:|
| SEND_SMS                          | BIND_REMOTEVIEWS            |
| DELETE_CACHE_FILES                | READ_CALL_LOG               |
| WRITE_APN_SETTINGS                | READ_SOCIAL_STREAM          |
| INSTALL_PACKAGES                  | WRITE_PROFILE               |
| ACCESS_LOCATION_EXTRA_COMMANDS    | ADD_VOICEMAIL               |
| WRITE_HISTORY_BOOKMARKS           | WRITE_USER_DICTIONARY       |
| RECEIVE_SMS                       | WRITE_CALL_LOG              |
| UPDATE_DEVICE_STATS               | BIND_TEXT_SERVICE           |
| READ_SMS                          | BIND_VPN_SERVICE            |
| WRITE_SMS                         | READ_PROFILE                |
| READ_HISTORY_BOOKMARKS            | WRITE_SOCIAL_STREAM         |
| CONTROL_LOCATION_UPDATES          | AUTHENTICATE_ACCOUNTS       |
| DELETE_PACKAGES                   | NFC                         |
| RECEIVE_WAP_PUSH                  | READ_SYNC_STATS             |
| RESTART_PACKAGES                  | USE_CREDENTIALS             |
| PROCESS_OUTGOING_CALLS            | SUBSCRIBED_FEEDS_WRITE      |
| BIND_WALLPAPER                    | MANAGE_ACCOUNTS             |
| CLEAR_APP_USER_DATA               | READ_USER_DICTIONARY        |
| RECEIVE_MMS                       | CHANGE_WIFI_MULTICAST_STATE |
| READ_PHONE_STATE                  | MASTER_CLEAR                |
| SET_WALLPAPER                     | SET_TIME                    |
| HARDWARE_TEST                     | WRITE_GSERVICES             |
| CHANGE_CONFIGURATION              | DUMP                        |
| MOUNT_UNMOUNT_FILESYSTEMS         | SET_TIME_ZONE               |
| RECEIVE_BOOT_COMPLETED            | BIND_ACCESSIBILITY_SERVICE  |
| READ_LOGS                         | READ_SYNC_SETTINGS          |
| SET_PREFERRED_APPLICATIONS        | SET_PROCESS_LIMIT           |
| CALL_PHONE                        | INSTALL_LOCATION_PROVIDER   |
| ACCESS_COARSE_LOCATION            | WRITE_SYNC_SETTINGS         |
| MODIFY_PHONE_STATE                | SUBSCRIBED_FEEDS_READ       |
| DISABLE_KEYGUARD                  | BIND_INPUT_METHOD           |
| CHANGE_WIFI_STATE                 | CALL_PRIVILEGED             |
| ACCESS_FINE_LOCATION              | BROADCAST_STICKY            |
| CLEAR_APP_CACHE                   | REORDER_TASKS               |
| ACCESS_WIFI_STATE                 | SET_ACTIVITY_WATCHER        |
| WRITE_EXTERNAL_STORAGE            | MODIFY_AUDIO_SETTINGS       |
| READ_CONTACTS                     | MOUNT_FORMAT_FILESYSTEMS    |
| GET_PACKAGE_SIZE                  | RECORD_AUDIO                |
| WRITE_SECURE_SETTINGS             | BIND_APPWIDGET              |
| DEVICE_POWER                      | GET_ACCOUNTS                |
| ACCESS_NETWORK_STATE              | READ_CALENDAR               |
| WRITE_CONTACTS                    | CAMERA                      |
| CHANGE_COMPONENT_ENABLED_STATE    | ACCESS_SURFACE_FLINGER      |
| SET_WALLPAPER_HINTS               | PERSISTENT_ACTIVITY         |
| SYSTEM_ALERT_WINDOW               | BROADCAST_WAP_PUSH          |
| VIBRATE                           | REBOOT                      |
| WRITE_SETTINGS                    | WRITE_CALENDAR              |
| CHANGE_NETWORK_STATE              | GLOBAL_SEARCH               |
| WAKE_LOCK                         | BIND_DEVICE_ADMIN           |
| ACCESS_MOCK_LOCATION              | BATTERY_STATS               |
| EXPAND_STATUS_BAR                 | INTERNAL_SYSTEM_WINDOW      |
| GET_TASKS                         | BLUETOOTH                   |
| SET_ORIENTATION                   | READ_EXTERNAL_STORAGE       |
| FLASHLIGHT                        | READ_FRAME_BUFFER           |

## 30 permissões selecionadas após PRNR+SPR

|               |                        |
|------------------------|------------------------|
| ACCESS_NETWORK_STATE   | CHANGE_WIFI_STATE      |
| WRITE_EXTERNAL_STORAGE | WRITE_SETTINGS         |
| READ_PHONE_STATE       | CAMERA                 |
| WAKE_LOCK              | CALL_PHONE             |
| ACCESS_WIFI_STATE      | WRITE_SMS              |
| RECEIVE_BOOT_COMPLETED | WRITE_CONTACTS         |
| VIBRATE                | READ_EXTERNAL_STORAGE  |
| GET_ACCOUNTS           | MANAGE_ACCOUNTS        |
| ACCESS_FINE_LOCATION   | USE_CREDENTIALS        |
| ACCESS_COARSE_LOCATION | READ_HISTORY_BOOKMARKS |
| SEND_SMS               | CHANGE_NETWORK_STATE   |
| READ_CONTACTS          | RECORD_AUDIO           |
| RECEIVE_SMS            | READ_SYNC_SETTINGS     |
| READ_SMS               | RESTART_PACKAGES       |
| GET_TASKS              | BLUETOOTH              |

## 27 permissões selecionadas após PRNR+SPR+PMAR

|                        |                        |
|------------------------|------------------------|
| ACCESS_NETWORK_STATE   | CHANGE_WIFI_STATE      |
| WRITE_EXTERNAL_STORAGE | WRITE_SETTINGS         |
| READ_PHONE_STATE       | CAMERA                 |
| WAKE_LOCK              | CALL_PHONE             |
| RECEIVE_BOOT_COMPLETED | WRITE_CONTACTS         |
| VIBRATE                | READ_EXTERNAL_STORAGE  |
| GET_ACCOUNTS           | USE_CREDENTIALS        |
| ACCESS_FINE_LOCATION   | READ_HISTORY_BOOKMARKS |
| ACCESS_COARSE_LOCATION | CHANGE_NETWORK_STATE   |
| SEND_SMS               | RECORD_AUDIO           |
| READ_CONTACTS          | READ_SYNC_SETTINGS     |
| RECEIVE_SMS            | RESTART_PACKAGES       |
| READ_SMS               | BLUETOOTH              |
| GET_TASKS              |                        |

