from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)