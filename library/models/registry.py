from sqlalchemy.orm import registry

table_registry = registry()

def import_models():
    __import__('library.models.book')
    __import__('library.models.romanticist')
    __import__('library.models.user')
