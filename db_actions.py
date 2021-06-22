import json
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base


def get_postgres_instance():
    with open("parameters.json") as file:
        data = json.load(file)
        database = PostgersqlDBManagement(username=data["postgres_user"], password=data["postgres_pw"],
                                          url=data["postgres_url"], dbname=data["postgres_db"])
    return database


class DBManagement:
    def __condition_filter_to_string(self, filter):
        if "_" in filter:
            del filter["_"]
        if filter != {}:
            query_string = f""
            conditions = []
            if "batchid" in filter:
                conditions.append(
                    f"batch_inspectionid in (select batch_inspectionid from batchview where batchid IN {str(filter['batchid']).replace('[','(').replace(']',')')})")
            if "interval" in filter:
                if "from_datetime" in filter:
                    del filter["from_datetime"]
                if "to_datetime" in filter:
                    del filter["to_datetime"]
                conditions.append(
                    f"timestamp > (SELECT NOW() - interval '{filter['interval'][0]}')::text")

            if "from_datetime" in filter:
                conditions.append(
                    f"timestamp > '{filter['from_datetime'].replace('T', ' ')}'")
            if "to_datetime" in filter:
                conditions.append(
                    f"timestamp < '{filter['to_datetime'].replace('T', ' ')}'")
            if len(conditions) > 0:
                query_string += " Where "
                query_string += " AND ".join(conditions)
            return query_string
        return ""

    def get_table_names(self):
        return self.metadata.tables.keys()

    def get_view_names(self):
        return [r for r, in self.engine.execute(
            "select viewname from pg_catalog.pg_views where schemaname NOT IN ('pg_catalog', 'information_schema')order by schemaname, viewname;")]

    def get_table_columns(self, table_name):
        return self.engine.execute(f"SELECT * FROM {table_name} LIMIT 0").keys()

    def get_table_column_values(self, table_name, column_name, filter=None):
        filter = dict(filter)
        if "_" in filter:
            del filter["_"]
        if filter != {}:
            return [r for r, in self.engine.execute(f"SELECT {column_name} from {table_name} {self.__condition_filter_to_string(filter)} GROUP BY {column_name}")]
        if filter == {}:
            return [r for r, in self.engine.execute(f"SELECT {column_name} from {table_name} GROUP BY {column_name}")]

    def get_table(self, table_name, filter=None):
        filter = dict(filter)
        if "_" in filter:
            del filter["_"]
        if filter != {}:
            query_string = f"SELECT * FROM {table_name} " + \
                self.__condition_filter_to_string(filter)
            return self.engine.execute(query_string)
        if filter == {}:
            return self.engine.execute(f"SELECT * FROM {table_name}")

    def delete(self, filter):
        triggerheader_ids = self.get_table_column_values(
            "trigger_image_links", "headerid", filter)
        batchheader_ids = self.get_table_column_values(
            "batch", "headerid", filter)
        trigger_delete = self.engine.execute(
            f"DELETE FROM trigger_image_links {self.__condition_filter_to_string(filter)}")
        batch_delete = self.engine.execute(
            f"DELETE FROM batch {self.__condition_filter_to_string(filter)}")
        new_trigger_header_ids = self.get_table_column_values(
            "trigger_image_links", "headerid", filter)
        new_batch_header_ids = self.get_table_column_values(
            "batch", "headerid", filter)
        for id in triggerheader_ids:
            if id in new_trigger_header_ids:
                triggerheader_ids.remove(id)
        for id in batchheader_ids:
            if id in new_batch_header_ids:
                triggerheader_ids.remove(id)
        if len(triggerheader_ids) > 0:
            self.engine.execute(
                f"DELETE FROM triggerheader WHERE id in {str(triggerheader_ids).replace('[','(').replace(']',')')}")
        if len(batchheader_ids) > 0:
            self.engine.execute(
                f"DELETE FROM batchheader WHERE id in {str(batchheader_ids).replace('[','(').replace(']',')')}")
        return {"batch": batch_delete.rowcount, "trigger_image_links": trigger_delete.rowcount}


class PostgersqlDBManagement(DBManagement):
    def __init__(self, username, password, url, dbname):
        self.engine = create_engine(
            f'postgresql+psycopg2://{username}:{password}@{url}/{dbname}')
        self.metadata = MetaData()
        self.metadata.reflect(self.engine)
        self.Base = automap_base(metadata=self.metadata)
        self.Base.prepare()


class SQLiteDBManagement(DBManagement):
    def __init__(self, path_to_sqlite_db):
        self.engine = create_engine(f"sqlite+pysqlite:///{path_to_sqlite_db}")
        self.metadata = MetaData()
        self.metadata.reflect(self.engine)
        self.Base = automap_base(metadata=self.metadata)
        self.Base.prepare()
