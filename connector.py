import pymysql
import psycopg2

from config import load_conf


class Connector(object):
    def __init__(self):
        self._conn = None
        self._cur = None

        self.connect()
        self.close()

    def connect(self):

        conf = load_conf()
        host = conf["host"]
        port = conf["port"]
        user = conf["user"]
        passwd = conf["password"]
        db = conf["database"]

        self._conn = psycopg2.connect(host=host, port=port, user=user,
                                      password=passwd, database=db)
        self._cur = self._conn.cursor()

    def execute(self, sql):
        try:
            self._cur.execute(sql)
            self._conn.commit()
        except Exception as e:
            print('Exception: %s' % e)

    def commit(self):
        self._conn.commit()

    def close(self):
        self._cur.close()
        self._conn.close()

    def cursor(self):
        return self._cur

    def commit(self):
        self._conn.commit()

    def close(self):
        self._cur.close()
        self._conn.close()

    def cursor(self):
        return self._cur


class Connector_sql(object):
    def __init__(self):
        self._conn = None
        self._cur = None

        self.connect()
        self.close()

    def connect(self):

        conf = load_conf()
        host = conf["host_sql"]
        port = conf["port_sql"]
        user = conf["user_sql"]
        passwd = conf["password_sql"]
        db = conf["database_sql"]

        self._conn = pymysql.connect(host=host, port=port, user=user,
                                     password=passwd, database=db)
        self._cur = self._conn.cursor()

    def execute(self, sql):
        try:
            self._cur.execute(sql)
            self._conn.commit()
        except Exception as e:
            print('Exception: %s' % e)

    def commit(self):
        self._conn.commit()

    def close(self):
        self._cur.close()
        self._conn.close()

    def cursor(self):
        return self._cur