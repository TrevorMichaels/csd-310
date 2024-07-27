import mysql.connector
from mysql.connector import errorcode
import datetime

def get_best_selling_wines_report():
    config = {
        "user": "bravo",
        "password": "password",
        "host": "localhost",
        "database": "bacchus_winery",
        "raise_on_warnings": True
    }

    try:
        db = mysql.connector.connect(**config)
        cursor = db.cursor()

        # SQL query to retrieve best-selling wines
        query = """
        SELECT Wine.wine_name, WineOrder.order_date, WineOrderDetails.quantity
        FROM Wine
        JOIN WineOrderDetails ON Wine.wine_type = WineOrderDetails.wine_type
        JOIN WineOrder ON WineOrder.wine_order_id = WineOrderDetails.wine_order_id
        ORDER BY WineOrder.order_date;
        """

        cursor.execute(query)

        # Printing the report
        print("\nBest-Selling Wines Report:")
        print(f"{'Wine Name':<20}{'Order Date':<15}{'Quantity Ordered':<15}")
        for (wine_name, order_date, quantity) in cursor:
            formatted_date = order_date.strftime('%Y-%m-%d') if isinstance(order_date, datetime.date) else 'N/A'
            formatted_quantity = f"{quantity:.0f}" if quantity is not None else 'N/A'
            print(f"{wine_name:<20}{formatted_date:<15}{formatted_quantity:<15}")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("The supplied username or password are invalid")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("The specified database does not exist")
        else:
            print(err)
    finally:
        if db.is_connected():
            cursor.close()
            db.close()

# Run the function
get_best_selling_wines_report()