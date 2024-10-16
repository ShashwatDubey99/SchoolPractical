with open("./txt_files/for7and8.txt") as f:
    data=f.read().split()
    finalstr=""
    for i in data:
        finalstr=finalstr+i+"#"
    print(finalstr)