import pandas as pd
import numpy as np
# Define rows and values
# rows = ['EmployeeID', 'Name', 'Department', 'Position', 'Salary', 'HireDate', 'PerformanceScore', 'ProjectsCompleted', 'SalesAchieved', 'CustomerSatisfactionScore', 'Attendance']
# values = [
#     [1, 'Laura', 'HR', 'Manager', 65732, '2015-01-31', 4, 16, 92800, 10, 232],
#     [2, 'James', 'Sales', 'Clerk', 116511, '2015-02-28', 1, 10, 37089, 9, 212],
#     [3, 'Bond', 'Marketing', 'Analyst', 116516, '2015-03-31', 5, 19, 88217, 4, 214],
#     [4, 'Malik', 'Sales', 'Manager', 45110, '2015-04-30', 2, 17, 36788, 3, 213],
#     [5, 'Mastan', 'Sales', 'Manager', 51290, '2015-05-31', 5, 12, 38938, 3, 207]
# ]

# user_email = ['laura.london@jda.com', 'james.bond@jda.com', 'bond.brothers@jda.com', 'malik.malakpet@jda.com', 'masth.mutton@jda.com']

# file_path = r"Employeedata.xlsx"

# df = pd.DataFrame(values, columns=rows)
# rename_col = df.rename(columns={"EID": "EmployeeID"}, inplace=True)

# drop_row = df.drop(["SalesAchieved"], axis=1)
# group_by_col = df.groupby(['Department'])['Position'].count()
# group_by_col = df[df['Position'] == 'Sales'].groupby('Department')['Position'].count()
# get_man_count = df[(df['Department'] == 'Sales') & (df['Position'] == 'Manager')].shape[0]
# print("total count of dept and pos is:", group_by_col)
# print("manager count", get_man_count)
# with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
#     .to_excel(writer, sheet_name="Employees", index=False)
#     print("row droped in xl filesheet")
# df['Email'] = user_email
# with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
#     df.to_excel(writer, sheet_name='Employees', index=False)

# print(f"Data inserted into '{file_path}'")

# sorting

# sort_Data = df.groupby(['Department'], sort=True).count()
# sorted_df = sort_Data.sort_values('Department', ascending=True)
# print(sorted_df)

#filna values

# condition = (df['Name'] == 'James') & (df['PerformanceScore'] == pd.NA)
# df.loc[condition, 'PerformanceScore'] = df.loc[condition, 'PerformanceScore'].dropna()
# print("Updated DataFrame with NaN value in James' PerformanceScore:")
# print(df)


#dropna
# condition = (df['Name'] == 'James') & (df['PerformanceScore'] == 1)
# df.loc[condition, 'PerformanceScore'].dropna()

# with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
#     df.to_excel(writer, sheet_name='Employees', index=False)
#     print("NaN value added and file saved")


# read&write data

# import os
# print(os.path.abspath('world_alcohol.csv'))

# with open(file_path, mode='w+'):
#     df = pd.DataFrame("")

file_path = r'world_alcohol.csv'

# try:
#     with open(file_path, 'r') as file:
#         content = file.read()
#         print("File content:")
#         print(content)

#     data = pd.read_csv(file_path)
#     if data.empty:
#         print("CSV file is empty bro")
#     else:
#         print("Successfully loaded data from CSV:")
#         print(data)
# except pd.errors.EmptyDataError:
#     print("Error: CSV file is empty bro.")


# new_data = {
#     "Year": [1986],
#     "Region": ["South-Upper Asia"],
#     "Country": ["Democratic 's Republic of Korea"],
#     "Product": ["Wine"],
#     "Quantity": [0]
# }

# try:
#     df = pd.t(file_path)
# except FileNotFoundError:
#     df = pd.DataFrame()
# new_row = pd.DataFrame(new_data)
# df = pd.concat([df, new_row], ignore_index=True)
# df.to_csv(file_path, index=False)

# print("New row added into file... :)")

# import pandas as pd

# file_path = 'world_alcohol.csv'

# try:
#     df = pd.read_csv(file_path)
#     with pd.ExcelWriter("Alchdata.xlsx", engine='xlsxwriter')as writer:
#         df.to_excel(writer,sheet_name="JAMESBOND" ,index=False)
#         print("data inserted into new file")
# except FileNotFoundError:
#     print(f"Error: File '{file_path}' not found.")
# except Exception as e:
#     print(f"An error occurred: {str(e)}")
# import pandas as pd
# technologies = [
#             ("Spark", 22000,'30days',1000.0),
#             ("PySpark",25000,'50days',2300.0),
#             ("Hadoop",23000,'55days',1500.0)
#             ]
# df = pd.DataFrame(technologies,columns = ['Courses','Fee','Duration','Discount'])

# data = df.to_json(orient='split')
# print("Create DataFrame:\n", data)

# import matplotlib.pyplot as plt 
# import pandas as pd 
# file = pd.read_excel(r'Alchdata.xlsx') 
# print(file)
# x_axis = file['X values'] 
# y_axis = file['Y values'] 
# plt.bar(x_axis, y_axis, width=5) 
# plt.xlabel("X-Axis") 
# plt.ylabel("Y-Axis") 
# plt.show() 

import matplotlib.pyplot as james
import pandas as pd

data = {
    'Fruit': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'],
    'Quantity': [25, 40, 30, 15, 20]
}
df = pd.DataFrame(data)
df.to_csv('fruit_data.csv', index=False)
file = pd.read_csv('fruit_data.csv')
james.bar(file['Fruit'], file['Quantity'], color=['skyblue', 'green', 'yellow', 'red'])
james.xlabel("Fruits axis")
james.ylabel("Quantity axis")
james.title("Fruit Quantity Visualization")
james.xticks(rotation=45)
james.tight_layout()
james.show()
