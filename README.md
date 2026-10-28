🤖 Automated Indian Weather Twitter Bot
An automated Python bot that fetches real-time weather and air quality (AQI) data for major Indian cities, generates immersive, story-like weather updates using the Groq API (Llama 3.3), creates realistic city-specific AI images using Pollinations AI, and posts them directly to Twitter (X) every 24 hours.

✨ Features
Multi-City Rotation: Randomly selects from major Indian cities (Chennai, Delhi, Bengaluru, Mumbai, Kolkata, Hyderabad).

Real-Time Data: Fetches live temperatures, humidity, wind speeds, UV index, and US EPA Air Quality Index (AQI) via WeatherAPI.

AI Storyteller: Uses Groq's llama-3.3-70b-versatile model to turn raw data into an evocative, personal narrative under 280 characters.

Location-Aware AI Images: Features a built-in landmark mapping dictionary (e.g., India Gate for Delhi, Howrah Bridge for Kolkata) to prompt the AI generator for accurate, context-specific city photos.

Automated Scheduling: Runs persistently in the background, posting updates automatically every 24 hours.

🛠️ Prerequisites & Tech Stack
Python 3.8+

Libraries required:

Bash
pip install requests tweepy schedule
🔑 Required API Keys
To run this bot, you will need keys from the following services:

WeatherAPI: Get a free key at weatherapi.com

Groq API: Get a free developer key at console.groq.com

Twitter Developer Account: An app with OAuth 1.0a User Context credentials (API Key, API Key Secret, Access Token, and Access Token Secret) configured with Read and Write permissions.

🚀 Installation & Running
Clone the repository:

Bash
git clone https://github.com/YOUR_USERNAME/your-repo-name.git
cd your-repo-name
Install dependencies:

Bash
pip install requests tweepy schedule
Configure your API keys:
Open the Python script and replace the placeholder strings with your actual API keys:

Python
WEATHER_API_KEY = "your_weather_api_key"
GROQ_API_KEY = "your_groq_api_key"
TWITTER_API_KEY = "your_twitter_api_key"
TWITTER_API_KEY_SECRET = "your_twitter_secret"
TWITTER_ACCESS_TOKEN = "your_access_token"
TWITTER_ACCESS_TOKEN_SECRET = "your_access_token_secret"
Run the bot:

Bash
python weather_bot.py
(Note: The script will execute the first job immediately upon startup, and then enter a background loop to post every 24 hours. Keep your terminal or cloud server running.)

⚙️ How It Works
Fetch: WeatherAPI pulls current metrics and air quality.

Write: Groq API processes the metrics into a creative, human-like tweet complete with hashtags.

Visualize: Pollinations AI builds a customized image prompt using city landmarks and current weather conditions, saving a temporary graphic.

Post: Tweepy uploads the image media and publishes the final status update to Twitter.

Clean: Local files are cleaned up automatically after posting.

📝 License
This project is open-source and available under the MIT License.
