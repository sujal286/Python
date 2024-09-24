my_dict={
    "name" : "Rohit Sharma",
     "best" : 264 ,
     "nationality" : "Indian",
      "Average" : 60.34,
}

print(my_dict.values())

for i,j in my_dict.items():
    print(i,j)

my_dict2={
    "name" : "Virat Kohli",
    "best" :183,
    "nationality": "Indian",
    "Average": 100.56,
}

merge_dict={**my_dict,**my_dict2}

for i,j in merge_dict.items():
    print(i,j)


print(len(my_dict))