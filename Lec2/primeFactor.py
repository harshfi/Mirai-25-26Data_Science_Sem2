
def prime_factors(n):
    i=2

    while(n>1):

        if(n%i==0):
            print(i)
            n=n//i
        else:
            i+=1


prime_factors(150)





n=50