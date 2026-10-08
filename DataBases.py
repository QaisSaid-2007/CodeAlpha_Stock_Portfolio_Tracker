from BluePrint import Abst_Data
import pandas as pd
import matplotlib.pyplot as plt

class Data(Abst_Data):
    
    def stock_market(self) -> pd.DataFrame:
        df = pd.read_excel("Portfolio_Stock_Tracker_Large.xlsx")
        pd.set_option('display.max_rows',None)
        return df

    def users_portfolio_database(self) -> pd.DataFrame:
        df = pd.read_csv("Users_Portfolio.csv",dtype={"Balance":float,"Profit":float,"Investments":'str'})
        return df

    def display_portfolio(self,username:str) -> None:
        df_portfolio = self.users_portfolio_database()
        stocks_code = df_portfolio.loc[df_portfolio['Username'] == username,'Investments'].iloc[0]
        profit = df_portfolio.loc[df_portfolio['Username'] == username, 'Profit'].iloc[0]

        if isinstance(stocks_code,float):
            print(f"\n{username} - Investments: ${abs(10000 + (10000 * (profit / 100)))} | Profit: {profit}%\n")
            return None

        stocks_shares: dict[str,str] = {}
        step1: list[str] = stocks_code.split('$')
        for s in step1:
            key,value = s.split('^')
            stocks_shares[key] = stocks_shares.get(key,0) + int(value)

        plt.style.use("Solarize_Light2")
        plt.title(f"{username} - Investments: ${abs(10000 + (10000 * (profit / 100)))} | Profit: {profit}%")
        plt.pie(stocks_shares.values(),labels=stocks_shares.keys(),shadow=True,autopct="%1.1f%%")
        plt.legend(stocks_shares.values())
        total_shares = sum(stocks_shares.values())

        plt.show()
        

    def users_database(self) -> pd.DataFrame:
        df = pd.read_csv("Usernames_Passwrods.csv",dtype={'Password':str})
        return df


def main() -> None:
    pass

if __name__ == "__main__":
    main()