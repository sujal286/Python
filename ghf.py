def prime(num):
    my_list=[]
    if(num==1):
        return 1
    for i in range(2,num+1):
        for j in range(2,i):
            if(i%j!=0):
                my_list.append(i)
                break
    return my_list

p=prime(15)
print(p)