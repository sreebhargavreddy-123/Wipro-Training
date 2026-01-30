*** Settings ***
Library    SeleniumLibrary


*** Variables ***
${url}        https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}    chrome


*** Keywords ***
Open OrangeHRM
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
    Wait Until Element Is Visible    name=username    10s

OrangeHRM Login
    [Arguments]    ${username}    ${password}
    Input Text    name=username    ${username}
    Input Text    name=password    ${password}
    Capture Page Screenshot    beforelogin.png
    Click Button    xpath=//button[@type='submit']
    Wait Until Page Contains Element    xpath=//span[@class='oxd-userdropdown-tab']    10s
    Capture Page Screenshot    afterlogin.png
    Close Browser


*** Test Cases ***
OrangeHRM Login Test
    Open OrangeHRM
    OrangeHRM Login    Admin    admin123
