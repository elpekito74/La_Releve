import openai

# Set your OpenAI API key directly
openai.api_key = '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'

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=150,
        temperature=0.7,
    )
    return response['choices'][0]['message']['content'].strip()

# Example usage
prompt = input("Say to GPT: ")
response = chat_with_gpt(prompt)
print(response)