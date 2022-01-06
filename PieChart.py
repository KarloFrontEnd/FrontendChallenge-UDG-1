from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

slices = [1439323776, 1380004385, 331002651, 273523615, 220892340, 212559417]
labels = ['China', 'India', 'United States', 'Indonesia', 'Pakistan', 'Brazil']


plt.pie(slices, labels=labels, shadow=True, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})

plt.title("Top 5 Countries Population")
plt.tight_layout()
plt.show()
