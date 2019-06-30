import csv, redis, json
import sys

def csv_to_SQL( csv_file ):
  with open (csv_file, 'r') as f:
    reader = csv.reader(f)
    columns = next(reader)
    query = 'insert into MyTable({0}) values ({1})'
    query = query.format(','.join(columns), ','.join('?' * len(columns)))
    cursor = connection.cursor()
    for data in reader:
        cursor.execute(query, data)
    cursor.commit()

REDIS_HOST = 'localhost'

def read_csv_data(csv_file, ik, iv):
    with open(csv_file, encoding='utf-8') as csvf:
        csv_data = csv.reader(csvf)
        return [(r[ik], r[iv]) for r in csv_data]

def store_data(conn, data):
    for i in data:
        conn.setnx(i[0], i[1])
    return data


def main():
    if len(sys.argv) < 2:
    sys.exit(
        "Usage: %s file.csv [key_column_index, value_column_index]"
        % __file__
    )
    columns = (0, 1) if len(sys.argv) < 4 else (int(x) for x in sys.argv[2:4])
    data = read_csv_data(sys.argv[1], *columns)
    conn = redis.Redis(REDIS_HOST)
    print (json.dumps(store_data(conn, data)))

if '__main__' == __name__:
    main()
