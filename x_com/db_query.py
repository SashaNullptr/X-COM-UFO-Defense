import psycopg2

def send_query_no_results(query):

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

def send_query(query):

    conn = None
    result = None

    try:
        params = config(DB_CONFIG)
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
