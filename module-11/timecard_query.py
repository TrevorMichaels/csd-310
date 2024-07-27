import mysql.connector
from mysql.connector import errorcode

def get_daily_time_card_report():
    config = {
        "user": "bravo",
        "password": "password",
        "host": "localhost",
        "database": "bacchus_winery",
        "raise_on_warnings": True
    }

    # Prompting the user to enter a date
    date = input("Please enter the date for the time card report (YYYY-MM-DD): ")

    try:
        db = mysql.connector.connect(**config)
        cursor = db.cursor()

        # SQL query to retrieve employee hours for a specific date
        query = """
        SELECT Employee.employee_id, Employee.employee_name, EmployeeHours.date, EmployeeHours.hours_worked
        FROM Employee
        JOIN EmployeeHours ON Employee.employee_id = EmployeeHours.employee_id
        WHERE EmployeeHours.date = %s
        ORDER BY Employee.employee_id;
        """

        cursor.execute(query, (date,))

        # Printing the report with proper formatting for date and hours
        print(f"\nEmployee Time Card Report for {date}:")
        print(f"{'Employee ID':<12}{'Employee Name':<25}{'Date':<12}{'Hours Worked':<15}")
        for (employee_id, employee_name, emp_date, hours_worked) in cursor:
            formatted_date = emp_date.strftime('%Y-%m-%d') if emp_date else 'N/A'
            formatted_hours = f"{hours_worked:.2f}" if hours_worked else 'N/A'
            print(f"{employee_id:<12}{employee_name:<25}{formatted_date:<12}{formatted_hours:<15}")

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
get_daily_time_card_report()