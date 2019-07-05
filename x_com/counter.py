from x_com.db_query import send_query_fetchone


def count_rows_in_table():

    count_command = 'SELECT COUNT(*) from ufo_data'
    result = send_query_fetchone(count_command)
    number_of_rows = result[0]

    return { "count" : number_of_rows }
