import psycopg2
def table():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="1234", host="localhost", port="5433")

    cursor = conn.cursor()
    cursor.execute('''create table employees(Name Text, ID int, Age int);''')
    print("Table Created Successfully.")

    conn.commit()
    conn.close()

table()

def data():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="1234", host="localhost", port="5433")

    cursor = conn.cursor()

    name = input('Enter Name: ')
    id = input('Enter ID: ')
    age = input('Enter Age: ')

    query = '''insert into employees(Name, ID, Age) values(%s,%s,%s);'''
    print("Data Added Successfully.")

    conn.commit()
    conn.close()



