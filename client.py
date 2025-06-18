from openai import openAI
client = openAI(
    api_key='sk-proj-Wxs17ehGk2PnwmzCHcDwT3B1bkFJFMj6bYTk9jG1bkZaFTcj',
)

completion=client.chat.completions.create(
    model="gpt-3.5-turbo",
    message=[
        {"role": "system","content":"you are virtual assistant name as Jarvis skilled in general task like alexa and google cloud"},
        {"role":"user","content":"what is coding"}
    ]
)
print(completion.choices[0].message.content)