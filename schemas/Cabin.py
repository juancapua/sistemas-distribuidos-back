from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, Boolean, String
from config.db import meta, engine

cabin = Table("cabins", meta,
               Column("id", Integer, primary_key=True),
                Column("name", String(255)), 
                Column("beds", Integer), 
                Column("price", Integer))

meta.create_all(engine)