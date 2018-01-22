from configs import sqlite_settings
import sqlite3 as sql


def authorize():
    conn = sql.connect(**sqlite_settings)
    return conn


def terminate(conn):
    conn.commit()
    conn.close()
