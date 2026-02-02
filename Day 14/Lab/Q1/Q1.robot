*** Settings ***
Library    SeleniumLibrary

Suite Setup       Suite Level Setup
Suite Teardown    Suite Level Teardown
Test Setup        Test Level Setup
Test Teardown     Test Level Teardown


*** Variables ***
${BROWSER}    chrome
${URL}        https://www.google.com


*** Keywords ***
Suite Level Setup
    Log    ===== Suite Setup Started =====

Suite Level Teardown
    Log    ===== Suite Teardown Completed =====

Test Level Setup
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

Test Level Teardown
    Close Browser


*** Test Cases ***
Verify Google Title
    [Tags]    smoke    regression
    Title Should Be    Google

Verify Google Search Box
    [Tags]    smoke
    Page Should Contain Element    name=q
