#!/usr/local/bin/python3
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    """

    TABLES

    """
    team_stats_table = """ CREATE TABLE IF NOT EXISTS team_stats (
                                    team_name    text     PRIMARY KEY,
                                    team_seed    integer,
                                    R1_Vegas_Pct real     NOT NULL,
                                    R2_Vegas_Pct real     NOT NULL,
                                    R3_Vegas_Pct real     NOT NULL,
                                    R4_Vegas_Pct real     NOT NULL,
                                    R5_Vegas_Pct real     NOT NULL,
                                    R6_Vegas_Pct real     NOT NULL,
                                    R1_Pick_Pct  real     NOT NULL,
                                    R2_Pick_Pct  real     NOT NULL,
                                    R3_Pick_Pct  real     NOT NULL,
                                    R4_Pick_Pct  real     NOT NULL,
                                    R5_Pick_Pct  real     NOT NULL,
                                    R6_Pick_Pct  real     NOT NULL
                                );"""

    conn = create_connection(r"./2019Tournament.db")

    if conn:
        create_table(conn, team_stats_table)
        conn.close()

if __name__ == '__main__':
    main()

