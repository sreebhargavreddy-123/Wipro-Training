*** Settings ***
Suite Setup       Open Browser To Login Page
Suite Teardown    Close Browser
Test Template     Login Test
Library           SeleniumLibrary

*** Variables ***
${URL}            https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}        chrome

*** Test Cases ***
Valid Login
    Admin    admin123

Invalid Login
    Admin    wrongpass

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

Login Test
    [Arguments]    ${username}    ${password}
    Go To    ${URL}
    Wait Until Element Is Visible    xpath=//input[@name='username']    10s
    Input Text    xpath=//input[@name='username']    ${username}
    Input Text    xpath=//input[@name='password']    ${password}
    Click Button    xpath=//button[@type='submit']
