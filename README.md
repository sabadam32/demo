# Demo - Coding Exercise

## Dependencies
- Python 3.12
- git

## Installation
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
