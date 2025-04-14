import streamlit as st
from resume_rank import score_resume

st.set_page_config(page_title="Resume Pilot AI", layout="centered")
st.title("📄 Resume Pilot AI")
st.subheader("🚀 Get your resume scored instantly using GPT-4")

resume = st.text_area("✍️ Paste Your Resume Here", height=300)
jd = st.text_area("📌 Paste the Job Description Here", height=300)

if st.button("💡 Score My Resume"):
    if resume and jd:
        with st.spinner("Scoring in progress..."):
            result = score_resume(resume, jd)
        st.success("Here’s your result:")
        st.write(result)
    else:
        st.warning("Please fill in both the resume and job description.")
