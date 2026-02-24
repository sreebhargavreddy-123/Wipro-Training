*** Settings ***
Resource    ../resources/keywords.robot
Suite Setup    Create Foodie Session

*** Test Cases ***
Register Restaurant Without Name
    ${body}=    Create Dictionary    category=Indian

    ${resp}=    POST On Session
    ...    foodie
    ...    /api/v1/restaurants
    ...    json=${body}
    ...    expected_status=any

    Log    ${resp.text}
    Status Should Be    400    ${resp}