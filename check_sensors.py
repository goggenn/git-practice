import yaml

with open("config.yml", "r") as file:
    data = yaml.safe_load(file)

print(f"It is max: {data["max_days_since_calibration"]} days since calibration")