import configparser

def connect():
    """Retrieves developer credentials and confirms connection to Twitter API"""
    config_obj = configparser.ConfigParser()
    config_obj.read('config.ini')

    return config_obj