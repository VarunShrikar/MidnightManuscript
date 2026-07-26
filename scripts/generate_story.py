import os
from pathlib import Path
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parent.parent

PROMPT_FILE = PROJECT_ROOT / "config" / "prompts" / "story_prompt.md"

OUTPUT_DIR = PROJECT_ROOT / "output" / "stories"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

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

existing_files = sorted(OUTPUT_DIR.glob("story_*.json"))

next_number = len(existing_files) + 1

output_file = OUTPUT_DIR / f"story_{next_number:03}.json"

with open(output_file, "w", encoding="utf-8") as file:
    json.dump(story, file, indent=4)

print("====================================")
print(" Midnight Manuscript ")
print("====================================")
print()

print("✅ Story generated successfully!")
print(f"📖 Title : {story['title']}")
print(f"💾 Saved : {output_file}")