![alt text](https://fwhibbit.es/wp-content/uploads/2018/04/botfather-900x444.jpg) 

# File Bot
Bot de Telegram para descargar ficheros del servidor donde estemos ejecutándolo.

### Pre-requisitos 📋

* Tendrás que crear un bot con BotFather. A través del siguiente enlace puedes ver las instrucciones para crearlo:
https://planetachatbot.com/c%C3%B3mo-crear-un-bot-para-telegram-y-darle-funcionalidad-c5c7ec833f49

Cuando lo tengas creado, deberás guardar el token facilitado al crear el bot.

## Despliegue en VM :computer:
* En el caso de no querer usar Docker para ejecutar el bot, es necesario realizar la instalación de la librería pyTelegramBotAPI con:
```
pip install pyTelegramBotAPI
```

* Deberás declarar dos variables de entorno que serán "TOKEN" (con el contenido del token que te facilitaron al crear el bot) y "FOLDER", con la ruta completa del directorio al que queremos acceder.

* Para hacerlo funcionar, únicamente deberás ejecutar el siguiente comando dentro de la carpeta src:
```
python3 main.py
```

## Despliegue con Docker :whale:

* Primero construiremos la imagen que contendrá nuestro bot:
```
docker build -t file-bot .
```

* Después levantaremos el contenedor. Al levantar el contenedor vamos a montar una carpeta del servidor de docker, que debemos especificarlo en la parte del comando donde indica "carpeta_host". La "carpeta_contenido" será la carpeta dentro del contenedor donde tengamos los ficheros:
```
docker run -dti --env TOKEN="nuestro_token" --env FOLDER="/carpeta_contenido" -v /carpeta_host/:/carpeta_contenido --name file-bot-container file-bot 
```

## Librerías usadas :books:
Python:
* [pyTelegramBotAPI]: https://github.com/eternnoir/pyTelegramBotAPI - Usada para crear el bot.
* [os]: https://docs.python.org/3/library/os.html - Usada para acceder a los ficheros del servidor.