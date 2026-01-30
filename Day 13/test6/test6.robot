*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=./testdata.xlsx
Suite Setup    Open Application
Suite Teardown    Close Browser
Test Template    Register Login Flow

*** Variables ***
${URL}      https://tutorialsninja.com/demo/
${BROWSER}  chrome

*** Test Cases ***
Register Login Using Excel
    ${firstname}    ${lastname}    ${email}    ${telephone}    ${password}

*** Keywords ***
Open Application
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    1s

Register Login Flow
    [Arguments]    ${firstname}    ${lastname}    ${email}    ${telephone}    ${password}

    ${timestamp}=    Get Time    epoch
    ${unique_email}=    Set Variable    ${email}${timestamp}@test.com

    Register User    ${firstname}    ${lastname}    ${unique_email}    ${telephone}    ${password}
    Logout From Application
    Login User    ${unique_email}    ${password}
    Logout From Application

Register User
    [Arguments]    ${firstname}    ${lastname}    ${email}    ${telephone}    ${password}

    Click Element    xpath=//span[text()='My Account']
    Click Element    xpath=//a[text()='Register']

    Input Text    id=input-firstname    ${firstname}
    Input Text    id=input-lastname     ${lastname}
    Input Text    id=input-email        ${email}
    Input Text    id=input-telephone    ${telephone}
    Input Text    id=input-password     ${password}
    Input Text    id=input-confirm      ${password}

    Click Element    xpath=//input[@name='agree']
    Click Button     xpath=//input[@value='Continue']

    Wait Until Page Contains    Your Account Has Been Created    10s

Login User
    [Arguments]    ${email}    ${password}

    Click Element    xpath=//span[text()='My Account']
    Click Element    xpath=//a[text()='Login']

    Input Text    id=input-email    ${email}
    Input Text    id=input-password    ${password}
    Click Button    xpath=//input[@value='Login']

    Wait Until Page Contains    My Account    10s

Logout From Application
    Click Element    xpath=//span[text()='My Account']
    Click Element    xpath=//a[text()='Logout']
    Wait Until Page Contains    Account Logout    10s
    Go To    ${URL}
