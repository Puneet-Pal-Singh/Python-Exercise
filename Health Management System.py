"""
This Program logs clients data like exercise,diet and display it with time stamp when needed.
"""


# Health Management System
client_list = {1:"Harry", 2:"Rohan", 3:"Hammad"}
log_list = {1:"Exercise", 2:"Diet"}

def getdate():
    import datetime
    return datetime.datetime.now()

try:
    print("Select Client Name:")
    for key, value in client_list.items():
        print("Press", key, "for", value, "\n", end="")
    client_name = int(input("Enter here:"))

    print("Selected Client : ", client_list[client_name], "\n", end="")

    print("Press 1 for Log-")
    print("Press 2 for Retrieve-")
    op = int(input("Enter Here:"))

    if op is 1:
        for key, value in log_list.items():
            print("Press", key, "to log", value, "\n", end="")
        log_name = int(input("Enter here:"))

        print("Selected Job : ", log_list[log_name])
        f = open(client_list[client_name] + "_" + log_list[log_name] + ".txt", "a")
        k = 'y'
        while(k is not "n"):
            print("Enter", log_list[log_name], "\n", end="")
            mytext = input()
            f.write("[ " + str(getdate()) + " ] : " + mytext + "\n")
            k = input("ADD MORE ? y/n:")
            continue
        f.close()

    elif op is 2:
        for key, value in log_list.items():
            print("Press", key, "to retrieve", value,"\n", end="")
        log_name = int(input("Enter here:"))

        print(client_list[client_name], "-", log_list[log_name], "Report : ", "\n", end="")
        f = open(client_list[client_name] + "_" + log_list[log_name] + ".txt", "rt")
        contents = f.readlines()
        for line in contents:
            print(line, end="")
        f.close()

    else:
        print("Invalid Input !!!")

except Exception as e:
    print("Wrong Input !!!")
    
 # Output
 
    Select Client Name:
Press 1 for Harry 
Press 2 for Rohan 
Press 3 for Hammad 
Enter here:1
Selected Client :  Harry 
Press 1 for Log-
Press 2 for Retrieve-
Enter Here:1
Press 1 to log Exercise 
Press 2 to log Diet 
Enter here:1
Selected Job :  Exercise
Enter Exercise 
Dumbbell Curls
ADD MORE ? y/n:y
Enter Exercise 
Barbell
ADD MORE ? y/n:n


Select Client Name:
Press 1 for Harry 
Press 2 for Rohan 
Press 3 for Hammad 
Enter here:1
Selected Client :  Harry 
Press 1 for Log-
Press 2 for Retrieve-
Enter Here:2
Press 1 to retrieve Exercise 
Press 2 to retrieve Diet 
Enter here:1
Harry - Exercise Report :  
[ 2019-07-25 21:02:48.692245 ] : Barbell
[ 2019-08-28 21:01:46.956440 ] : Dumbbell Curls
[ 2019-08-28 21:02:13.702637 ] : Barbell

