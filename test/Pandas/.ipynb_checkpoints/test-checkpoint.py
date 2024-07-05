import pandas as james
import numpy as np
result = james.read_excel(r"EmployeeData.xlsx", engine="openpyxl")

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

print(result.to_excel())