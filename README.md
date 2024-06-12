# SneakerNet CLI 

## Author

Emmanuel Otieno

## Overview

- SneakerNet is a command-line interface (CLI) application designed to manage a database of sneakers, including operations such as listing, adding, updating, and deleting shoes, customers, and orders. It utilizes SQLite for database management and provides a simple yet powerful tool for sneaker enthusiasts or businesses looking to track their inventory and sales.

***

## Files and their functions

#### connection.py

This file establishes a connection to the SQLite database named sneaker_net.db. It initializes a cursor object (CURSOR) for executing SQL commands on the database.

#### models.py

Contains the definitions for three classes:

- Shoe: Represents individual shoe items with attributes like name, brand, size, and price. Includes methods for creating the shoe table, saving a shoe, updating its price, and deleting it.

- Customer: Represents customers with attributes like first name, last name, and address. Includes methods for creating the customer table, saving a customer, updating their address, and deleting them.

- Order: Represents orders placed by customers, linking them to specific shoes and quantities. Includes methods for creating the order table, creating an order, and managing order details.

#### seed.py

Seeds the database with initial data for shoes, customers, and orders. This includes creating tables and inserting sample data to demonstrate how the system works

## Generating database

To create the database for the application and insert initial data, run the seed.py file as follows:

```
python lib/seed.py

```

## Usage

To run the CLI application, execute the cli.py script. Upon launching, you will see a menu presenting several options for managing sneakers, customers, and orders. Select an option by entering its corresponding number, and follow the prompts to perform the desired action.

Example:
```
python lib/cli.py

```

After running the above command, you'll interact with the CLI as follows:

```
What do you want to do?
0. Quit
1. List all Customers
2. Find Customer by Name
...

```

## Contributing

Contributions to SneakerNet are welcome Please feel free to submit pull requests or open issues for bugs or feature requests.

## License

SneakerNet is licensed under the MIT License