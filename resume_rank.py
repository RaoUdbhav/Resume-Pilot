from openai import OpenAI
import os

# Get API key from environment (Streamlit Secrets)
client = OpenAI(api_key=os.getenv("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"))

def score_resume(resume, jd):
    prompt = f"""
You are a hiring expert. Rate the following resume against the job description.
Provide a score out of 10 and 3 suggestions for improvement.

Resume:
{resume}

Job Description:
{jd}

Return the result in this format:
Score: X/10
Suggestions:
1.
2.
3.
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
