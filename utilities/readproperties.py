import configparser

config=configparser.RawConfigParser()
config.read("C:\\Users\\Hp\\PycharmProjects\\NopCpmmerceApp\\configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getBaseUrl():
        url=config.get("common info","base_url")
        return url

    @staticmethod
    def getusername():
        name=config.get("common info", "user")
        return name

    @staticmethod
    def getPassword():
        passw= config.get("common info", "password")
        return passw