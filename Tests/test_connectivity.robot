*** Settings ***
Library    ../Resource/Libraries/MyCustomLibrary.py

*** Test Cases ***
Test Library Keyword
    My Keyword    Hello Robot Framework!

*** Test Cases ***
Test AWS Connection
    Verify AWS Connection
