from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import config


engine = create_engine(config.get_settings().database_url)
Session = sessionmaker(engine)
