

def taylor(val,precision):
    next = 1
    total = 0
    for i in range(0,precision):
        posorneg = (-1) ** i
        top = val ** (2 * i + 1 ) * posorneg
        final = 1
        for i in range(next):
            final = final * (next -i)
        next +=2  
        total += top/final
        print(top,final)
    return total

if __name__ == "__main__":
    print(taylor(1.57,51))