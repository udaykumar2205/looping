#wap to absolute difference between sum of even and odd in given list.
l=eval(input())
ec=0
oc=0
for i in l:
        if i%2==0:
            ec+=i
        else:
            oc+=i
            print(ec)
            print(oc)
            print(abs(ec-oc))
            
