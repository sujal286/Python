keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
my_dict={}
for i,j in zip(keys,values):
    my_dict[i]=j

sorted_dict=dict(sorted(my_dict.items()))
print(sorted_dict)