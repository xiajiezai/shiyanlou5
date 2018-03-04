class BaseConfig(object):
    """base class"""
    SECRET_KEY = 'make sure to set a very secret key'

class DevelopmentConfig(BaseConfig):
    """ environment configuration for development  """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@localhost:3306/simpledu?charset=utf8'


class ProductionConfig(BaseConfig):

    pass


class TestingConfig(BaseConfig):
    pass


configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}


