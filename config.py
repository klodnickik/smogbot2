from dotenv import load_dotenv
load_dotenv()

import os

class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))

    DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')