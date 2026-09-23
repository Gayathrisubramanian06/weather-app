# Weather App 🌤️

A simple desktop GUI Weather Application built with Python and Tkinter that fetches real-time weather information using the OpenWeatherMap API.

---

## 🚀 Features

- **Intuitive GUI**: Built with Tkinter and TTK widgets.
- **Select State / City**: Dropdown list to pick Indian states and union territories.
- **Live Weather Data**:
  - Weather Condition (Climate)
  - Weather Description
  - Temperature in °C
  - Atmospheric Pressure

---

## 🛠️ Prerequisites

- Python 3.x
- `requests` library

To install the required library:
```bash
pip install requests
```

---

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Gayathrisubramanian06/weather-app.git
   cd weather-app
   ```

2. Configure your API key:
   - Copy `config.example.py` to `config.py`:
     ```bash
     cp config.example.py config.py
     ```
   - Open `config.py` and replace `"YOUR_API_KEY_HERE"` with your actual OpenWeatherMap API key.

3. Run the application:
   ```bash
   python main.py
   ```

---

## 📌 Built With

- **Python**
- **Tkinter** (Standard GUI Library)
- **OpenWeatherMap API**
