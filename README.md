# 🌙 MidnightManuscript

> AI-powered horror story generation pipeline that creates cinematic stories, generates consistent AI artwork, and assembles them into videos.

---

## Overview

MidnightManuscript is an end-to-end AI content generation project.

The goal is to automate the creation of horror videos by combining multiple AI tools into one pipeline.

The pipeline currently works like this:

Story Prompt --> Gemini --> Structured JSON Story --> ComfyUI + FLUX --> Scene Images --> Video Creation --> YouTube / Instagram

---

## Features

- AI horror story generation using Google Gemini
- Structured JSON output
- Character consistency across scenes
- Cinematic image prompts
- Local FLUX image generation with ComfyUI
- Automatic story storage
- Modular Python architecture

---

## Tech Stack

- Python
- Google Gemini API
- ComfyUI
- FLUX
- Git
- GitHub

---

## Current Project Structure

```
MidnightManuscript/
│
├── assets/
│   ├── images/
│   └── videos/
│
├── config/
│   └── prompts/
│       └── story_prompt.md
│
├── docs/
├── examples/
├── output/
│   └── stories/
│
├── prompts/
├── python/
├── scripts/
│   ├── generate_story.py
│   └── test_gemini.py
│
├── workflows/
│   ├── MidnightManuscript_v1.json
│   └── MidnightManuscript_API.json
│
├── README.md
└── .gitignore
```

---

## Current Progress

- ✅ Repository created
- ✅ GitHub connected
- ✅ Gemini API integrated
- ✅ Story generation working
- ✅ JSON output working
- ✅ Automatic story saving
- ✅ ComfyUI workflow created

---

## Roadmap

### Phase 1
- [x] Generate horror stories
- [x] Save structured JSON
- [x] Generate cinematic image prompts

### Phase 2
- [ ] Connect Python to ComfyUI
- [ ] Generate Scene 1 automatically
- [ ] Generate all 10 scenes

### Phase 3
- [ ] Assemble video
- [ ] Add subtitles
- [ ] Add narration
- [ ] Add background music

### Phase 4
- [ ] Upload automatically
- [ ] Schedule videos
- [ ] Support multiple genres

---

## License

MIT License
