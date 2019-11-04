import matplotlib as plt

labels = 'Python', 'C++', 'Ruby', 'Java', 'PHP', 'Pearl'

sizes = {33,52,12,17,62,48}
seperated = {.1,0,0,0,0,0}

plt.pie(sizes, labels = labels, autopct='%1.1f%%', explode=seperated)
plt.axis('equal')

plt.show()

