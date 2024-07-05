# import zipfile
# import pandas as pd

# class Paisa:
#     def __init__(self, user_name, user_number, user_ammount, user_email, deposit_amount):
#         self.user_name = user_name
#         self.user_number = user_number
#         self.user_ammount = user_ammount
#         self.user_email = user_email
#         self.deposit_amount= deposit_amount

#     def create_account(self):
#         user_data = {
#             "ACCOUNT_NUMBER": [self.user_number],
#             "USER_NAME": [self.user_name],
#             "USER_AMMOUNT": [self.user_ammount],
#             "USER_EMAIL": [self.user_email]
#         }
#         df = pd.DataFrame(user_data)
#         try:
#             existing_df = pd.read_excel("PaisaData.xlsx", engine='openpyxl')
#             updated_df = pd.concat([existing_df, df], ignore_index=True)
#         except FileNotFoundError:
#             print("File not found. Creating a new Excel file.")
#             updated_df = df
#         except (ValueError, zipfile.BadZipFile):
#             print("File is not a valid Excel file or is corrupted. Creating a new Excel file.")
#             updated_df = df
#         try:
#             updated_df.to_excel("PaisaData.xlsx", index=False, engine='openpyxl')
#             print("User created successfully with name and account number:", self.user_name, self.user_number)
#         except Exception as e:
#             print(f"Failed to write to Excel file: {e}")

#     def deposit_amount(self):
#         try:
#             df = pd.read_excel("PaisaData.xlsx", engine="openpyxl")
#             if self.user_number in df["ACCOUNT_NUMBER"].values:
#                 df.loc[df["ACCOUNT_NUMBER"] == self.user_number, 'USER_AMMOUNT'] += self.deposit_amount
#                 df.to_excel("PaisaData.xlsx", index=False, engine='openpyxl')
#                 print(f"Deposited {self.deposit_amount} to account number {self.user_number}.")
#             else:
#                 print(f"Account number {self.user_number} not found.")
#         except Exception as e:
#             print(f"An error occurred: ",e)


# obj1 = Paisa("nj", 12345, 2000, "nj@gmail.com", 0)
# # obj1.create_account()

# obj1.deposit_amount(500)


import zipfile
import pandas as pd

class Paisa:
    def __init__(self, user_name, user_number, user_ammount, user_email, deposit_amount=0):
        self.user_name = user_name
        self.user_number = user_number
        self.user_ammount = user_ammount
        self.user_email = user_email
        self.deposit_amount = deposit_amount

    def create_account(self):
        user_data = {
            "ACCOUNT_NUMBER": [self.user_number],
            "USER_NAME": [self.user_name],
            "USER_AMMOUNT": [self.user_ammount],
            "USER_EMAIL": [self.user_email]
        }
        df = pd.DataFrame(user_data)
        try:
            existing_df = pd.read_excel("PaisaData.xlsx", engine='openpyxl')
            updated_df = pd.concat([existing_df, df], ignore_index=True)
        except FileNotFoundError:
            print("File not found. Creating a new Excel file.")
            updated_df = df
        except (ValueError, zipfile.BadZipFile):
            print("File is not a valid Excel file or is corrupted. Creating a new Excel file.")
            updated_df = df
        try:
            updated_df.to_excel("PaisaData.xlsx", index=False, engine='openpyxl')
            print("User created successfully with name and account number:", self.user_name, self.user_number)
        except Exception as e:
            print(f"Failed to write to Excel file: {e}")

    def make_deposit(self, amount):
        try:
            df = pd.read_excel("PaisaData.xlsx", engine="openpyxl")
            if self.user_number in df["ACCOUNT_NUMBER"].values:
                df.loc[df["ACCOUNT_NUMBER"] == self.user_number, 'USER_AMMOUNT'] += amount
                df.to_excel("PaisaData.xlsx", index=False, engine='openpyxl')
                print(f"Deposited {amount} to account number {self.user_number}.")
            else:
                print(f"Account number {self.user_number} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
    def make_withdraw(self, amount):
        try: 
            df = pd.read_excel("PaisaData.xlsx", engine="openpyxl")
            if self.user_number in df["ACCOUNT_NUMBER"].values:
                df.loc[df['ACCOUNT_NUMBER'] == self.user_number, 'USER_AMMOUNT'] -= amount
                df.to_excel("PaisaData.xlsx",index=False, engine='openpyxl')
                print(f"Withdraw {amount} done in account number {self.user_number}.")
            else:
                print(f"User not having sufficient money in account number {self.user_number}")
        except FileNotFoundError:
            print("File not found man..:(")

    
    def get_balance(self):
        try:
            df = pd.read_excel("PaisaData.xlsx", engine="openpyxl")
            if self.user_number in df["ACCOUNT_NUMBER"].values:
                balance = df.loc[df["ACCOUNT_NUMBER"] == self.user_number, 'USER_AMMOUNT'].values[0]
                print(f"The current balance for account number {self.user_number} is {balance}.")
                return balance
            else:
                print(f"Account number {self.user_number} not found.")
                return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

# Create account uffff!!!!!!!!!!!1
obj1 = Paisa("nj", 12345, 2000, "nj@gmail.com")
# obj1.create_account()
# obj1.make_deposit(500)
obj1.make_withdraw(500)
obj1.get_balance()
