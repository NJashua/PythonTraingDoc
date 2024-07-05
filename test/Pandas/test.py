import pandas as james
import numpy as np
result = james.read_csv(r"Sample-Spreadsheet-1000-rows.csv", encoding='ISO-8859-1')

# print(result.to_string())

# hello_masteru = james.Series([1,2,3,4,5], ["HEY", "HELLO", "JAMES", "BOLO", "GURU"])
# hello_masteru = james.Series({"name": "nithin jashua", "age":23, "email": "nithinjashua@gmail.com"})
# hello_masteru = james.Series(['hey', 23, 'hello', 'james bond', james.NA])
# arr = [12]
# mon = [1]
# hello_masteru = james.Series(data=arr, index=mon, dtype=np.float64)
# print(hello_masteru)

# print(hel)

# res=james.Series(range(1,6)+2, index=[x for x in range(1,6)])
# # val = res.loc[]
# print(result

# print(result.to_excel('to_excel.xlsx', index= False ))
# with open(r"to_excel.xlsx", mode='r') as file:
#     data = file.readlines(3)
#     print(data)

# data = result.to_dict()
# print(data)
# for i in data:
#     print(i)
# # print(data)

# james_array = np.array([[23,2,3,4,45,53], [4,3,4,2,53,5]], np.int32)
# vslue = james_array.shape
# get_data = james.DataFrame(james_array)
# print(get_data)
# name = james.Series(["nithin", "jashua", "mersy"])
# email = james.Series(["nithinjashua!@gmail.com", "jashua1@gmail.com", "mersy@gmail.com"])
# dict_data = {"name": name, "email" : email}
# result = james.DataFrame(dict_data)
# print(result)

# import pandas as pd
# import numpy as np
# technologies   = ({
#     'Courses':["Spark","PySpark","Hadoop","Python","Pandas",None,"Spark","Python"],
#     'Fee' :[22000,25000,23000,24000,np.nan,25000,25000,22000],
#     'Duration':['30day','50days','55days','40days','60days','35day','','50days'],
#     'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
#           })
# row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']

# df = pd.DataFrame(technologies, index=row_labels)
# # result_df = df.query("Courses in ('Spark','PySpark')") 
# # result_df = df.query("Fee>=23000 and Fee<=24000")
# # result_df = df.loc[df['Courses'].isin(["Spark", "Pyspark"])]
# # result_df = df.loc[~df['Courses'].isin(["Spark", "PySpark"])]
# # result_df = df.loc[(df['Discount'] >= 1200) & (df['Fee'] >= 23000)]
# # result_df = df.apply(lambda row: row[df['Courses'].isin(['Spark','PySpark'])])
# # result_df = df[df['Courses'] == "Spark"]
# # result_df = df['Courses'].str.contains("spark")
# # result_df = df["Courses"].str.lower().str.contains("spark")
# # result_df = df["Courses"].str.startswith("P")
# courses = ["Python", "Java", "JS"]
# result_df = df.assign(Courses = courses)
# print("data inserted", result_df)

# import pandas as pd
# import numpy as np

# with open("Datamanuplate.xlsx", mode='w+'):
#     technologies = {
#         'Courses': ["Spark", "PySpark", "Hadoop", "Python", "Pandas", None, "Spark", "Python"],
#         'Fee': [22000, 25000, 23000, 24000, np.nan, 25000, 25000, 22000],
#         'Duration': ['30day', '50days', '55days', '40days', '60days', '35day', '', '50days'],
#         'Discount': [1000, 2300, 1000, 1200, 2500, 1300, 1400, 1600]
#     }
#     row_labels = ['r0', 'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7']

#     df = pd.DataFrame(technologies, index=row_labels)

#     # Uncomment any of the following lines to perform different operations

#     # Filter rows where Courses are 'Spark' or 'PySpark'
#     # result_df = df.query("Courses in ('Spark','PySpark')")

#     # Filter rows where Fee is between 23000 and 24000
#     # result_df = df.query("Fee >= 23000 and Fee <= 24000")

#     # Filter rows where Courses are 'Spark' or 'PySpark'
#     # result_df = df.loc[df['Courses'].isin(["Spark", "PySpark"])]

#     # Filter rows where Courses are not 'Spark' or 'PySpark'
#     # result_df = df.loc[~df['Courses'].isin(["Spark", "PySpark"])]

#     # Filter rows where Discount is >= 1200 and Fee is >= 23000
#     # result_df = df.loc[(df['Discount'] >= 1200) & (df['Fee'] >= 23000)]

#     # Apply a function to each row (Example given does not make sense, corrected to filter using apply)
#     # result_df = df[df.apply(lambda row: row['Courses'] in ['Spark','PySpark'], axis=1)]

#     # Filter rows where Courses is 'Spark'
#     # result_df = df[df['Courses'] == "Spark"]

#     # Filter rows where Courses contains the string 'spark' (case insensitive)
#     # result_df = df['Courses'].str.contains("spark", case=False, na=False)

#     # Filter rows where Courses starts with 'P'
#     # result_df = df['Courses'].str.startswith("P", na=False)

#     courses = ["Python", "Java", "JS"]
#     result_df = df.insert(Courses=courses)
#     # result_df.to_excel("Datamanuplate.xlsx")

#     print("Data inserted and saved to sampledata.xlsx")

import pandas as pd
import numpy as np

technologies = {
    'Courses': ["Spark", "PySpark", "Hadoop", "Python", "Pandas", None, "Spark", "Python"],
    'Fee': [22000, 25000, 23000, 24000, np.nan, 25000, 25000, 22000],
    'Duration': ['30day', '50days', '55days', '40days', '60days', '35day', '', '50days'],
    'Discount': [1000, 2300, 1000, 1200, 2500, 1300, 1400, 1600]
}
row_labels = ['r0', 'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7']

df = pd.DataFrame(technologies, index=row_labels)
# new_courses = ["Python", "Java", "JS", "C++", "Ruby", "Go", "PHP", "Swift"]
# df['New Courses'] = new_courses

# result = df.info()
# print(result)
# with pd.ExcelWriter("Datamanuplate.xlsx") as writer:
#     df.to_excel(writer)

print("DataFrame has been saved to 'Datamanuplate.xlsx'.")
