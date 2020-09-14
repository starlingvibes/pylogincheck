while True:
    username = ["admin", "sysadmin", "ceo", "cto"]
    user = input ("Enter a username: ")
    if (user == username[0]) or (user == username[1]) or (user == username[2]) or (user == username[3]):
        print ("Please proceed to login with ID")
    else:
        print ("Invalid user")
