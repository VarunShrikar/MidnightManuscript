import os
from pathlib import Path
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parent.parent

PROMPT_FILE = PROJECT_ROOT / "config" / "prompts" / "story_prompt.md"

OUTPUT_FILE = PROJECT_ROOT / "output" / "stories" / "story_001.json"

with open(PROMPT_FILE, "r", encoding="utf-8") as file:
    prompt = file.read()

if not prompt.strip():
    raise ValueError("The prompt file is empty.")

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

response = client.models.generate_content(
    model="gemini-flash-latest",
    contents=prompt
)

story = json.loads(response.text)

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    json.dump(story, file, indent=4)

print("✅ Story generated successfully!")
print(f"📖 {story['title']}")
print(f"💾 Saved to: {OUTPUT_FILE}")