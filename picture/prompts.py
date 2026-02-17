CONTENT_PROMPT_CHALLENGE_SOLUTION_IMPACT = """
You are a senior LinkedIn content strategist.

Create content for a professional single-image {Social_Media_Platform} post.

Return STRICT JSON only.

Topic: {topic}
niche: {niche}
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

CONTENT_PROMPT_TIPS = """
You are a senior LinkedIn content strategist.

Create content for a professional single-image LinkedIn post featuring actionable tips.

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
   {{"title": "Tip 1", "points": [""]}},
   {{"title": "Tip 2", "points": [""]}},
   {{"title": "Tip 3", "points": [""]}},
   {{"title": "Tip 4", "points": [""]}},
   {{"title": "Tip 5", "points": [""]}}
 ],
 "cta": ""
}}
"""

CONTENT_PROMPT_MYTH_VS_FACT = """
You are a senior LinkedIn content strategist.

Create content for a professional single-image LinkedIn post using a 'Myth vs Fact' format.

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
   {{"title": "Myth 1", "points": [""]}},
   {{"title": "Fact 1", "points": [""]}},
   {{"title": "Myth 2", "points": [""]}},
   {{"title": "Fact 2", "points": [""]}},
   {{"title": "Myth 3", "points": [""]}},
   {{"title": "Fact 3", "points": [""]}}
 ],
 "cta": ""
}}
"""

CONTENT_PROMPT_STEP_BY_STEP = """
You are a senior LinkedIn content strategist.

Create content for a professional single-image LinkedIn post as a step-by-step guide.

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
   {{"title": "Step 1", "points": [""]}},
   {{"title": "Step 2", "points": [""]}},
   {{"title": "Step 3", "points": [""]}},
   {{"title": "Step 4", "points": [""]}}
 ],
 "cta": ""
}}
"""

CONTENT_PROMPT_MISTAKES_TO_AVOID = """
You are a senior LinkedIn content strategist.

Create content for a professional single-image LinkedIn post highlighting common mistakes to avoid.

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
   {{"title": "Mistake 1", "points": [""]}},
   {{"title": "Mistake 2", "points": [""]}},
   {{"title": "Mistake 3", "points": [""]}},
   {{"title": "Mistake 4", "points": [""]}},
   {{"title": "Mistake 5", "points": [""]}}
 ],
 "cta": ""
}}
"""
