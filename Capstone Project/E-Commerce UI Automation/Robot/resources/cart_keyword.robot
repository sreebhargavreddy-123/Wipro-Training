*** Settings ***
Library    SeleniumLibrary
Resource   locators.resource

*** Keywords ***
Add Product To Cart
    Click Element    ${FIRST_PRODUCT}
    Wait Until Element Is Visible    ${ADD_TO_CART_BUTTON}    10s

    Click Element    ${ADD_TO_CART_BUTTON}
    Wait Until Element Is Visible    ${NOTIFICATION_BAR}    10s

Go To Cart And Remove Item
    Click Element    ${CART_LINK}
    Wait Until Page Contains    Shopping cart    10s

    Select Checkbox    ${REMOVE_CHECKBOX}
    Click Element    ${UPDATE_CART_BUTTON}

    Wait Until Page Contains    Your Shopping Cart is empty!    10s
