import requests
import random
from datetime import datetime, timedelta

# API Keys
WEATHER_API_KEY = "f4ed27622e29484a8c342846251210"
GROQ_API_KEY = "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"  # Replace with your Groq API key

CITIES = ["Chennai", "Delhi", "Bengaluru", "Mumbai", "Kolkata", "Hyderabad"]

def get_detailed_weather(city):
    """Fetch detailed weather + air quality data for a city"""
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city},India&aqi=yes"
    response = requests.get(url)
    data = response.json()
    
    weather = {
        'city': data['location']['name'],
        'region': data['location']['region'],
        'country': data['location']['country'],
        'local_time': data['location']['localtime'],
        'temp_c': data['current']['temp_c'],
        'feels_like_c': data['current']['feelslike_c'],
        'condition': data['current']['condition']['text'],
        'wind_kph': data['current']['wind_kph'],
        'humidity': data['current']['humidity'],
        'uv': data['current']['uv'],
        'aqi_us': data['current']['air_quality']['us-epa-index'],
        'pm2_5': data['current']['air_quality']['pm2_5'],
        'pm10': data['current']['air_quality']['pm10']
    }
    return weather

# --- MODIFICATION START ---
# This new function generates a narrative-style tweet.

def generate_story_tweet_with_groq(weather_data):
    """Generate a descriptive, story-like weather tweet using Groq API"""
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # New prompt designed to generate a story-like paragraph
    prompt = f"""
Write a descriptive, story-like weather update for {weather_data['city']}, India.

Your task is to create a single, evocative paragraph of about 6 to 7 lines. Don't just list the facts; weave them into a narrative that paints a picture of the city's atmosphere.

- Start by setting the scene based on the weather condition: '{weather_data['condition']}'.
- Naturally mention the temperature ({weather_data['temp_c']}°C) and the "feels like" temperature ({weather_data['feels_like_c']}°C) as part of the story.
- Subtly comment on the air quality (AQI is {weather_data['aqi_us']}) and what it means for being outdoors.
- The tone should be personal and immersive, as if a local is describing their evening.
- Conclude the paragraph with 3-4 fitting hashtags.

CURRENT WEATHER DATA:
- City: {weather_data['city']}
- Temperature: {weather_data['temp_c']}°C
- Feels Like: {weather_data['feels_like_c']}°C
- Condition: {weather_data['condition']}
- Air Quality Index (US EPA): {weather_data['aqi_us']}
"""
    
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.8,  # Higher temperature for more creative, narrative text
        "max_tokens": 300   # Increased tokens to allow for a longer paragraph
    }
    
    response = requests.post(url, headers=headers, json=payload)
    result = response.json()
    
    return result['choices'][0]['message']['content']

# --- MODIFICATION END ---


def generate_image(prompt):
    """Generate an AI image from Pollinations API"""
    url = f"https://image.pollinations.ai/prompt/{prompt}"
    response = requests.get(url)
    filename = "weather_image.png"
    with open(filename, "wb") as f:
        f.write(response.content)
    return filename

def main():
    # Randomly choose a city
    city = random.choice(CITIES)
    print(f"📍 Selected City: {city}\n")
    
    # Get weather data
    print("🔄 Fetching current weather data...")
    current = get_detailed_weather(city)
    
    # Display raw weather data
    print(f"\n📊 Weather Data for {city}")
    print(f"🌡 Temp: {current['temp_c']}°C (Feels like {current['feels_like_c']}°C)")
    print(f"💨 Wind: {current['wind_kph']} km/h")
    print(f"💧 Humidity: {current['humidity']}%")
    print(f"☀ UV Index: {current['uv']}")
    print(f"🏭 AQI (US EPA): {current['aqi_us']} | PM2.5: {current['pm2_5']} | PM10: {current['pm10']}")
    
    # --- MODIFICATION START ---
    # Generate a story tweet
    print("\n✍ Generating story-like tweet with Groq AI (llama-3.3-70b-versatile)...\n")
    story_tweet = generate_story_tweet_with_groq(current) # Call the new function
    
    print("="*70)
    print("📝 WEATHER STORY TWEET")
    print("="*70)
    print(story_tweet) # Print the generated story
    print("="*70)
    # --- MODIFICATION END ---
    
    # Generate image
    print(f"\n🎨 Generating AI image...")
    prompt = f"{current['condition']} weather in {city}, India, realistic photo"
    image_path = generate_image(prompt)
    print(f"🖼 Image saved as: {image_path}")
    
    # Display image in Colab
    try:
        from IPython.display import Image, display
        print("\n📷 Displaying image:")
        display(Image(filename=image_path))
    except ImportError:
        print("(Image display requires IPython environment like Jupyter or Colab)")
    
    # Save the story tweet to a file
    tweet_filename = f"weather_story_{city}_{datetime.now().strftime('%Y%m%d')}.txt"
    with open(tweet_filename, "w", encoding="utf-8") as f:
        f.write(f"Weather Story for {city}\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("="*70 + "\n\n")
        f.write(story_tweet)
    print(f"\n💾 Story saved to: {tweet_filename}")

# Run the system
if __name__ == "__main__":
    main()