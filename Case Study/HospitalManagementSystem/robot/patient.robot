*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}      http://127.0.0.1:5000/register
${BROWSER}  chrome

@{NAMES}    Ravi    Sita    Aman
@{AGES}     30      25      40

*** Test Cases ***
Register Multiple Patients (Data Driven)
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    FOR    ${i}    IN RANGE    0    3
        Input Text    name=name    ${NAMES}[${i}]
        Input Text    name=age     ${AGES}[${i}]
        Click Button    xpath=//input[@type='submit']
        Sleep    1s
        Go To    ${URL}
    END

    Close Browser
