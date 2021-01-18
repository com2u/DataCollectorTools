from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base


class PostgersqlDBManagement:
    def __init__(self, username, password, url, dbname):
        self.engine = create_engine('postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=username,
                                                                                          pw=password,
                                                                                          url=url,
                                                                                          db=dbname))
        self.metadata = MetaData()
        self.metadata.reflect(self.engine)
        self.Base = automap_base(metadata=self.metadata)
        self.Base.prepare()

    def get_table_names(self):
        return self.metadata.tables.keys()

    def get_table_columns(self, table_name):
        return self.metadata.tables[table_name].columns

    def get_table(self, table_name):
        return self.engine.execute(f"SELECT * FROM {table_name}")

    def delete_array(self, table_name, column, condition):
        return self.engine.execute(f"DELETE FROM {table_name} WHERE {column} IN {str(tuple(condition))}")

    def delete_single_value(self, table_name, column, condition):
        return self.engine.execute(f"DELETE FROM {table_name} WHERE {column}='{condition}'")

    def delete(self, tablename, column, condition):
        if condition is tuple or list:
            return self.delete_array(tablename, column, condition)
        else:
            return self.delete_single_value(tablename, column, condition)


class SQLiteDBManagement(PostgersqlDBManagement):
    def __init__(self, path_to_sqlite_db):
        self.engine = create_engine(f"sqlite+pysqlite:///{path_to_sqlite_db}")
        self.metadata = MetaData()
        self.metadata.reflect(self.engine)
        self.Base = automap_base(metadata=self.metadata)
        self.Base.prepare()
