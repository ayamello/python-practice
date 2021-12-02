from flask import Flask
from environs import Env

env = Env()
env.read_env()

def init_app(app: Flask):
    app.config['SQLALCHEMY_DATABASE_URI'] = env('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
