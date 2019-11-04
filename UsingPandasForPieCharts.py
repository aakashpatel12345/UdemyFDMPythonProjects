import matplotlib as plt
import pandas as pd


raw_data = { "names": ["Aakash", "Tahmoor", "Dimitar", "Mehtab", "Derek", "Wil"],
"jan_ir": [100,50,20,30,56,42],
"feb_ir": [120,70,80,50,60,20],
"march_ir": [180,50,60,40,30,90]}

dataFrame = pd.DataFrame(raw_data, columns = ["names", "jan_ir", "feb_ir", "march_ir"] )

dataFrame["total_ir"] = dataFrame["jan_ir"] + dataFrame["feb_ir"] + dataFrame["march_ir"]

color = [(1,.4,.4),(1,.6,.1),(.3,.5,.5),(.8,.2,.7),(.5,.8,.6),(.1,.5,.2),]

plt.pie(df[total_ir] labels = df["names"], color = color, autopct='%1.1f%%')

plt.axis("equal")

plt.show()

#print(dataFrame)