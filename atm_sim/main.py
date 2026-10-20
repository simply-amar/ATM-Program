prt_list = ["Check Balance", "Deposite Money", "Withdraw Money", "Exit"]
balance = []


while True:
    total_balance = sum(balance)
    i=0
    for items in prt_list:
        i += 1
        print(f"{i}.{items}")
    
    opt = int(input("Enter the corresponding number for the function you want to perform: "))


    if  opt == 1:
        print("The balance in your account is:",total_balance)
        continue
    elif opt == 2:
        depo_amt = int(input("Enter the amount you want to deposite to your account: "))
        balance.append(depo_amt)
        print(f"Deposited {depo_amt}")
        print(f'Now your balance is {total_balance}')
        continue
    elif opt == 3:
        withd_amt = int(input("Enter the amount you want to withdraw: "))
        if withd_amt>balance:
            print(f"You can't withdraw the amount of money that you don't have. Please withdraw below {total_balance}")
    elif opt == 4:
        exit()
    else:
        print("Enter the correct operator")
        break