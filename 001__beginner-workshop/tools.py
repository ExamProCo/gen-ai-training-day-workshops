def get_date_time():
  # Define the Eastern Time Zone offset
  # Note: This doesn't account for daylight saving time changes
  eastern_offset = timedelta(hours=-5)
  eastern_tz = timezone(eastern_offset, name="EST")

  # Get the current time and convert it to Eastern Time
  now = datetime.now(timezone.utc).astimezone(eastern_tz)

  return {
    "date": now.strftime("%Y-%m-%d"),
    "time": now.strftime("%H:%M:%S"),
    "timezone": "Eastern Time (EST)"
  }

def get_weather(location):
  weather_data = {
    "New York": {"temperature": 22, "condition": "Sunny"},
    "London": {"temperature": 15, "condition": "Cloudy"},
    "Tokyo": {"temperature": 28, "condition": "Rainy"},
    "Toronto": {"temperature":-20, "condition": "Brr... Cold"}
  }
  return weather_data.get(location, {"temperature": 20, "condition": "Unknown"})

def get_historical_fact():
  facts =[
    "Jesse Owens was born on this day of September 12, in 1913 in Oakville, Alabama, U.S.—died March 31, 1980, Tucson, Arizona. He was an American track-and-field athlete who became one of the sport’s most legendary competitors after winning four gold medals at the 1936 Olympic Games in Berlin.",
    "On this day of Sept. 12th 1992, astronaut Mae Jemison became the first African American woman to fly in space, part of the STS-47 Spacelab J mission.",
    "On this day of Sept. 12th 1959 the TV series Bonanza premiered on NBC, and it became one of the longest-running westerns in broadcast history."
  ]
  return {"2024-11-03": random.choice(facts)}

weather_tools = [
  { "toolSpec": {
    "name": "get_date_time",
    "description": "Get the current date and time in Eastern Time Zone.",
    "inputSchema": {
      "json": { "type": "object", "properties": {}, "required": [] }
    }
  }},
  { "toolSpec": {
    "name": "get_weather",
    "description": "Get the current weather for a location",
    "inputSchema": {
      "json": {
        "type": "object",
        "properties": { "location": {"type": "string", "description": "The city to get weather for"} },
        "required": ["location"]
      }
    }
  }},
  { "toolSpec": {
    "name": "get_historical_fact",
    "description": "Get a historical fact that occurred on the current date",
    "inputSchema": { "json": { "type": "object", "properties": {}, "required": [] } }
  }}
]
