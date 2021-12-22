from src.config.database import db
from flask_sqlalchemy import SQLAlchemy
from injector import inject
from sqlalchemy import orm
from copy import deepcopy


class BaseRepository():

    @inject
    def __init__(self, db: SQLAlchemy):
        self._db = db
        self._model = None
        self._auto_commit = False
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._db.get_engine(),
            ),
        )
        self.session: orm.Session = self._session_factory()

    @property
    def model(self) -> db.Model:
        return self._model
    
    @model.setter
    def model(self, model: db.Model):
        self._model = model

    @property
    def auto_commit(self) -> bool:
        return self._auto_commit
    
    @auto_commit.setter
    def auto_commit(self, auto_commit):
        self._auto_commit = auto_commit

    def save(self):

        with self.session as session:
            session.add(self.model)
            session.flush()
            session.expunge_all()
            session.commit()