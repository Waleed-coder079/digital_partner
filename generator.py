from ai_content import generate_content
from ai_background import generate_background
from renderer import render_post

def generate_post():
    topic = "How AI automation transforms eCommerce support"
    audience = "eCommerce founders"
    goal = "Promotional"
    tone = "Professional"

    print("Generating content...")
    content = generate_content(topic, audience, goal, tone)

    print("Generating background...")
    bg = generate_background()

    print("Rendering final image...")
    img = render_post(bg, content)

    path = "output/post.png"
    img.save(path)

    print("Saved:", path)

if __name__ == "__main__":
    generate_post()
