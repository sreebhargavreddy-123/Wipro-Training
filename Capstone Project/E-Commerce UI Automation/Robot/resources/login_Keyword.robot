*** Settings ***
Library    SeleniumLibrary
Resource   locators.resource

*** Keywords ***
Login To Application
    [Arguments]    ${email}    ${password}

    Click Element    ${LOGIN_LINK}
    Wait Until Element Is Visible    ${EMAIL_FIELD}    10s

    Input Text    ${EMAIL_FIELD}      ${email}
    Input Text    ${PASSWORD_FIELD}   ${password}
    Click Element    ${LOGIN_BUTTON}

    Wait Until Page Contains    Log out    10s

Logout From Application
    Click Element    ${LOGOUT_LINK}
    Wait Until Page Contains    Log in    10s
