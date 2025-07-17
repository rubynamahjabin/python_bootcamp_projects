import csv
import pandas

# Read CSV using built-in csv module
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)

    temperatures = []
    for row in data:
        print(row)
        if row[1] != 'temp':  # Skip header row
            temperatures.append(int(row[1]))

    print("Temperatures from CSV:", temperatures)

# Read CSV using pandas
data = pandas.read_csv("weather_data.csv")
print(data["temp"])

# Convert to dictionary
data_dict = data.to_dict()
print("Data as dictionary:\n", data_dict)

# Convert temp column to list
temp_list = data["temp"].to_list()
print("Temperature list:", temp_list)

# Calculate average temperature (manual)
average = sum(temp_list) / len(temp_list)
print("Average temperature (manual):", average)

# Calculate mean and max using pandas
print("Average temperature (pandas):", data["temp"].mean())
print("Maximum temperature:", data["temp"].max())

# Get a row where day is Monday
print("Weather on Monday:\n", data[data.day == "Monday"])

# Get temperature only for Monday
monday_temp = data[data.day == "Monday"].temp
print("Monday's temperature:", monday_temp)

# Create a DataFrame from scratch and save it
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print("Student DataFrame:\n", data)

#Save to CSV (without index)
data.to_csv("new_data.csv")
