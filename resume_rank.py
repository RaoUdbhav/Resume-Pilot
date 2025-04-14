import openai
import os

# entered OpenAI API key here
openai.api_key = "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"  # Replaced with actual key

def score_resume(resume, jd):
    prompt = f"""
Act as an expert HR recruiter. Analyze this resume against the given job description.
Provide a matching score out of 10 and give 3 improvement tips.

Resume:
{resume}

Job Description:
{jd}

Return clearly:
Score: X/10
Suggestions:
1.
2.
3.
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']
