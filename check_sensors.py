import json

import pandas as pd
import yaml

with open("config.yml", "r") as file:
    config = yaml.safe_load(file)

max_days = config["max_days_since_calibration"]
output_file = config["output_file"]


#Reads the data
sensors = pd.read_excel("sensors.xlsx")
calibrations = pd.read_csv("calibrations.csv")


# Join data using the sensor_id
data = pd.merge(sensors, calibrations, on="sensor_id")


# Finding overdue sensors
overdue_sensors = data[
    data["days_since_calibration"] > max_days
]


# Keep the information requested in the task
overdue_sensors = overdue_sensors[
    ["sensor_id", "lab_room", "owner", "days_since_calibration"]
]


# Convert to list for JSON
result = overdue_sensors.to_dict(orient="records")


# Write to the JSON file
with open(output_file, "w") as file:
    json.dump(result, file, indent=2)

