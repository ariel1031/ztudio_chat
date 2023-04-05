import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role":"user", "content":"Emotionally analyze the following sentences and choose one of the following as a result: 'Joy', 'Sad', 'Fear', 'Angry', 'Hate', 'Surprised', 'Interest', 'Bored' or 'Pain'. '야 오늘 알바 월급 들어왔다'"}
    ]
)
print(completion)