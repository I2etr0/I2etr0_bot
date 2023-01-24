FROM python:latest
LABEL mainteiner="yyaroslav43@gmail.com"

RUN apt update -y \
 && apt install net-tools vim -y \
 && mkdir /mnt/bot \
 && pip install telebot pyTelegramBotAPI

WORKDIR /mnt/bot

CMD ["python3", "/mnt/bot/bot.py"]