import requests
import os

def score_resume(resume, jd):
    prompt = f"""
Rate how well this resume matches the job description.

Instructions:
- Give a score out of 10
- Explain your reasoning briefly
- Suggest 3 improvements in bullet points

Format your response like this:

Score: X/10  
Reason: ...  
Suggestions:  
1. ...  
2. ...  
3. ...

Resume:
{resume}

Job Description:
{jd}
"""

    API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

    headers = {
        "Authorization": f"Bearer {os.getenv('HF_TOKEN')}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 200
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    try:
        output = response.json()
        if isinstance(output, list) and "generated_text" in output[0]:
            return output[0]["generated_text"].replace(prompt, "").strip()
        elif "error" in output:
            return f"❌ Hugging Face Error: {output['error']}"
        else:
            return f"⚠️ Unexpected response format: {output}"
    except Exception as e:
        return f"💥 Exception occurred: {str(e)}"
