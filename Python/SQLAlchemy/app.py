from flask import Flask, jsonify, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQL_DATABASE_URL'] = r"empdb.db"

