import time
cdetails=[123456789,987654321]
card=int(input("Please Enter Card Details: "))
time.sleep(5)
for i in cdetails:
    if i == card:
        print("Your card No.:",card)
    else:
        break
password=1234
pin=int(input("Enter Your ATM PIN: "))
balance=5000
if pin==password:
    while True:
        print("""
          1 == Balance
          2 == Withdrae Balance
          3 == Desposit Balance
          4 -- Exit
          """)
        try:
            option=int(input("Please Enter Your Choice: "))
        except:
            print("Please Enter Valid Option!")
        if option==1:
            print(f"Your Current balance is {balance}")
        elif option==2:
            withdraw_amnt=int(input("Please enter withdraw amt: "))
            balance=balance-withdraw_amnt
            print(f"{withdraw_amnt} is debited from you Account")
            print(f"Your Updated balance is {balance}")
        elif option==3:
            deposit_amnt=int(input("Please Enter Deposit Amount: "))
            balance=balance+deposit_amnt
            print(f"{deposit_amnt} is credited to your account")
            print(f"Your current Balance is {balance}")
        elif option==4:
            print("Bye!")
            break
        else:
            print("Wrong Input Please try again!")