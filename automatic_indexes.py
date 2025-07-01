import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename1 = r'C:\Users\Stephen_Gonzales1\Documents\AdvPython\CSV\death_valley_2018_simple.csv'
filename2 = r'C:\Users\Stephen_Gonzales1\Documents\AdvPython\CSV\sitka_weather_2018_simple.csv'

stations,dates,highs,lows=[],[],[],[]

with open(filename1) as f1:
    reader= csv.reader(f1)
    header_row= next(reader)
    print(header_row)

    # Get dates, and high and low temperatures from this file.
    for row in reader:
        station="Death_Valley"
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high=int(row[4])
            low=int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            stations.append(station)
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    for index, column_header in enumerate(header_row):
        print(index,column_header)

with open(filename2) as f2:
    reader= csv.reader(f2)
    header_row= next(reader)
    print(header_row) 
    
    # Get dates, and high and low temperatures from this file.
    for row in reader:
        station="Sitka"
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high=int(row[5])
            low=int(row[6])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            stations.append(station)
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    for index, column_header in enumerate(header_row):
        print(index,column_header)



# Plot the high and low temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')

# Format plot
title = "Daily high and low temperatures - 2018\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()