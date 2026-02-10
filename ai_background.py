from PIL import Image, ImageDraw, ImageFilter
import io
import random

def _vertical_gradient(w, h, top=(248, 250, 252), bottom=(235, 242, 255)):
    base = Image.new("RGB", (w, h), top)
    top_r, top_g, top_b = top
    bot_r, bot_g, bot_b = bottom
    for y in range(h):
        t = y / (h - 1)
        r = int(top_r + (bot_r - top_r) * t)
        g = int(top_g + (bot_g - top_g) * t)
        b = int(top_b + (bot_b - top_b) * t)
        for x in range(w):
            base.putpixel((x, y), (r, g, b))
    return base

def generate_background():
    w = h = 1080
    img = _vertical_gradient(w, h)

    draw = ImageDraw.Draw(img, "RGBA")

    # Soft abstract blobs
    for _ in range(6):
        x0 = random.randint(-100, 800)
        y0 = random.randint(-100, 800)
        x1 = x0 + random.randint(300, 600)
        y1 = y0 + random.randint(300, 600)
        color = random.choice([
            (120, 180, 255, 35),
            (255, 200, 120, 35),
            (120, 220, 180, 35),
        ])
        draw.ellipse([x0, y0, x1, y1], fill=color)

    img = img.filter(ImageFilter.GaussianBlur(2))

    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")
    return img_bytes.getvalue()
