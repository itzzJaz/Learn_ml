import pandas as pd
data = {"Item":["Pizza","Candy Bar","Burger","Potato"],"Quantity":[1,2,1,5],"Price Per Unit":[5,2,6,1]}
total_price = []
for i in range(len(data["Quantity"])):
    total_price.append(data["Quantity"][i]*data["Price Per Unit"][i])
data["total_price"]=total_price
df = pd.DataFrame(data,index=[f"Item {i+1}" for i in range(len(data))])
print(df)
item = input("Enter the item name: ")
result = df[df["Item"].str.contains(item, case=False)]
if result.empty:
    print("Item not found")
else:
    print(result)
