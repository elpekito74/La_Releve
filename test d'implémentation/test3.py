import openai

# Set your OpenAI API key directly
openai.api_key = "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"

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message['content'])