*** Settings ***
Library    BuiltIn

*** Test Cases ***
Verify Environment Setup
    [Documentation]    Verifies Python, Robot Framework, and SeleniumLibrary with graceful failure

    # 1. Verify Python installation
    ${py_status}    ${py_version}=    Run Keyword And Ignore Error
    ...    Evaluate    __import__('sys').version
    Run Keyword If    '${py_status}' == 'FAIL'
    ...    Fail    Python is not installed or not accessible
    Log    Python version: ${py_version}
    Log To Console    Python version: ${py_version}

    # 2 & 4. Verify Robot Framework installation and print version
    ${rf_status}    ${rf_version}=    Run Keyword And Ignore Error
    ...    Evaluate    __import__('robot').__version__
    Run Keyword If    '${rf_status}' == 'FAIL'
    ...    Fail    Robot Framework is not installed
    Log    Robot Framework version: ${rf_version}
    Log To Console    Robot Framework version: ${rf_version}

    # 3. Verify SeleniumLibrary installation
    ${sel_status}    ${sel_msg}=    Run Keyword And Ignore Error
    ...    Import Library    SeleniumLibrary
    Run Keyword If    '${sel_status}' == 'FAIL'
    ...    Fail    SeleniumLibrary is missing. Install using: pip install robotframework-seleniumlibrary
    Log    SeleniumLibrary imported successfully
    Log To Console    SeleniumLibrary imported successfully
