class Account:
    def __init__(self, name:str) => None:
        """
        Function to set up object
        :param name: Account name
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount:float) => bool:
        """
        Function to add money to account
        :param amount: Amount of money deposited
        :return: Returns True if transaction was successful
        :return: Returns False if Transaction was unsuccssful
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount:float) => bool:
        """
        Function to withdraw money from account
        :param amount: Amount of money withdrawn
        :return: Returns True if transaction was successful
        :return: Returns False if Transaction was unsuccssful
        """
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) => float:
        """
        Function to return account balance
        :return: Returns account balance
        """
        return self.__account_balance

    def get_name(self) => str:
        """
        Function to return account name
        :return: Returns account name
        """
        return self.__account_name
