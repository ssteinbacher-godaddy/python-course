#get details of loan
money_owed = float(input('How much money do you owe in dollars?\n')) 
apr = float(input('What is the annual percentage rate of the loan? \n'))
payment = float(input('What will your monthly payment be in dollars? \n'))  
months = int(input('How many months will it take to pay off the loan? \n')) 

monthly = apr / 12 / 100

for i in range(months):
    #calculate monthly payment
    interest_paid = money_owed * monthly
    #add in interest
    money_owed = money_owed + interest_paid

    if (money_owed - payment < 0):
        print('The last payment is', money_owed)
        print('You paid off the loan in', i+1, 'months')
        break
    #make payment
    money_owed = money_owed - payment

    print('Paid', payment, 'of which', interest_paid, 'was interest', end= ' ')
    print('Now I owe', money_owed)
