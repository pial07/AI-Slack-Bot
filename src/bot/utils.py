import os
from openai import OpenAI
import helpers
import pprint

OPENAI_API_KEY=helpers.config("OPENAI_API_KEY", default=None )

def get_openai_client():
    return OpenAI(
        api_key=OPENAI_API_KEY,

    )

def chat_with_openai(message,model="gpt-4o",raw=False):
    client = get_openai_client()
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", 
             "content": "You are an amazing code assistant"
             },
            {
                "role": "user",
                "content": message,
            },
        ],
    )
    if raw:
        return response
    return response.choices[0].message.content 
    