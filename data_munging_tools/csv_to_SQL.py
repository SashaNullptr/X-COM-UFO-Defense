import csv, psycopg2
import sys
import os

from x_com import send_query_no_results

def create_ufo_data_table():
    """ create tables in the PostgreSQL database"""
    # id,occurred_at,city,state,country,shape,duration_seconds,duration_text,description,reported_on,latitude,longitude
    create_table_command =
        """
        CREATE TABLE ufo_data (
            id SERIAL,
            occurred_at TIMESTAMP,
            city TEXT,
            state CHAR(2),
            country CHAR(2),
            shape TEXT,
            duration_seconds INTEGER,
            duration_text TEXT,
            reported_on DATE,
            latitude FLOAT8,
            longitude FLOAT8
        )
        """
        send_query_no_results(create_table_command)

def csv_to_SQL( csv_file ):
  with open (csv_file, 'r') as f:
    reader = csv.reader(f)
    columns = next(reader)
    query = 'insert into ufo_data({0}) values ({1})'
    query = query.format(','.join(columns), ','.join('?' * len(columns)))
    cursor = connection.cursor()
    for data in reader:
        cursor.execute(query, data)
    cursor.commit()

def main():
    create_ufo_data_table()
    data_sets_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
    csv_file_path = os.path.join(data_sets_dir,'ufo-sightnings.csv')
    csv_to_SQL(csv_file_path)

if '__main__' == __name__:
    main()
