# 1.	Postgresql bazaga python yordamida ulaning .
# Product nomli jadval yarating  (id,name,price, color,image) .

import psycopg2

conn = psycopg2.connect(database="n42",
                        user="postgres",
                        password="1201",
                        host="localhost",
                        port=5432)

cur = conn.cursor()
create_table = """ CREATE TABLE IF NOT EXISTS PRODUCT (
    ID INT NOT NULL AUTO_INCREMENT,
    NAME VARCHAR(50) NOT NULL,
    PRICE FLOAT NOT NULL,
    COLOUR VARCHAR(30) NOT NULL,
    IMAGE TEXT NOT NULL);"""
cur.execute(create_table)

# 2.	Insert_product , select_all_products , update_product,delete_product nomli funksiyalar yarating.
def insert_product():
    insert_query = """INSERT INTO PRODUCT (NAME, PRICE, COLOUR, IMAGE)
    values ( 'Iphone 15', '1200$','blue','http://urlimage'),
           ( 'Iphone 15', '1200$','red','http://urlimage');
           """
    cur.execute(insert_query)
    conn.commit()

def select_all_product():
    select_all_query = """SELECT * FROM PRODUCT;"""
    cur.execute(select_all_query)
    return cur.fetchall()

def update_product():
    update_query = """UPDATE PRODUCT SET color ='silver' where color = 'blue';
    """
    cur.execute(update_query)
    conn.commit()

def delete_product():
    delete_query = """DELETE FROM PRODUCT
    WHERE ID = 1;"""
    cur.execute(delete_query)
    conn.commit()
    print("Product deleted")

# 3.	Alphabet nomli class yozing .
# class obyektlarini  iteratsiya qilish imkoni   bo’lsin (iterator).
# obyektni for sikli orqali iteratsiya qilinsa 26 ta alifbo xarflari chiqsin


import string

class AlphabetGenerator:
    def __init__(self):
        self.alphabet = list(string.ascii_lowercase)

    def generate_alphabet(self):
        return self.alphabet
generator = AlphabetGenerator()
alphabet = generator.generate_alphabet()
print(alphabet)


#
# 4.	print_numbers va print_leters nomli funksiyalar yarating.
# prit_numbers funksiyasi (1,5) gacha bo’lgan sonlarni ,
# print_letters esa  ‘’ABCDE” belgilarni loop da bitta dan time sleep(1) qo’yib ,parallel 2ta thread yarating.
# Ekranga parallel ravishda itemlar chiqsin.

import threading
import time
def print_letters():
    for i in 'ABCDE':
        print(i)
        time.sleep(1)
def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(1)
thread1 = threading.Thread(target=print_letters())
thread2 = threading.Thread(target=print_numbers())

start_time = time.time()

thread1.start()
thread2.start()


thread1.join()
thread2.join()

end_time = time.time()

print(end_time - start_time)
print('Done')

# 5.	Product nomli class yarating (1 – misoldagi Product ).Product classiga save() nomli object method yarating.
# Uni vazifasi object attributelari orqali bazaga saqlasin.

class Product:
    def save(self,db_params):
        with DbConnect(db_params) as cur:
            insert_query = 'insert into Product (name,color) values (%s,%s);'
            insert_params = (self.name, self.color)
            cur.execute(insert_query, insert_params)
            print('INSERT 0 1')

    def __repr__(self):
        return f'Book({self.id} => {self.name} => {self.author})'

# 6.	DbConnect nomli ContextManager yarating.
# Va uning vazifasi python orqali PostGresqlga ulanish (conn,cur)

class DbConnect:
    def __init__(self, db_params):
        self.db_params = db_params
        self.conn = psycopg2.connect(**self.db_params)

    def __enter__(self):
        self.cur = self.conn.cursor()
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()


