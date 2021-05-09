FROM python

COPY src /www/app 

WORKDIR /www/app

RUN pip3 install pyTelegramBotAPI

CMD ["python3", "-u", "main.py"]