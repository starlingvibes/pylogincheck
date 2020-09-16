while True:
    username = ["admin", "sysadmin", "ceo", "cto"]
    user = input ("Enter a username: ")
    if user in username:
        print ("Please proceed to login with ID")
    else:
        print ("Invalid user")
