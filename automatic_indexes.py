import csv
from datetime import datetime

infile1 = open(r'C:\Users\Stephen_Gonzales1\Documents\AdvPython\CSV\sitka_weather_2018_simple.csv')

csv_file1 = csv.reader(infile1)

header_row1=next(csv_file1)

print(header_row1) 

for index, col_header in enumerate(header_row1):
    print(index, col_header)


highs1 = []
dates1=[]
lows1 = []

some_date= datetime.strptime('2018-07-01', '%Y-%m-%d')

print(type(some_date))

for row in csv_file1:
    highs1.append(int(row[5]))
    lows1.append(int(row[6]))
    some_date = datetime.strptime(row[2], '%Y-%m-%d')
    dates1.append(some_date)



infile2 = open(r'C:\Users\Stephen_Gonzales1\Documents\AdvPython\CSV\death_valley_2018_simple.csv')

csv_file2 = csv.reader(infile2)

header_row2=next(csv_file2)

print(header_row2) 

for index, col_header in enumerate(header_row2):
    print(index, col_header)


highs2 = []
dates2=[]
lows2 = []


for row in csv_file2:
    try:
        some_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[4])
        low = int(row[5])
        
    except ValueError:
        print(f"Missing data for {some_date}")
    
    else:
        highs2.append(int(row[4]))
        lows2.append(int(row[5]))
        dates2.append(some_date)


import matplotlib.pyplot as plt

fig = plt.figure()

# plt.plot(dates,highs, c='red', alpha=0.5)
# plt.plot(dates,lows, c='blue', alpha=0.5)

# plt.fill_between(dates,highs,lows, facecolor='blue',alpha=0.1)

# plt.title("Daily low and high temperatures - 2018", fontsize=16)
# plt.xlabel("Dates", fontsize=16)
# plt.ylabel("Temps (F)",fontsize=16)
# plt.tick_params(axis="both",which="major",labelsize=16)



#plt.show()

plt.subplot(2,1,1)
plt.plot(dates1,highs1, c='red', alpha=0.5)
plt.plot(dates1,lows1, c='blue', alpha=0.5)

plt.fill_between(dates1,highs1,lows1, facecolor='blue',alpha=0.1)
plt.title("SITKA AIRPORT, AK US")

plt.subplot(2,1,2)
plt.plot(dates2,highs2, c='red', alpha=0.5)
plt.plot(dates2,lows2, c='blue', alpha=0.5)

plt.fill_between(dates2,highs2,lows2, facecolor='blue',alpha=0.1)

plt.title("DEATH VALLEY, CA US")

plt.suptitle("Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US")

fig.autofmt_xdate()

plt.show()  