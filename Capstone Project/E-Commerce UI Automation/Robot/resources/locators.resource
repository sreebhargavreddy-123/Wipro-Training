*** Variables ***
${REGISTER_LINK}         link:Register
${LOGIN_LINK}            link:Log in
${LOGOUT_LINK}           link:Log out

${GENDER_RADIO}          gender
${FIRSTNAME_FIELD}       id:FirstName
${LASTNAME_FIELD}        id:LastName
${EMAIL_FIELD}           id:Email
${PASSWORD_FIELD}        id:Password
${CONFIRM_PASSWORD}      id:ConfirmPassword
${REGISTER_BUTTON}       id:register-button
${LOGIN_BUTTON}          xpath://input[@value='Log in']

${SEARCH_BOX}            id:small-searchterms
${SEARCH_BUTTON}         xpath://input[@value='Search']

${FIRST_PRODUCT}         xpath:(//h2[@class='product-title']/a)[1]
${ADD_TO_CART_BUTTON}    xpath://input[@value='Add to cart']
${NOTIFICATION_BAR}      id:bar-notification
${CART_LINK}             xpath://span[text()='Shopping cart']

${REMOVE_CHECKBOX}       xpath://input[@name='removefromcart']
${UPDATE_CART_BUTTON}    xpath://input[@name='updatecart']
