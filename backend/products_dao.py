import mysql.connector
from sql_connections import get_mysql_connection
def get_all_products(connection):

    cursor=connection.cursor()

    query="select * from gs.products"

    cursor.execute(query)

    response = []

    for (product_id,name,price,category_id,uom_id) in cursor:
        response.append({"product_id": product_id, "name": name,
                          "price": price, "category_id": category_id, 
                          "uom_id": uom_id})
        

    return response

if __name__ == "__main__":
    connection = get_mysql_connection()
    print(get_all_products(connection))