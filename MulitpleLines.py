#can install thorugh pip
import matplotlib.pyplot as plt

#years = [1,1000,1500,1600,1700,1800,1850,1900,1950,1955,1960,1965,1970,1975,1980,1985,1990,1995,2000,2005,2010,2015]

#pops = [200,400,458,580,682,791,1000,1262,1630,2325,2750,3010,3322,3682,4061,4440,4853,5310,6127,6520,6930,7340]


years = [1950,1955,1960,1965,1970,1975,1980,1985,1990,1995,2000,2005,2010,2015]

pops = [1.630,2.325,2.750,3.010,3.322,3.682,4.061,4.440,4.853,5.310,6.127,6.520,6.930,7.340]

#colours and labels
plt.plot(years, pops, "--", color=(255/255,100/255,100/255))
plt.ylabel("Population (in billion)")
plt.xlabel("Year")
plt.title("Population Growth")


#multiple lines
deaths = [1.2, 1.7, 1.8, 2.2, 2.5, 2.7, 2.9, 3, 3.1 , 3.3 , 3.5, 3.8, 4.0, 4.3]
plt.plot(years, deaths, color=(.6..6.1))




plt.show()