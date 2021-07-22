import json
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base


def get_postgres_instance(username=None, password=None, url=None, dbname=None):
    with open("parameters.json") as file:
        data = json.load(file)
    if username == None:
        username = data["postgres_user"]
    if password == None:
        password = data["postgres_pw"]
    if url == None:
        url = data["postgres_url"]
    if dbname == None:
        dbname = data["postgres_db"]
    database = PostgersqlDBManagement(
        username=username, password=password, url=url, dbname=dbname)
    return database


class DBManagement:
    def __condition_filter_to_string(self, filter):
        filter = {k: v for k, v in filter.items() if v[0] != ''}
        if "_" in filter:
            del filter["_"]
        if filter != {}:
            query_string = f""
            conditions = []
            if "tablename" in filter:
                conditions.append(
                    f"tablename in {str(filter['tablename']).replace('[','(').replace(']',')')}")
            if "batchname" in filter:
                conditions.append(
                    f"batch_inspectionid in (select batch_inspectionid from batchview where batchname IN {str(filter['batchname']).replace('[','(').replace(']',')')})")

            if "to_datetime_offset" not in filter:
                if "to_date" in filter or "to_time" in filter:
                    conditions.append(
                        f"timestamp < '{filter['to_date'][0] if 'to_date' in filter else ''} {filter['to_time'][0] if 'to_time' in filter else ''}'")
            elif "to_datetime_offset" in filter:
                conditions.append(
                    f"timestamp < (SELECT '{filter['to_date'][0] if 'to_date' in filter else ''}" +
                    f"{filter['to_time'][0] if 'to_time' in filter else ''} {'NOW()' if 'to_date' not in filter and 'to_time' not in filter else ''}::timestamp" +
                    f"+ interval '{filter['from_datetime_offset'][0]}')::text")

            if "from_datetime_offset" not in filter:
                if "from_date" in filter or "from_time" in filter:
                    conditions.append(
                        f"timestamp > '{filter['from_date'][0] if 'from_date' in filter else ''} {filter['from_time'][0] if 'from_time' in filter else ''}'")
            elif "from_datetime_offset" in filter:
                conditions.append(
                    f"""timestamp > (SELECT {"'" if 'from_date' in filter or 'from_time' in filter else ''}
                    {filter['from_date'][0] if 'from_date' in filter else ''} {filter['from_time'][0] if 'from_time' in filter else ''}
                    {"'" if 'from_date' in filter or 'from_time' in filter else ''}
                    {'NOW()' if 'from_date' not in filter and 'from_time' not in filter else ''}::timestamp
                    + interval '{filter['from_datetime_offset'][0]}')::text""")

            if "to_datetime_offset" not in filter:
                if "to_date" in filter or "to_time" in filter:
                    conditions.append(
                        f"timestamp < '{filter['to_date'][0] if 'to_date' in filter else ''} {filter['to_time'][0] if 'to_time' in filter else ''}'")
            elif "to_datetime_offset" in filter:
                conditions.append(
                    f"""timestamp < (SELECT {"'" if 'to_date' in filter or 'to_time' in filter else ''}
                    {filter['to_date'][0] if 'to_date' in filter else ''} {filter['to_time'][0] if 'to_time' in filter else ''}
                    {"'" if 'to_date' in filter or 'to_time' in filter else ''}
                    {'NOW()' if 'to_date' not in filter and 'to_time' not in filter else ''}::timestamp
                    + interval '{filter['to_datetime_offset'][0]}')::text""")

            if len(conditions) > 0:
                query_string += " Where "
                query_string += " AND ".join(conditions)
            return query_string
        return ""

    def get_table_names(self):
        return sorted(self.metadata.tables.keys())

    def get_view_names(self):
        return sorted([r for r, in self.engine.execute(
            "select viewname from pg_catalog.pg_views where schemaname NOT IN ('pg_catalog', 'information_schema')order by schemaname, viewname;")])

    def get_table_columns(self, table_name):
        return sorted(self.engine.execute(f"SELECT * FROM {table_name} LIMIT 0").keys())

    def get_table_column_values(self, table_name, column_name, filter=None):
        if filter != None:
            filter = dict(filter)
            if "_" in filter:
                del filter["_"]
            if filter != {}:
                return [r for r, in self.engine.execute(f"SELECT {column_name} from {table_name} {self.__condition_filter_to_string(filter)} GROUP BY {column_name}")]
        return [r for r, in self.engine.execute(f"SELECT {column_name} from {table_name} GROUP BY {column_name}")]

    def get_table(self, table_name, filter=None):
        if filter != None:
            filter = dict(filter)
            if "_" in filter:
                del filter["_"]
            if filter != {}:
                query_string = f"SELECT * FROM {table_name} " + \
                    self.__condition_filter_to_string(filter)
                return self.engine.execute(query_string)
        return self.engine.execute(f"SELECT * FROM {table_name}")

    def delete_vision(self, filter):
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

    def delet_view_template(self, id):
        if self.engine.execute(f"DELETE FROM viewfilter WHERE id = {id}").rowcount > 0:
            return True
        else:
            return False


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
