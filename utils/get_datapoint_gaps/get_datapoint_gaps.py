from pygeotemporal.sensors import SensorsApi
from pygeotemporal.datapoints import DatapointsApi

from time import time, sleep
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
import yaml
import csv

config = yaml.load(open("get_datapoint_gaps/config.yml", 'r'), Loader=yaml.FullLoader)

clock = time()

host = config['host']
username = config['username']
password = config['password']

sensorclient = SensorsApi(host=host, username=username, password=password)
datapointclient = DatapointsApi(host=host, username=username, password=password)

print("------- starting quantification of gaps")

sensors = sensorclient.sensors_get().json()['sensors']

print("sensor count:", len(sensors))

gaps_by_sensor_id = {}
count = 0

for sensor in sensors:

    count += 1

    print(" ")
    print("Starting gap quantification for sensor_id:", sensor['id'],',',
          "sensor_count:", count,',',
          "max_time:", sensor['max_end_time'][:10], ',',
          "min_time:", sensor['min_start_time'][:10], ',',
          "start time(h):", (time() - clock) / 3600)

    # add sensor_id key to gaps_by_sensor_id
    gaps_by_sensor_id[sensor['id']] = {
        "start_time": sensor['min_start_time'],
        "end_time": sensor['max_end_time'],
        "coordinates": sensor['geometry']['coordinates'],
        "gaps": {}
    }
    # add owner if available
    if 'network' in sensor['properties']['type']:
        gaps_by_sensor_id[sensor['id']]['owner'] = sensor['properties']['type']['network']
    else:
        gaps_by_sensor_id[sensor['id']]['owner'] = "unknown"

    # set start and end time for looping over months
    start_date = datetime.strptime(sensor['min_start_time'][:10], '%Y-%m-%d')
    end_month = None
    end_date = datetime.strptime(sensor['max_end_time'][:10], '%Y-%m-%d')

    datapoints_all = []
    count_datapoints = 0
    # get datapoints one month at a time
    while start_date <= end_date:

        end_month = start_date + relativedelta(months=+1)
        print("getting datapints for range:", start_date.strftime('%Y-%m-%d'), end_month.strftime('%Y-%m-%d'))

        datapoints = datapointclient.get_datapoints_by_sensor_id(sensor['id'],
                                                                 start_date.strftime('%Y-%m-%d'),
                                                                 end_month.strftime('%Y-%m-%d')).json()

        for datapoint in datapoints:
            count_datapoints += 1
            datapoints_all.append(datapoint)

        start_date = end_month + relativedelta(days=+1)
    print("n datapoints:", len(datapoints_all))

    # create list of datapoint dates
    start_times = []
    for datapoint in datapoints_all:
        try:
            start_times.append(datetime.strptime(datapoint['start_time'][:10], '%Y-%m-%d'))
        except Exception as e:
            print("Error getting datapoint")

    start_times.sort()

    # get gap days length, start date, and end date using config['min_gap_length']
    hold_time = None
    for start_time in start_times:
        if hold_time == None:
            hold_time = start_time
        else:
            # <class 'datetime.timedelta'>
            num_days = (start_time - hold_time).days
            if num_days > config['min_gap_length']:

                if num_days not in gaps_by_sensor_id[sensor['id']]['gaps']:
                    gaps_by_sensor_id[sensor['id']]['gaps'][num_days] =[]

                gaps_by_sensor_id[sensor['id']]['gaps'][num_days].append(
                    {
                        'start': hold_time.strftime("%Y-%m-%d"),
                        'end': start_time.strftime("%Y-%m-%d")
                    }
                )

            hold_time = start_time

    print('saving csv for sensor_id:', sensor['id'])

    # append gaps to file
    with open(config['download_location'], 'a+', newline='') as csv_file:
        fieldnames = ['sensor_id', 'owner', 'lat', 'lon', 'sensor_start_date', 'sensor_end_date', 'gap_days',
                      'gap_start', 'gap_end']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for sensor_gap_size in gaps_by_sensor_id[sensor['id']]['gaps']:
            for gap_dates in gaps_by_sensor_id[sensor['id']]['gaps'][sensor_gap_size]:
                writer.writerow({
                    'sensor_id': sensor['id'],
                    'owner': gaps_by_sensor_id[sensor['id']]['owner'],
                    'lat': gaps_by_sensor_id[sensor['id']]['coordinates'][1],
                    'lon': gaps_by_sensor_id[sensor['id']]['coordinates'][0],
                    'sensor_start_date': gaps_by_sensor_id[sensor['id']]['start_time'][:10],
                    'sensor_end_date': gaps_by_sensor_id[sensor['id']]['end_time'][:10],
                    'gap_days': sensor_gap_size,
                    'gap_start': gap_dates['start'],
                    'gap_end': gap_dates['end']
                })


print("Finished. total time(h):",(time() - clock)/3600)