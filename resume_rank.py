import requests

def score_resume(resume, jd):
    prompt = f"""Rate the following resume against the job description.
Provide a score out of 10 and 3 suggestions.

Resume:
{resume}

Job Description:
{jd}
"""

    API_URL = "https://api-inference.huggingface.co/models/openchat/openchat-3.5-0106"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": prompt,
        "parameters": {
            "do_sample": False,
            "max_new_tokens": 300
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    output = response.json()

    return output[0]["generated_text"].replace(prompt, "").strip()
