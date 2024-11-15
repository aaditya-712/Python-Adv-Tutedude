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

    name = input('Enter Name: ')
    id = int(input('Enter ID: '))
    age = int(input('Enter Age: '))

    query = '''insert into employees(Name,ID,Age) values(%s,%s,%s);'''
    cursor.execute(query, (name, id, age))
    print("Data Added Successfully.")

    conn.commit()
    conn.close()

data()



# def extract():
#     conn = psycopg2.connect(dbname="postgres", user="postgres", password="1234", host="localhost", port="5433")

#     cursor = conn.cursor()
#     cursor.execute('''select * from employees;''')
#     show = cursor.fetchone()
#     print(show)
#     print(show[0])
#     # print("Data Added Successfully.")

#     conn.commit()
#     conn.close()

# extract()