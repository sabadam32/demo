# Demo - Coding Exercise

## Dependencies
- Python 3.12
- git

## Installation
You have a couple of options for executing these tests.
- Local Machine installtion
- GitHub CodeSpace

### Local Machine Installation
Follow the steps below to install and run the tests locally.  Easier if you have Python 3 installed already and you want to actually view the tests running in the browser.  
It is mostly the same between Windows and Mac / Linux, but there are setup scripts that will help install the virtual environment and packages needed to run everything.

1. Clone the repo using **git**. If you do not have **git** installed you can download the zip file and extract it to a location on your computer.  The CLI to clone it is:
```bash
git clone https://github.com/sabadam32/demo.git
cd demo
```
2. Run the secup script to bootstrap the environment.
```bash
./setup.sh
```
or for Windows
```cmd
setup.bat
```
3. Activate the environment and run the tests.
```bash
source .venv/bin/activate
```
or for Windows you should already be activated after running the Setup.bat file.  If you ever need to activate the environment use:
```cmd
venv/Scripts/Activate.bat
```
4. Execute the tests by running the pytest command.  

To run them without opening the browser use:
```bash
pytest -v
```
To open the browser window while the tests are running use:
```bash
pytest -v --headed
```
### GitHub CodeSpace
Follow these steps to run it on GitHub codespace.  Nothing needed on your local machine for you to run it, but cannot view tests running in the browser.

1. From the `Code` button in the repository select the `Codespaces` tab.
2. Click the `Create codespace on main` button and wait for it to setup.
3. In the terminal window run `pip install -r requirements.txt`
4. Setup playwright broser by running `python -m playwright install --with-deps chromium`
5. Run the tests `pytest -vv`
