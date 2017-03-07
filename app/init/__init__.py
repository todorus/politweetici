from flask import Flask

api = Flask("politweetici")


@api.errorhandler(401)
def custom_401(error):
    return('', 401)
