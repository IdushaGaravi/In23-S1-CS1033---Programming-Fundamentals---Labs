# Exercise L5.E3

def sum_average(total):
    ''' get average of each student'''
    print('Total:', total, 'Average:','%0.1f'% (total/3))

for _ in range(4):        
    marks_per_person=list(map(int, input().split()))    # get marks per student
    total=sum(marks_per_person)     # get total of each student
    sum_average(total)      # call sum_average function
