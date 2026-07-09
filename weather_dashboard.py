import requests
import matplotlib.pyplot as plt

# Enter your OpenWeather API Key
API_KEY ="1dcd60243e687d8f8f1c3d564aa371ed"

# City Name
CITY = "Delhi"

# API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# Get Data
response = requests.get(url)
data = response.json()

# Check for errors
if response.status_code != 200:
    print("Error:", data.get("message", "Something went wrong"))
    exit()

# Extract Weather Data
temperature = data["main"]["temp"]
humidity = data["main"]["humidity"]
pressure = data["main"]["pressure"]

# Print Data
print("Weather Report")
print("----------------------")
print("City:", CITY)
print("Temperature:", temperature, "°C")
print("Humidity:", humidity, "%")
print("Pressure:", pressure, "hPa")

# Create Bar Chart
labels = ["Temperature", "Humidity", "Pressure"]
values = [temperature, humidity, pressure]

plt.figure(figsize=(8,5))
plt.bar(labels, values)
plt.title(f"Weather Data of {CITY}")
plt.ylabel("Values")
plt.grid(axis="y")

# Save Chart
plt.savefig("weather_dashboard.png")

# Show Chart
plt.show()

print("Dashboard saved as weather_dashboard.png")