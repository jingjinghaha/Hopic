
WTF_CSRF_ENABLED = True
SECRET_KEY = 'web-information-retrieval-and-data-mining'

import os
basedir = os.path.abspath(os.path.dirname(__file__))
WHOOSH_BASE = os.path.join(basedir, 'search.db')
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
