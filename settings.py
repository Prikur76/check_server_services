from environs import Env

env = Env()
env.read_env()


TG_BOT_TOKEN = env.str('TG_BOT_TOKEN', '')
SUPPORT_CHAT_ID = env.str('SUPPORT_CHAT_ID', '')

CLOUD = env.str('CLOUD', 'MyCloud')
SERVER_NAME = env.str('SERVER_NAME', 'MyServer')

SERVICES = {
    'devman_notify_bot': 'Devman (bot)',
    'converter_pdf': 'Converter PDF',
}
