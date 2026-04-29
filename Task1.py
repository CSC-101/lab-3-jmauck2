more = [x + 1 for x in [1,2,3,4]] #Step1: x=1. Step2: x=2. Step3: x=3. Step4: x=4.
print(more)     #More = [2, 3, 4, 5]

def square(n:int) -> int:   #n=1, return 1. n=2, return 4. n=3, return 9. n=4, return 16.
    return n*n

squares = [square(x) for x in [1,2,3,4]]    #squares = [1, 4, 9, 16]. This is a list of the returned values from above.
print(squares)

#def check(n:int)->bool: #n=0, return False. n=1, return False. n=2, return False. n=3, return True. n=4, return True.
    #return n>2

#answer = [x for x in range(5) if check(x)]
#print(answer)           #Answer = [3, 4]

def inc(m:int)->int:     #m=0, reutrn 1. m=1, return 2. m=2, return 3. m=3, return 4. m=4, return 5.
    return m+1

def check(n:int)->bool:  #n=0, return False. n=1, return False. n=2, return False. n=3, return True. n=4, return True.
    return n>2

answer = [inc(x) for x in range(5) if check(x)]     #Answer = [4, 5]
print(answer)
