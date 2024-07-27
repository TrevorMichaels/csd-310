import mysql.connector
from mysql.connector import errorcode

def create_employee_report():
    # Database configuration
    config = {
        'user': 'bravo',
        'password': 'password',
        'host': 'localhost',
        'database': 'bacchus_winery',
        'raise_on_warnings': True
    }

    try:
        # Connect to the MySQL database
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        # SQL query to fetch quarterly hours
        query = '''
        SELECT employee_id, quarter, total_hours
        FROM QuarterlyHours
        ORDER BY employee_id, quarter;
        '''

        # Execute the query
        cursor.execute(query)

        # Fetch the results
        results = cursor.fetchall()

        # Check if results were fetched
        if results:
            print("Employee Quarterly Hours Report:")
            for (employee_id, quarter, total_hours) in results:
                print(f"Employee ID: {employee_id}, Quarter: {quarter}, Total Hours: {total_hours}")
        else:
            print("No data found.")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    finally:
        # Close the cursor and the connection
        if 'cursor' in locals():
            cursor.close()
        if 'cnx' in locals() and cnx.is_connected():
            cnx.close()

if __name__ == "__main__":
    create_employee_report()