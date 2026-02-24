import configparser
import os

class ConfigReader:

    config = configparser.ConfigParser()

    # Get absolute path to config.ini
    config_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "config",
        "config.ini"
    )

    config.read(config_path)

    @classmethod
    def get_base_url(cls):
        return cls.config.get("DEFAULT", "base_url")

    @classmethod
    def get_browser(cls):
        return cls.config.get("DEFAULT", "browser")

    @classmethod
    def get_implicit_wait(cls):
        return cls.config.getint("DEFAULT", "implicit_wait")

    @classmethod
    def get_explicit_wait(cls):
        return cls.config.getint("DEFAULT", "explicit_wait")

    @classmethod
    def get_test_data_path(cls):
        return cls.config.get("DEFAULT", "test_data_path")

    @classmethod
    def get_customer_info_url(cls):
        return cls.config.get("DEFAULT", "customer_info_url")

