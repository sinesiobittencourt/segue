from datetime import timedelta

DEBUG = True
TESTING = False

SQLALCHEMY_POOL_SIZE = None
SQLALCHEMY_POOL_TIMEOUT = None
SQLALCHEMY_POOL_RECYCLE = None
SQLALCHEMY_DATABASE_URI = 'postgresql://segue:segue@localhost/segue'


JWT_SECRET_KEY = 'sshh'
JWT_DEFAULT_REALM = 'Login Required'
JWT_AUTH_URL_RULE = None
JWT_AUTH_ENDPOINT = None
JWT_ALGORITHM     = 'HS256'
JWT_VERIFY        = True
JWT_LEEWAY        = 0
JWT_VERIFY_EXPIRATION =  True
JWT_EXPIRATION_DELTA = timedelta(days=30)

CORS_HEADERS = 'Content-Type,Authorization'

MAIL_SERVER = 'localhost'
MAIL_PORT   = 1025
MAIL_DEFAULT_SENDER = 'teste@softwarelivre.org'
