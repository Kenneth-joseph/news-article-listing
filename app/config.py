class Config:
    '''
    General configuration parent class
    '''

    # NEWS_API_KEY='a6d0d273ebbf40b4b0756970156d6f5d'
    NEWS_API_URL='https://newsapi.org/v2/everything?q={}&apiKey={}'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True