# ${\textsf{\color{darkorange}Demo - Coding Exercise}}$
This is the demo for the swaglabs test site.  The exercise focuses on the checkout flow, but the framework is build to easily add additional tests for other scenarios.

## ${\textsf{\color{orangered}Dependencies}}$
- Python 3.12
- git

## ${\textsf{\color{orangered}Installation}}$
You have a couple of options for executing these tests.
- Local Machine installtion
- GitHub CodeSpace

### ${\textsf{\color{orangered}Local Machine Installation}}$
Follow the steps below to install and run the tests locally.  Easier if you have Python 3 installed already and you want to actually view the tests running in the browser.  
It is mostly the same between Windows and Mac / Linux, but there are setup scripts that will help install the virtual environment and packages needed to run everything.

1. Clone the repo using **git**. If you do not have **git** installed you can download the zip file and extract it to a location on your computer.  The CLI to clone it is:
```bash
git clone https://github.com/sabadam32/demo.git
cd demo
```
2. Run the script to bootstrap the environment and execute the tests.
```bash
./run.sh
```
or for Windows
```cmd
run.bat
```

To run tests manually without opening the browser run:
```bash
pytest -v
```
To open the browser window while the tests are running use:
```bash
pytest -v --headed
```
### ${\textsf{\color{orangered}GitHub CodeSpace}}$
Follow these steps to run it on GitHub codespace.  Nothing needed on your local machine for you to run it, but cannot view tests running in the browser.

1. From the `Code` button in the repository select the `Codespaces` tab.
2. Click the `Create codespace on main` button and wait for it to setup.
3. In the terminal window run `pip install -r requirements.txt`
4. Setup playwright broser by running `python -m playwright install --with-deps chromium`
5. Run the tests `pytest -v`

## ${\textsf{\color{orangered}Structure}}$
I used the Page object model along with a fluent design flow.  All element locators and actions for a page are kept together.  The fluent design allows the test to be more readable and self documenting.
### ${\textsf{\color{orangered}Pages}}$
Page objects are all found in the **pages** folder.  This is the top level of the framework. There are also utility classes for componenets common all pages.  Those are separated into the **utility** subfolder
### ${\textsf{\color{orangered}Tests}}$
All tests will be found in the **tests** folder.  I am using Pytest for this demo which will find all tests automatically in this folder and run them.  The test files can be setup in different ways.  I chose to group the tests by user flow. Since we are concerned with the checkout flow for this demo, all tests will be in the `test_checkout.py` file

## ${\textsf{\color{orangered}Test Descriptions}}$
1. *test_happy_path_checkout* - Validates that a user can add an item to the cart and checkout.  This test has multiple assertions to ensure that each step succeeds.
2. *test_must_login_to_shop* - One of the negative scenarios is that we canot shop without logging in first.
3. *test_must_enter_user_information* - We must enter user information before we checkout
4. *test_cannot_bypass_user_information_step* - Since all fields are required this screen should not be able to be bypassed. ${\textsf{\color{red}Fails}}$
5. *test_valid_postal_code* - These are numberic and should be validated on server side and client side. ${\textsf{\color{red}Fails}}$
6. *test_input_length* - There should be a reasonable limit on form input fields. ${\textsf{\color{red}Fails}}$
7. *test_username_and_password_required* - Test that the username and password are both required
8. *test_password_case_sensitive* - passwords should be case sensative.
9. *test_username_case_sensative* - although not required, it is a good idea to implement this.
10. *test_no_clue_given_for_invalid_credentials* - To help prevent brute forcing an account it is important for the error message to not indicate if the username or password specifically was incorrect.  This is implicit in the 2 tests above but it is better to be explicit.