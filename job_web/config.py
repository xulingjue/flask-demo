
class BaseConfig(object):
    SECRET_KEY = 'makesure to set a very secret key'
    JOB_INDEX_PER_PAGE = 18
    COMPANY_INDEX_PER_PAGE = 20
    COMPANY_DETAIL_PER_PAGE = 10
    LIST_PER_PAGE = 15


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:12345678@localhost:3306/flask_demo?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    pass


configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
