from openai import OpenAI

client = OpenAI(
    api_key="sk-OeJKLgdHstcVJqmLK76D1HOcghZLhDgd5Vm3zE05eaR3yyB9",
    base_url="https://api.chatanywhere.tech/v1"
)




def gpt_35_api(messages: list):
    completion = client.chat.completions.create(model="gpt-5", messages=messages)
    return completion.choices[0].message.content


def gpt_35_api_stream(messages: list):
    stream = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=messages,
        stream=True,
    )
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")







from balethon import Client
from balethon.conditions import at_state

bot = Client('900766790:thzDoNjmf9WEU03wzgfAquieMJNwJRWBS6Y')

@bot.on_message(at_state(None))
async def home_state(message):
    await message.reply( 'سلام ' )
    message.author.set_state('NAME')


@bot.on_message(at_state('NAME'))
async def name_state(message):
    msg = [{'role': 'user', "id": "pmpt_abc123test",'content': '{}'.format(message.text)},]
    name = gpt_35_api(msg)
    await message.reply(name)
    message.author.set_state('NAME')


@bot.on_message(at_state('AGE'))
async def age_state(message):
    age = message.text
    await message.reply(
        f'You are {age} years old, good for you!\nHave a nice day!'
    )
    message.author.del_state()

bot.run(debug=True, port=8050, host='0.0.0.0')
