import os


VERSION = '0.0.1'

TOKEN = os.environ.get('TOKEN')
DATABASE = os.environ.get('DATABASE', 'default.db')
ENV_REF = os.environ.get('ENV_REF', 'development')
