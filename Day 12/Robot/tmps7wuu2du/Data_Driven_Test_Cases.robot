Language: English

*** Settings ***
Suite Setup       Open Browser    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login    chrome
Suite Teardown    Close Browser
Test Template     Login Test
Library           SeleniumLibrary

*** Test Cases ***
Valid Login
    Admin    admin123

Invalid Login
    Admin    wrongpass

*** Keywords ***
Login Test
    [Arguments]    ${username}    ${password}
    Wait Until Element Is Visible    xpath=//input[@name='username']    10s
    Input Text    xpath=//input[@name='username']    ${username}
    Input Text    xpath=//input[@name='password']    ${password}
    Click Button    xpath=//button[@type='submit']
