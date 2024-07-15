import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "bravo",
    "password": "password",
    "host": "localhost",
    "database": "bacchus_winery",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    print("\nDatabase user {} connected to MySQL on host {} with database {}".format(
        config["user"], config["host"], config["database"]))
    
    cursor = db.cursor()

    # Query 1: Select all fields for the Supplier table
    cursor.execute("SELECT * FROM Supplier")
    print("\nSuppliers:")
    for (supplier_id, supplier_name, supplier_contact) in cursor:
        print(f"Supplier ID: {supplier_id}, Supplier Name: {supplier_name}, Supplier Contact: {supplier_contact}")

    # Query 2: Select all fields for the SupplyItem table
    cursor.execute("SELECT * FROM SupplyItem")
    print("\nSupply Items:")
    for (supply_item_id, item_name, supplier_id) in cursor:
        print(f"Supply Item ID: {supply_item_id}, Item Name: {item_name}, Supplier ID: {supplier_id}")

    # Query 3: Select all fields for the SupplyOrder table
    cursor.execute("SELECT * FROM SupplyOrder")
    print("\nSupply Orders:")
    for (order_id, estimated_delivery_date, tracking_number) in cursor:
        print(f"Order ID: {order_id}, Estimated Delivery Date: {estimated_delivery_date}, Tracking Number: {tracking_number}")

    # Query 4: Select all fields for the SupplyOrderDetails table
    cursor.execute("SELECT * FROM SupplyOrderDetails")
    print("\nSupply Order Details:")
    for (order_id, supply_item_id, quantity) in cursor:
        print(f"Order ID: {order_id}, Supply Item ID: {supply_item_id}, Quantity: {quantity}")

    # Query 5: Select all fields for the Employee table
    cursor.execute("SELECT * FROM Employee")
    print("\nEmployees:")
    for (employee_id, employee_name, role) in cursor:
        print(f"Employee ID: {employee_id}, Employee Name: {employee_name}, Role: {role}")

    # Query 6: Select all fields for the EmployeeHours table
    cursor.execute("SELECT * FROM EmployeeHours")
    print("\nEmployee Hours:")
    for (record_id, employee_id, date, hours_worked) in cursor:
        print(f"Record ID: {record_id}, Employee ID: {employee_id}, Date: {date}, Hours Worked: {hours_worked}")

    # Query 7: Select all fields for the Distributor table
    cursor.execute("SELECT * FROM Distributor")
    print("\nDistributors:")
    for (distributor_id, distributor_name, distributor_contact) in cursor:
        print(f"Distributor ID: {distributor_id}, Distributor Name: {distributor_name}, Distributor Contact: {distributor_contact}")

    # Query 8: Select all fields for the Wine table
    cursor.execute("SELECT * FROM Wine")
    print("\nWines:")
    for (wine_id, wine_type, wine_name) in cursor:
        print(f"Wine ID: {wine_id}, Wine Type: {wine_type}, Wine Name: {wine_name}")

    # Query 9: Select all fields for the WineInventory table
    cursor.execute("SELECT * FROM WineInventory")
    print("\nWine Inventory:")
    for (wine_inventory_id, wine_id, quantity) in cursor:
        print(f"Wine Inventory ID: {wine_inventory_id}, Wine ID: {wine_id}, Quantity: {quantity}")

    # Query 10: Select all fields for the WineOrder table
    cursor.execute("SELECT * FROM WineOrder")
    print("\nWine Orders:")
    for (wine_order_id, order_date, distributor_id) in cursor:
        print(f"Wine Order ID: {wine_order_id}, Order Date: {order_date}, Distributor ID: {distributor_id}")

    # Query 11: Select all fields for the WineOrderDetails table
    cursor.execute("SELECT * FROM WineOrderDetails")
    print("\nWine Order Details:")
    for (wine_order_id, wine_type, quantity) in cursor:
        print(f"Wine Order ID: {wine_order_id}, Wine Type: {wine_type}, Quantity: {quantity}")

    input("\n\nPress any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)

finally:
    # It's safer to check if 'db' is defined and is open before trying to close it
    if 'db' in locals() and db.is_connected():
        db.close()