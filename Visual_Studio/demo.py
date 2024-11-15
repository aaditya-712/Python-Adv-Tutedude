import psycopg2
conn = psycopg2.connect(dbname="postgres", user="postgres", password="1234", host="localhost", port="5433")

cursor = conn.cursor()
cursor.execute('''create table employees(Name Text, ID int, Age int);''')
print("Table Created Successfully.")

conn.commit()
conn.close()

