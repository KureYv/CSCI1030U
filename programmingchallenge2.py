

def sqrt (num):
    lower = 0
    upper = num

    guess = (lower+upper)/2.0

    while abs(guess ** 2.0 - num) >= 0.00000001:
        if guess ** 2.0 < num:
            lower = guess
        elif guess ** 2.0 > num:
            upper = guess
        guess = (lower+upper)/2.0
    print(f'guess = {guess}')


if __name__ == '__main__':
    sqrt(2.0)