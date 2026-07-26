import json
from pathlib import Path

import requests

# Load latest story
stories_folder = Path("output/stories")
story_files = sorted(stories_folder.glob("*.json"))
latest_story = story_files[-1]

with open(latest_story, "r", encoding="utf-8") as f:
    story = json.load(f)

# Load ComfyUI workflow
workflow_file = Path("workflows/MidnightManuscript_API.json")

with open(workflow_file, "r", encoding="utf-8") as f:
    workflow = json.load(f)

print("Workflow loaded successfully.")

# Submit every scene
for scene in story["scenes"]:
    prompt = scene["image_prompt"]

    workflow["2"]["inputs"]["text"] = prompt

    response = requests.post(
        "http://127.0.0.1:8188/prompt",
        json={"prompt": workflow}
    )

    response.raise_for_status()

    prompt_id = response.json()["prompt_id"]

    print(f"Submitted Scene {scene['scene']} (Prompt ID: {prompt_id})")