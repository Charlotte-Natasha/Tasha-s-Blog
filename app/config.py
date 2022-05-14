class Config:
    """"""
    pass

class ProdConfig(Config):
    """"""
    
class DevConfig(Config):
    DEBUG = True

config_options = {
    'prod':ProdConfig, 
    'dev':DevConfig
}    