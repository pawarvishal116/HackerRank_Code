import matplotlib.pyplot as plt
import numpy as np

years = [1990, 1992, 1994, 1996, 1998, 2000, 2003, 2005, 2007, 2010]

sachin_runs = [500, 700, 1100, 1500, 1800, 1200, 1700, 1300, 900, 1500]
kohli_runs = [0, 0, 500, 800, 1100, 1300, 1500, 1800, 1900, 2100]
sehwag_runs = [0, 300, 800, 1200, 1500, 1700, 1600, 1400, 1000, 0]

x = np.arange(len(years))
width=0.25

plt.bar(x - width, sachin_runs, width=width, label="Sachin")
plt.bar(x, years, width=width, label="Virat")
plt.bar(x + width, sehwag_runs, width=width, label="Sehwag")

plt.xlabel("Year")
plt.ylabel("Runs")
plt.title("Run Comparison")
plt.xticks(x, years)             # Show actual year instead of 0,1,2,...
plt.legend()            # Show label
print(plt.show())       # Print plot
