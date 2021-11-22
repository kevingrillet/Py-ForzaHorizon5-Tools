from configparser import SafeConfigParser


class HandlerConfig:
    path: str = None
    config: SafeConfigParser = SafeConfigParser()

    def __init__(self, path: str):
        """
        Create handler and read config from path
        :param path:
        """
        self.set_path(path)

    def get_value(self, key: str = None, default: str = None, section: str = "main") -> str:
        """
        Get value from config
        :param key:
        :param default:
        :param section:
        :return:
        """
        if not self.config:
            raise NameError("No config file loaded")
        if not (section and key):
            raise NameError("Missing parameter")
        return self.config.get(section, key, fallback=default)

    def set_path(self, path: str = None):
        """
        Set path to config and load it in self.config
        :param path:
        """
        self.path = path
        if not path:
            raise NameError("Missing path")
        self.config.read(self.path)
        if not self.config.has_section("main"):
            self.config.add_section("main")

    def set_value(self, key: str = None, value: str = None, section: str = "main"):
        """
        Set value and save config.ini
        :param key:
        :param value:
        :param section:
        """
        if not (section and key and value):
            raise NameError("Missing parameter")
        self.config.set(section, key, value)
        self.config.write(open(self.path, 'w'))
