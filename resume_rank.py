import requests

def score_resume(resume, jd):
    prompt = f"""Rate the following resume against the job description.
Provide a score out of 10 and 3 suggestions.

Resume:
{resume}

Job Description:
{jd}
"""

    API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"


    import os

    headers = {
    "Authorization": f"Bearer {os.getenv('HF_TOKEN')}",
    "Accept": "application/json",
    "Content-Type": "application/json"
                }


    payload = {
    "inputs": f"""Rate this resume against the job description.
    Give a score out of 10 and 3 suggestions for improvement.

    Resume:
    {resume}

    Job Description:
    {jd}""",
    "parameters": {
        "max_new_tokens": 300
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
