from sqlalchemy import create_engine, MetaData

engine = create_engine("postgresql://postgres:postgres@sistemas-distribuidos-db.ctenle4v3yjy.us-east-1.rds.amazonaws.com:5432/initial_db")

meta = MetaData()

conn = engine.connect()