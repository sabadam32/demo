# Description: Setup the environment for the project
python -m venv .venv
source .venv/bin/activate

# Install the dependencies
pip install -r requirements.txt --no-cache-dir
playwright install chromium
