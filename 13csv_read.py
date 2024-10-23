import csv

with open("csv_files/13users.csv","w") as f:
    writer = csv.writer(f)
    writer.writerow(["username","password"])
    writer.writerow(["omori","omori123"])
    writer.writerow(["mori","mori123"])
    writer.writerow(["sunny","sunny123"])

def display_1_coloumn(coloumn):
    try: 
      with open("csv_files/users.csv","r") as f:
          reader = csv.reader(f)
          for row in reader:
              print(row[coloumn-1])
    except:
        "Invalid Coloumn"                
display_1_coloumn(int(input("Enter Coloumn Number: ")))        