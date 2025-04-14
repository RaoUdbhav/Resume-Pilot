@echo off

cd /d "%~dp0"

echo :) Activating virtual environment...

call env\scripts\activate.bat

echo ^|^ Running resume pilot (streamlit app...)
streamlit run app.py

pause