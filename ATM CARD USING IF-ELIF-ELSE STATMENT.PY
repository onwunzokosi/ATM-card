server =[1234.6534,7864,0000]
pin =int(input('please enter pin:'))
options=['withdraw','transfer','enquire']
amount=[500,1000,2000,5000,10000,'0thers']
if pin in server:
    print('pin correct')
    account_type=['current','savings','fixed']
    print(account_type)
    select_type=input('select account type:')
    if select_type in account_type:
        print('do you wish to withdraw,transfer or enquire')
        a=input('select optiions:')
        if a in options:
            print(amount)
            d=int(input('enter amount:'))
            if d in amount:
                print('collect cash')
            else:
                print('insufficient fund')
                print('enter lower amount')
        else:
            print('choose a valid options')
    else:
        print('invalid account type')
else:
    print('incorrect pin')
