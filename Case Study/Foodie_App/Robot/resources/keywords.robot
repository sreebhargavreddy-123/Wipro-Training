*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    String
Resource   variables.robot

*** Keywords ***

# =================================================
# SESSION
# =================================================

Create Foodie Session
    ${headers}=    Create Dictionary    Content-Type=${CONTENT_TYPE}
    Create Session    foodie    ${BASE_URL}    headers=${headers}

# =================================================
# RESTAURANT
# =================================================

Register Restaurant
    [Arguments]    ${category}=${DEFAULT_CATEGORY}    ${location}=${DEFAULT_LOCATION}
    ${rand}=    Generate Random String    4    [NUMBERS]
    ${name}=    Set Variable    FoodHub_${rand}

    ${body}=    Create Dictionary
    ...    name=${name}
    ...    category=${category}
    ...    location=${location}
    ...    contact=${DEFAULT_CONTACT}
    ...    images=["img1.jpg"]

    ${resp}=    POST On Session    foodie    /api/v1/restaurants    json=${body}
    Status Should Be    201    ${resp}

    ${json}=    Set Variable    ${resp.json()}
    Set Suite Variable    ${RESTAURANT_ID}    ${json["id"]}

Approve Restaurant
    ${resp}=    PUT On Session
    ...    foodie
    ...    /api/v1/admin/restaurants/${RESTAURANT_ID}/approve

    Status Should Be    200    ${resp}

# =================================================
# DISH
# =================================================

Add Dish
    [Arguments]
    ...    ${dish_name}=${DEFAULT_DISH_NAME}
    ...    ${dish_type}=${DEFAULT_DISH_TYPE}
    ...    ${price}=${DEFAULT_PRICE}

    ${body}=    Create Dictionary
    ...    name=${dish_name}
    ...    type=${dish_type}
    ...    price=${price}
    ...    available_time=${DEFAULT_AVAILABLE}
    ...    image=${DEFAULT_IMAGE}

    ${resp}=    POST On Session
    ...    foodie
    ...    /api/v1/restaurants/${RESTAURANT_ID}/dishes
    ...    json=${body}

    Status Should Be    201    ${resp}
    ${json}=    Set Variable    ${resp.json()}
    Set Suite Variable    ${DISH_ID}    ${json["id"]}

Enable Dish
    ${body}=    Create Dictionary    enabled=${True}

    ${resp}=    PUT On Session
    ...    foodie
    ...    /api/v1/dishes/${DISH_ID}/status
    ...    json=${body}

    Status Should Be    200    ${resp}

# =================================================
# USER
# =================================================

Register User
    ${rand}=    Generate Random String    4    [NUMBERS]
    ${email}=    Set Variable    user${rand}@gmail.com

    ${body}=    Create Dictionary
    ...    name=User_${rand}
    ...    email=${email}
    ...    password=${DEFAULT_PASSWORD}

    ${resp}=    POST On Session
    ...    foodie
    ...    /api/v1/users/register
    ...    json=${body}

    Status Should Be    201    ${resp}
    ${json}=    Set Variable    ${resp.json()}
    Set Suite Variable    ${USER_ID}    ${json["id"]}

# =================================================
# ORDER
# =================================================

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

    Status Should Be    201    ${resp}
    ${json}=    Set Variable    ${resp.json()}
    Set Suite Variable    ${ORDER_ID}    ${json["id"]}

View Orders By User
    ${resp}=    GET On Session
    ...    foodie
    ...    /api/v1/users/${USER_ID}/orders

    Status Should Be    200    ${resp}

# =================================================
# RATING
# =================================================

Add Rating
    ${body}=    Create Dictionary
    ...    order_id=${ORDER_ID}
    ...    rating=${DEFAULT_RATING}
    ...    comment=${DEFAULT_COMMENT}

    ${resp}=    POST On Session
    ...    foodie
    ...    /api/v1/ratings
    ...    json=${body}

    Status Should Be    201    ${resp}