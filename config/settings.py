DEBUG = True

SERVER_NAME = 'mini.local:8000'
# SERVER_NAME = 'mini.local:8000'
SECRET_KEY = 'insecurekeyfordev'

# SQLAlchemy.
db_uri = 'postgresql://bookmark_app:devpassword@postgres:5432/bookmark_app'
SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False
