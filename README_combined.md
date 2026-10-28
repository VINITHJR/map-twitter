# 🌦️ Environmental Intelligence & Weather Automation Projects

This repository documents two Python/web projects focused on weather, air quality, environmental monitoring, and automated weather updates.

- **[Automated Indian Weather X Bot](#-automated-indian-weather-x-bot):** Creates AI-written weather updates and city-specific images, then schedules posts to X (formerly Twitter).
- **[Live Environmental & Disaster Data Map](#-live-environmental--disaster-data-map):** An interactive map for exploring weather, air quality, severe-weather information, and earthquake data by location.

> **Important:** These are separate applications and may have different source files and setup requirements. Keep each application's files in its own folder, or adapt the project structure below to match your actual repository.

---

# 🤖 Automated Indian Weather X Bot

An automated Python bot that fetches current weather and air-quality data for major Indian cities, generates short, story-like weather updates with the Groq API, creates city-specific AI images using Pollinations AI, and publishes updates to X.

## ✨ Features

- **Multi-city rotation:** Randomly selects a city from Chennai, Delhi, Bengaluru, Mumbai, Kolkata, and Hyderabad.
- **Live weather data:** Retrieves temperature, humidity, wind speed, UV index, and air-quality data through WeatherAPI.
- **AI-generated updates:** Uses Groq's `llama-3.3-70b-versatile` model to turn weather data into an engaging post intended to fit within 280 characters.
- **City-aware image prompts:** Uses landmark mappings (for example, India Gate for Delhi and Howrah Bridge for Kolkata) to guide image generation.
- **Scheduled posting:** Runs a job every 24 hours while the script remains running.
- **Temporary-file cleanup:** Removes generated image files after the posting workflow finishes, if implemented in the script.

## 🧰 Tech Stack & APIs

- **Language:** Python 3.8+
- [WeatherAPI](https://www.weatherapi.com/) — weather and air-quality data
- [Groq API](https://console.groq.com/) — AI-generated text
- [Pollinations AI](https://pollinations.ai/) — image generation
- [Tweepy](https://www.tweepy.org/) — X API integration
- [Schedule](https://schedule.readthedocs.io/) — recurring jobs
- [Requests](https://requests.readthedocs.io/) — HTTP requests

## 🔑 Prerequisites

Before running the bot, make sure you have:

- Python 3.8 or newer installed.
- API credentials for WeatherAPI and Groq.
- An X Developer account and an app with the permissions and API access needed to publish posts and upload media.
- Network access to the required services.

### Required credentials

1. **WeatherAPI key:** Create an account at [weatherapi.com](https://www.weatherapi.com/).
2. **Groq API key:** Create a key in the [Groq Console](https://console.groq.com/).
3. **X API credentials:** Configure an X Developer app with user-context authentication and the permissions needed to publish posts and upload media. Media upload availability may depend on your API access level.

The bot uses these environment-variable names:

- `WEATHER_API_KEY`
- `GROQ_API_KEY`
- `TWITTER_API_KEY`
- `TWITTER_API_KEY_SECRET`
- `TWITTER_ACCESS_TOKEN`
- `TWITTER_ACCESS_TOKEN_SECRET`

**Security:** Never commit API keys, access tokens, or secrets to GitHub. Use environment variables or a local `.env` file excluded from version control. Revoke or rotate any secret that has already been exposed.

## 🚀 Installation & Running

### 1. Clone the repository

Replace the example URL with your repository URL:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

### 2. Create and activate a virtual environment (recommended)

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install requests tweepy schedule
```

You can also save these packages in a `requirements.txt` file:

```text
requests
tweepy
schedule
```

### 4. Configure API credentials

In `weather_bot.py`, read the credentials from environment variables rather than hard-coding them:

```python
import os

WEATHER_API_KEY = os.environ["WEATHER_API_KEY"]
GROQ_API_KEY = os.environ["GROQ_API_KEY"]
TWITTER_API_KEY = os.environ["TWITTER_API_KEY"]
TWITTER_API_KEY_SECRET = os.environ["TWITTER_API_KEY_SECRET"]
TWITTER_ACCESS_TOKEN = os.environ["TWITTER_ACCESS_TOKEN"]
TWITTER_ACCESS_TOKEN_SECRET = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]
```

Set these variables in your terminal before running the bot.

**Windows PowerShell:**

```powershell
$env:WEATHER_API_KEY = "your_weather_api_key"
$env:GROQ_API_KEY = "your_groq_api_key"
$env:TWITTER_API_KEY = "your_twitter_api_key"
$env:TWITTER_API_KEY_SECRET = "your_twitter_api_key_secret"
$env:TWITTER_ACCESS_TOKEN = "your_twitter_access_token"
$env:TWITTER_ACCESS_TOKEN_SECRET = "your_twitter_access_token_secret"
```

**macOS / Linux:**

```bash
export WEATHER_API_KEY="your_weather_api_key"
export GROQ_API_KEY="your_groq_api_key"
export TWITTER_API_KEY="your_twitter_api_key"
export TWITTER_API_KEY_SECRET="your_twitter_api_key_secret"
export TWITTER_ACCESS_TOKEN="your_twitter_access_token"
export TWITTER_ACCESS_TOKEN_SECRET="your_twitter_access_token_secret"
```

These terminal variables generally last only for the current terminal session. If you use a `.env` file, make sure `.env` is listed in `.gitignore` and use an appropriate environment-variable loader.

### 5. Start the bot

```bash
python weather_bot.py
```

The described workflow runs a post at startup and then schedules another run every 24 hours. Confirm that behavior in your code before relying on it. The machine or server must remain online, and the script must continue running for scheduled jobs to execute.

## ⚙️ How It Works

1. **Fetch:** Requests current weather and air-quality metrics from WeatherAPI.
2. **Write:** Sends the data to Groq to generate a short weather narrative.
3. **Create an image:** Builds a prompt from the selected city, a mapped landmark, and the weather conditions, then requests an image from Pollinations AI.
4. **Publish:** Uses Tweepy and your X credentials to publish the post and attach the image, provided your X API access supports the required operations.
5. **Clean up:** Removes temporary image files if cleanup is implemented and the files are no longer needed.

## 🛡️ Reliability Notes

- Handle API errors, timeouts, rate limits, and failed image generation.
- Verify that the generated post fits X's current limits and complies with platform automation rules.
- Ensure the AI narrative does not invent weather conditions that are absent from the API response.
- Check current pricing, API limits, model availability, and terms for each third-party service.
- A local `schedule` loop is not a hosted service. For always-on operation, use a reliable server or an external scheduler.

---

# 🌍 Live Environmental & Disaster Data Map

An interactive web-based map application built with **Leaflet.js** and **OpenStreetMap**. It is designed to let users click a location and explore weather, air-quality, severe-weather, and seismic information from integrated data APIs.

## ✨ Features

- **Interactive map:** Uses Leaflet and OpenStreetMap, allowing users to pan, zoom, and click locations around the globe.
- **Reverse geocoding:** Identifies the nearest town or city and country for a clicked location, subject to API coverage.
- **Current date and weather:** Displays the current date and local temperature in Celsius.
- **Air-quality monitoring:** Displays PM2.5 concentration in µg/m³ and an air-quality category, if supported by the API response and implemented in the application.
- **Severe-weather alerts:** Intended to highlight severe weather events such as hurricanes, tropical storms, and tornadoes when suitable alert data is available.
- **Earthquake and tsunami information:** Integrates the USGS Earthquake API to display recent significant earthquake information and any tsunami-related flag included in the returned data.

> **Data limitation:** The exact features available depend on the APIs, endpoints, and response fields used by your implementation. A nearby earthquake is not necessarily the nearest event in every situation, and a tsunami flag in an earthquake feed is not the same as an active tsunami warning. Use official emergency sources for safety-critical alerts.

## 🛠️ Tech Stack & APIs

- **Frontend:** HTML5, CSS3, vanilla JavaScript
- **Mapping library:** [Leaflet.js](https://leafletjs.com/) v1.9.4
- **Map tiles:** [OpenStreetMap](https://www.openstreetmap.org/)
- **Weather, air quality, and geocoding:** [OpenWeatherMap API](https://openweathermap.org/)
- **Earthquake data:** [USGS Earthquake Hazards Program](https://earthquake.usgs.gov/earthquakes/feed/)

## 📋 Prerequisites

- A modern web browser such as Chrome, Firefox, Edge, or Safari.
- A free API key from [OpenWeatherMap](https://openweathermap.org/).
- Internet access to load the map tiles and call the APIs.

## 🚀 Installation & Running Locally

This is intended to be a client-side HTML, CSS, and JavaScript application, so a separate backend or Node.js setup is not required unless your implementation adds one.

### 1. Clone or download the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

### 2. Open the project

Open the project folder in Visual Studio Code or another code editor. Locate the main HTML file, such as `index.html` or `map.html`.

### 3. Configure your OpenWeatherMap API key

Find the API key placeholder in your JavaScript and replace it with your own key:

```javascript
const API_KEY = "YOUR_OPENWEATHERMAP_API_KEY";
```

For a public repository, remember that a key placed in browser-side JavaScript is visible to visitors. Restrict the key in your provider settings where possible, monitor usage, and never use a privileged secret in frontend code. For stronger protection, proxy API calls through a backend.

### 4. Run the application

**Recommended: VS Code Live Server**

1. Install the **Live Server** extension in VS Code.
2. Open the main HTML file.
3. Right-click the file and select **Open with Live Server**, or click **Go Live** in the status bar.

You can also serve the files using another local static web server. Opening the HTML file directly may work, but a local server can avoid browser restrictions with some requests.

## 📸 Usage

1. Open the map in your browser.
2. Click a location on the map, such as a major city or coastal area.
3. Review the information displayed in the popup or information panel. Depending on the implementation and API responses, it may include:
   - Location name and country
   - Current date and temperature
   - PM2.5 concentration and air-quality category
   - Weather or severe-weather information
   - Recent earthquake magnitude, location, and tsunami-related data

## ⚠️ Safety & Data Notes

- API data may be delayed, unavailable, or incomplete.
- Do not treat this project as an official emergency-alert system.
- Check official meteorological, disaster-management, and local-authority sources for warnings and instructions.
- Follow the attribution and usage policies for OpenStreetMap, OpenWeatherMap, and USGS data.
- Avoid publishing API keys in a public repository.

---

## 🗂️ Suggested Repository Structure

If both projects are maintained in the same repository, a structure like this can keep their files separate:

```text
your-repository/
├── README.md
├── .gitignore
├── weather-x-bot/
│   ├── weather_bot.py
│   └── requirements.txt
└── environmental-disaster-map/
    ├── index.html
    ├── style.css
    └── script.js
```

Adjust the filenames and folders to match the actual files in your project. If the two projects are in separate repositories, use a separate README for each repository or remove the section that does not belong to that repository.

## 📄 License & Attribution

Choose a license that matches how you want others to use the code. If you intend to use the MIT License, add a `LICENSE` file containing the MIT License text before describing the code as MIT-licensed.

Map tiles and data may have separate attribution and usage requirements. Follow the relevant provider terms and credit OpenStreetMap contributors where required.

## 🤝 Contributing

Contributions are welcome. Before submitting changes:

1. Describe the problem or feature.
2. Test the affected application and API integrations.
3. Never include credentials, access tokens, or private configuration files in commits.
4. Update this README when setup instructions or functionality changes.
