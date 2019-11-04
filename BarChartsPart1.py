import matplotlib.pyplot as plt
import numpy as np

col_count = 3 # used to manually split the bars
bar_width = .2

korea_scores = {554,536,538}
canada_scores = {518,523,525}
china_scores = {613,578,588}
france_scores = {495,585,499}

index = np.arrange(count) # act as x axis

k1 = plt.bar(index, korea_scores,
label = "Korea", bar_width, alpha = .4)

c1 = plt.bar(index + .2, canada_scores,
label = "Canada", bar_width,alpha = .4)

ch1 = plt.bar(index + .4, china_scores,
label = "China", bar_width, alpha = .4)

f1 = plt.bar(index + .6, france_scores,
label = "France", bar_width, alpha = .4)

plt.ylabel("Mean score in PISA 2012")
plt.xlabel("Subjects")
plt.title("Test scores by Country")


plt.xticks(index + .3/2, ("Mathematics", "Reading", "Science"))

#e.g of legend
#plt.legend(edgecolor=(1,0,0), facecolor=(1,.4,.4), shadow =None)
plt.legend(frameon=False, loc = 2, bbox_to_anchor=(1,1)

plt.grid(True)


def CreateLabels(data):
  for item in data:
    height = item.get_height()
    plt.text(item.get_x() + item.get_width() / 2., height*1.05, "%d" % int(height),
    ha="center", va = "bottom"
    )


CreateLabels(k1)
CreateLabels(c1)
CreateLabels(ch1)
CreateLabels(f1)

'''
integer = 365
print ("There are " + str(integer) + " days in a year")

#or can do 

print ("There are %d days in a year" % integer)
'''

#for item in k1:
  #print(item.get_height())
  #print(item.get_width())
  #print(item.get_x())
  #print(item.get_y())


plt.show()
