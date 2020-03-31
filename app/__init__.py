from config import Config
from app import models
import logging

## logging configuration

FORMAT = '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
logging.basicConfig(format=FORMAT, level='DEBUG')



