import psycopg2
def table():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="1234", host="localhost", port="5433")

    cursor = conn.cursor()
    cursor.execute('''create table employees(Name Text, ID int, Age int);''')
    print("Table Created Successfully.")

    conn.commit()
    conn.close()

def data():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="1234", host="localhost", port="5433")

    cursor = conn.cursor()
    cursor.execute('''insert into employees(Name, ID, Age) values('Aaditya', 01, 20);''')
    print("Data Added Successfully.")

    conn.commit()
    conn.close()


def extract():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="1234", host="localhost", port="5433")

    cursor = conn.cursor()
    cursor.execute('''select * from employees;''')
    show = cursor.fetchone()
    print(show)
    print(show[0])
    # print("Data Added Successfully.")

    conn.commit()
    conn.close()

extract()