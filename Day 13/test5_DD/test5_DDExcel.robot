*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=./testdata.xlsx
Suite Setup    Open Application
Suite Teardown    Close Browser
Test Template    Login Using Excel Data

*** Variables ***
${URL}      https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}  chrome

*** Keywords ***
Open Application
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    name=username    15s

Login Using Excel Data
    [Arguments]    ${username}    ${password}

    Wait Until Element Is Visible    name=username    10s
    Clear Element Text    name=username
    Input Text    name=username    ${username}

    Clear Element Text    name=password
    Input Text    name=password    ${password}

    Click Button    xpath=//button[@type='submit']

    # Wait for either dashboard or error
    Sleep    5s

    ${success}=    Run Keyword And Return Status
    ...    Page Should Contain Element    xpath=//header

    IF    ${success}
        Log    ✅ Valid login: ${username}
        Capture Page Screenshot
        Slow Logout
    ELSE
        Log    ❌ Invalid login: ${username}
        Page Should Contain    Invalid credentials
        Capture Page Screenshot
    END

Slow Logout
    # Dashboard clearly visible
    Wait Until Element Is Visible
    ...    xpath=//header//span[contains(@class,'oxd-userdropdown-tab')]    10s
    Sleep    3s    # 👈 dashboard visibility delay

    Click Element
    ...    xpath=//header//span[contains(@class,'oxd-userdropdown-tab')]

    Wait Until Element Is Visible
    ...    xpath=//a[text()='Logout']    10s
    Sleep    2s    # 👈 logout menu visible

    Click Link    Logout
    Wait Until Element Is Visible    name=username    10s

*** Test Cases ***
TC_Login_With_Excel
    Login Using Excel Data
