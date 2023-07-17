import openai

openai.api_key = "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"    #key is from sohailmalikraja2 account with moms number

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Give me an essay about penguins"}])
print(completion.choices[0].message.content)