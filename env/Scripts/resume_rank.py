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
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']
