import psycopg2
from x_com import config

def evac_priorties():

    sightings_by_city_query = "SELECT city, COUNT(*) FROM ufo_data WHERE country LIKE \'us\' GROUP BY city ORDER BY COUNT(*) DESC;"

    sightings = []

    try:
        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        cur.execute(sightings_by_city_query)

        def process_result():
            result = cur.fetchone()
            entry = {"city":result[0],"count":result[1]}
            return entry

        sightings = [ process_result() for _ in range(10) ]

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return {"sightings":sightings}