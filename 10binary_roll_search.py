import pickle 

with open("bin_files/binary_roll.bin", "wb") as f:
    
    data =[{"name":"Omori","roll":1},
    {"name":"Mori","roll":2},
    {"name":"Sunny","roll":3},]

    pickle.dump(data, f)

def search_roll(roll):
    with open("bin_files/binary_roll.bin", "rb") as f:
        data = pickle.load(f)
        for i in data:
            if i["roll"] == roll:
                return i["name"]
        return "Not Found"
    
print(search_roll(int(input("Enter Roll Number: "))))    