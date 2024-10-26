import pickle 
with open("bin_files/15cities.bin","wb") as f:
    data=[{"name":"Miku","house_no":1,"city":"Tokyo","pincode":12345},
    {"name":"Sana","house_no":2,"city":"Tokyo","pincode":12345},
    {"name":"Shalinee","house_no":3,"city":"Delhi","pincode":555555},]

    pickle.dump(data,f)

def search_Delhi():
    with open("bin_files/15cities.bin","rb") as f:
        data = pickle.load(f)
        for i in data:
            if i["city"] == "Delhi":
                print(i)
search_Delhi()                