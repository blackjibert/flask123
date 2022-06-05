

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'
    SECRET_KEY = 'ADFHADFIU'


class ProductionConfig(BaseConfig):
    DATABASE_URI = 'mysql://user@pro/foo'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    DATABASE_URI = 'mysql://user@dev/foo'


class TestingConfig(BaseConfig):
    TESTING = True
    DATABASE_URI = 'mysql://user@test/foo'