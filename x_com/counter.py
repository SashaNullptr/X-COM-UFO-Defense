import psycog2
from x_com.db_query import send_query

def count_rows_in_col():

    count_command = 'SELECT COUNT(*) from table'
    results = send_query(counter_query)
    number_of_rows = result[0]

    return number_of_rows
