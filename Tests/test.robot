*** Settings ***
Library    DatabaseLibrary
Library    DataDriver    ../Resource/InputFile/test_data.csv    file_format=csv


*** Test Cases ***
Verify datadriven approach
    [Template]    Validate Credentials
    [Template]    Validate Hello
    [Documentation]    Test data-driven login functionality.

*** Keywords ***
Validate Credentials
    [Arguments]    ${username}    ${password}
    Log To Console    Username: ${username}, Password: ${password}
    
    
Validate hello
    [Arguments]    ${username}
    Log To Console    Hello:${username}