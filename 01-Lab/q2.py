import pandas as pd


class AccountError(ValueError):
    pass


class AccountsDataFrame(pd.DataFrame):
    def __init__(self, name, acc_no, acc_type, adhaar_no, balance, csv_path=''):
        super().__init__({
            'Name': name,
            'Account_Number': acc_no,
            'Account_Type': acc_type,
            'Adhaar_No': adhaar_no,
            'Balance': balance
        })
        self.csv_path = csv_path
    
    def input_acc_no(self, new):
        acc_no = int(input("Enter the account number: "))
        is_present = acc_no in self['Account_Number'].values
        if not new and not is_present:
            print("Account number not found")
            raise AccountError
        elif new and is_present:
            print("Account number already exists")
            raise AccountError
        return acc_no
    
    def input_acc_type(self):
        acc_type = input("Enter the account type: ").strip().upper()
        if acc_type not in ['SB', 'CA']:
            print("Invalid account type")
            raise AccountError
        return acc_type
    
    def input_amount(self, string="amount"):
        amount = int(input(f"Enter the {string}: "))
        if amount <= 0:
            print("Invalid amount")
            raise ValueError
        return amount
    
    def get_acc_type(self, acc_no):
        return self[self['Account_Number'] == acc_no]['Account_Type'].values[0]
    
    def get_balance(self, acc_no):
        return self[self['Account_Number'] == acc_no]['Balance'].values[0]
    
    def add_record(self, name, acc_no, acc_type, adhaar_no, balance):
        self.loc[len(self)] = [name, acc_no, acc_type, adhaar_no, balance]
        print("Record added successfully:")
        print(self.iloc[-1])
    
    def delete_record(self, acc_no):
        self.drop(self[self['Account_Number'] == acc_no].index, inplace=True)
        self.reset_index(drop=True, inplace=True)
        print("Record deleted successfully.")
    
    def update_balance(self, acc_no, amount):
        self.loc[self['Account_Number'] == acc_no, 'Balance'] += amount
        print(f"Balance updated successfully to: {self.get_balance(acc_no)}")
    
    def save(self):
        self.to_csv(self.csv_path, index=False)


sbi_df = AccountsDataFrame(
    ['Ram', 'Sam', 'Prabhu'],
    [9893893891, 9893893898, 9893893871],
    ['SB', 'CA', 'SB'],
    [959389389173, 959389389179, 959389389159],
    [8989839, 7690990, 989330],
    csv_path='SBIAccountHolder.csv'
)
sbi_df.save()

print("Welcome to SBI Bank")
print(sbi_df)

print("\nOperations related to SBI Bank:")
print(" 1. Append Record")
print(" 2. Delete Record")
print(" 3. Credit Amount")
print(" 4. Debit Amount")
print(" 5. Print Account Details")
print(" 6. Exit")

while True:
    opt = int(input("\nEnter your choice: "))
    print()
    if opt == 6:
        print("Exiting...")
        break

    if opt == 1:
        print("Append Record: ")

        try:
            name = input("Enter the name: ")
            acc_no = sbi_df.input_acc_no(new=True)
            acc_type = sbi_df.input_acc_type()
            adhaar_no = int(input("Enter the adhaar number: "))
            balance = sbi_df.input_amount(string="initial balance")
        except ValueError:
            print("Invalid input")
            continue

        sbi_df.add_record(name, acc_no, acc_type, adhaar_no, balance)
        sbi_df.save()

    elif opt == 2:
        print("Delete Record: ")

        try:
            acc_no = sbi_df.input_acc_no(new=False)
        except AccountError:
            continue

        sbi_df.delete_record(acc_no)
        sbi_df.save()

    elif opt == 3:
        print("Credit Amount: ")

        try:
            acc_no = sbi_df.input_acc_no(new=False)
            print("Current Balance: ", sbi_df.get_balance(acc_no))
            amount = sbi_df.input_amount()
        except AccountError:
            continue

        sbi_df.update_balance(acc_no, amount)
        sbi_df.save()

    elif opt == 4:
        print("Debit Amount: ")

        try:
            acc_no = sbi_df.input_acc_no(new=False)
            print("Current Balance: ", sbi_df.get_balance(acc_no))
            amount = sbi_df.input_amount()
        except AccountError:
            continue

        if sbi_df.get_acc_type(acc_no) == 'SB':
            if sbi_df.get_balance(acc_no) - amount < 0:
                print("Insufficient balance")
                continue

        sbi_df.update_balance(acc_no, -amount)
        sbi_df.save()

    elif opt == 5:
        print("Print Account Details: ")
        
        try:
            acc_no = sbi_df.input_acc_no(new=False)
        except AccountError:
            continue
        
        print(sbi_df[sbi_df['Account_Number'] == acc_no])
