from x_com.db_query import send_query_fetchone


def unique_ship_shapes():

    # Get number of unique shapes where shape entry is non-null.
    unique_shapes_query = "SELECT COUNT(*) FROM (SELECT DISTINCT shape FROM ufo_data) AS temp WHERE shape <> '';"
    result = send_query_fetchone(unique_shapes_query)
    unique_shapes = result[0]

    return { "count" : unique_shapes }