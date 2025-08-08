username = ['admin', 'Kriztel', 'Aj', 'Mecaella', 'Bawit']
for username in username:
    if username == 'admin':
        print(f"Hello {username}, would you like to see the status report today?\n")
    elif username == "":
        print(f"We need to find some users!")
    else:
        print(f"Hello {username} \n")