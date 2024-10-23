import csv

with open("csv_files/14users.csv","w") as f:
    writer = csv.writer(f)
    writer.writerow(["username","password"])
    writer.writerow(["omori","omori123"])
    writer.writerow(["mori","mori123"])
    writer.writerow(["sunny","sunny123"])

def auth(username,password):
    with open("csv_files/users.csv","r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == username and row[1] == password:
                return "User Found"
        return "User Not Found"
while True:
    print('''1 to add user
2 to search user
3 to exit''')
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        with open("users.csv","a") as f:
            writer = csv.writer(f)
            writer.writerow([username,password])
    if choice == 2:
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        print(auth(username,password))
    if choice == 3:
        break 