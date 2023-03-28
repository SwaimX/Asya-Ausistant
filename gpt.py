import openai
from .cfg import openai_tk

openai.api_key = openai_tk

context = ""

def gpt_executor(msg):
    global context
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=context + msg,
        temperature=0.5,
        max_tokens=200,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=["You:"],
    )
    context += response.choices[0].text
    return context

if __name__ == "__main__":
    while True:
        msg = input("Введіть текст: ")
        if msg == "Нова тема":
            context = ""
        else:
            ans = gpt_executor(msg)
            print(ans)