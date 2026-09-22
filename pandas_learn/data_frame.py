import pandas as pd
#Data Frame is a tabular data structure with rows and columns
data = {"Name":["SpongeBob","Patrick","Squidward"],
        "Age":[30,35,50],}
dataframe = pd.DataFrame(data,index = [f"Employee {x+1}" for x in range(len(data["Name"]))]) # Conversion of list to Data Frame
print(dataframe)
print(dataframe.iloc[1]) # prints only the specified item in the data frame

dataframe["Jobs"]= ["Chef","NA","Cashier"] # Add a new colum
new_row = pd.DataFrame([{"Name":"Sandy","Age":28,"Jobs":"Scientist"}],index=["Employee 4"])
dataframe = pd.concat([dataframe,new_row]) ## Adds the row , this concatenates ie combines dataframes
print(dataframe)