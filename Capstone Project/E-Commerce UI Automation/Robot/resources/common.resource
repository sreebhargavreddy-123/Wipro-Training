*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BASE_URL}    https://demowebshop.tricentis.com
${BROWSER}     chrome

#${BASE_URL}    https://demowebshop.tricentis.com
#${BROWSER}     firefox

#${BASE_URL}    https://demowebshop.tricentis.com
#${BROWSER}     edge

*** Keywords ***
Open Browser To Application
    Run Keyword If    '${BROWSER}' == 'chrome'    Open Chrome Browser
    ...    ELSE IF    '${BROWSER}' == 'firefox'    Open Firefox Browser
    ...    ELSE IF    '${BROWSER}' == 'edge'    Open Edge Browser
    ...    ELSE    Fail    Unsupported browser: ${BROWSER}

    Maximize Browser Window
    Register Keyword To Run On Failure    Capture Page Screenshot


Open Chrome Browser
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys
    Call Method    ${options}    add_argument    --ignore-certificate-errors
    Call Method    ${options}    add_argument    --allow-running-insecure-content
    Open Browser    ${BASE_URL}    chrome    options=${options}
    Sleep    2s
    Press Keys    NONE    thisisunsafe


Open Firefox Browser
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].FirefoxOptions()    sys
    Call Method    ${options}    set_preference    security.cert_pinning.enforcement_level    0
    Call Method    ${options}    set_preference    acceptInsecureCerts    True
    Open Browser    ${BASE_URL}    firefox    options=${options}


Open Edge Browser
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].EdgeOptions()    sys
    Call Method    ${options}    add_argument    --ignore-certificate-errors
    Open Browser    ${BASE_URL}    edge    options=${options}
    Sleep    2s
    Press Keys    NONE    thisisunsafe


Close Browser Session
    Close Browser