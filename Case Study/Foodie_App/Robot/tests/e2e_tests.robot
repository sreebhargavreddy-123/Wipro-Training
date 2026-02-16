*** Settings ***
Resource    ../resources/keywords.robot

*** Test Cases ***
End To End Foodie Flow
    Create Foodie Session
    Register Restaurant
    Approve Restaurant
    Add Dish
    Enable Dish
    Register User
    Place Order
    View Orders By User