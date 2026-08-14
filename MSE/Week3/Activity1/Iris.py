from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
iris = fetch_ucirepo(id=53) 
  
# data (as pandas dataframes) 
X = iris.data.features 
y = iris.data.targets 
data = iris.data.original
  
# metadata 
print(iris.metadata) 
  
# variable information 
print(iris.variables) 

# activity
print("Total number of records:", len(data))
print("Total number of different flowers:", data["class"].nunique())
print("Names of different flowers:")
print(data["class"].unique())