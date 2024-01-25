import json


class AppConfig:
    _config = None

    @classmethod
    def load_config(cls, file_path):
        with open(file_path) as f:
            cls._config = json.load(f)

    @classmethod
    def get_config(cls, keys):
        config_data = cls._config
        for key in keys.split('.'):
            config_data = config_data.get(key, {})
        return config_data or None



# Загрузка конфигурации при запуске приложения
AppConfig.load_config('app_config.json')

# Получение значения конфигурации
assert AppConfig.get_config('database') == {
    'host': '127.0.0.1', 'port': 5432,
    'database_name': 'postgres_db',
    'user': 'owner',
    'password': 'ya_vorona_ya_vorona'}
assert AppConfig.get_config('database.user') == 'owner'
assert AppConfig.get_config('database.password') == 'ya_vorona_ya_vorona'
assert AppConfig.get_config('database.pass') is None
assert AppConfig.get_config('password.database') is None

config = AppConfig()
assert config.get_config('max_connections') == 10
assert config.get_config('min_connections') is None

conf = AppConfig()
assert conf.get_config('max_connections') == 10
assert conf.get_config('database.user') == 'owner'
assert conf.get_config('database.host') == '127.0.0.1'
assert conf.get_config('host') is None

print('Good')

db = {
  "database": {
    "host": "127.0.0.1",
    "port": 5432,
    "database_name": "postgres_db",
    "user": "owner",
    "password": "ya_vorona_ya_vorona"
  },
  "api_key": "hUFHu834837248jhoiHF89",
  "log_level": "debug",
  "max_connections": 10
}

