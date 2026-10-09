
# 📈 Stock Portfolio Tracker — Python OOP Project

A console-based **Stock Portfolio Tracker** built with Python and Object-Oriented Programming (OOP). The application allows users to create accounts, log in, buy and sell shares, manage their investment portfolios, track simulated stock price movements, and visualize their investments using Pandas and Matplotlib.

---

## 📖 Project Overview

This project is a stock portfolio management application developed as part of my Python Programming Internship at CodeAlpha.

The application provides a menu-driven interface where users can create an account, log in, manage their stock investments, and view their portfolio information. It uses Pandas DataFrames to manage structured data and CSV and Excel files to store user information, portfolio balances, investments, and stock market data.

The project also includes simulated stock price fluctuations and a visualization feature that displays the distribution of a user's investments using a pie chart.

---

## 🎯 Purpose of the Project

The purpose of this project is to:

- Build a functional stock portfolio management application using Python.
- Apply Object-Oriented Programming principles to organize the code.
- Implement account creation, login, and password-reset functionality.
- Allow users to buy and sell shares while managing their available balance.
- Calculate portfolio profit percentages using simulated stock prices.
- Store and update structured data using Pandas, CSV, and Excel files.
- Visualize investment distribution using Matplotlib.
- Practice abstraction, inheritance, encapsulation, composition, and type hints.

---

## 💼 Application Features

### 🔐 Account Management

- **Sign Up:** Create a new account with a username and password.
- **Login:** Access an existing account.
- **Password Reset:** Change a password after an unsuccessful login attempt.
- **Account Validation:** Check usernames, passwords, and password confirmation.
- **Starting Balance:** New accounts receive an initial balance of $10,000.

### 📊 Stock Market

- Display the available stock market.
- View stock tickers, company names, and stock prices.
- Select stocks using their ticker symbols.
- Validate stock symbols before completing transactions.
- Simulate stock price fluctuations using Python's `random` module.

### 💰 Buy Shares

- Select a stock using its ticker symbol.
- View its current simulated price.
- Calculate the maximum number of shares affordable with the available balance.
- Enter the number of shares to purchase.
- Calculate the total transaction cost.
- Update the user's remaining balance and investments.

### 💸 Sell Shares

- Display the stocks currently owned by the user.
- Select which stock to sell.
- Specify the number of shares to sell.
- Validate the selected stock and quantity.
- Add the sale proceeds to the user's available balance.
- Update the stored portfolio.

### 📈 Portfolio Tracking

- Track the stocks owned by each user.
- Store the quantity of each stock held.
- Maintain the user's available cash balance.
- Calculate a portfolio profit percentage based on the application's simulated prices and balance calculations.
- Save portfolio updates to persistent files.

### 🥧 Investment Visualization

- Generate a pie chart showing the distribution of shares across the stocks in the portfolio.
- Display the user's investment and profit information in the chart title.
- Use Matplotlib's `Solarize_Light2` plotting style.

---

## 📁 Complete Project Structure

```text
CodeAlpha_Stock_Portfolio_Tracker/
│
├── MainProgram.py
│   # Main application, portfolio operations, and authentication
│
├── DataBases.py
│   # Loads stock market data and user databases
│   # Displays portfolio information and charts
│
├── BluePrint.py
│   # Abstract base classes defining application structure
│
├── Portfolio_Stock_Tracker_Large.xlsx
│   # Stock market data and simulated stock prices
│
├── Usernames_Passwrods.csv
│   # Usernames and passwords
│
├── Users_Portfolio.csv
│   # User balances, investments, and profit percentages
│
└── README.md
    # Project documentation
```

---

## 📂 File Descriptions

### 🖥️ `MainProgram.py`

The main application file. It contains the core logic for authentication and portfolio management.

**Main classes:**

- **`Portfolio`** — Manages the user's stock investments and financial transactions.
- **`Login_Signin`** — Handles account creation, login, password resetting, and user database updates.

**Main functionality:**

- Displays the main application menu.
- Accepts user input for account and portfolio operations.
- Implements buying and selling shares.
- Updates the user's balance and investment records.
- Simulates stock price fluctuations.
- Calculates portfolio profit percentages.
- Saves updated information to CSV and Excel files.

**Run this file to start the application.**

### 🗄️ `DataBases.py`

Responsible for loading and managing the application's data.

It contains the `Data` class, which provides methods to:

- Load the stock market from `Portfolio_Stock_Tracker_Large.xlsx`.
- Load user portfolio information from `Users_Portfolio.csv`.
- Load account information from `Usernames_Passwrods.csv`.
- Display a user's portfolio and profit percentage.
- Generate a pie chart showing the distribution of owned shares.

