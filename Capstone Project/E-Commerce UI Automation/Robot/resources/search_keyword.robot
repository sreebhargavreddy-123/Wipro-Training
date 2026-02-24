*** Settings ***
Library    SeleniumLibrary
Resource   locators.resource

*** Keywords ***
Search Product
    [Arguments]    ${product}

    Input Text    ${SEARCH_BOX}    ${product}
    Click Element    ${SEARCH_BUTTON}

    Wait Until Page Contains    ${product}    10s
