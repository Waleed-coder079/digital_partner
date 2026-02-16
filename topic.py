import os
import sqlite3
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Configuration
Niche = "SaaS"
Target_Audience_Role = "Startup founders"
Content_Objective = "Educational"
Social_Media_Platform = "LinkedIn"

# Database configuration
DB_NAME = "topics.db"

# Initialize OpenAI Client
API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=API_KEY)


def init_database():
    """Initialize SQLite database for storing topics"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS topics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()


def get_previous_topics():
    """Retrieve all previously generated topics from database"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('SELECT topic FROM topics ORDER BY created_at DESC')
    topics = [row[0] for row in cursor.fetchall()]
    
    conn.close()
    return topics


def add_topic_to_database(topic):
    """Add a new topic to the database"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    try:
        cursor.execute('INSERT INTO topics (topic) VALUES (?)', (topic,))
        conn.commit()
        print(f"✓ Topic saved to database")
    except sqlite3.IntegrityError:
        print(f"⚠ Topic already exists in database")
    finally:
        conn.close()


def generate_trending_topic():
    # Get previous topics from database
    previous_topics = get_previous_topics()
    
    prompt = f"""You are an expert social media strategist for {Niche} companies targeting {Target_Audience_Role}. 
Generate a trending social media topic for today that aligns with the content objective: {Content_Objective}

IMPORTANT RULES:
1. Generate ONLY ONE single topic - do not provide multiple options
2. The topic must be unique and not appear in this list of previously used topics: {previous_topics}
3. Output exactly one short sentence suitable as a {Social_Media_Platform} post topic
4. Do not include hashtags, captions, emojis, numbering, or bullet points - only the topic itself
5. Return only the topic text with no additional explanation or commentary"""

    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {"role": "system", "content": "You are an expert social media strategist."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=150
    )
    
    # Extract only the first line/topic in case multiple are returned
    result = response.choices[0].message.content.strip()
    # Get the first line or first sentence
    first_line = result.split('\n')[0].strip()
    generated_topic = first_line if first_line else result
    
    # Save the generated topic to database
    add_topic_to_database(generated_topic)
    
    return generated_topic

if __name__ == "__main__":
    # Initialize database on first run
    init_database()
    
    print("=" * 70)
    print("TOPIC GENERATOR WITH DATABASE")
    print("=" * 70)
    
    # Display previously generated topics
    previous_topics = get_previous_topics()
    print(f"\n📚 Previously Generated Topics ({len(previous_topics)} total):")
    if previous_topics:
        for i, topic in enumerate(previous_topics[:5], 1):  # Show last 5
            print(f"   {i}. {topic}")
        if len(previous_topics) > 5:
            print(f"   ... and {len(previous_topics) - 5} more")
    else:
        print("   (None yet)")
    
    print("\n" + "=" * 70)
    print("GENERATING NEW TOPIC...")
    print("=" * 70 + "\n")
    
    topic = generate_trending_topic()
    print(f"\n🎯 Grounded Trending Topic:\n{topic}")
