from math import radians, cos, sin, asin, sqrt

# Courtesy of  https://stackoverflow.com/a/4913653
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

import psycopg2
from x_com.db_config import config

def closest_to_area_52():

    area_52_lat = 46.5476
    area_52_long = -87.3956

    def distance_to_a_52(lat,long):
        return haversine(long, lat, area_52_long, area_52_lat)

    conn = None
    closest_to_area_52 = None

    try:
        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        select_and_sort_query = """
                            SELECT
                              *,
                              ST_Distance(
                                ST_MakePoint(latitude, longitude),
                                ST_MakePoint(46.5476, -87.3956)
                              ) AS distance
                            FROM
                              ufo_Data
                            ORDER BY
                              distance ASC;
                            """
        cur.execute(select_and_sort_query)

        closest_to_area_52 = [ cur.fetchone() for _ in range(3) ]

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
    formatted_top_entries = [format_row_data(row) for row in closest_to_area_52]

    return {"sightings":formatted_top_entries}
