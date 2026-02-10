from PIL import Image, ImageDraw, ImageFont
import io

WIDTH = 1080
HEIGHT = 1080

ACCENT = (32, 102, 189)       # blue
TEXT = (15, 23, 42)           # dark slate
MUTED = (71, 85, 105)         # slate
CARD = (255, 255, 255, 230)   # semi white

def wrap(draw, text, font, max_width):
    lines = []
    words = text.split()
    line = ""
    for w in words:
        test = (line + " " + w).strip()
        wsize = draw.textlength(test, font=font)
        if wsize <= max_width:
            line = test
        else:
            if line:
                lines.append(line)
            line = w
    if line:
        lines.append(line)
    return lines

def render_post(bg_bytes, content):
    img = Image.open(io.BytesIO(bg_bytes)).convert("RGBA")
    img = img.resize((WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)

    title_font = ImageFont.truetype("fonts/Inter-Bold.ttf", 60)
    sub_font = ImageFont.truetype("fonts/Inter-Regular.ttf", 32)
    section_font = ImageFont.truetype("fonts/Inter-Bold.ttf", 34)
    body_font = ImageFont.truetype("fonts/Inter-Regular.ttf", 26)

    # Card panels for columns
    padding = 60
    col_w = 300
    gap = 30
    top = 260
    bottom = 880

    x1 = padding
    x2 = x1 + col_w + gap
    x3 = x2 + col_w + gap

    for x in [x1, x2, x3]:
        draw.rounded_rectangle(
            [x, top, x + col_w, bottom],
            radius=24,
            fill=CARD
        )

    # Headline
    y = 60
    for line in wrap(draw, content["headline"], title_font, WIDTH - 2 * padding):
        draw.text((padding, y), line, font=title_font, fill=TEXT)
        y += 70

    # Subheadline (optional)
    if content.get("subheadline"):
        for line in wrap(draw, content["subheadline"], sub_font, WIDTH - 2 * padding):
            draw.text((padding, y), line, font=sub_font, fill=MUTED)
            y += 40

    # Sections
    col_x = [x1 + 20, x2 + 20, x3 + 20]
    start_y = top + 20

    for i, sec in enumerate(content["sections"]):
        x = col_x[i]
        y = start_y

        draw.text((x, y), sec["title"], font=section_font, fill=ACCENT)
        y += 48

        for p in sec["points"]:
            lines = wrap(draw, p, body_font, col_w - 40)
            for l in lines:
                draw.text((x, y), "• " + l, font=body_font, fill=TEXT)
                y += 30
            y += 10

    # CTA
    draw.text((padding, 940), content["cta"], font=section_font, fill=TEXT)

    return img
