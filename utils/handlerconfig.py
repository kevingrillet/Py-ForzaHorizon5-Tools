from configparser import SafeConfigParser


class HandlerConfig:
    path: str = None
    config: SafeConfigParser = None

    def __init__(self, path: str = None):
        self.config = SafeConfigParser()
        self.set_path(path)

    def get_value(self, key: str = None, default: str = None, section: str = "main") -> str:
        if section and key:
            return self.config.get(section, key, fallback=default)
        else:
            raise NameError("Missing parameter")

    def set_path(self, path: str = None):
        self.path = path
        if path:
            self.config.read(self.path)
            if not self.config.has_section("main"):
                self.config.add_section("main")
        else:
            raise NameError("Missing path")

    def set_value(self, key: str = None, value: str = None, section: str = "main"):
        if section and key and value:
            self.config.set(section, key, value)
            self.config.write(open(self.path, 'w'))
        else:
            raise NameError("Missing parameter")
