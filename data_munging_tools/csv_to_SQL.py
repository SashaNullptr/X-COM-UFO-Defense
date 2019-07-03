import csv, psycog2
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

def main():
    pass

if '__main__' == __name__:
    main()
