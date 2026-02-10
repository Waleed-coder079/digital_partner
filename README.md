# Structure Content Generator

Generate visually appealing, ready-to-post social media images with AI-powered content and modern backgrounds.

## Features

- AI-generated content for LinkedIn/social posts (headline, sections, CTA)
- Stylish, soft-gradient backgrounds with abstract shapes
- Clean, readable layout with card panels for each section
- Output: 1080×1080 PNG, perfect for LinkedIn, Instagram, etc.

## Requirements

- Python 3.8+
- [OpenAI API key](https://platform.openai.com/)
- [Pillow](https://pypi.org/project/Pillow/)
- [openai](https://pypi.org/project/openai/)
- Inter font files in `fonts/` directory (`Inter-Bold.ttf`, `Inter-Regular.ttf`)

## Setup

1. **Clone this repo**  
   ```
   git clone <your-repo-url>
   cd structure_content_generator
   ```

2. **Create and activate a virtual environment**  
   ```
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install dependencies**  
   ```
   pip install -r requirements.txt
   ```

4. **Set your OpenAI API key**  
   ```
   $env:OPENAI_API_KEY="sk-..."   # PowerShell
   ```

5. **Add Inter font files**  
   - Download from [Google Fonts](https://fonts.google.com/specimen/Inter)
   - Place `Inter-Bold.ttf` and `Inter-Regular.ttf` in a `fonts/` folder.

## Usage

Run the generator:

```
python generator.py
```

Output will be saved as `output/post.png`.

## Customization

- Edit `generator.py` to change the topic, audience, goal, or tone.
- Tweak layout/colors in `renderer.py`.
- Adjust background style in `ai_background.py`.

## Troubleshooting

- **Text not readable?**  
  Make sure you use the provided renderer, which overlays real text on the image.
- **Fonts missing?**  
  Download and place the required Inter font files in the `fonts/` directory.
- **OpenAI errors?**  
  Ensure your API key is set and you have access to the required model.

---

**Enjoy creating beautiful, AI-powered social posts!**