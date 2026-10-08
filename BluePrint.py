from abc import ABC, abstractmethod
import pandas as pd
 
class Abst_Portfolio(ABC):
    
    @abstractmethod
    def buy_stock(self) -> None:
        ...
    
    @abstractmethod
    def sell_stock(self) -> None:
        ...
        
class Abst_Data(ABC):
    
    @abstractmethod
    def stock_market(self) -> pd.DataFrame:
        ...

    @abstractmethod
    def users_portfolio_database(self) -> pd.DataFrame:
        ...

    @abstractmethod
    def display_portfolio(self):
        ...

class Abst_Login_Signin(ABC):

    @abstractmethod
    def login(self) -> bool:
        ...

    @abstractmethod
    def signin(self) -> bool:
        ...

    @abstractmethod
    def reset_password(self) -> None:
        ...

