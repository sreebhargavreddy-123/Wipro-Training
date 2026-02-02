*** Settings ***
Library    SeleniumLibrary

Suite Setup    Open Browser To Application
Suite Teardown    Close Browser

*** Variables ***
${BROWSER}     chrome
${URL}         https://testautomationpractice.blogspot.com/
${NAME}        John
${GENDER}      male
${DAY}         sunday
${COUNTRY}     India
${EXPECTED}    India

*** Keywords ***
Open Browser To Application
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

*** Test Cases ***
Verify Browser Automation With BuiltIn Keywords
    # Text Box
    Input Text    id=name    ${NAME}

    # Radio Button
    Click Element    id=${GENDER}

    # Check Box
    Click Element    id=${DAY}

    # Drop-down
    Select From List By Label    id=country    ${COUNTRY}

    # Built-in Keyword: Sleep
    Sleep    2s

    # Form Validation using Built-in Keyword
    ${selected}=    Get Selected List Label    id=country
    Should Be Equal    ${selected}    ${EXPECTED}

    # Built-in Keyword: Run Keyword If
    Run Keyword If    '${selected}' == 'India'    Log    Form filled successfully