### 🧩 `BluePrint.py`

Contains the abstract base classes used to establish the application's structure.

These include:

- `Abst_Portfolio` — Defines the required interface for portfolio operations.
- `Abst_Login_Signin` — Defines the required interface for authentication operations.
- `Abst_Data` — Defines the required interface for data-management operations.

These abstract classes help establish a consistent structure for the application's main components.

### 📊 `Portfolio_Stock_Tracker_Large.xlsx`

Stores the stock market data used by the application.

The application reads stock information from this workbook and updates the stock prices when simulated market movements occur.

**Note:** The stock prices are simulated by the application rather than fetched from a live financial market API.

### 👤 `Usernames_Passwrods.csv`

Stores the account information used by the application.

The file contains the following fields:

| Column | Description |
|---|---|
| `Username` | The user's account username |
| `Password` | The user's password |

**Security note:** This learning project stores passwords as plain text. A production application should use secure password hashing and appropriate authentication protections.

### 💼 `Users_Portfolio.csv`

Stores the financial and investment information associated with each user.

| Column | Description |
|---|---|
| `Username` | The user's account username |
| `Balance` | Available cash balance |
| `Investments` | Encoded stock tickers and quantities |
| `Profit` | Calculated portfolio profit percentage |

The file is updated when users create accounts, purchase shares, sell shares, or when the application recalculates portfolio information.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python 3** | Core programming language |
| **Pandas** | DataFrames, filtering, calculations, and data manipulation |
| **Matplotlib** | Investment distribution visualization |
| **CSV** | Persistent storage for account and portfolio information |
| **Excel** | Storage of stock market data |
| **ABC module** | Abstract base classes and interface enforcement |
| **Random module** | Simulated stock price movements |
| **Type Hints** | Improved code readability and type clarity |
| **Git & GitHub** | Version control and project hosting |

### Python

Used to implement the application's logic, account management, financial calculations, user interaction, and transaction workflows.

### Pandas

Used to read, filter, update, and save tabular data.

Examples include retrieving a user's balance, finding stock prices using ticker symbols, updating investments, and calculating profit percentages.

### Matplotlib

Used to visualize the composition of a user's portfolio through a pie chart.

### CSV and Excel

Used to maintain application data between program sessions without requiring a database server.

### Abstract Base Classes

Used to define application interfaces and enforce a consistent structure across classes.

---

## 🎮 How the Application Works

### Application Flow

1. The application starts and displays the authentication menu.
2. The user chooses to log in, create an account, or quit.
3. During account creation, the user chooses a username and password and confirms the password.
4. A successful account creation initializes the user's portfolio with a starting balance of $10,000.
5. After authentication, the application displays the portfolio menu.
6. The user chooses to buy shares, sell shares, view the portfolio, or quit.
7. The application validates inputs and performs the selected operation.
8. Portfolio balances and investment records are updated and saved.
9. The user can view a pie chart representing the distribution of their owned shares.

### Buying Shares

When buying shares, the application:

1. Displays the stock market.
2. Requests a valid stock ticker.
3. Retrieves the stock's name and price.
4. Calculates the maximum affordable quantity.
5. Requests the desired number of shares.
6. Calculates the total cost.
7. Deducts the cost from the user's balance.
8. Updates and saves the investment information.

The transaction cost is calculated as:

```python
total_cost = shares * stock_price
```

The remaining balance is calculated as:

```python
new_balance = round(users_balance - total_cost, 2)
```

### Selling Shares

When selling shares, the application:

1. Retrieves the user's existing investments.
2. Displays the available stocks to sell.
3. Requests a stock ticker and quantity.
4. Validates that the user owns the selected stock and enough shares.
5. Calculates the sale proceeds.
6. Adds the proceeds to the user's balance.
7. Updates the investment records.

The sale proceeds are calculated as:

```python
sale_proceeds = share_price * shares_to_sell
```

### Simulated Stock Prices

The application uses Python's `random` module to simulate stock price movements.

Prices may increase or decrease when the simulation runs. The updated prices are saved to the Excel workbook.

These values are for demonstration purposes and do not represent real-time market prices.

### Profit Calculation

The application calculates a percentage based on the portfolio balance and the value of its recorded investments relative to the initial $10,000 balance.

The general percentage formula is:

```python
profit_percentage = (
    (portfolio_value - initial_balance)
    / initial_balance
) * 100
```

