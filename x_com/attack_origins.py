import psycopg2
from x_com.db_config import config

def closest_to_area_52():

    conn = None
    closest = None

    try:
        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

            area_52_lat = 46.5476
            area_52_long = -87.3956

        select_and_sort_query = """
                            SELECT
                              *,
                              ST_Distance(
                                ST_MakePoint(longitude,latitude),
                                ST_MakePoint(-87.3956,46.5476)
                              ) AS distance
                            FROM
                              ufo_Data
                            ORDER BY
                              distance ASC;
                            """
        cur.execute(select_and_sort_query)

        closest = [ cur.fetchone() for _ in range(3) ]

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    def format_row_data(row):
        return {
            'id':row[0],
            'occurred_at':row[1],
            'city':row[2],
            'state':row[3],
            'country':row[4],
            'shape':row[5],
            'duration_seconds':row[6],
            'duration_text':row[7],
            'description':row[8],
            'reported_on':row[9],
            'latitude':row[10],
            'longitude':row[11],
            'distance':row[12]
        }
    formatted_top_entries = [format_row_data(row) for row in closest]

    return {"sightings":formatted_top_entries}
