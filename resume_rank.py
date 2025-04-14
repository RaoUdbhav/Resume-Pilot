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

    try:
        output = response.json()
        # Show raw response in Streamlit for debugging (optional)
        # st.write("Raw response:", output)

        if isinstance(output, list) and "generated_text" in output[0]:
            return output[0]["generated_text"].replace(prompt, "").strip()
        elif "error" in output:
            return f"❌ Hugging Face Error: {output['error']}"
        else:
            return f"⚠️ Unexpected response format: {output}"
    except Exception as e:
        return f"💥 Exception occurred: {str(e)}"