The result is rounded to two decimal places in the application's calculations.

This is a simplified simulation, not a complete investment-performance or tax calculation.

### Portfolio Visualization

When the user chooses to view their portfolio, the application can display a pie chart showing the relative quantities of the stocks they own.

The chart uses Matplotlib to label the stock tickers and show their relative proportions.

---

## ▶️ Installation Instructions

### 1. Prerequisites

Install Python 3.10 or a compatible newer version.

Check your installed version:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone https://github.com/QaisSaid-2007/CodeAlpha_Stock_Portfolio_Tracker.git
```

Navigate to the project directory:

```bash
cd CodeAlpha_Stock_Portfolio_Tracker
```

### 3. Create a Virtual Environment (Recommended)

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install Required Libraries

Install Pandas, Matplotlib, and the Excel-reading dependency:

```bash
pip install pandas matplotlib openpyxl
```

`openpyxl` is required by Pandas to read and write `.xlsx` workbooks.

### 5. Verify the Project Files

Ensure the following files are present in the project directory:

- `MainProgram.py`
- `DataBases.py`
- `BluePrint.py`
- `Portfolio_Stock_Tracker_Large.xlsx`
- `Usernames_Passwrods.csv`
- `Users_Portfolio.csv`

Keep the filenames and capitalization consistent with the Python imports and file paths.

---

## 🚀 How to Run the Project

Start the application by running:

```bash
python MainProgram.py
```

Follow the on-screen prompts to:

- Create an account or log in.
- Buy shares.
- Sell shares.
- View your portfolio.
- View the investment distribution chart.
- Exit the application.

---

## 🧠 Main Python Concepts Demonstrated

- **Object-Oriented Programming (OOP)** — Organizing application logic into classes.
- **Abstraction** — Defining abstract interfaces for portfolio, authentication, and data operations.
- **Inheritance** — Implementing classes that follow abstract base classes.
- **Encapsulation** — Grouping data and related operations within classes.
- **Composition** — Using the `Data` class to provide data to other application components.
- **Type Hints** — Specifying expected types for function arguments and return values.
- **Pandas DataFrames** — Managing structured user, stock, and portfolio data.
- **Data Filtering** — Retrieving specific records using conditions.
- **File Handling** — Reading and writing CSV and Excel files.
- **Input Validation** — Checking ticker symbols, share quantities, and account information.
- **Pattern Matching** — Using `match` and `case` to handle menu options.
- **Nested Functions** — Organizing calculations within methods.
- **Randomization** — Simulating changes in stock prices.
- **Data Visualization** — Displaying investment distribution with Matplotlib.
- **Financial Calculations** — Calculating transaction costs, balances, and profit percentages.

---

## 🎓 Learning Outcomes

By developing this project, I practiced and strengthened my ability to:

- Design a multi-file Python application using OOP.
- Build and use abstract base classes.
- Separate data-management logic from application logic.
- Work with Pandas DataFrames to manipulate structured information.
- Implement account creation and login workflows.
- Perform buying and selling transactions.
- Maintain persistent data using CSV and Excel files.
- Generate visual reports using Matplotlib.
- Apply input validation and type hints.
- Organize a Python project for version control and portfolio presentation.

---

## 🚀 Future Improvements

Potential improvements for future versions include:

- Integrate a financial market API to retrieve real stock prices.
- Add transaction history with timestamps.
- Introduce more detailed profit and loss calculations.
- Improve password security using password hashing.
- Migrate CSV and Excel storage to a relational database such as MySQL.
- Add unit tests for authentication and portfolio transactions.
- Improve error handling for missing or corrupted files.
- Add portfolio performance charts over time.
- Introduce stock search, filtering, and sorting.
- Build a graphical user interface or web dashboard.
- Support dividends, transaction fees, and average purchase prices.

---

## 👤 Author — Qais Said

**Python Programming Intern at CodeAlpha**

This project was developed as part of my Python Programming Internship at CodeAlpha.

It demonstrates my practical application of Python, Object-Oriented Programming, Pandas, Matplotlib, data persistence, and portfolio-management logic.

**GitHub Repository:** [CodeAlpha_Stock_Portfolio_Tracker](https://github.com/QaisSaid-2007/CodeAlpha_Stock_Portfolio_Tracker)

---

## 📜 License

This project is intended for educational and learning purposes.

Please refer to the repository's license file, if available, for the applicable usage and distribution terms.

---

**Disclaimer:** This project is an educational stock portfolio simulation. It does not provide financial advice, use live market prices, or execute real stock trades.
