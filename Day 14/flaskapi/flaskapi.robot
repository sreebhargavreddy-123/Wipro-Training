*** Settings ***
Library    RequestsLibrary

*** Variables ***
${baseurl}    http://127.0.0.1:5000

*** Test Cases ***
Verify Get_User
    Create Session    mysession    ${baseurl}
    ${response}=    GET On Session    mysession    /users
    Status Should Be    200    ${response}
    ${res_json}=    Set Variable    ${response.json()}
    Log    ${res_json}    console=True


Verify Get Single User Not Found
    Create Session    mysession    ${baseurl}
    ${response}=    Run Keyword And Expect Error    *404*    GET On Session    mysession    /users/99
    Log    User not found as expected    console=True


Create New User
    ${data}=    Create Dictionary    name=Hema    job=Tester
    ${response}=    POST On Session    mysession    /users    json=${data}
    Status Should Be    201    ${response}
    ${res_json}=    Set Variable    ${response.json()}
    Log    ${res_json}    console=True
