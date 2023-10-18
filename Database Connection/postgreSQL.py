import psycopg2
import random
from faker import Faker

class Postgres:

    def __init__(self):
        hostname = 'localhost'
        dbname = 'Testing'
        user = 'postgres'
        password = 'password'
        self.conn = psycopg2.connect(f"host={hostname} dbname={dbname} user={user} password={password}")
        print('-------Connected-------')
        self.cur = self.conn.cursor()

        self.fake = Faker()
    
    def get_all_data(self):
        self.cur.execute('select * from employee.employee_details;')
        data = self.cur.fetchall()
        print(data)

    def insert_new_data(self):
        
        name = self.fake.name()
        city = self.fake.address()
        age = self.fake.random_int(20,40)
        sal = self.fake.random_int(20000,400000)
        self.cur.execute(f"insert into employee.employee_details (name, city, age, salary) values ('{name}', '{city}', {age}, {sal})")
        print('----------Data Inserted-------------')

    def delete_record(self, id):
        self.cur.execute(f"delete from employee.employee_details where id={id}")
        print('----------Record Deleted-------------')

    def teardown(self):
        self.conn.commit()
        self.conn.close()
        print('-------Connection Closed-------')

if __name__ == '__main__':
    ps = Postgres()
    ps.get_all_data()
    # ps.insert_new_data()
    ps.delete_record(1)
    ps.get_all_data()
    ps.teardown()