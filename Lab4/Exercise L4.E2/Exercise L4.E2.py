# Exercise L4.E2

x = int(input('Input number: '))
total=0
lst=[]
if x<2:     # Check if input is less than 2
    print('Invalid Input')
else:       # If input is greater then two
    for j in range(2, x+1):
        for i in range(1, j):
            if j%i==0:
                total=total+i
        if total>j:
            lst.append(j)
        total=0    # Change total to zero before going to the next j
    print('Number of abundant numbers from 1 to',x,'is',len(lst))

