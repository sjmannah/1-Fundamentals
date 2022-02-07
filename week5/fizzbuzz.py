def fizzbuzz(num):
    
    for x in range(num+1):
        if x == 0:
            continue
        elif ((x % 3) == 0) & ((x % 5) == 0):
            print("FizzBuzz")
        elif (x % 3) == 0:
            print("Fizz")
        elif (x % 5) == 0:
            print("Buzz")
        else: 
            print(x)

fizzbuzz(50)
        
