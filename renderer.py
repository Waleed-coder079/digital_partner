from PIL import Image, ImageDraw, ImageFont
import io
import math

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

def render_challenge_solution_impact(bg_bytes, content):
    img = Image.open(io.BytesIO(bg_bytes)).convert("RGBA")
    img = img.resize((WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)

    title_font = ImageFont.truetype("fonts/Inter-Bold.ttf", 60)
    sub_font = ImageFont.truetype("fonts/Inter-Regular.ttf", 32)
    section_font = ImageFont.truetype("fonts/Inter-Bold.ttf", 34)
    body_font = ImageFont.truetype("fonts/Inter-Regular.ttf", 26)

    col_w = 300
    gap = 30
    padding = 60
    top = 260
    bottom = 880
    num_sections = len(content["sections"])
    total_width = num_sections * col_w + (num_sections - 1) * gap
    start_x = (WIDTH - total_width) // 2
    col_x = [start_x + i * (col_w + gap) + 20 for i in range(num_sections)]

    for i in range(num_sections):
        x = start_x + i * (col_w + gap)
        draw.rounded_rectangle(
            [x, top, x + col_w, bottom],
            radius=24,
            fill=CARD
        )

    y = 60
    for line in wrap(draw, content["headline"], title_font, WIDTH - 2 * padding):
        draw.text((padding, y), line, font=title_font, fill=TEXT)
        y += 70

    if content.get("subheadline"):
        for line in wrap(draw, content["subheadline"], sub_font, WIDTH - 2 * padding):
            draw.text((padding, y), line, font=sub_font, fill=MUTED)
            y += 40

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

    draw.text((padding, 940), content["cta"], font=section_font, fill=TEXT)
    return img

def render_tips(bg_bytes, content):
    img = Image.open(io.BytesIO(bg_bytes)).convert("RGBA")
    img = img.resize((WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)

    title_font = ImageFont.truetype("fonts/Inter-Bold.ttf", 60)
    sub_font = ImageFont.truetype("fonts/Inter-Regular.ttf", 32)
    section_font = ImageFont.truetype("fonts/Inter-Bold.ttf", 30)
    body_font = ImageFont.truetype("fonts/Inter-Regular.ttf", 24)

    padding = 60
    card_h = 180
    card_w = 320
    gap = 30
    num_sections = len(content["sections"])
    total_width = num_sections * card_w + (num_sections - 1) * gap
    start_x = (WIDTH - total_width) // 2
    y = 60

    for line in wrap(draw, content["headline"], title_font, WIDTH - 2 * padding):
        draw.text((padding, y), line, font=title_font, fill=TEXT)
        y += 70

    if content.get("subheadline"):
        for line in wrap(draw, content["subheadline"], sub_font, WIDTH - 2 * padding):
            draw.text((padding, y), line, font=sub_font, fill=MUTED)
            y += 40

    card_y = 260
    for i, sec in enumerate(content["sections"]):
        x = start_x + i * (card_w + gap)
        draw.rounded_rectangle(
            [x, card_y, x + card_w, card_y + card_h],
            radius=20,
            fill=CARD
        )
        draw.text((x + 20, card_y + 20), sec["title"], font=section_font, fill=ACCENT)
        y2 = card_y + 60
        for p in sec["points"]:
            lines = wrap(draw, p, body_font, card_w - 40)
            for l in lines:
                draw.text((x + 20, y2), "• " + l, font=body_font, fill=TEXT)
                y2 += 28

    draw.text((padding, 940), content["cta"], font=section_font, fill=TEXT)
    return img

def render_myth_vs_fact(bg_bytes, content):
    img = Image.open(io.BytesIO(bg_bytes)).convert("RGBA")
    img = img.resize((WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)

    title_font = ImageFont.truetype("fonts/Inter-Bold.ttf", 60)
    sub_font = ImageFont.truetype("fonts/Inter-Regular.ttf", 32)
    section_font = ImageFont.truetype("fonts/Inter-Bold.ttf", 28)
    body_font = ImageFont.truetype("fonts/Inter-Regular.ttf", 22)

    padding = 60
    grid_w = 420
    grid_h = 180
    gap_x = 30
    gap_y = 30
    cols = 2
    rows = (len(content["sections"]) + 1) // 2
    start_x = (WIDTH - (cols * grid_w + (cols - 1) * gap_x)) // 2
    start_y = 260

    y = 60
    for line in wrap(draw, content["headline"], title_font, WIDTH - 2 * padding):
        draw.text((padding, y), line, font=title_font, fill=TEXT)
        y += 70

    if content.get("subheadline"):
        for line in wrap(draw, content["subheadline"], sub_font, WIDTH - 2 * padding):
            draw.text((padding, y), line, font=sub_font, fill=MUTED)
            y += 40

    for i, sec in enumerate(content["sections"]):
        col = i % 2
        row = i // 2
        x = start_x + col * (grid_w + gap_x)
        y2 = start_y + row * (grid_h + gap_y)
        draw.rounded_rectangle(
            [x, y2, x + grid_w, y2 + grid_h],
            radius=18,
            fill=CARD
        )
        draw.text((x + 20, y2 + 20), sec["title"], font=section_font, fill=ACCENT)
        y3 = y2 + 60
        for p in sec["points"]:
            lines = wrap(draw, p, body_font, grid_w - 40)
            for l in lines:
                draw.text((x + 20, y3), "• " + l, font=body_font, fill=TEXT)
                y3 += 24

    draw.text((padding, 940), content["cta"], font=section_font, fill=TEXT)
    return img

def render_step_by_step(bg_bytes, content):
    img = Image.open(io.BytesIO(bg_bytes)).convert("RGBA")
    img = img.resize((WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)

    title_font = ImageFont.truetype("fonts/Inter-Bold.ttf", 60)
    sub_font = ImageFont.truetype("fonts/Inter-Regular.ttf", 32)
    section_font = ImageFont.truetype("fonts/Inter-Bold.ttf", 28)
    body_font = ImageFont.truetype("fonts/Inter-Regular.ttf", 22)

    padding = 60
    step_w = 900
    step_h = 120
    gap_y = 30
    start_x = (WIDTH - step_w) // 2
    start_y = 260

    y = 60
    for line in wrap(draw, content["headline"], title_font, WIDTH - 2 * padding):
        draw.text((padding, y), line, font=title_font, fill=TEXT)
        y += 70

    if content.get("subheadline"):
        for line in wrap(draw, content["subheadline"], sub_font, WIDTH - 2 * padding):
            draw.text((padding, y), line, font=sub_font, fill=MUTED)
            y += 40

    for i, sec in enumerate(content["sections"]):
        y2 = start_y + i * (step_h + gap_y)
        draw.rounded_rectangle(
            [start_x, y2, start_x + step_w, y2 + step_h],
            radius=16,
            fill=CARD
        )
        draw.text((start_x + 20, y2 + 20), sec["title"], font=section_font, fill=ACCENT)
        y3 = y2 + 60
        for p in sec["points"]:
            lines = wrap(draw, p, body_font, step_w - 40)
            for l in lines:
                draw.text((start_x + 20, y3), "• " + l, font=body_font, fill=TEXT)
                y3 += 24

    draw.text((padding, 940), content["cta"], font=section_font, fill=TEXT)
    return img

def render_mistakes_to_avoid(bg_bytes, content):
    img = Image.open(io.BytesIO(bg_bytes)).convert("RGBA")
    img = img.resize((WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)

    title_font = ImageFont.truetype("fonts/Inter-Bold.ttf", 60)
    sub_font = ImageFont.truetype("fonts/Inter-Regular.ttf", 32)
    section_font = ImageFont.truetype("fonts/Inter-Bold.ttf", 28)
    body_font = ImageFont.truetype("fonts/Inter-Regular.ttf", 22)

    padding = 60
    card_w = 900
    card_h = 100
    gap_y = 20
    start_x = (WIDTH - card_w) // 2
    start_y = 260

    y = 60
    for line in wrap(draw, content["headline"], title_font, WIDTH - 2 * padding):
        draw.text((padding, y), line, font=title_font, fill=TEXT)
        y += 70

    if content.get("subheadline"):
        for line in wrap(draw, content["subheadline"], sub_font, WIDTH - 2 * padding):
            draw.text((padding, y), line, font=sub_font, fill=MUTED)
            y += 40

    for i, sec in enumerate(content["sections"]):
        y2 = start_y + i * (card_h + gap_y)
        draw.rounded_rectangle(
            [start_x, y2, start_x + card_w, y2 + card_h],
            radius=14,
            fill=CARD
        )
        draw.text((start_x + 20, y2 + 20), sec["title"], font=section_font, fill=ACCENT)
        y3 = y2 + 50
        for p in sec["points"]:
            lines = wrap(draw, p, body_font, card_w - 40)
            for l in lines:
                draw.text((start_x + 20, y3), "• " + l, font=body_font, fill=TEXT)
                y3 += 22

    draw.text((padding, 940), content["cta"], font=section_font, fill=TEXT)
    return img

def render_arrow_flow(bg_bytes, content):
    """Horizontal arrow flow with boxes (like your 3rd image)."""
    img = Image.open(io.BytesIO(bg_bytes)).convert("RGBA")
    img = img.resize((WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)
    title_font = ImageFont.truetype("fonts/Inter-Bold.ttf", 60)
    section_font = ImageFont.truetype("fonts/Inter-Bold.ttf", 34)
    body_font = ImageFont.truetype("fonts/Inter-Regular.ttf", 26)
    padding = 60

    # Draw headline
    y = 60
    for line in wrap(draw, content["headline"], title_font, WIDTH - 2 * padding):
        draw.text((padding, y), line, font=title_font, fill=TEXT)
        y += 70

    # Arrow body
    arrow_y = 350
    arrow_h = 180
    arrow_w = 260
    gap = 40
    num = len(content["sections"])
    total_w = num * arrow_w + (num - 1) * gap
    start_x = (WIDTH - total_w) // 2

    for i, sec in enumerate(content["sections"]):
        x = start_x + i * (arrow_w + gap)
        # Draw box
        draw.rounded_rectangle([x, arrow_y, x + arrow_w, arrow_y + arrow_h], radius=30, fill=ACCENT)
        # Draw arrow (except last)
        if i < num - 1:
            arrow_tip = x + arrow_w + gap // 2
            arrow_mid = arrow_y + arrow_h // 2
            draw.polygon([
                (x + arrow_w, arrow_mid - 20),
                (arrow_tip, arrow_mid),
                (x + arrow_w, arrow_mid + 20)
            ], fill=ACCENT)
        # Section title and points
        draw.text((x + 24, arrow_y + 24), sec["title"], font=section_font, fill=(255,255,255))
        y2 = arrow_y + 70
        for p in sec["points"]:
            lines = wrap(draw, p, body_font, arrow_w - 48)
            for l in lines:
                draw.text((x + 24, y2), "• " + l, font=body_font, fill=(255,255,255))
                y2 += 28

    draw.text((padding, 940), content["cta"], font=section_font, fill=TEXT)
    return img

def render_chevron_vertical(bg_bytes, content):
    """Vertical chevron boxes (like your last image)."""
    img = Image.open(io.BytesIO(bg_bytes)).convert("RGBA")
    img = img.resize((WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)
    title_font = ImageFont.truetype("fonts/Inter-Bold.ttf", 60)
    section_font = ImageFont.truetype("fonts/Inter-Bold.ttf", 34)
    body_font = ImageFont.truetype("fonts/Inter-Regular.ttf", 26)
    padding = 60

    y = 60
    for line in wrap(draw, content["headline"], title_font, WIDTH - 2 * padding):
        draw.text((padding, y), line, font=title_font, fill=TEXT)
        y += 70

    chevron_w = 220
    chevron_h = 110
    gap = 30
    start_x = padding
    start_y = 260

    for i, sec in enumerate(content["sections"]):
        y2 = start_y + i * (chevron_h + gap)
        # Draw chevron (triangle + rectangle)
        points = [
            (start_x, y2 + chevron_h // 2),
            (start_x + 40, y2),
            (start_x + chevron_w, y2),
            (start_x + chevron_w, y2 + chevron_h),
            (start_x + 40, y2 + chevron_h)
        ]
        draw.polygon(points, fill=ACCENT)
        # Section title and points
        draw.text((start_x + 60, y2 + 18), sec["title"], font=section_font, fill=(255,255,255))
        y3 = y2 + 54
        for p in sec["points"]:
            lines = wrap(draw, p, body_font, chevron_w - 70)
            for l in lines:
                draw.text((start_x + 60, y3), "• " + l, font=body_font, fill=(255,255,255))
                y3 += 24

    draw.text((padding, 940), content["cta"], font=section_font, fill=TEXT)
    return img

def render_connected_circles(bg_bytes, content):
    """Horizontal connected circles (like your 1st and 2nd images)."""
    img = Image.open(io.BytesIO(bg_bytes)).convert("RGBA")
    img = img.resize((WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)
    title_font = ImageFont.truetype("fonts/Inter-Bold.ttf", 60)
    section_font = ImageFont.truetype("fonts/Inter-Bold.ttf", 34)
    body_font = ImageFont.truetype("fonts/Inter-Regular.ttf", 26)
    padding = 60

    y = 60
    for line in wrap(draw, content["headline"], title_font, WIDTH - 2 * padding):
        draw.text((padding, y), line, font=title_font, fill=TEXT)
        y += 70

    num = len(content["sections"])
    circle_r = 110
    gap = 80
    total_w = num * (2 * circle_r) + (num - 1) * gap
    start_x = (WIDTH - total_w) // 2
    cy = 420

    # Draw connecting lines
    for i in range(num - 1):
        x1 = start_x + i * (2 * circle_r + gap) + circle_r * 2
        x2 = x1 + gap
        draw.line([(x1, cy), (x2, cy)], fill=ACCENT, width=12)

    # Draw circles and content
    for i, sec in enumerate(content["sections"]):
        cx = start_x + i * (2 * circle_r + gap) + circle_r
        draw.ellipse([cx - circle_r, cy - circle_r, cx + circle_r, cy + circle_r], fill=ACCENT)
        draw.text((cx - 30, cy - 30), sec["title"], font=section_font, fill=(255,255,255))
        y2 = cy + 50
        for p in sec["points"]:
            lines = wrap(draw, p, body_font, 2 * circle_r - 40)
            for l in lines:
                draw.text((cx - circle_r + 20, y2), "• " + l, font=body_font, fill=(255,255,255))
                y2 += 24

    draw.text((padding, 940), content["cta"], font=section_font, fill=TEXT)
    return img

def render_vertical_arrow_flow(bg_bytes, content):
    """Vertical arrow flow with boxes (like a process flow)."""
    img = Image.open(io.BytesIO(bg_bytes)).convert("RGBA")
    img = img.resize((WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)
    title_font = ImageFont.truetype("fonts/Inter-Bold.ttf", 60)
    section_font = ImageFont.truetype("fonts/Inter-Bold.ttf", 34)
    body_font = ImageFont.truetype("fonts/Inter-Regular.ttf", 26)
    padding = 60

    y = 60
    for line in wrap(draw, content["headline"], title_font, WIDTH - 2 * padding):
        draw.text((padding, y), line, font=title_font, fill=TEXT)
        y += 70

    box_w = 600
    box_h = 120
    gap = 60
    start_x = (WIDTH - box_w) // 2
    start_y = 260

    for i, sec in enumerate(content["sections"]):
        y2 = start_y + i * (box_h + gap)
        draw.rounded_rectangle([start_x, y2, start_x + box_w, y2 + box_h], radius=30, fill=ACCENT)
        # Draw arrow (except last)
        if i < len(content["sections"]) - 1:
            arrow_tip = y2 + box_h + gap // 2
            arrow_mid = start_x + box_w // 2
            draw.polygon([
                (arrow_mid - 20, y2 + box_h),
                (arrow_mid, arrow_tip),
                (arrow_mid + 20, y2 + box_h)
            ], fill=ACCENT)
        draw.text((start_x + 24, y2 + 24), sec["title"], font=section_font, fill=(255,255,255))
        y3 = y2 + 60
        for p in sec["points"]:
            lines = wrap(draw, p, body_font, box_w - 48)
            for l in lines:
                draw.text((start_x + 24, y3), "• " + l, font=body_font, fill=(255,255,255))
                y3 += 28

    draw.text((padding, 940), content["cta"], font=section_font, fill=TEXT)
    return img

def render_chevron_horizontal(bg_bytes, content):
    """Horizontal chevron boxes (like a process flow)."""
    img = Image.open(io.BytesIO(bg_bytes)).convert("RGBA")
    img = img.resize((WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)
    title_font = ImageFont.truetype("fonts/Inter-Bold.ttf", 60)
    section_font = ImageFont.truetype("fonts/Inter-Bold.ttf", 34)
    body_font = ImageFont.truetype("fonts/Inter-Regular.ttf", 26)
    padding = 60

    y = 60
    for line in wrap(draw, content["headline"], title_font, WIDTH - 2 * padding):
        draw.text((padding, y), line, font=title_font, fill=TEXT)
        y += 70

    chevron_w = 220
    chevron_h = 110
    gap = 30
    num = len(content["sections"])
    total_w = num * chevron_w + (num - 1) * gap
    start_x = (WIDTH - total_w) // 2
    y2 = 350

    for i, sec in enumerate(content["sections"]):
        x = start_x + i * (chevron_w + gap)
        # Draw chevron (rectangle + triangle)
        points = [
            (x, y2),
            (x + chevron_w - 40, y2),
            (x + chevron_w, y2 + chevron_h // 2),
            (x + chevron_w - 40, y2 + chevron_h),
            (x, y2 + chevron_h)
        ]
        draw.polygon(points, fill=ACCENT)
        draw.text((x + 24, y2 + 24), sec["title"], font=section_font, fill=(255,255,255))
        y3 = y2 + 54
        for p in sec["points"]:
            lines = wrap(draw, p, body_font, chevron_w - 70)
            for l in lines:
                draw.text((x + 24, y3), "• " + l, font=body_font, fill=(255,255,255))
                y3 += 24

    draw.text((padding, 940), content["cta"], font=section_font, fill=TEXT)
    return img

# Add these to your render_post dispatcher:
def render_post(bg_bytes, content, structure="ChallengeSolutionImpact"):
    if structure == "ChallengeSolutionImpact":
        return render_challenge_solution_impact(bg_bytes, content)
    elif structure == "Tips":
        return render_tips(bg_bytes, content)
    elif structure == "MythVsFact":
        return render_myth_vs_fact(bg_bytes, content)
    elif structure == "StepByStep":
        return render_step_by_step(bg_bytes, content)
    elif structure == "MistakesToAvoid":
        return render_mistakes_to_avoid(bg_bytes, content)
    elif structure == "ArrowFlow":
        return render_arrow_flow(bg_bytes, content)
    elif structure == "ChevronVertical":
        return render_chevron_vertical(bg_bytes, content)
    elif structure == "ConnectedCircles":
        return render_connected_circles(bg_bytes, content)
    elif structure == "VerticalArrowFlow":
        return render_vertical_arrow_flow(bg_bytes, content)
    elif structure == "ChevronHorizontal":
        return render_chevron_horizontal(bg_bytes, content)
    else:
        return render_challenge_solution_impact(bg_bytes, content)
