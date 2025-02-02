###   1.  Loading the data  ==============================
import pandas as pd
manish=pd.read_csv("D:/Tranning_Python/Practice.py/Cleardata.csv")
print(manish.to_string())


###  2.  Cleaning the dataframe ==============================
###   Here he will return a new dataframe with no empty cells
import pandas as pd 
df=pd.read_csv("D:/Tranning_Python/Practice.py/Cleardata.csv")
new_df=df.dropna()
print(new_df.to_string())

##   3. Replace Entry with a value ===============
import pandas as pd 
manish=pd.read_csv("D:/Tranning_Python/Practice.py/Cleardata.csv")
manish.fillna(130,inplace=True)
print(manish.to_string())

###  4. Replace only for one column =================================
import pandas as pd
manish=pd.read_csv("D:/Tranning_Python/Practice.py/Cleardata.csv")
manish["Calories"].fillna(130,inplace=True)
print(manish.to_string())

#### 5. Replace using mean ==============================
import pandas as pd
manish=pd.read_csv("D:/Tranning_Python/Practice.py/Cleardata.csv")
X=manish["Calories"].mean()
manish["Calories"].fillna(X,inplace=True)
print(manish.to_string())

### 6. Replace using median ====================
import pandas as pd 
manish=pd.read_csv("D:/Tranning_Python/Practice.py/Cleardata.csv")
X=manish["Calories"].median()
manish["Calories"].fillna(X,inplace=True)
print(manish.to_string())

### 7. Rplace using mode ====================
import pandas as pd
manish=pd.read_csv("D:/Tranning_Python/Practice.py/Cleardata.csv")
X=manish["Calories"].mode()[0]  ## 0 is use for index number and also read about more
manish["Calories"].fillna(X,inplace=True)
print(manish.to_string())



#####  1.--- load and display original data 
import pandas as pd 
manish=pd.read_csv("D:/Tranning_Python/Practice.py/Cleardata.csv")
print(manish.to_string())

#### 2.---- convert 'date' column  to datetime -- errors='coerce' replace invalid formate with Nat
manish['Date']=pd.to_datetime(manish['Date'],errors='coerce')
print(manish.to_string())
### 3. Remove  row with null values in 'date' column 
manish=pd.read_csv("D:/Tranning_Python/Practice.py/Cleardata.csv")
manish['Date']=pd.to_datetime(manish['Date'],errors='coerce')
manish.dropna(subset=['Date'],inplace=True)
print(manish.to_string())

##  4. Manually correcting tha 'Duration'value for the 7th row who replace 120(on index 7)
import pandas as pd
manish=pd.read_csv("D:/Tranning_Python/Practice.py/Cleardata.csv")
manish.loc[7,'Duration']=120
print(manish.to_string())


### 8.  Using loop 
for i in  manish.index:
    if manish.loc[i,'Duration']>120:
        manish.loc[i,'Duration']=90
print(manish.to_string())

###  Alternation approch for data removing 
import pandas as pd
manish=pd.read_csv("D:/Tranning_Python/Practice.py/Cleardata.csv")
for i in manish.index:
    if manish.loc[i,'Duration']>60:
        manish.drop(i,inplace=True)
print(manish.to_string())


####   remove duplicate values 
import pandas as pd
manish=pd.read_csv("D:/Tranning_Python/Practice.py/Cleardata.csv")
# print(manish.to_string())
print(manish.duplicated())


import pandas as pd
manish=pd.read_csv("D:/Tranning_Python/Practice.py/Cleardata.csv")
manish.drop_duplicates(inplace=True)
print(manish.to_string())

