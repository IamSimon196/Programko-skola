import matplotlib.pyplot as plt
heights = [10, 8, 15, 30, 5, 11, 6, 23]

x = [i * 2 for i in range(len(heights))]  
colors = ['red'] * 3 + ['green'] * 3 + ['blue'] * (len(heights) - 6)

plt.bar(x, heights, width=2, color=colors, edgecolor='black', linewidth=1, zorder=3)
plt.xticks(x, range(len(heights))) 
plt.show()