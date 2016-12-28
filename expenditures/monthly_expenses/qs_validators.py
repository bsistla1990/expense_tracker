from .models import *

def validate_qs(model, *args):
    if model is None or args is None:
        raise Exception

