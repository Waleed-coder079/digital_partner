from openai import OpenAI
import json
import re
from prompts import CONTENT_PROMPT_MYTH_VS_FACT as CONTENT_PROMPT
from dotenv import load_dotenv
from openai import OpenAI
import os
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    timeout=60
)
# client = OpenAI(timeout=60)

def generate_content(topic, audience, goal, tone):
    prompt = CONTENT_PROMPT.format(
        topic=topic,
        audience=audience,
        goal=goal,
        tone=tone
    )

    res = client.responses.create(
        model="gpt-4o-mini",
        input=prompt,
        temperature=0.7
    )

    text = (getattr(res, "output_text", None) or "").strip()

    if not text and hasattr(res, "output"):
        parts = []
        for item in res.output:
            content = getattr(item, "content", [])
            for c in content:
                if hasattr(c, "text"):
                    parts.append(c.text)
        text = "".join(parts).strip()

    if not text:
        raise ValueError("Empty response from model")

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{[\s\S]*\}", text)
        if match:
            return json.loads(match.group(0))
        raise
