*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    String
Resource   variables.robot

*** Keywords ***

# -------------------------------------------------
# SESSION
# -------------------------------------------------

Create Foodie Session
    ${headers}=    Create Dictionary    Content-Type=${CONTENT_TYPE}
    Create Session    foodie    ${BASE_URL}    headers=${headers}

# -------------------------------------------------
# RESTAURANT
# -------------------------------------------------

Register Restaurant
    ${rand}=    Generate Random String    4    [NUMBERS]
    ${name}=    Set Variable    FoodHub_${rand}

    ${body}=    Create Dictionary
    ...    name=${name}
    ...    category=Indian
    ...    location=Hyderabad
    ...    contact=9876543210
    ...    images=["img1.jpg"]

    ${resp}=    POST On Session
    ...    foodie
    ...    /api/v1/restaurants
    ...    json=${body}
    ...    expected_status=any

    Status Should Be    201    ${resp}
    ${json}=    Set Variable    ${resp.json()}
    Set Suite Variable    ${RESTAURANT_ID}    ${json["id"]}

Approve Restaurant
    ${resp}=    PUT On Session
    ...    foodie
    ...    /api/v1/admin/restaurants/${RESTAURANT_ID}/approve
    ...    expected_status=any

    Status Should Be    200    ${resp}

# -------------------------------------------------
# DISH
# -------------------------------------------------

Add Dish
    ${body}=    Create Dictionary
    ...    name=Chicken Biryani
    ...    type=Non-Veg
    ...    price=250
    ...    available_time=Lunch
    ...    image=biryani.jpg

    ${resp}=    POST On Session
    ...    foodie
    ...    /api/v1/restaurants/${RESTAURANT_ID}/dishes
    ...    json=${body}
    ...    expected_status=any

    Status Should Be    201    ${resp}
    ${json}=    Set Variable    ${resp.json()}
    Set Suite Variable    ${DISH_ID}    ${json["id"]}

Enable Dish
    ${body}=    Create Dictionary    enabled=${True}

    ${resp}=    PUT On Session
    ...    foodie
    ...    /api/v1/dishes/${DISH_ID}/status
    ...    json=${body}
    ...    expected_status=any

    Log    ${resp.text}
    Status Should Be    200    ${resp}

# -------------------------------------------------
# USER
# -------------------------------------------------

Register User
    ${rand}=    Generate Random String    4    [NUMBERS]
    ${email}=    Set Variable    user${rand}@gmail.com

    ${body}=    Create Dictionary
    ...    name=Bhargav
    ...    email=${email}
    ...    password=123456

    ${resp}=    POST On Session
    ...    foodie
    ...    /api/v1/users/register
    ...    json=${body}
    ...    expected_status=any

    Status Should Be    201    ${resp}
    ${json}=    Set Variable    ${resp.json()}
    Set Suite Variable    ${USER_ID}    ${json["id"]}

# -------------------------------------------------
# ORDER
# -------------------------------------------------

Place Order
    ${dish_id_int}=    Convert To Integer    ${DISH_ID}
    ${dish_list}=      Create List    ${dish_id_int}

    ${body}=    Create Dictionary
    ...    user_id=${USER_ID}
    ...    restaurant_id=${RESTAURANT_ID}
    ...    dishes=${dish_list}

    ${resp}=    POST On Session
    ...    foodie
    ...    /api/v1/orders
    ...    json=${body}
    ...    expected_status=any

    Status Should Be    201    ${resp}

View Orders By User
    ${resp}=    GET On Session
    ...    foodie
    ...    /api/v1/users/${USER_ID}/orders
    ...    expected_status=any

    Status Should Be    200    ${resp}