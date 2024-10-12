import psycopg2
import random
import time
from datetime import datetime, timedelta

# Database connection details
DB_HOST = "dpg-cr47cdbv2p9s73cncaeg-a.frankfurt-postgres.render.com"
DB_NAME = 'sales_l75i'
DB_USER = 'sales_l75i_user'
DB_PASSWORD = 'MenwGm7zvU5nFOd1L6UeAPRwiDZ95FLD'

conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)
cursor = conn.cursor()

# List of sample electronic products and countries
products = {
    "Smartphone": 699.99,
    "Laptop": 999.99,
    "Tablet": 499.99,
    "Smartwatch": 199.99,
    "Headphones": 149.99,
    "Camera": 799.99
}
countries = ["USA", "UK", "Germany", "France", "Japan", "Australia"]

# Function to insert random data
def insert_random_data():
    product_name, item_price = random.choice(list(products.items()))
    quantity = random.randint(1, 100)
    sale_date = datetime.now().date() - timedelta(days=random.randint(0, 365))
    total_amount = round(item_price * quantity, 2)
    country = random.choice(countries)
    
    query = """
    INSERT INTO realtime_sales (product_name, quantity, sale_date, total_amount, country, item_price)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (product_name, quantity, sale_date, total_amount, country, item_price))
    conn.commit()
    print(f"Inserted: {product_name}, {quantity}, {sale_date}, {total_amount}, {country}, {item_price}")

# Insert data every 5 seconds
try:
    while True:
        insert_random_data()
        time.sleep(5)
except KeyboardInterrupt:
    print("Stopped by user")
finally:
    cursor.close()
    conn.close()


# select * from realtime_sales;

# drop table realtime_sales;

# CREATE TABLE realtime_sales (
#     sale_id SERIAL PRIMARY KEY,
#     product_name VARCHAR(100) NOT NULL,
#     quantity INT NOT NULL,
#     sale_date DATE NOT NULL,
#     total_amount DECIMAL(10, 2) NOT NULL,
#     country VARCHAR(50) NOT NULL,
#     item_price DECIMAL(10, 2) NOT NULL
# );


