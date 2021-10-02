import math
def is_prime_fast(number):
    if (number!=2 and number%2==0) or number in [0,1]:
        #print(5)
        return False
    elif number==2:
        #print(6)
        return True
    else:
        for i in range(3,int(math.sqrt(number))+1,2):
            if number%i==0:
         #       print(7)
                return False
    return True
