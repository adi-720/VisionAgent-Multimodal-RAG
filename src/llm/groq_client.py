import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


def get_llm_client():

    return Groq(api_key=os.getenv("GROQ_API_KEY"))
