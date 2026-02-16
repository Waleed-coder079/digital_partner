# Structure Content Generator

Generate visually appealing, ready-to-post social media images with AI-powered content and **10 unique design layouts**.

---

## Features

- **AI-generated content** for LinkedIn/social posts (headline, sections, CTA)
- **10 modern, professional layouts** (columns, rows, arrows, chevrons, circles, flows, etc.)
- **Stylish backgrounds** with gradients and abstract shapes
- **High-resolution output**: 1080×1080 PNG, perfect for LinkedIn, Instagram, etc.
- **Batch generation**: Each post is rendered in all 10 layouts for you to pick the best

---

## Requirements

- Python 3.8+
- [OpenAI API key](https://platform.openai.com/)
- [Pillow](https://pypi.org/project/Pillow/)
- [openai](https://pypi.org/project/openai/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- Inter font files in `fonts/` directory (`Inter-Bold.ttf`, `Inter-Regular.ttf`)

---

## Setup

1. **Clone this repo**  
   ```sh
   git clone <your-repo-url>
   cd structure_content_generator
   ```

2. **Create and activate a virtual environment**  
   ```sh
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install dependencies**  
   ```sh
   pip install -r requirements.txt
   ```

4. **Set your OpenAI API key**  
   - Create a `.env` file in the project root:
     ```
     OPENAI_API_KEY=sk-...
     ```

5. **Add Inter font files**  
   - Download from [Google Fonts](https://fonts.google.com/specimen/Inter)
   - Place `Inter-Bold.ttf` and `Inter-Regular.ttf` in a `fonts/` folder.

---

## Usage

Run the generator:

```sh
python generator.py
```

- Output will be saved as `output/post_<LayoutName>.png` (10 images per run, one for each layout).

---

## Customization

- Edit `generator.py` to change the topic, audience, goal, or tone.
- Tweak layout/colors in `renderer.py`.
- Adjust background style in `ai_background.py`.
- Add or modify prompt templates in `prompts.py`.

---

## Layouts Included

- Challenge/Solution/Impact (columns)
- Tips (horizontal cards)
- Myth vs Fact (grid)
- Step-by-Step (vertical steps)
- Mistakes to Avoid (vertical list)
- Arrow Flow (horizontal arrow boxes)
- Chevron Vertical (vertical chevrons)
- Connected Circles (horizontal process)
- Vertical Arrow Flow (vertical process)
- Chevron Horizontal (horizontal chevrons)

---

## Troubleshooting

- **Text not readable?**  
  Make sure you use the provided renderer, which overlays real text on the image.
- **Fonts missing?**  
  Download and place the required Inter font files in the `fonts/` directory.
- **OpenAI errors?**  
  Ensure your API key is set in `.env` and you have access to the required model.

---

**Enjoy creating beautiful, AI-powered social posts in multiple styles!**