from flask import Flask, request, render_template, url_for, redirect, flash, jsonify
from models import db, connect_db, Pet

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://ronaldlopez:123456@localhost:5432/adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "secret"

connect_db(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
