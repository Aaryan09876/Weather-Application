# ================================
# PROFESSIONAL WEATHER APP
# Python + Tkinter + OpenWeatherMap
# ================================

# Install requests:
# pip install requests

import requests
from tkinter import *
from datetime import datetime
from tkinter import messagebox


# ================================
# API KEY
# ================================
API_KEY = "80b9f1899ca9c5210f2e3a1dfcb4014d"

# ================================
# FUNCTION TO GET WEATHER
# ================================
def get_weather():

    city = city_entry.get().strip()

    # Empty input check
    if city == "":
        messagebox.showwarning("Input Error", "Please enter city name")
        return

    try:
        # API URL
        url = (
            f"https://api.openweathermap.org/data/2.5/weather?"
            f"q={"city"}&appid={"80b9f1899ca9c5210f2e3a1dfcb4014d"}&units=metric"
        )

        # Request
        response = requests.get(url, timeout=10)

        # Convert to JSON
        data = response.json()

        # Check success
        if response.status_code == 200:

            # Weather Data
            city_name = data["name"]
            country = data["sys"]["country"]

            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]

            weather = data["weather"][0]["main"]
            description = data["weather"][0]["description"]

            wind_speed = data["wind"]["speed"]

            # Weather Emoji
            emoji = "☀"

            if weather == "Clouds":
                emoji = "☁"
            elif weather == "Rain":
                emoji = "🌧"
            elif weather == "Thunderstorm":
                emoji = "⛈"
            elif weather == "Snow":
                emoji = "❄"
            elif weather == "Mist":
                emoji = "🌫"

            # Final Output
            result = (
                f"{emoji} WEATHER REPORT {emoji}\n\n"
                f"📍 City: {city_name}, {country}\n\n"
                f"🌡 Temperature: {temp} °C\n"
                f"🤒 Feels Like: {feels_like} °C\n\n"
                f"☁ Weather: {weather}\n"
                f"📝 Description: {description}\n\n"
                f"💧 Humidity: {humidity}%\n"
                f"📊 Pressure: {pressure} hPa\n\n"
                f"🌬 Wind Speed: {wind_speed} m/s"
            )

            weather_label.config(text=result)

        else:
            messagebox.showerror(
                "Error",
                "City not found!\nPlease enter correct city name."
            )

    except requests.exceptions.ConnectionError:
        messagebox.showerror(
            "Network Error",
            "No internet connection"
        )

    except requests.exceptions.Timeout:
        messagebox.showerror(
            "Timeout Error",
            "Request timeout\nTry again later"
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            f"Something went wrong\n{e}"
        )

# ================================
# MAIN WINDOW
# ================================
root = Tk()

root.title("Professional Weather App")
root.geometry("550x650")
root.resizable(False, False)
root.configure(bg="#0f172a")

# ================================
# HEADING
# ================================
title_label = Label(
    root,
    text="Weather Application",
    font=("Arial", 26, "bold"),
    bg="#0f172a",
    fg="white"
)
title_label.pack(pady=20)

# ================================
# ENTRY BOX
# ================================
city_entry = Entry(
    root,
    font=("Arial", 18),
    width=25,
    justify=CENTER,
    bd=3
)
city_entry.pack(pady=15)

# ================================
# BUTTON
# ================================
search_button = Button(
    root,
    text="Check Weather",
    font=("Arial", 16, "bold"),
    bg="#38bdf8",
    fg="black",
    padx=15,
    pady=8,
    command=get_weather
)
search_button.pack(pady=10)

# ================================
# RESULT LABEL
# ================================
weather_label = Label(
    root,
    text="Enter city name and click button",
    font=("Arial", 15),
    bg="#0f172a",
    fg="white",
    justify=LEFT
)
weather_label.pack(pady=30)

# ================================
# FOOTER
# ================================
footer = Label(
    root,
    text="Powered by OpenWeatherMap API",
    font=("Arial", 10),
    bg="#0f172a",
    fg="gray"
)
footer.pack(side=BOTTOM, pady=10)

# ================================
# RUN APPLICATION
# ================================
root.mainloop()


print("======================================")
print("   WEATHER BASED ROUTINE PLANNER")
print("======================================\n")

# User Inputs
city = input("Enter City Name: ")

temperature = float(input("Enter Temperature (°C): "))
rain_probability = int(input("Enter Rain Probability (%): "))
humidity = int(input("Enter Humidity (%): "))
wind_speed = float(input("Enter Wind Speed (km/h): "))

thunderstorm = input("Thunderstorm Warning? (yes/no): ").lower()

print("\n======================================")
print(f" Routine Suggestions for {city}")
print("======================================\n")

# Clothes Washing Suggestion
if rain_probability < 40:
    print("🧺 Wash clothes before 2 PM")
else:
    print("⚠️ Avoid washing clothes today")

# Jogging Suggestion
if temperature < 28 and rain_probability < 30:
    print("🏃 Best jogging time: 6 AM - 7 AM")
elif temperature < 35:
    print("🏃 Best jogging time: 5 AM - 6 AM")
else:
    print("⚠️ Too hot for jogging in daytime")

# Travel Suggestion
if rain_probability > 60 or thunderstorm == "yes":
    print("🚗 Avoid travel after 5 PM due to rain")
else:
    print("🚗 Travel conditions are good")

# Umbrella Suggestion
if rain_probability > 50:
    print("🌂 Carry umbrella")

# Outdoor Work
if temperature > 35:
    print("☀️ Avoid outdoor work from 12 PM - 3 PM")

# Humidity Check
if humidity > 80:
    print("💧 High humidity today, drink more water")

# Wind Condition
if wind_speed > 30:
    print("🌪️ Strong winds expected today")

# AC / Fan Suggestion
if temperature >= 35:
    print("❄️ AC recommended")
elif temperature >= 28:
    print("🌀 Fan is enough")
else:
    print("🌤️ Pleasant weather today")

# Water Reminder
if temperature > 30:
    print("🥤 Drink water every 1 hour")

# Gardening Suggestion
if rain_probability < 30:
    print("🌱 Good time for gardening in evening")
else:
    print("🌱 Rain may help watering plants naturally")

# Sleep Suggestion
if temperature > 32:
    print("😴 Sleep with proper ventilation")

print("\n======================================")
print("   HAVE A GREAT DAY 😊")
print("======================================")
