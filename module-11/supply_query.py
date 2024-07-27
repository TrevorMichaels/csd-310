import mysql.connector
from mysql.connector import errorcode

def get_supply_inventory_report():
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

        # SQL query to retrieve supply inventory and supplier details
        query = """
        SELECT si.item_name, si.supply_item_id, sod.quantity, s.supplier_id, s.supplier_name, s.supplier_contact
        FROM SupplyItem si
        JOIN SupplyOrderDetails sod ON si.supply_item_id = sod.supply_item_id
        JOIN Supplier s ON si.supplier_id = s.supplier_id
        ORDER BY si.item_name;
        """

        cursor.execute(query)

        # Printing the report
        print("\nSupply Inventory Report:")
        print(f"{'Item Name':<20}{'Item ID':<10}{'Quantity':<10}{'Supplier ID':<12}{'Supplier Name':<20}{'Supplier Contact':<25}")
        for (item_name, supply_item_id, quantity, supplier_id, supplier_name, supplier_contact) in cursor:
            print(f"{item_name:<20}{supply_item_id:<10}{quantity:<10}{supplier_id:<12}{supplier_name:<20}{supplier_contact:<25}")

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
get_supply_inventory_report()