import json
from openai import OpenAI
from ..tools import DummyWeather

client = OpenAI()

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What's the weather in Paris in celsius?"}
]

first = client.chat.completions.create(
    model="gpt-4o-2024-08-06",
    messages=messages,
    tools=[DummyWeather.definition],
)

choice = first.choices[0].message

if choice.get("tool_calls"):
    messages.append({
        "role": "assistant",
        "tool_calls": [tc.model_dump() for tc in choice.tool_calls], 
        "content": choice.content or ""  # models sometimes include content alongside tool calls
    })

    for tc in choice.tool_calls:
        args = json.loads(tc.function.arguments or "{}")
        result = DummyWeather.get_weather(**args)

        messages.append({
            "role": "tool",
            "tool_call_id": tc.id,
            "name": tc.function.name, 
            "content": json.dumps(result)
        })

    final = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=messages
    )

    print("Final assistant answer:")
    print(final.choices[0].message.content)
else:
    print(choice.content)
