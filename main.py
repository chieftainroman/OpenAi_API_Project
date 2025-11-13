from dotenv import load_dotenv
from openai import OpenAI
import os 


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

genre =  input("Enter a genre for the story: ")

user_input = ""

while user_input != "exit":
    
    user_input = input("Ask something: ")
    
    if user_input != "exit":
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            max_tokens=200,
            messages=[
            {"role": "system", "content": "You are a creative storyteller."},
            {"role": "assistant", "content": "When responding, first provide a short title on its own line prefixed with 'Title:'. Then provide the short story."},
            {"role": "user", "content": f"Write a short story about {user_input} in the genre of {genre}"},
            ],
        )
        
        print(response.choices[0].message.content)


