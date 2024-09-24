import numpy as np
import pandas as pd
my_dict={
    "name":["Sujal","Swayam","Ayush","Naveen"],
    "marks":[100,34,67,90],
     "city":["kolkata","Ranchi","goa","sikkim"]
}
df=pd.DataFrame(my_dict)
print(pd.DataFrame(my_dict))
df.to_csv('friend.csv')