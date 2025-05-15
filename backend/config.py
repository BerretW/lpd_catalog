# config.py
import json
from pathlib import Path

CONFIG_FILE = Path(__file__).parent / "config.json"

def load_config():
    if not CONFIG_FILE.exists():
        default_config = {
            "database": {
                "type": "sqlite",  # nebo "mariadb"
                "sqlite_path": "database.db",
                "mariadb": {
                    "user": "user",
                    "password": "password",
                    "host": "localhost",
                    "port": 3306,
                    "database": "security_db"
                }
            }
        }
        with open(CONFIG_FILE, "w") as f:
            json.dump(default_config, f, indent=4)
        return default_config
    else:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)

def get_database_url():
    config = load_config()
    db = config["database"]
    if db["type"] == "sqlite":
        return f"sqlite:///{db['sqlite_path']}"
    elif db["type"] == "mariadb":
        mariadb = db["mariadb"]
        return (
            f"mysql+pymysql://{mariadb['user']}:{mariadb['password']}"
            f"@{mariadb['host']}:{mariadb['port']}/{mariadb['database']}"
        )
    else:
        raise ValueError("Unsupported database type in config.json")
