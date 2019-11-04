import matplotlib as plt
import pandas as pd

#simplifies process of making data


#without pandas
data=[{
  "name": "Nick",
  "jan_ir": 123,
  "feb_ir": 100,
  "march_ir": 165
},
{"name": "Panda",
  "jan_ir": 123,
  "feb_ir": 100,
  "march_ir": 5
}]

#for person in data:
  ##would need to calculate the total_ir individually


#pip3 install pandas
##would need to copy and paste to add more entries to the dictionary

raw_data = { "names": ["Aakash", "Tahmoor", "Dimitar", "Mehtab", "Derek", "Wil"],
"jan_ir": [100,50,20,30,56,42],
"feb_ir": [120,70,80,50,60,20],
"march_ir": [180,50,60,40,30,90]}

dataFrame = pd.DataFrame(raw_data, columns = ["names", "jan_ir", "feb_ir", "march_ir"] )

dataFrame["total_ir"] = dataFrame["jan_ir"] + dataFrame["feb_ir"] + dataFrame["march_ir"]

print(dataFrame)