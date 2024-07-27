import mysql.connector
from mysql.connector import errorcode

def get_wine_inventory_report():
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

        # SQL query to retrieve wine inventory details
        query = """
        SELECT w.wine_id, w.wine_name, wi.quantity
        FROM Wine w
        JOIN WineInventory wi ON w.wine_id = wi.wine_id
        ORDER BY w.wine_name;
        """

        cursor.execute(query)

        # Printing the report
        print("\nWine Inventory Report:")
        print(f"{'Wine ID':<8}{'Wine Name':<20}{'Quantity in Stock':<20}")
        for (wine_id, wine_name, quantity) in cursor:
            print(f"{wine_id:<8}{wine_name:<20}{quantity:<20}")

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
get_wine_inventory_report()