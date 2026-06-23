import os
import json
import urllib.request
import urllib.parse
import urllib.error


def load_api_key():
    """
    Reads the API key from a file called .env in the same folder.

    The .env file should have one line that looks like this:
        OPENWEATHER_API_KEY=your_key_here

    We read the file ourselves (line by line) so we don't need to
    install any extra packages.
    """
    env_path = os.path.join(os.path.dirname(__file__), ".env")

    if not os.path.exists(env_path):
        return None

    with open(env_path) as env_file:
        for line in env_file:
            line = line.strip()
            # Skip blank lines and comment lines (lines starting with #)
            if not line or line.startswith("#"):
                continue
            if line.startswith("OPENWEATHER_API_KEY="):
                # Take everything after the first "=" sign
                return line.split("=", 1)[1].strip()

    return None


def get_weather(city):
    """
    Looks up the current weather for a city using the OpenWeatherMap API.

    Returns a friendly text description, or an error message string
    (we return the error as text instead of raising, to match the
    style of the other functions in this project).
    """
    api_key = load_api_key()
    if not api_key:
        return "No API key found. Please put your key in the .env file."

    # Build the web address (URL) we want to ask for weather data.
    # urlencode safely turns our settings into a query string like:
    #   ?q=London&appid=KEY&units=metric
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = urllib.parse.urlencode({
        "q": city,
        "appid": api_key,
        "units": "metric",  # use Celsius
    })
    url = f"{base_url}?{params}"

    try:
        with urllib.request.urlopen(url) as response:
            data = json.load(response)
    except urllib.error.HTTPError as error:
        if error.code == 404:
            return f"Could not find a city called '{city}'."
        if error.code == 401:
            return "The API key was rejected. Please check your .env file."
        return f"Something went wrong (HTTP error {error.code})."
    except urllib.error.URLError:
        return "Could not connect to the weather service. Are you online?"

    # Pull the pieces we care about out of the data the API sent back.
    description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]

    return (
        f"Weather in {city.title()}:\n"
        f"  Condition:   {description}\n"
        f"  Temperature: {temperature}C (feels like {feels_like}C)\n"
        f"  Humidity:    {humidity}%"
    )


if __name__ == "__main__":
    city = input("Enter a city: ").strip()
    print(get_weather(city))