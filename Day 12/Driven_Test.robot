*** Settings ***
Library           SeleniumLibrary

*** Test Cases ***
Valid Login
    Open Browser    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login    chrome
    Wait Until Element Is Visible    xpath=//input[@name='username']    20s
    Input Text    xpath=//input[@name='username']    Admin
    Input Text    xpath=//input[@name='password']    admin123
    Click Element    xpath=//button[@type='submit']
    Sleep    3s
    Close Browser

Invalid Login
    Open Browser    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login    chrome
    Wait Until Element Is Visible    xpath=//input[@name='username']    20s
    Input Text    xpath=//input[@name='username']    Admin
    Input Text    xpath=//input[@name='password']    wrongpass
    Click Element    xpath=//button[@type='submit']
    Sleep    3s
    Close Browser
