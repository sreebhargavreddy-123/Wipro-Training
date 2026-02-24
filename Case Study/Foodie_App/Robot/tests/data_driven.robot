*** Settings ***
Resource    ../resources/keywords.robot
Suite Setup    Create Foodie Session

*** Test Cases ***
Register Multiple Restaurants
    [Template]    Register Restaurant
    Indian      Hyderabad
    Chinese     Bangalore
    Italian     Mumbai