def ProdANDSum(*args):
    prod = 1
    sum = 0
    for i in range(10):

        prod *= args[i]
        sum += args[i]
    return {"Product": prod, "Sum": sum}
print(ProdANDSum(1,1,1,1,1,1,1,1,1,1,1,1))