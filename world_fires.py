import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    column_header = next(reader)

    
    # Find index where min and max are stored
    for index, column_header in enumerate(column_header):
        if column_header == 'latitude':
            lat_index = int(index)
        elif column_header == 'longitude':
            lon_index = int(index)
        elif column_header == 'brightness':
            brightness_index = int(index)

    
    lats, lons, brightness_all = [], [], []
    for row in reader:
        try:
            lat = row[lat_index]
            lon = row[lon_index]
            brightness = float(row[brightness_index])
        except ValueError:
            print('Error')
            continue
        else:
            lats.append(lat)
            lons.append(lon)
            brightness_all.append(brightness)
            
# Map the fires.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'color': brightness_all,
        'colorscale': 'inferno',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'},
    }
}]

my_layout = Layout(title="Global fires in 24hrs")
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')