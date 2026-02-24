*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=../variables/users.csv    dialect=unix    encoding=utf-8

Resource   ../resources/common.resource
Resource   ../resources/register_keyword.robot
Resource   ../resources/login_keyword.robot
Resource   ../resources/search_keyword.robot
Resource   ../resources/cart_keyword.robot

Test Setup       Open Browser To Application
Test Teardown    Close Browser Session

*** Test Cases ***
E2E Flow for user ${firstname}
    [Template]    Complete User Flow

*** Keywords ***
Complete User Flow
    [Arguments]    ${firstname}    ${lastname}    ${password}    ${product}    ${gender}

    ${email}=    Register New User    ${firstname}    ${lastname}    ${password}    ${gender}
    Logout From Application

    Login To Application    ${email}    ${password}
    Search Product          ${product}
    Add Product To Cart
    Go To Cart And Remove Item
    Logout From Application
