import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, sessionmaker

from src.infrastructure.adapters.database import Base


@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_db.sqlite'
    return app


@pytest.fixture
def db(app):
    db = SQLAlchemy(app)
    Base.metadata.create_all(bind=db.engine)
    yield db
    Base.metadata.drop_all(bind=db.engine)


@pytest.fixture
def session(app, db):
    with app.app_context():
        connection = db.engine.connect()
        transaction = connection.begin()
        session = scoped_session(sessionmaker(bind=connection, binds={}))
        db.session = session
        yield session
        transaction.rollback()
        connection.close()
        session.remove()
