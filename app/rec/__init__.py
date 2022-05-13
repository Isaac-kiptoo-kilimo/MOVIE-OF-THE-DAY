from flask import Blueprint
rec = Blueprint('rec',__name__)
from . import views,errors,forms
