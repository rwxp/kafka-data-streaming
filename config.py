from dotenv import load_dotenv
import os

# Cargar las variables del archivo .env
load_dotenv()

# Leer las variables de entorno
API_KEY = os.getenv('API_KEY')
ENDPOINT_SCHEMA_URL = os.getenv('ENDPOINT_SCHEMA_URL')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')
BOOTSTRAP_SERVER = os.getenv('BOOTSTRAP_SERVER')
SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL')
SSL_MECHANISM = os.getenv('SSL_MECHANISM')
SCHEMA_REGISTRY_API_KEY = os.getenv('SCHEMA_REGISTRY_API_KEY')
SCHEMA_REGISTRY_API_SECRET = os.getenv('SCHEMA_REGISTRY_API_SECRET')


def config_values():
    return (
        API_KEY,
        ENDPOINT_SCHEMA_URL,
        API_SECRET_KEY,
        BOOTSTRAP_SERVER,
        SECURITY_PROTOCOL,
        SSL_MECHANISM,
        SCHEMA_REGISTRY_API_KEY,
        SCHEMA_REGISTRY_API_SECRET
    )
