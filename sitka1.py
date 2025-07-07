import csv

infile = open(r'C:\Users\Stephen_Gonzales1\Documents\AdvPython\CSV\sitka_weather_07-2018_simple.csv')

csv_file = csv.reader(infile)

header_row=next(csv_file)

print(header_row)

for index, col_header in enumerate(header_row):
    print(index, col_header)


highs = []

for row in csv_file:
    highs.append(int(row[5]))

print(highs)

import matplotlib.pyplot as plt

plt.plot(highs, c='red')

plt.title("Daily high temps, July 2018", fontsize=16)
plt.xlabel("")
plt.ylabel("Temps (F)",fontsize=16)
plt.tick_params(axis="both",which="major",labelsize=16)

plt.show()
