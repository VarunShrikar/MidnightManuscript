import requests
import json
from pathlib import Path

# Load latest story
stories_folder = Path("output/stories")
story_files = sorted(stories_folder.glob("*.json"))
latest_story = story_files[-1]

with open(latest_story, "r", encoding="utf-8") as f:
    story = json.load(f)

scene = story["scenes"][0]
prompt = scene["image_prompt"]

# Load ComfyUI workflow
workflow_file = Path("workflows/MidnightManuscript_API.json")

with open(workflow_file, "r", encoding="utf-8") as f:
    workflow = json.load(f)

print("Workflow loaded successfully.")

workflow["2"]["inputs"]["text"] = prompt
print(workflow["2"]["inputs"]["text"])

response = requests.post(
    "http://127.0.0.1:8188/prompt",
    json={"prompt": workflow}
)

print(response.status_code)
print(response.text)