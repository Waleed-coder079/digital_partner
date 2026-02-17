from ai_content import generate_content
from ai_background import generate_background
from renderer import render_post
import os

from topic import Social_Media_Platform


def generate_post():
    topic = "How AI automation transforms eCommerce support"
    niche = "eCommerce"
    audience = "eCommerce founders"
    goal = "Promotional"
    tone = "Professional"
    Social_Media_Platform = "LinkedIn"

    print("Generating content...")
    content = generate_content(topic, audience, goal, tone, Social_Media_Platform, niche)

    print("Generating background...")
    bg = generate_background()

    print("Rendering all designs...")
    structures = [
        "ChallengeSolutionImpact",
        "Tips",
        "MythVsFact",
        "StepByStep",
        "MistakesToAvoid",
        "ArrowFlow",
        "ChevronVertical",
        "ConnectedCircles",
        "VerticalArrowFlow",
        "ChevronHorizontal"
    ]
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    for structure in structures:
        img = render_post(bg, content, structure=structure)
        path = f"{output_dir}/post_{structure}.png"
        img.save(path)
        print("Saved:", path)

if __name__ == "__main__":
    generate_post()
