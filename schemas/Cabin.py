from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, Boolean, String
from config.db import meta, engine

cabin = Table("cabins", meta,
               Column("id", Integer, primary_key=True),
                Column("image", String(255)), 
                Column("available", Boolean), 
                Column("description", String(255)))

meta.create_all(engine)