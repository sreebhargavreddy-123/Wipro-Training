*** Settings ***
Suite Setup       Open Browser To Login Page
Suite Teardown    Close Browser
Library           SeleniumLibrary

*** Variables ***
${URL}            https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}        chrome

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    xpath=//input[@name='username']    5s

Login
    [Arguments]    ${username}    ${password}
    Input Text    xpath=//input[@name='username']    ${username}
    Input Text    xpath=//input[@name='password']    ${password}
    Click Element    xpath=//button[@type='submit']

Logout
    Wait Until Element Is Visible    xpath=//span[@class='oxd-userdropdown-tab']    5s
    Click Element    xpath=//span[@class='oxd-userdropdown-tab']
    Click Element    xpath=//a[text()='Logout']
    Wait Until Element Is Visible    xpath=//input[@name='username']    5s

*** Test Cases ***
Valid Login
    Login    Admin    admin123
    Sleep    3s
    Logout

Invalid Login
    Login    Admin    wrongpass
    Sleep    3s
    Page Should Contain    Invalid credentials
