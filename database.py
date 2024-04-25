import psycopg2

    
conn=psycopg2.connect(
    user="postgres",
    dbname="myduka",
    password="brina5511",
    port=5432,
    host="localhost"
)
cur=conn.cursor()

def get_products():
    cur.execute("select * from products;")
    prods=cur.fetchall()
    for prod in prods:
        print(prod)

get_products()

def get_data(table_name):
    select=f"select * from {table_name}"
    cur.execute(select)
    results=cur.fetchall()
    for i in results:
        print(i)

get_data("products")
# get_data("sales")

def insert_products(values):
    insert=f"insert into products(name,buying_price,selling_price,stock_quantity)values{values}"
    cur.execute(insert)
    conn.commit()
#product_value=("milk",20,50,3)
# insert_products(product_value)

get_data("products")
get_data("sales")


def insert_products(values):
    insert="""insert into products
    (name,buying_price,selling_price,stock_quantity)values(%s,%s,%s,%s)"""
    cur.execute(insert,values)
    conn.commit()
product_value=("cookies",20,50,2)
insert_products(product_value)
get_data("products")
get_data("sales")


# create  a function to insert sales (2 ways)











