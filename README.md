# TELEGRAM BOT FOR CHECK MY SERVERS

Телеграм бот для проверки состояния запущенных сервисов на сервере.

## Как работает

Скрипт запускается на сервере, проверяет статус сервисов в systemctl. 
В случае, если сервис не запущен, то отправляет сообщение пользователю в служебный бот. 

## Зависимости
Должен быть установлен `python`.\
Установите зависимости командой **`python -r requirements.txt`**.\
Для запуска скрипта создайте файл .env в корневой директории проекта 
и запишите содержимое в формате `КЛЮЧ=ЗНАЧЕНИЕ`:

```
TG_BOT_TOKEN=<TOKEN-YOUR-BOT>
SUPPORT_CHAT_ID=<ID-YOUR-CHAT>
CLOUD=<NAME-YOUR-CLOUD>
SERVER_NAME=<NAME-YOUR-SERVER>
```

## Как запустить
Для запуска скрипта введите следующие команды:
TODO


## Лицензия
TODO

## Цели проекта.
Проект создан в познавательных целях.