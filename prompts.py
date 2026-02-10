CONTENT_PROMPT = """
You are a senior LinkedIn content strategist.

Create content for a professional single-image LinkedIn post.

Return STRICT JSON only.

Topic: {topic}
Audience: {audience}
Goal: {goal}
Tone: {tone}

JSON format:
{{
 "headline": "",
 "subheadline": "",
 "sections": [
   {{"title": "Challenge", "points": ["", "", ""]}},
   {{"title": "Solution", "points": ["", "", ""]}},
   {{"title": "Impact", "points": ["", "", ""]}}
 ],
 "cta": ""
}}
"""
