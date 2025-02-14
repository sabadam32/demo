py -m venv venv
call venv/Scripts/activate.bat

pip install -r requirements.txt --no-cache-dir
playwright install chromium

pytest -v --headed