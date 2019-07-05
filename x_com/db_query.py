import psycopg2
from x_com.db_config import config


def send_query_fetchone_no_results(query):

    conn = None

    try:
        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        cur.execute(query)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def send_query_fetchone(query):

    conn = None
    result = None

    try:
        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        cur.execute(query)
        result = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return result
