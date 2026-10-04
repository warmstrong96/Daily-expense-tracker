# Daily Expense Tracker

A command-line expense tracking application built with Python. The project allows users to record, view, categorize, and analyze expenses while automatically saving the data to a CSV file for persistence between sessions.

## Features

* Add new expenses with:

  * Amount
  * Description
  * Category
  * Date
* Automatically use the current date when no date is entered
* Save expenses to a CSV file
* Load previously saved expenses when the application starts
* View all recorded expenses
* Calculate:

  * Total spending
  * Average expense
  * Number of expense entries
  * Spending totals by category
* Validate user input
* Validate existing CSV data
* Handle file and data errors without crashing
* Confirm before deleting all saved expenses
* Clear all saved expense data

## Technologies Used

* **Python**
* `csv` — storing and retrieving expense data
* `datetime` — handling expense dates
* `pathlib` — managing the CSV file path
* `collections.defaultdict` — calculating totals by category
* `math` — validating numeric expense amounts

## How It Works

When the application starts, it checks for an existing `expenses.csv` file and loads any previously saved expenses.

Users can then select an option from the menu to add an expense, view their expenses, generate a summary, clear their saved data, or exit the application.

Each expense is stored with four pieces of information:

```text
Amount
Description
Category
Date
```

The application uses input validation to prevent invalid amounts, empty descriptions or categories, and incorrectly formatted dates.

## Expense Reports

The summary feature calculates the total and average expense and also groups expenses by category.

Example:

```text
Expense summary:
Entries: 5
Total: $142.50
Average: $28.50
Totals by category:
  Food: $65.00
  Transportation: $47.50
  Entertainment: $30.00
```

## Data Storage

Expense information is stored locally in an `expenses.csv` file.

The CSV uses the following fields:

```text
amount,description,category,date
```

This allows expense information to remain available after the program is closed and restarted.

## Error Handling

The application includes validation and error handling for situations such as:

* Invalid expense amounts
* Negative or zero amounts
* Invalid dates
* Missing descriptions or categories
* Incorrect CSV formatting
* File read/write errors
* Empty expense lists
* Unexpected end of user input

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/daily-expense-tracker.git
```

### 2. Navigate to the project directory

```bash
cd daily-expense-tracker
```

### 3. Run the application

```bash
python "Daily expense tracker(1).py"
```

The program will create `expenses.csv` automatically when expenses are saved.

## Project Structure

```text
daily-expense-tracker/
│
├── Daily expense tracker(1).py
├── expenses.csv
└── README.md
```

## What I Learned

This project helped me strengthen my Python programming skills while working through a practical problem. I practiced working with lists and dictionaries, functions, loops, conditional statements, file handling, CSV data, input validation, error handling, and basic data analysis.

I also improved the project from a simple expense-tracking program into a more complete application by adding persistent data storage, validation, reporting, and safer file operations.

## Future Improvements

Potential future improvements include:

* A graphical user interface
* Monthly and yearly spending reports
* Expense editing and deletion by individual entry
* Budget tracking
* Data visualization
* Exporting reports
* Database storage such as SQLite
* AI-powered expense insights
* Natural-language queries for analyzing spending

## Author

**William Armstrong**

Information Technology Student
Miami Dade College
