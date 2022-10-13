import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates, precipitation = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            daily_precipitation = float(row[3])
        except ValueError:
            continue
        else:
            dates.append(current_date)
            precipitation.append(daily_precipitation)
    
    # Plot the points
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, precipitation, c='blue')

    # Format the plot
    ax.set_title('Sitka Yearly Rainfall - 2018', fontsize=24)
    ax.set_xlabel("", fontsize=16)
    ax.set_ylabel('Rainfall in inches', fontsize=14)
    fig.autofmt_xdate()
    plt.ylim([0, 120])
    ax.tick_params(axis='both', which='major', labelsize=16)
    
    plt.show()
        
            
