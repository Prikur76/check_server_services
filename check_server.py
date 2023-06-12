import logging
import subprocess
import time
import textwrap as tw

from telegram import Bot

import settings

logger = logging.getLogger(__name__)

bot = Bot(token=settings.TG_BOT_TOKEN)


def is_server_up(service_name):
    """
    Возвращает вывод статуса сервиса сервера в случае, если сервис в состоянии "active".
    """
    process = subprocess.run(['systemctl', 'status', service_name],
                             stdout=subprocess.PIPE)
    output = process.stdout.decode('utf-8')
    return 'Active: active (running)' in output


def check_server():
    """
    Возвращает в бот сообщение об остановке сервисов или
    об ошибках данного бота
    """
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(funcName)s: %(message)s',
        level=logging.INFO
    )

    services = settings.SERVICES
    chat_id = settings.SUPPORT_CHAT_ID
    cloud = settings.CLOUD
    server = settings.SERVER_NAME

    try:
        for service_name in services:
            if not is_server_up(service_name):
                message = """\
                🔔🔔🔔
                Check server %s (%s): service %s is down 👎. 
                Please take action!
                """ % (server, cloud, services[service_name])
                bot.send_message(chat_id=chat_id, text=tw.dedent(message))
    except Exception as e:
        logger.exception(e)
        bot.send_message(chat_id=chat_id, text=str(e))


if __name__ == '__main__':
    while True:
        check_server()
        time.sleep(300)
