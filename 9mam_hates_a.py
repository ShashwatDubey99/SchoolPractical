with open("txt_files/for9.txt") as f:
    data=f.readlines()
    new_data=[]
    for i in data:
        if "a" in i:
            new_data.append(i)
with open("txt_files/for9_a.txt","w") as f:
    f.writelines(new_data)                    