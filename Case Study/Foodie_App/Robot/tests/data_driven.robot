*** Settings ***
Resource    ../resources/keywords.robot
Suite Setup    Create Foodie Session

*** Test Cases ***
Register Multiple Restaurants
    [Template]    Register Restaurant With Data
    Indian    Hyderabad
    Chinese   Bangalore

*** Keywords ***
Register Restaurant With Data
    [Arguments]    ${category}    ${location}

    ${rand}=    Generate Random String    4    [NUMBERS]
    ${name}=    Set Variable    FoodHub_${rand}

    ${body}=    Create Dictionary
    ...    name=${name}
    ...    category=${category}
    ...    location=${location}
    ...    contact=9999999999
    ...    images=["img1.jpg"]

    ${resp}=    POST On Session
    ...    foodie
    ...    /api/v1/restaurants
    ...    json=${body}
    ...    expected_status=any

    Log    ${resp.text}
    Status Should Be    201    ${resp}