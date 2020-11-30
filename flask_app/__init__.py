from flask import Flask
import urllib3

# Instaniate global app variable
app = Flask(__name__)

from . import routes