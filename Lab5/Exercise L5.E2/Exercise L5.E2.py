# Exercise L5.E2

sub = ['I', 'We']
verb = ['play', 'watch']
obj = list(map(str, input().split()))

for i in sub:
    for j in obj:
        for k in verb:
            print(i,k,j+'.')
