# -*- coding: utf-8 -*-
import os
import openai
import json

openai.api_key = os.getenv("OPENAI_API_KEY")
completion = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    messages = [
        {"role":"system", "content":"Analyze the next sentence and recommend a 'gesture' that the speaker of the sentence would do. As a result of the gesture recommendations in the sentence, you 'wave your hand', 'hit the person next to you', 'kiss you', 'hurray', and 'cover your face with your hands'. you can choose one of them. For example, if I send the sentence, '권민철: 오늘 알바비 들어왔다' you can recommend the action of 'hurray'. Now, analyze the sentence."},
        {"role":"user", "content":"Analyze the next sentence and recommend a 'gesture' that the speaker of the sentence would do. As a result of the gesture recommendations in the sentence, you 'wave your hand', 'hit the person next to you', 'kiss you', 'hurray', and 'cover your face with your hands'. you can choose one of them. For example, if I send the sentence, '권민철: 오늘 알바비 들어왔다' you can recommend the action of 'hurray'. Now, analyze the sentence."}
    ]
)

print(completion)
print("completion['choices'][0]['message']['content'] : " , completion['choices'][0]['message']['content']) #겁나 중요한 놈
