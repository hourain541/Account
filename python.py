all_acccounts = []
import random


def open_account(cnic ,title, initial_deposite):
  account= {'cinic'              :cnic,
            'title'              :title,
            'balance'            :initial_deposite,
            'account_balance'    :random.randint(1001,9999),
            'pin'                :random.randint(1001,9999)
  }
  all_acccounts.append(account)
  return f""" your account has succuessfully created
              your account number is {account['account_number']}
              your pin is {account['pin']}"""
def transfer(account,pin,amt,bacc):
    for ba in all_acccounts:
      if ba['account_number'] ==bacc:
        for acc in all_acccounts:
          if acc['account_number'] ==account:
            if acc['pin'] ==pin:
              if acc['balance'] >=amt:
                acc['balance'] -=amt
                return f'{amt} transfered successfully.'
              else:
                return "Insufficient Amount"
            else:
              return "Invalid Account Number"
        else:
          return "Invalid Beneficiary Account Number"         