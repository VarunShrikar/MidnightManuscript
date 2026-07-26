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

For every scene, generate a detailed cinematic image_prompt suitable for Stable Diffusion XL or Flux. The prompt must completely describe the character's appearance, clothing, environment, lighting, atmosphere, camera angle, and visual style. Every image_prompt must preserve the same character appearance throughout all 10 scenes.

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
      "description": "",
      "image_prompt": ""
    }
  ]
}

Do not include explanations.

Do not use Markdown.

Return only JSON.