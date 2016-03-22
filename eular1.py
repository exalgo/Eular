
t = input()
while( t > 0 ):
    n1= input()
    n=n1-1
    sum = 0
    sum = ((3 * ((n/3)  *  ((n/3)+1))/2) + (5 * ((n/5)  *  ((n/5)+1))/2) -(15 * ((n/15) * ((n/15)+1))/2) )
    print sum
    t=t-1