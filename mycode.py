name=input("Enter Your Name:")
balance=float(input("Enter your account balance:"))
withdraw=float(input("Enter your withdraw balance:"))


if withdraw<=balance:
    balance=balance-withdraw
    print("Transaction in sucessfull")
    print(f"*{name}* Your Remaning Account Balance is:",balance)
else:
    print(f"{name} You Have Insufficient Balance")
    
print("ATM Transaction is Sucessfull")
print("*********THANK YOU***********")
print("        Visit Again       ")
