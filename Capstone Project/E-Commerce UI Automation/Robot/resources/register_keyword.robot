*** Settings ***
Library    SeleniumLibrary
Library    String
Resource   locators.resource

*** Keywords ***
Register New User
    [Arguments]    ${firstname}    ${lastname}    ${password}    ${gender}

    Click Element    ${REGISTER_LINK}
    Wait Until Element Is Visible    ${FIRSTNAME_FIELD}    10s

    ${gender_lower}=    Convert To Lower Case    ${gender}
    Click Element       id:gender-${gender_lower}

    Input Text    ${FIRSTNAME_FIELD}    ${firstname}
    Input Text    ${LASTNAME_FIELD}     ${lastname}

    ${random}=    Generate Random String    4    [NUMBERS]
    ${email}=     Set Variable    test${random}@mail.com

    Input Text    ${EMAIL_FIELD}        ${email}
    Input Text    ${PASSWORD_FIELD}     ${password}
    Input Text    ${CONFIRM_PASSWORD}   ${password}

    Click Element    ${REGISTER_BUTTON}
    Wait Until Page Contains    Your registration completed    10s

    RETURN    ${email}
