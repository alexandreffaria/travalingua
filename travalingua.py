from elevenlabs import generate, play, voices, set_api_key, User

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
set_api_key(api_key) 
voices_list = voices()
# print(voices_list)
user = User.from_api()
print(user)

audio = generate(
  text="Fadas fofas fazem festa na floresta, fofurinhas felizes flutuam fazendo festinhas fofas!",
  voice="Tais",
  model="eleven_multilingual_v2"
)

play(audio)
print(audio)


