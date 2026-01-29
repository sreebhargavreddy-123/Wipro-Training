*** Settings ***
Library    BuiltIn

*** Variables ***
${GREETING}      Hello, Robot Framework!
@{ITEMS}         Apple    Banana    Orange

*** Test Cases ***
Log Scalar Variable
    Log    ${GREETING}
    Log To Console    ${GREETING}

Log List Variable
    Log    List contains: @{ITEMS}
    Log To Console    First item is: ${ITEMS}[0]
