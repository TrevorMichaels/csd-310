-- Drop the database user if it exists
DROP USER IF EXISTS 'bravo'@'localhost';

-- Create the database user and grant them all privileges to the bacchus_winery database
CREATE USER 'bravo'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';

-- Grant all privileges to the bacchus_winery database to the user 'bravo' on localhost
GRANT ALL PRIVILEGES ON bacchus_winery.* TO 'bravo'@'localhost';

-- Make sure to apply the changes immediately
FLUSH PRIVILEGES;

-- Create tables
CREATE TABLE Supplier (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,
    supplier_name VARCHAR(255) NOT NULL,
    supplier_contact VARCHAR(255)
);

CREATE TABLE SupplyItem (
    supply_item_id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(255) NOT NULL,
    supplier_id INT,
    FOREIGN KEY (supplier_id) REFERENCES Supplier(supplier_id)
);

CREATE TABLE SupplyOrder (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    estimated_delivery_date DATE,
    tracking_number VARCHAR(255)
);

CREATE TABLE SupplyOrderDetails (
    order_id INT,
    supply_item_id INT,
    quantity INT,
    PRIMARY KEY (order_id, supply_item_id),
    FOREIGN KEY (order_id) REFERENCES SupplyOrder(order_id),
    FOREIGN KEY (supply_item_id) REFERENCES SupplyItem(supply_item_id)
);

CREATE TABLE Employee (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_name VARCHAR(255) NOT NULL,
    role VARCHAR(255)
);

CREATE TABLE EmployeeHours (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    date DATE,
    hours_worked DECIMAL(5, 2),
    FOREIGN KEY (employee_id) REFERENCES Employee(employee_id)
);

CREATE TABLE Distributor (
    distributor_id INT AUTO_INCREMENT PRIMARY KEY,
    distributor_name VARCHAR(255) NOT NULL,
    distributor_contact VARCHAR(255)
);

CREATE TABLE Wine (
    wine_id INT AUTO_INCREMENT PRIMARY KEY,
    wine_type VARCHAR(255) NOT NULL,
    wine_name VARCHAR(255)
);

CREATE TABLE WineInventory (
    wine_inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    wine_id INT,
    quantity INT,
    FOREIGN KEY (wine_id) REFERENCES Wine(wine_id)
);

CREATE TABLE WineOrder (
    wine_order_id INT AUTO_INCREMENT PRIMARY KEY,
    order_date DATE,
    distributor_id INT,
    FOREIGN KEY (distributor_id) REFERENCES Distributor(distributor_id)
);

CREATE TABLE WineOrderDetails (
    wine_order_id INT,
    wine_type VARCHAR(255),
    quantity INT,
    PRIMARY KEY (wine_order_id, wine_type),
    FOREIGN KEY (wine_order_id) REFERENCES WineOrder(wine_order_id)
);

-- Insert data
INSERT INTO Supplier (supplier_name, supplier_contact) VALUES
('Supplier A', 'Contact A'),
('Supplier B', 'Contact B'),
('Supplier C', 'Contact C');

INSERT INTO SupplyItem (item_name, supplier_id) VALUES
('Bottles', 1),
('Corks', 1),
('Labels', 2),
('Boxes', 2),
('Vats', 3),
('Tubing', 3);

INSERT INTO SupplyOrder (estimated_delivery_date, tracking_number) VALUES
('2024-08-01', 'TN001'),
('2024-08-15', 'TN002'),
('2024-09-01', 'TN003');

INSERT INTO SupplyOrderDetails (order_id, supply_item_id, quantity) VALUES
(1, 1, 100),
(1, 2, 100),
(2, 3, 200),
(2, 4, 200),
(3, 5, 50),
(3, 6, 50);

INSERT INTO Employee (employee_name, role) VALUES
('Tony Stark', 'Finance and Payroll'),
('Natasha Romanoff', 'Marketing'),
('Clint Barton', 'Marketing Assistant'),
('Steve Rogers', 'Production Manager'),
('Thor Odinson', 'Production'),
('Bruce Banner', 'Production');

INSERT INTO EmployeeHours (employee_id, date, hours_worked) VALUES
(1, '2024-07-01', 8.0),
(2, '2024-07-01', 7.5),
(3, '2024-07-01', 8.0),
(4, '2024-07-01', 9.0),
(5, '2024-07-01', 8.5),
(6, '2024-07-01', 8.0);

INSERT INTO Distributor (distributor_name, distributor_contact) VALUES
('Distributor A', 'Contact A'),
('Distributor B', 'Contact B'),
('Distributor C', 'Contact C');

INSERT INTO Wine (wine_type, wine_name) VALUES
('Merlot', 'Merlot Wine'),
('Cabernet', 'Cabernet Wine'),
('Chablis', 'Chablis Wine'),
('Chardonnay', 'Chardonnay Wine');

INSERT INTO WineInventory (wine_id, quantity) VALUES
(1, 100),
(2, 200),
(3, 150),
(4, 120);

INSERT INTO WineOrder (order_date, distributor_id) VALUES
('2024-07-10', 1),
('2024-07-11', 2),
('2024-07-12', 3);

INSERT INTO WineOrderDetails (wine_order_id, wine_type, quantity) VALUES
(1, 'Merlot', 50),
(1, 'Cabernet', 30),
(2, 'Chablis', 20),
(3, 'Chardonnay', 25);