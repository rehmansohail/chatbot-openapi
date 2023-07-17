import openai

openai.api_key = ""    #use your own openai api key here

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Give me an essay about penguins"}])
print(completion.choices[0].message.content)