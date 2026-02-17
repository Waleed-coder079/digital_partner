import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


# Configuration variables
g_topic = "Leveraging advanced analytics for data-driven product decisions in early-stage SaaS."
Niche = "SaaS"
Audience = "Startup founders"
Goal = "Educational"
Social_Media_Platform = "LinkedIn"
Tone = "Professional"

# Initialize OpenAI API Client
API_KEY = os.getenv('OPENAI_API_KEY')
if not API_KEY:
    raise ValueError("OPENAI_API_KEY not found in .env file")

client = OpenAI(api_key=API_KEY)

def generate_text_post(topic, niche, Audience, Goal, platform, Tone):
    """
    Generate a complete text post with description and hashtags based on the topic and configuration
    """
    prompt = f"""You are an expert social media content writer for {niche} companies targeting {Audience}.

Topic: {topic}
Platform: {platform}
Content Objective: {Goal}
Tone: {Tone}

Generate a complete social media post in this exact format:

POST TEXT:
Write a compelling 1-2 paragraph post that expands on the topic. Make it suitable for {platform}. Include a call-to-action that encourages engagement from {Audience}. The post should be conversational, professional, and value-driven.

HASHTAGS:
Generate 5-8 relevant hashtags that match the topic and {niche}. Format them properly with # symbol.

RULES:
1. Keep the post professional but conversational and authentic
2. Focus on value and relevance for {Audience}
3. Make hashtags specific to the {niche} and topic
4. Include industry-relevant hashtags
5. Include a clear call-to-action (CTA)
6. Do not repeat the topic verbatim - expand and enhance it
7. Output ONLY the post text and hashtags - no additional commentary
8. Do not use "POST TEXT:" or "HASHTAGS:" labels in the output - just provide the content"""
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert social media content writer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=800
        )
        
        # Check if response exists
        if response is None or not response.choices:
            raise ValueError("API returned no response")
        
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        print(f"Error generating content: {str(e)}")
        raise


if __name__ == "__main__":
    print("=" * 70)
    print("COMPLETE TEXT POST GENERATOR")
    print("=" * 70)
    print(f"\nTopic: {g_topic}")
    print(f"Niche: {Niche}")
    print(f"Target Audience: {Audience}")
    print(f"Platform: {Social_Media_Platform}")
    print(f"Objective: {Goal}\n")
    print(f"Tone: {Tone}\n")
    
    print("=" * 70)
    print("GENERATING TEXT POST...")
    print("=" * 70)
    
    text_post = generate_text_post(
        topic=g_topic,
        niche=Niche,
        target_audience=Audience,
        content_objective=Goal,
        platform=Social_Media_Platform,
        tone=Tone
    )
    
    print(f"\n{text_post}")
    
    print("\n" + "=" * 70)
    print("READY TO POST!")
    print("=" * 70)
