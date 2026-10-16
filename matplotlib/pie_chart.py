import matplotlib.pyplot as plt

explode = [0, 0.3, 0, 0]  # Only highlight Sachin's slice


labels = ["Sachin", "Sehwag", "Kohli", "Yuvraj"]
runs = [18000, 8000, 12000, 9500]

colors = ['#ff2356','#89b313','#33ef11','#ffdc10']
 
wedgeprops={'edgecolor': 'black', 'linewidth': 2, 'linestyle': '-'}
plt.title("Career Runs of Indian Batsmen")

for angle in range(0, 1000, 10):
    plt.clf()                          # Clear previous chart
    plt.pie(runs, labels=labels, colors=colors, wedgeprops=wedgeprops, explode=explode, shadow=True, autopct='%1.1f%%', startangle=angle)
    plt.title(f"Career Runs of Indian Batsmen - Angle: {angle}")
    plt.pause(0.30)                    # to rotate pie every 30 second
plt.show()
