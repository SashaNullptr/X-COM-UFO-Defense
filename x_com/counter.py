import psycog2

def count_rows_in_col():

    count_command = 'SELECT COUNT(*) from table'
    cur.execute(count_command)
    results = cur.fetchone()
    number_of_rows = result[0]

    return number_of_rows
