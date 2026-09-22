import pandas as pd
data = {"Name":["SpongeBob","Patrick","Squidward","Koyi"],
        "Age":[30,35,50,90],}
dataframe = pd.DataFrame(data,index = [f"Employee {x+1}" for x in range(len(data["Name"]))]) # Conversion of list to Data Frame
print(dataframe)
print(dataframe.iloc[1]) # prints only the specified item in the data frame
