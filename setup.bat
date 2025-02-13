# Description: Setup the environment for the project
python -m venv venv
venv/Scripts/activate.bat

# Install the dependencies
pip install -r requirements.txt --no-cache-dir
playwright install chromium
