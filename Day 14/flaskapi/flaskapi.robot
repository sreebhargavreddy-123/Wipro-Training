*** Settings ***
Library    RequestsLibrary

*** Variables ***
${baseurl}    http://127.0.0.1:5000

*** Test Cases ***
Create new user
    Create Session    postingsession    ${baseurl}
    ${data}=    Create Dictionary    name=varsha
    ${response}=    POST On Session    postingsession    /users    json=${data}
    Status Should Be    201    ${response}
    ${user_json}=    Evaluate    $response.json()
    Log    ${user_json}    console=True

Update user using PUT
    Create Session    postingsession    ${baseurl}
    ${data}=    Create Dictionary    name=Pooja
    ${response}=    PUT On Session    postingsession    /users/1    json=${data}
    Status Should Be    200    ${response}
    ${user_json}=    Evaluate    $response.json()
    Log    ${user_json}    console=True

Update user again (PUT instead of PATCH)
    Create Session    postingsession    ${baseurl}
    ${data}=    Create Dictionary    name=Pooja patched
    ${response}=    PUT On Session    postingsession    /users/1    json=${data}
    Status Should Be    200    ${response}
    ${user_json}=    Evaluate    $response.json()
    Log    ${user_json}    console=True

Verify Get All Users
    Create Session    mysession    ${baseurl}
    ${response}=    GET On Session    mysession    /users
    Status Should Be    200    ${response}
    ${res_json}=    Evaluate    $response.json()
    Log    ${res_json}    console=True

Verify Get Single user
    Create Session    mysession    ${baseurl}
    ${response}=    GET On Session    mysession    /users/3
    Status Should Be    200    ${response}
    ${res_json}=    Evaluate    $response.json()
    Log    ${res_json}    console=True

Verify Get Single user not found
    Create Session    mysession    ${baseurl}
    ${response}=    GET On Session    mysession    /users/99999    expected_status=anything
    Status Should Be    404    ${response}
    ${res_json}=    Evaluate    $response.json()
    Log    ${res_json}    console=True

Verify Delete user method not allowed
    Create Session    mysession    ${baseurl}
    ${response}=    DELETE On Session    mysession    /users/1    expected_status=anything
    Status Should Be    405    ${response}
