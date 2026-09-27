import os
import yaml

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config", "config.yaml")

class ConfigReader:
    _config = None

    @classmethod
    def _load(cls):
        if cls._config is None:
            with open(CONFIG_PATH, 'r') as f:
                cls._config = yaml.safe_load(f)
        return cls._config

    @classmethod
    def get_env_config(cls):
        config = cls._load()
        env = os.getenv("ENV", config.get("environment", "qa"))
        if env not in config:
            raise ValueError(f"Environment '{env}' not found in config.yaml")
        return config[env]

    @classmethod
    def get_user(cls, user_key: str):
        config = cls._load()
        users = config.get("users", {})
        if user_key not in users:
            raise ValueError(f"user {user_key} not found in config.yaml")
        return users[user_key]

    @classmethod
    def get_base_url(cls):
        return cls.get_env_config()["base_url"]
    
    @classmethod
    def get_browser(cls):
        return cls.get_env_config().get("browser", "chrome")

    @classmethod
    def is_headless(cls):
        return cls.get_env_config().get("headless", True)

    @classmethod
    def get_implicit_wait(cls):
        return cls.get_env_config().get("implicit_wait", 5)

    @classmethod
    def get_explicit_wait(cls):
        return cls.get_env_config().get("explicit_wait", 10)