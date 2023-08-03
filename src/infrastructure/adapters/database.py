import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Connection, RootTransaction, create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

db = SQLAlchemy()

engine = create_engine(
    os.environ.get('DATABASE_URL', 'sqlite:///dev_database.sqlite'), echo=True
)

Base = declarative_base()


def init_app(app: Flask) -> None:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'DATABASE_URL', 'sqlite:///dev_database.sqlite'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)


connection: Connection = engine.connect()
transaction: RootTransaction = connection.begin()

Session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=connection)
)
