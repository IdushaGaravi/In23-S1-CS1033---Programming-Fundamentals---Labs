# Exercise L4.E1

def isPrime(num):
    if num == 1 or num==0:      # 1  and 0 are not considered a prime number
        print('non-prime')
    else:
        j = 2
        while j <= (num)**0.5:
            if num % j == 0:        # Find non prime numbers
                print('non-prime')
                return
            j += 1
        print('prime')

while True:
    num = int(input())
    if num < 0:     # Check whether input is negative before calling the function
        break
    else:
        isPrime(num)    # Calling isPrime function
       
