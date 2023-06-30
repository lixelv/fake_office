# Python SQLite Database with Fake Data

This repository contains Python code that utilizes the `sqlite3` and `fake` libraries to generate fake data for companies and their offices. The purpose of this code is to practice using the `fake` library for creating randomized, dummy data. The code is not intended for any practical use.

## Files in the Repository

### db.py

This file defines the `SQLite` class, responsible for managing the SQLite database. The class constructor initializes the database connection, creates two tables (`Company` and `Office`), and commits the changes. The `SQLite` class provides methods to read company and office data from the database, as well as add new companies along with their respective offices.

### main.py

This script allows the user to specify the number of times they want to add a company to the database. It creates an instance of the `SQLite` class and calls the `add_company` method the specified number of times.

### read.py

This script reads and prints the contents of the `Company` and `Office` tables in the database. It creates an instance of the `SQLite` class, fetches the data, and displays it using the `prettytable` library for a more organized representation.

### url.py

This module provides a single function, `from_example_to_email`, which takes an email address as input and replaces the domain part of the address with a random domain from a predefined list. This is used to generate random email addresses for the offices in the `Office` table.

The `fake` library is used to generate various types of fake data, such as company names, addresses, phone numbers, and names for directors.

Keep in mind that this code is purely for practice and doesn't serve any practical purpose. It's intended for learning how to work with SQLite databases and generate fake data using the `fake` library.
