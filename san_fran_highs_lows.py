import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/san_fran_weather_2018.csv'
with open(filename) as f:
    reader = csv.reader(f)
    column_header = next(reader)
    
    # Find index where min and max are stored
    for index, column_header in enumerate(column_header):
        if column_header == 'TMAX':
            max_index = int(index)
        elif column_header == 'TMIN':
            min_index = int(index)
        elif column_header == 'NAME':
            city_index = int(index)
            
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            city = row[city_index].title()
            high = int(row[max_index])
            low = int(row[min_index])
        except ValueError:
            print(f'Data not available for {current_date}')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
            
# Plot the highs and lows
plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(15, 9))
ax.plot(dates, highs, c='blue', alpha=0.5)
ax.plot(dates, lows, c='red', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format the plot
ax.set_title(f"High and Low Temperatures - 2018\n{city}", fontsize=18)
ax.set_xlabel("", fontsize=10)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=5)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
