from BluePrint import Abst_Portfolio, Abst_Login_Signin
from DataBases import Data
import pandas as pd
import random

class Portfolio(Abst_Portfolio):
    def __init__(self) -> None:
        self.stock_market = Data().stock_market()
        self.Users_Portfolio = Data().users_portfolio_database()

    def update_stock_calculate_profit(self) -> None:
        def func_stock(x:float) -> float:
            market = ['+','-']
            trend = random.choice(market)
            if trend == '+':
                return abs(x + random.getrandbits(15) % 99)
            else:
                return abs(x - random.getrandbits(15) % 99)

        def func_profit(username:str,stocks_code:str) -> float:
            total: float = self.Users_Portfolio.loc[self.Users_Portfolio['Username'] == username,'Balance'].iloc[0]

            if stocks_code == '':
                return (( (total - 10000) / 10000) * 100 ).round(2)

            stocks_shares: dict[str,str] = {}
            step1: list[str] = stocks_code.split('$')
            for s in step1:
                key,value = s.split('^')
                stocks_shares[key] = stocks_shares.get(key,0) + int(value)

            for key,value in stocks_shares.items():
                share_price = self.stock_market.loc[self.stock_market['Ticker'] == key,'Price'].iloc[0]
                total += (share_price * value)
            
            return (( (total - 10000) / 10000) * 100 ).round(2)

        self.stock_market['Price'] = self.stock_market.apply(lambda x: func_stock(x['Price']),axis=1)
        self.stock_market.to_excel("Portfolio_Stock_Tracker_Large.xlsx",index=False)

        self.Users_Portfolio['Profit'] = self.Users_Portfolio.apply(lambda x: func_profit(x['Username'],x['Investments']),axis=1)
        self.Users_Portfolio.to_csv("Users_Portfolio.csv",index=False)
    
    def buy_stock(self,username:str) -> None:
        print("********** Stock Market **********\n")
        print(self.stock_market)
        print("\n********** Stock Market **********\n")

        users_balance: float = self.Users_Portfolio.loc[self.Users_Portfolio['Username'] == username,'Balance'].iloc[0]
        stocks_invested_in: str = self.Users_Portfolio.loc[self.Users_Portfolio['Username'] == username,'Investments'].iloc[0]
        ticker_valid: bool = False
        ticker: None|str = None

        while not ticker_valid:
            ticker = input("Enter the Ticker of the stock you want to buy: ")
            if ticker in set(self.stock_market['Ticker'].to_list()):
                ticker_valid = True
            else:
                print('Invalid stock ticker !!!')

        stock = self.stock_market.loc[self.stock_market['Ticker'] == ticker,["Stock Name","Price"]].iloc[0].to_dict()
        max_shares_to_buy: int = int(users_balance // stock['Price'])

        print(f"\nThe stock '{stock['Stock Name']}' is priced at ${stock['Price']}")
        print(f"Max shares you can buy: {max_shares_to_buy} shares") 

        valid_share: bool = False
        shares: None|int = None
        while not valid_share:
            shares = input("Enter the number of share you want to buy: ")
            if shares.isnumeric():
                if int(shares) <= max_shares_to_buy:
                    shares = int(shares)
                    valid_share = True
                else:
                    print("Invalid number of shares !!!")
            else:
                print("Invalid input !!!")

        stock_bought: str = stock['Stock Name']
        shares_bought: int = shares
        stock_price: float = stock['Price']
        total_cost: float = shares * stock_price
        
        new_balance: float = round(users_balance - total_cost,2)
        if str(stocks_invested_in) == 'nan':
            new_stocks_invested_in = ticker + '^' + str(shares_bought)
        else:
            new_stocks_invested_in = stocks_invested_in +'$' + ticker + '^' + str(shares_bought) 

        self.Users_Portfolio.loc[self.Users_Portfolio['Username'] == username, ['Balance','Investments']] = new_balance, new_stocks_invested_in

        self.Users_Portfolio.to_csv("Users_Portfolio.csv",index=False)
        
        print(f"\n********** --BUY -- Transaction Overview -- BUY -- **********")
        print(f"Stock: {stock_bought}\nShares: {shares_bought}\nStock price: {stock_price}$\nTotal: {total_cost}$\n")
        self.update_stock_calculate_profit()

    def sell_stock(self,username:str) -> None:
        stocks_code: str | float = self.Users_Portfolio.loc[self.Users_Portfolio['Username'] == username,'Investments'].iloc[0]
        balance: float = self.Users_Portfolio.loc[self.Users_Portfolio['Username'] == username, 'Balance'].iloc[0]

        if isinstance(stocks_code,float):
            print("\nYou don't have stocks to sell !!!\n")
            return

        stocks_shares: dict[str,str] = {}
        step1: list[str] = stocks_code.split('$')
        for s in step1:
            key,value = s.split('^')
            stocks_shares[key] = stocks_shares.get(key,0) + int(value)

        print("Whick of the following stocks you want to sell -> ")
        for key in stocks_shares.keys():
            print(f"{key} | ",end=' ')

        stock_wants_to_sell_ticker: str|None = None
        valid_stock: bool = False
        while not valid_stock:
            stock_wants_to_sell_ticker = input("\nEnter the stock you want to sell (ticker): ")
            if stock_wants_to_sell_ticker in stocks_shares:
                valid_stock = True
            else:
                print('Invalid input')

        shares_owned: int = int(stocks_shares[stock_wants_to_sell_ticker])
        shares_to_sell: int|None = None
        valid_shares: bool = False
        while not valid_shares:
            shares_to_sell = input(f"How many shares you want to sell (max = {shares_owned}): ") 
            if shares_to_sell.isnumeric():
                shares_to_sell = int(shares_to_sell)
                if 1 <= shares_to_sell <= shares_owned:
                    valid_shares = True
                else:
                    print('Invalid number of shares !!!')
            else:
                print('Invalid Input !!!')

        if shares_to_sell == shares_owned:
            del stocks_shares[stock_wants_to_sell_ticker]
        else:
            new_shares_value = shares_owned - shares_to_sell
            stocks_shares[stock_wants_to_sell_ticker] = str(new_shares_value)

        empty_investments: bool = len(stocks_shares) == 0

        share_price: float = self.stock_market.loc[self.stock_market['Ticker'] == stock_wants_to_sell_ticker,'Price'].iloc[0]
        new_balance: float = round(balance + (share_price * shares_to_sell),2)
        new_stocks_code: str = ''
        n: int = 0
        if not empty_investments:
            for key,value in stocks_shares.items():
                if n == 0:
                    new_stocks_code += f"{key}^{value}"
                else:
                    new_stocks_code += f"${key}^{value}"
                n += 1

        self.Users_Portfolio.loc[self.Users_Portfolio['Username'] == username,['Balance','Investments']] = new_balance, new_stocks_code
        self.Users_Portfolio.to_csv("Users_Portfolio.csv",index=False)

        print(f"\n********** --SELL -- Transaction Overview -- SELL -- **********")
        print(f"Stock: {stock_wants_to_sell_ticker}\nShares: {shares_to_sell}\nStock price: {share_price}$\nTotal: {share_price * shares_to_sell}$\n")
        self.update_stock_calculate_profit()

class Login_Signin(Abst_Login_Signin):
    """ Login_Signin class provides different ways for the user to either log in to his account or create a new account, with the ability to reset his password.
        Class Constructor: Gets the users' database via composition from another file (DataBases.py), which contains the usernames and passwords.
    """
    def __init__(self) -> None:
        self.users_database: pd.dataFrame = Data().users_database()
        self.Users_Portfolio = Data().users_portfolio_database()

    def update_users_database(self) -> None:
        """ Updates the original users' database every time a new account is created or a password is reset.
            Return type: None
        """
        self.users_database.to_csv("Usernames_Passwrods.csv",index=False)
    
    def login(self,username:str) -> bool:
        """ Logs the user back into their account.
            Return type: True if the login process was successful; otherwise, False if the password is incorrect or the account does not exist. """

        df = self.users_database[self.users_database['Username'] == username]

        if not df.empty:
            password = input(f"Username: {username} | Password: ")

            if df.iloc[0,1] == password:
                return True

            print("Wrong password !!!")
            wants_new_password = input('Enter (1) to create new password: ')

            if wants_new_password == '1':
                if self.reset_password(username):
                    self.update_users_database()
                    return True
        else:
            print("Username not found !!!")

        return False

    def signin(self) -> bool:
        """ Creates a new account.
            return type: True if the account is created, False if the account already exists or password check was not passed."""

        username = input("Enter your username to create your account: ")
        df = self.users_database[self.users_database['Username'] == username] 

        if df.empty:
            password = input(f"Enter your {username=} password: ")

            if input(f"Re-enter the password: ") == password:
                self.users_database.loc[len(self.users_database)] = {'Username':username,'Password':password}
                self.update_users_database()
                print("***** Account Created *****")
                self.Users_Portfolio.loc[len(self.Users_Portfolio),['Username','Balance']] = username,10000
                self.Users_Portfolio.to_csv("Users_Portfolio.csv",index=False)
                return True

            else:
                print("Passwords do not match !!!")
        else:
            print(f"{username=} is already taken try another username or login")

        return False

    def reset_password(self,username:str) -> bool:
        """Resets the password of the specified user.
           Returns:
                    bool: True if the password was successfully changed;
                    False if the two entered passwords do not match.
        """

        password = input(f'Enter your new password for the {username=}: ')
        password_check = input('Re-Enter the password: ')

        if password == password_check:
            self.users_database.loc[ self.users_database['Username'] == username,'Password'] = password
            print("*** Password changed ***")
            return True

        print("Passwords do not match !!!")

        return False

def main() -> None:
    print("*************** ON - Stock Portfolio - ON ***************")
    username: str = ''
    running_phase_1: bool = True
    ls: Login_Signin = Login_Signin()
    while running_phase_1:
        print("1 -> Login\n2 -> Sign in\n3 -> QUIT")
        method = input("Enter your method (1 for login or 2 for sign in): ")
        is_account: bool|None = None
        match method:
            case '1':
                username = input("Enter your Username to Login: ")
                is_account = ls.login(username)
                if is_account:
                    running_phase_1 = False
                else:
                    print("Failed to Login into your account !!!")
            case '2':
                is_account = ls.signin()
                if is_account:
                    running_phase_1 = False
                    print("Login again using your new account")
                    return None
                else:
                    print("Failed to create an account !!!")
            case '3':
                print("*************** OFF - Stock Portfolio - OFF ***************")
                running_phase_1 = False
                return None
            case _:
                print("You are only allowed to Enter 1 or 2 !!!")

    running_phase_2: bool = True
    pt : Portfolio = Portfolio()
    while running_phase_2:
        print("1 -> Buy Shares\n2 -> Sell Shares\n3 -> Show Portfolio\n4 -> QUIT")
        operation = input("Enter your Operation Option (number): ")
        match operation:
            case '1':
                pt.buy_stock(username)
            case '2':
                pt.sell_stock(username)
            case '3':
                Data().display_portfolio(username)
            case '4':
                print("*************** OFF - Stock Portfolio - OFF ***************")
                running_phase_2 = False
                return None
            case _:
                print("You are only allowed to Enter the number (1,2,3 or 4) !!!")

if __name__ == "__main__":
    main()