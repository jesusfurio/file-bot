![alt text](https://fwhibbit.es/wp-content/uploads/2018/04/botfather-900x444.jpg) 

# File Bot
Bot de Telegram para descargar ficheros del servidor donde estemos ejecutándolo.

/!\ La versión final es la del fichero "filebotv2.py". El fichero "filebotv1.py" es una versión antigua que dejo disponible para su descarga.

### Pre-requisitos 📋
* Es necesario realizar la instalación de la librería pyTelegramBotAPI con:
```
pip install pyTelegramBotAPI
```

* Tendrás que crear un bot con BotFather. A través del siguiente enlace puedes ver las instrucciones para crearlo:
https://planetachatbot.com/c%C3%B3mo-crear-un-bot-para-telegram-y-darle-funcionalidad-c5c7ec833f49

Cuando lo tengas creado, deberás modificar la variable "token" del código con el que te ha facilitado Bot Father al crear el bot.

* Por último, en la variable "folder" deberás indicar la ruta donde se encontrarán los ficheros que quieras descargar.

## Despliegue 📦
Para hacerlo funcionar, únicamente deberás ejecutar:
```
python3 filebotv2.py
```
Próximamente se incluirá un Dockerfile para hacerlo correr en un contenedor y añadir más seguridad. De esta manera aislaremos completamente el acceso a los ficheros.

## Construido con 🛠️
Librerías Python usadas:
* [pyTelegramBotAPI]: https://github.com/eternnoir/pyTelegramBotAPI - Usada para crear el bot.
* [os]: https://docs.python.org/3/library/os.html - Usada para acceder a los ficheros del servidor.