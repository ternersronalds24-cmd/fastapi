from fastapi import FastAPI, Query
import os
import requests
import socket
from groq import Groq
from dotenv import load_dotenv


app = FastAPI()

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

@app.get("/ip")
def read_ip():
    return {"your ip": IPAddr}

@app.get("/ai")
def ask_ai(prompt: str = Query(..., description="The prompt to send to the AI")):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="openai/gpt-oss-120b",
    )
    return {"response": chat_completion.choices[0].message.content}


#weather logic
url = "https://api.open-meteo.com/v1/forecast?latitude=56.946&longitude=24.1059&hourly=temperature_2m,rain&timezone=auto"
headers = {
    "Content-Type": "application/json"
}
response = requests.get(url)
data = response.json()


@app.get("/weather")
def weather_data():
    return {"Weather in riga": data}
