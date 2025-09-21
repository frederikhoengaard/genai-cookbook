class DummyWeather:
    definition = {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather in a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string"},
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
                "required": ["city"]
            },
        },
    }

    @staticmethod
    def get_weather(city: str, unit: str = "celsius"):
        if unit == "celsius":
            return {"city": city, "temperature": 21, "unit": "°C"}
        else:
            return {"city": city, "temperature": 70, "unit": "°F"}