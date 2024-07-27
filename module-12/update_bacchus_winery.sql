-- Drop the database user if it exists
DROP USER IF EXISTS 'bravo'@'localhost';

-- Create the database user and grant them all privileges to the bacchus_winery database
CREATE USER 'bravo'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';

-- Grant all privileges to the bacchus_winery database to the user 'bravo' on localhost
GRANT ALL PRIVILEGES ON bacchus_winery.* TO 'bravo'@'localhost';

-- Make sure to apply the changes immediately
FLUSH PRIVILEGES;

-- Create a table to store quarterly hours
CREATE TABLE IF NOT EXISTS QuarterlyHours (
    employee_id INT,
    quarter VARCHAR(10),
    total_hours DECIMAL(10,2),
    PRIMARY KEY (employee_id, quarter),
    FOREIGN KEY (employee_id) REFERENCES Employee(employee_id)
);

-- Insert data into QuarterlyHours from EmployeeHours
INSERT INTO QuarterlyHours (employee_id, quarter, total_hours)
SELECT
    eh.employee_id,
    CONCAT(YEAR(eh.date), '-', QUARTER(eh.date)) AS quarter,
    SUM(eh.hours_worked) AS total_hours
FROM
    EmployeeHours eh
GROUP BY
    eh.employee_id, quarter;