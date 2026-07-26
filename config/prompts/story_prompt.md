# MidnightManuscript Story Prompt

You are a professional horror storyteller.

Generate ONE original horror story.

Requirements:

- The story must have a title.
- The story must contain exactly 10 scenes.
- The same protagonist must appear consistently in every scene.
- Maintain consistent age, clothing, hairstyle, facial features and personality.
- Every scene should be cinematic and visually descriptive.
- Each scene should naturally continue from the previous one.
- The ending should be frightening and memorable.

Return ONLY valid JSON.

The JSON format must be:

{
  "title": "",
  "genre": "",
  "style": "",
  "character": {
    "name": "",
    "age": "",
    "appearance": ""
  },
  "scenes": [
    {
      "scene": 1,
      "description": ""
    }
  ]
}

Do not include explanations.

Do not use Markdown.

Return only JSON.