import configparser
import configparser
config=configparser.RawConfigParser()
# config.read(".\\Configurations\\config.ini")
config.read("C:\\Users\\Srikanth Chelukala\\PycharmProjects\\PyPract1\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url
    @staticmethod
    def getAppURL(area,vname):
        app_url=config.get(area,vname)
        return app_url
    @staticmethod
    def geturl():
        app_url=config.get('applitool','app_url')
        return app_url
    @staticmethod
    def getUsername():
        usrname=config.get('common info','username')
        return usrname

    @staticmethod
    def getamznappurl():
        url=config.get('amzon','amzn_url')
        return url
    @staticmethod
    def getamznusername():
        username=config.get('amzon','amzn_username')
        return username
    @staticmethod
    def getamznpassword():
        password=config.get('amzon','amzn_password')
        return password
