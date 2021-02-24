num = 407
if num > 1:
    for i in range(2, num):
        print (num,"bukan bilangan prima")
        print (i,"kali",num/i,"adalah",num)
        break
    else:
        print (num,"adalah bilangan prima")
else:
    print (num,"bukan bilangan prima")
    
