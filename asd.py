n = int(input())
s,m,l,xl,xxl,xxxl = map(int,input().split())
t,p = map(int,input().split())

for i in [s,m,l,xl,xxl,xxxl]:
    count = 0
    m = i - t
    while(m<0):
        if(m>0):
            break
        m -= i
        count += 1

print(count)
print(n//p,"",n%p)

