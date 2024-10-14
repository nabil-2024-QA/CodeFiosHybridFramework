# read data fron ini file
import configparser

config = configparser.RawConfigParser()
config.read('./Configuration/config.ini')

class read_config():
    @staticmethod
    def get_base_url():
         url = config.get('common info', 'base_url')
         return url

    @staticmethod
    def get_username():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('common info', 'password')
        return password