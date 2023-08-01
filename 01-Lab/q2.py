import pandas as pd


class AccountsData(dict):
    def __init__(self, name, acc_no, acc_type, adhaar_no, balance):
        self.update({
            'Name': name,
            'Account Number': acc_no,
            'Account Type': acc_type,
            'Adhaar_No': adhaar_no,
            'Balance': balance
        })


sbi_data = AccountsData(
    ['Ram', 'Sam', 'Prabhu'],
    [9893893891, 9893893898, 9893893871],
    ['SB', 'CA', 'SB'],
    [959389389173, 959389389179, 959389389159],
    [8989839, 7690990, 989330]
)

# sbi_data = {
#     'Name': ['Ram', 'Sam', 'Prabhu'],
#     'Account Number': [9893893891, 9893893898, 9893893871],
#     'Account Type': ['SB', 'CA', 'SB'],
#     'Adhaar_No': [959389389173, 959389389179, 959389389159],
#     'Balance': [8989839, 7690990, 989330]
# }

sbi_df = pd.DataFrame(sbi_data)

sbi_df.to_csv('SBIAccountHolder.csv', index=False)

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
    if opt == 6:
        print("Exiting...")
        break

    if opt == 1:
        print("Append Record: ")

        name = input("Enter the name: ")
        acc_no = int(input("Enter the account number: "))
        acc_type = input("Enter the account type: ")
        adhaar_no = int(input("Enter the adhaar number: "))
        balance = int(input("Enter the balance: "))
        new_record = AccountsData([name], [acc_no], [acc_type], [adhaar_no], [balance])

        sbi_df = pd.concat([sbi_df, new_record], ignore_index=True)
        sbi_df.to_csv('SBIAccountHolder.csv', index=False)
    
    elif opt == 2:
        print("Delete Record: ")
        acc_no = int(input("Enter the account number: "))
        sbi_df = sbi_df[sbi_df['Account Number'] != acc_no]
        sbi_df.to_csv('SBIAccountHolder.csv', index=False)

    elif opt == 3:
        print("Credit Amount: ")
        acc_no = int(input("Enter the account number: "))
        amount = int(input("Enter the amount to be credited: "))
        if amount <= 0:
            print("Invalid amount")
            continue
        sbi_df.loc[sbi_df['Account Number'] == acc_no, 'Balance'] += amount
        sbi_df.to_csv('SBIAccountHolder.csv', index=False)

    elif opt == 4:
        print("Debit Amount: ")
        acc_no = int(input("Enter the account number: "))
        amount = int(input("Enter the amount to be debited: "))
        if amount <= 0:
            print("Invalid amount")
            continue
        if sbi_df.loc[sbi_df['Account Number'] == acc_no, 'Balance'].values[0] < amount:
            print("Insufficient balance")
            continue
        sbi_df.loc[sbi_df['Account Number'] == acc_no, 'Balance'] -= amount
        sbi_df.to_csv('SBIAccountHolder.csv', index=False)

    elif opt == 5:
        print("Print Account Details: ")
        acc_no = int(input("Enter the account number: "))
        print(sbi_df[sbi_df['Account Number'] == acc_no])
