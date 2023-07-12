import openai
import argparse
import constants


parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="The prompt to send to OpenAI API")
args = parser.parse_args()


openai.api_key = constants.APIKEY

#messages = [{'role':'system','content':'create a python script to move files from download folder to a folder called to_delete'}]

messages = [{'role':'system','content': args.prompt}]

chat = openai.ChatCompletion.create(model='gpt-3.5-turbo',messages=messages, max_tokens=1000)
reply = chat['choices'][0].message.content
print(reply)