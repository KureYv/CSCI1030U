

def taylor(val):
    beginval = val
    total = beginval
    for i in range(val):
        newvaltop = beginval*beginval*beginval
        newvalbottom = 1+2*i
        for i in range(newvalbottom):
            newvalbottom1 = newvalbottom * newvalbottom -i * -1
        total+=(newvaltop/newvalbottom1)
    return total

if __name__ == "__main__":
    print(taylor(4))