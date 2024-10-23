import pickle

with open("bin_files/binary_marks.bin", "wb") as f:
    
    data =[{"roll":1,"name":"Omori","marks":90},
    {"roll":2,"name":"Mori","marks":80},
    {"roll":3,"name":"Sunny","marks":70},]

    pickle.dump(data, f)

def update_marks(roll, marks):
    with open("bin_files/binary_marks.bin", "rb+") as f:
        data = pickle.load(f)
        for i in data:
            if i["roll"] == roll:
                i["marks"] = marks
                f.seek(0)
                pickle.dump(data, f)
                return "Success",(i["name"],i["marks"])
        return "Not Found"    

print(update_marks(int(input("Enter Roll Number: ")), int(input("Enter Marks: "))))
