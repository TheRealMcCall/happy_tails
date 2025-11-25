# Testing
---
## Contents

* [Browser Compatibility](#browser-compatibility)
* [Responsiveness](#responsiveness)
* [Manual Testing](#manual-testing)
* [Automated Testing](#automated-testing)
* [User Stories Testing](#user-stories-testing)
* [Lighthouse Testing](#lighthouse-testing)
* [Validator Testing](#validator-testing)
* [Bugs](#bugs)
---

Some sections below contain collapsible screenshots and validation outputs — click each summary to expand and view details.

## Browser Compatibility

The website was tested on multiple browsers to confirm full compatibility and consistent rendering across platforms.

<details>
<summary>Click here to view Chrome screenshot - <strong>Working as Expected</strong></summary>

![Chrome Screenshot](/documentation/compatibility/chrome_compat.png)

</details>

<details>
<summary>Click here to view Firefox screenshot - <strong>Working as Expected</strong></summary>

![Firefox Screenshot](/documentation/compatibility/firefox_compat.png)

</details>

<details>
<summary>Click here to view Edge screenshot - <strong>Working as Expected</strong></summary>

![Edge Screenshot](/documentation/compatibility/edge_compat.png)

</details>

<details>
<summary>Click here to view Opera GX screenshot - <strong>Working as Expected</strong></summary>

![Opera Screenshot](/documentation/compatibility/operagx_compat.png)

</details>

## Responsiveness
The site was tested for responsive behaviour across multiple screen sizes and devices. All major content, forms, and controls adjust fluidly across viewport sizes with no layout-breaking issues observed.

**Tested Devices:**
- 1440p 27" Landscape Monitor
- Pixel 8 Pro Mobile Device

In addition to real device testing, 'Chrome DevTools’ responsive mode was used throughout development to verify breakpoints and content flow.

<details>
<summary>Click here to view 27" 1440p Desktop Monitor screenshot – <strong>Works as expected</strong></summary>

![1440p Desktop Screenshot](/documentation/responsive/1440p_desktop.png)

</details>

----
Responsiveness was also demonstrated using a short video recording of real device testing:

- [Google Pixel 8 Pro - Mobile Device](https://photos.app.goo.gl/7xxtSf2eWFppvVsG7)  

All navigation menus, forms, buttons, summaries, and tables were confirmed to be usable at small screen widths. The layout adapts seamlessly.

## Manual Testing

Thorough manual testing was done for all critical user interactions across pages.

### Global Navigation (Header)

Nav Items were tested logged in as an admin and as a shopper account in order to check correct navlinks are displayed for the relevant user type.

| Feature                          | Action | Expected Result                           | Works?              |
|----------------------------------|--------|-------------------------------------------|---------------------|
| Brand Name                       | Click  | Goes to homepage                          | Works as expected   |
| Products link                    | Click  | Navigates to the products list page       | Works as expected   |
| Wishlist icon (logged in)        | Click  | Navigates to the wishlist page            | Works as expected   |
| My Account link (logged in)      | Click  | Navigates to the My Account page          | Works as expected   |
| Logout Link (logged in)          | Click  | Navigates to the Logout Page              | Works as expected   |
| Login / Register (logged out)    | Click  | Navigates to the relevant page            | Works as expected   |
| Basket icon + badge              | Display| Shows number of items in basket           | Works as expected   |
| Basket icon + badge              | Click  | Navigates to the basket page              | Works as expected   |
| Products management link         | Click  | Navigates to the product management page  | Works as expected   |
| Nav links hover state            | Hover  | contrast change and underline             | Works as expected   |

---

### Global Navigation (Hamburger menu)

| Feature                          | Action | Expected Result                           | Works?              |
|----------------------------------|--------|-------------------------------------------|---------------------|
| Hamburger menu                   | Click  | lists nav items                           | Works as expected   |
| Brand Name                       | Click  | Goes to homepage                          | Works as expected   |
| Products link                    | Click  | Navigates to the products list page       | Works as expected   |
| Wishlist icon (logged in)        | Click  | Navigates to the wishlist page            | Works as expected   |
| My Account link (logged in)      | Click  | Navigates to the My Account page          | Works as expected   |
| Logout Link (logged in)          | Click  | Navigates to the Logout Page              | Works as expected   |
| Login / Register (logged out)    | Click  | Navigates to the relevant page            | Works as expected   |
| Basket icon + badge              | Display| Shows number of items in basket           | Works as expected   |
| Basket icon + badge              | Click  | Navigates to the basket page              | Works as expected   |
| Products management link         | Click  | Navigates to the product management page  | Works as expected   |

---

### Global Navigation (Footer)

| Feature                             | Action    | Expected Result                      | Works?              |
|-------------------------------------|-----------|--------------------------------------|---------------------|
| Delivery Info link                  | Click     | Delivery Info Modal dispays          | Works as expected   |
| Terms and conditions link           | Click     | Navigates to the terms page          | Works as expected   |
| Social links                        | Click     | Navigates to the relevant social page| Works as expected   |
| Newsletter Subscription             | Subscribe | Confirms subscription (mailchimp)    | Works as expected   |
| Icons and links hover state         | Hover     | contrast change and underline        | Works as expected   |

---

### Home Page

| Feature                  | Action                       | Expected Result                                                                         | Works?              |
|--------------------------|------------------------------|-----------------------------------------------------------------------------------------|---------------------|
| Introduction text        | View                         | Clear explanation of site purpose and value                                             | Works as expected   |
| “Shop now” buttons       | Click                        | Navigates to products list page                                                         | Works as expected   |
| Auth CTAs (logged out)   | Click Create account / Login | Navigate to Allauth signup or login pages                                               | Works as expected   |
| Auth CTAs (logged in)    | Click My account / My orders | Navigate to My Account page / My Orders page                                            | Works as expected   |
| Register benefits bar    | View                         | Carousel rotates through key account benefits for anonymous users                       | Works as expected   |
| Register “More info”     | Click                        | Modal opens with information about account benefits and can be closed with close button | Works as expected   |
| Nav link / buttons       | Hover                        | Contrast change on hover                                                                | Works as expected   |        

---

### Login Page

| Feature           | Action                                | Expected Result                                                             | Works?              |
|-------------------|---------------------------------------|-----------------------------------------------------------------------------|---------------------|
| Login form view   | View                                  | Form shows email/username and password fields                               | Works as expected   |
| Valid login       | Enter valid credentials + submit      | User is logged in and redirected to the appropriate page                    | Works as expected   |
| Invalid login     | Enter wrong credentials + submit      | Error message is displayed; user remains on login form                      | Works as expected   |
| Create account link| Click                                | Navigates to registration page                                              | Works as expected   |
| Nav link / buttons| Hover                                 | Contrast change on hover                                                    | Works as expected   |     

---

### Logout Page

| Feature           | Action          | Expected Result                                       | Works?              |
|-------------------|-----------------|-------------------------------------------------------|---------------------|
| Logout confirmation | Click Logout  | User is logged out and redirected (e.g. home page)    | Works as expected   |
| Auth links        | View            | Login / Register links appear instead of My Account   | Works as expected   |

---

### Register Page

| Feature             | Action                                | Expected Result                                                                 | Works?              |
|---------------------|---------------------------------------|---------------------------------------------------------------------------------|---------------------|
| Register form view  | View                                  | Form shows required fields (email, username if used, password, confirmation)   | Works as expected   |
| Valid registration  | Enter valid data + submit             | Account is created and user is either logged in or prompted to verify email    | Works as expected   |
| Missing data        | Submit with required fields empty     | Validation errors shown next to missing/invalid fields                          | Works as expected   |
| “Already have an account?” link| Click                      | Navigates to login page                                                         | Works as expected   |

---

### Products Page

| Feature                    | Action                                 | Expected Result                                                             | Works?              |
|----------------------------|----------------------------------------|-----------------------------------------------------------------------------|---------------------|
| View product list grid     | View                                   | Grid of available products displayed with name and price range              | Works as expected   |
| Category pills             | Click on a category                    | Product list filters to show only products from selected category           | Works as expected   |
| “All” category             | Click “All”                            | All products are shown regardless of category                               | Works as expected   |
| Search bar                 | Enter query + submit                   | Product list filters to products whose name/description matches query       | Works as expected   |
| No search results          | Search for non-existing term           | “No products found” style message displayed                                  | Works as expected   |
| Product card “View” button | Click                                  | Navigates to specific product detail page                                   | Works as expected   |

---

### Product Details Page

| Feature                           | Action                                                  | Expected Result                                                                                     | Works?              |
|-----------------------------------|---------------------------------------------------------|-----------------------------------------------------------------------------------------------------|---------------------|
| Product information               | View                                                    | Product name, image, description and price are displayed                                           | Works as expected   |
| Variant dropdown                  | Change selected variant                                 | Stock information and price update to reflect the selected variant                                 | Works as expected   |
| Low / out of stock warnings       | Select low or zero stock variants                       | Appropriate “low stock” or “out of stock” messages displayed                                       | Works as expected   |
| Quantity input                    | Change quantity                                         | Total price display updates based on selected quantity and variant price                           | Works as expected   |
| Add to basket (valid)             | Select in-stock variant, valid quantity, click button   | Item added to basket; success message shown; basket badge updated                                  | Works as expected   |
| Add to basket (beyond stock)      | Enter quantity greater than available stock             | Error or warning message shown; quantity limited or add prevented                                  | Works as expected   |
| Add to wishlist (logged in)       | Click heart icon                                        | Product added to user’s wishlist; icon changes to filled heart                                     | Works as expected   |
| Remove from wishlist (logged in)  | Click filled heart again                                | Product removed from wishlist; icon returns to outlined heart                                      | Works as expected   |

---

### My Account Page

| Feature                          | Action                                          | Expected Result                                                                       | Works?              |
|----------------------------------|-------------------------------------------------|---------------------------------------------------------------------------------------|---------------------|
| Profile summary display          | View                                            | First name, last name and email shown (with prompts if name fields not set)          | Works as expected   |
| Edit profile button              | Click                                           | Navigates to profile edit page                                                        | Works as expected   |
| Change password button           | Click                                           | Navigates to password change page (Allauth)                                          | Works as expected   |
| Wishlist preview                 | View                                            | Shows a short list of wishlist items (if any)                                         | Works as expected   |
| Remove from wishlist             | Click “Remove” button on preview item           | Product is removed from wishlist and list updates                                     | Works as expected   |
| Addresses list                   | View                                            | List of saved addresses displayed with label, address lines and phone number         | Works as expected   |
| Add address from profile         | Click “Add address”                             | Navigates to Add Address page                                                         | Works as expected   |
| Recent orders table              | View                                            | Recent orders shown with order number, date, total and status badges                  | Works as expected   |
| View all orders link             | Click (when recent orders exist)                | Navigates to My Orders page                                                           | Works as expected   |

---

### My Orders Page

| Feature              | Action                           | Expected Result                                                           | Works?              |
|----------------------|----------------------------------|---------------------------------------------------------------------------|---------------------|
| Orders table         | View                             | Table shows all orders with order number, date, total and status          | Works as expected   |
| Order detail link    | Click on an order number         | Navigates to detailed order view page                                     | Works as expected   |
| No orders message    | View with no orders              | Informational message shown instead of table                              | Works as expected   |

---

### Edit Profile Page

| Feature                  | Action                              | Expected Result                                                      | Works?              |
|--------------------------|-------------------------------------|----------------------------------------------------------------------|---------------------|
| Load profile form        | View                                | Form pre-populated with current first and last name                  | Works as expected   |
| Save valid changes       | Edit fields + submit                | Profile is updated and user is redirected back to My Account         | Works as expected   |

---

### Add Address Page

| Feature                          | Action                                    | Expected Result                                                          | Works?              |
|----------------------------------|-------------------------------------------|--------------------------------------------------------------------------|---------------------|
| Address form display             | View                                      | Blank address form with required fields visible                          | Works as expected   |
| Save valid address               | Enter valid data + submit                 | Address created and visible in My Account addresses list                 | Works as expected   |
| Missing required field           | Submit with required fields empty         | Validation errors displayed; address not created                         | Works as expected   |
| Set as default flags             | Tick default billing/delivery options     | Flags saved and reflected at checkout address dropdowns                  | Works as expected   |

---

### Edit Address Page

| Feature                          | Action                                      | Expected Result                                                         | Works?              |
|----------------------------------|---------------------------------------------|-------------------------------------------------------------------------|---------------------|
| Load address form                | Visit edit link from My Account             | Form pre-populated with existing address details                        | Works as expected   |
| Save valid changes               | Update fields + submit                      | Address updated and visible in My Account list                          | Works as expected   |
| Delete address link (from profile) | Click delete for an address               | Navigates to delete confirmation or removes address (depending on flow) | Works as expected   |

---

### Wishlist Page

| Feature                     | Action                                 | Expected Result                                                       | Works?              |
|-----------------------------|----------------------------------------|-----------------------------------------------------------------------|---------------------|
| Wishlist list display       | View                                   | Table/list of all products in wishlist is shown                       | Works as expected   |
| Product link                | Click product name                     | Navigates to product detail page                                      | Works as expected   |
| Remove from wishlist        | Click “Remove” button                  | Product removed from wishlist and list refreshes                       | Works as expected   |
| Empty wishlist state        | View with no wishlist items            | “Your wishlist is empty” message shown with button to browse products | Works as expected   |

---

### Basket Page

| Feature                           | Action                                      | Expected Result                                                                      | Works?              |
|-----------------------------------|---------------------------------------------|--------------------------------------------------------------------------------------|---------------------|
| Basket contents display           | View                                        | Table shows each item with name, image, quantity, unit price and line total         | Works as expected   |
| Increase quantity                 | Click + button                              | Quantity increases by 1; line total and basket total update                          | Works as expected   |
| Decrease quantity (>1)            | Click – button                              | Quantity decreases by 1; line total and basket total update                          | Works as expected   |
| Decrease quantity at 1            | Click trash-can variant of – button         | Item removed from basket                                                             | Works as expected   |
| Prevent negative quantity         | Try to enter negative or invalid number     | Quantity is clamped to minimum allowed value (e.g. 0 or 1)                           | Works as expected   |
| Empty basket button               | Click “Empty basket”                        | Confirmation modal opens                                                             | Works as expected   |
| Confirm empty basket              | Confirm in modal                            | All items removed; basket page shows empty state and basket badge shows 0           | Works as expected   |
| Proceed to checkout               | Click “Proceed to Checkout”                 | Navigates to Checkout page                                                           | Works as expected   |
| Empty basket state                | View with no items                          | Message shows that basket is empty with button to continue shopping                  | Works as expected   |

---

### Checkout Page

| Feature                               | Action                                             | Expected Result                                                                             | Works?              |
|---------------------------------------|----------------------------------------------------|---------------------------------------------------------------------------------------------|---------------------|
| Order summary table                   | View                                               | All basket items listed with correct quantity, unit price, subtotal and total               | Works as expected   |
| Free delivery threshold messaging     | Checkout with qualifying total                     | Delivery line shows “Free” where applicable and £0.00 cost                                  | Works as expected   |
| Billing address select                | Open dropdown + choose address                     | Selected billing address is used for order creation                                         | Works as expected   |
| Delivery address select               | Open dropdown + choose address                     | Selected delivery address is used for order creation                                        | Works as expected   |
| No saved addresses                    | Visit checkout with no addresses                   | Informational alert shown with prompt/button to add an address                             | Works as expected   |
| Address info button                   | Click “Info”                                       | Modal opens explaining difference between billing and delivery addresses                    | Works as expected   |
| Back to basket                        | Click “Back to Basket”                             | Navigates back to basket page                                                              | Works as expected   |
| Place order (valid)                   | Click “Place Order” with valid basket + addresses  | Stripe Checkout session created; user redirected to Stripe payment page                    | Works as expected   |
| Empty basket                          | Visit checkout with empty basket                   | Message shown that basket is empty and no order form displayed                             | Works as expected   |

---

### Terms & Conditions Page

| Feature                | Action                          | Expected Result                                          | Works?              |
|------------------------|---------------------------------|----------------------------------------------------------|---------------------|
| Footer link            | Click “Terms & Conditions”      | Navigates to Terms & Conditions page                     | Works as expected   |
| Content display        | Scroll                          | Full T&Cs text visible and readable                      | Works as expected   |
| Back to store button   | Click                           | Navigates to home page                                   | Works as expected   |

---

### Product Management Pages (Store owner / Admin Only)

| Feature                           | Action                                       | Expected Result                                                                | Works?              |
|-----------------------------------|----------------------------------------------|--------------------------------------------------------------------------------|---------------------|
| Admin link                        | Log in as superuser                          | Django admin dashboard loads                                                   | Works as expected   |
| Add product                       | Create new product with category and details | Product appears on products list page with correct category and slug           | Works as expected   |
| Edit product                      | Update product name/description/category     | Changes reflected on products list and detail pages                            | Works as expected   |
| Manage variants                   | Add/edit/delete variants and stock           | Variants available on product detail page; stock levels used by basket checks  | Works as expected   |

---

### Error 404 Page

| Feature                 | Action                                       | Expected Result                                                        | Works?              |
|-------------------------|----------------------------------------------|------------------------------------------------------------------------|---------------------|
| Invalid URL behaviour   | Visit non-existent URL                       | Custom 404 page displayed                                              | Works as expected   |
| 404 page navigation     | Click “Go home or go back buttons            | User navigated safely back to home or back a page                      | Works as expected   |

---

### Email Function Tests

| Feature / Email Type                   | Action                                                        | Expected Result                                                                 | Works?              |
|----------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------------------------|---------------------|
| Registration confirmation email        | Register a new user                                           | Confirmation/verification email received at provided address                    | Works as expected   |
| Password reset email                   | Use “Forgot password” flow                                    | Password reset email received with valid reset link                             | Works as expected   |
| Order confirmation email to user       | Complete a full checkout (successful payment)                 | Order confirmation email received containing order details and total            | Works as expected   |
| Order confirmation email to shop owner | a user has completed a full checkout (successful payment)     | Order confirmation email received containing order details and total            | Works as expected   |
| Newsletter subscription (Mailchimp)    | Submit email via footer form                                  | Mailchimp subscription flow completes and user is added to mail-list            | Works as expected   |

## Automated Testing

Automated tests were written using Django’s built-in test framework.

### How to Run the Tests

From the project root:

```bash
# Run all Django tests
python manage.py test

# Run tests with coverage
coverage run manage.py test

# Generate HTML coverage report
coverage html
```

### Test Coverage

Coverage was measured using the `coverage` package:

- **Overall coverage:** 64%  
- **Applications covered:** `store`, `basket`, `checkout`, `profiles`

<details>
<summary><strong>Click Here</strong> to view screenshots for the coverage reports</summary>

**Terminal coverage summary**

![Coverage Report](/documentation/testing/coverage_report.png)

**HTML coverage index**

![HTML Coverage Report](/documentation/testing/coverage_html.png)
</details>

### Test Summary

The table below summarises the main areas covered by automated tests:

| App       | Area Tested                     | Notes                                    |
|-----------|----------------------------------|------------------------------------------|
| store     | Models, views, URL resolution   | All key model methods and views covered.  |
| basket    | Add/update/remove item logic    | Edge cases for invalid quantities tested. |
| checkout  | Order creation, redirects       | Stripe session created for valid orders.  |
| profiles  | Profile & address creation      | Only logged-in access permitted.          |


## User Stories Testing

All user stories listed in the README were considered during development and testing.  
This section shows how each story was implemented and manually tested, or if it has been left for future development.

Screenshots demonstrating the implementation of each user story can be found in the [README User Stories section](/README.md#user-stories).

### Must Have

| User Story                                                                                                            | Feature or Page                               | Test Description                                                                                                          | Works?             |
|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------    |--------------------|
| As a user, I want to browse products by category so that I can easily find what I’m looking for.                      | Products page - category pills                | Click each category pill on the Products page and confirm that only products from that category are shown.                | Works as expected  |
| As a user, I want to search for products by name/keyword so that I can quickly locate a specific item.                | Products page - search bar                    | Enter a keyword and submit; confirm that the product list is filtered to matching products or shows a no-results message. | Works as expected  |
| As a user, I want to view product details (name, description, price, image) so that I can make an informed decision.  | Product detail page                           | Click “View” on a product card and confirm the page shows name, image, description, price and variant details.            | Works as expected  |
| As a customer, I want to add products to my basket so that I can keep track of what I intend to buy.                  | Product detail page - add to basket           | Choose a variant and quantity, click “Add to Basket”; confirm a success message shows and the basket badge updates.       | Works as expected  |
| As a customer, I can view and update my basket so that I can remove items before checkout.                            | Basket page                                   | Open the basket, change quantities, remove items and empty basket; confirm totals and basket badge update correctly.      | Works as expected  |
| As a customer, I want to register an account and log in so that I can save my details and view my order history.      | Allauth signup/login, My Account, My Orders   | Register a new account, log in, place an order, and confirm that My Account and My Orders display saved data.             | Works as expected  |
| As a customer, I want to checkout securely using Stripe so that I can pay online with confidence.                     | Checkout flow + Stripe Checkout               | Start from a populated basket, go to checkout, then proceed to Stripe test payment page and complete a test payment.      | Works as expected  |
| As a customer, I want to receive order confirmation so that I know my purchase went through.                          | Order confirmation email + success page       | Complete a test order; confirm the on-site success page shows order details and an order confirmation email is received.  | Works as expected  |

---

### Should Have

| User Story                                                                                                       | Feature or Page                                                  | Test Description                                                                                                         | Works?             |
|------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|--------------------|
| As a customer, I want to save my delivery details so that I don’t have to re-enter them each time I order.       | My Account - Addresses, Checkout address dropdowns               | Add one or more addresses in My Account; go to checkout and confirm they are available in the billing/delivery dropdowns.| Works as expected  |
| As a customer, I want to receive email confirmation of my order so that I have a receipt outside of the website. | Order confirmation email                                         | Place a test order and confirm that an order confirmation email is received with order number and summary.               | Works as expected  |
| As a returning customer, I want to view my past orders so that I can reorder items easily.                       | My Orders & Order Detail pages                                   | Log in as a user with orders, visit My Orders, open an order and verify that items and totals are displayed correctly.   | Works as expected  |
| As a store owner, I want to manage products so that I can keep the store up to date.                             | Product Management Page / Admin - Product/Variant/Stock models   | Log in to Django admin, add/edit/delete products and variants; confirm changes appear on the storefront pages.           | Works as expected  |
| As a store owner, I want to receive notifications of new orders so that I can fulfil them quickly.               | Order Email Confirmation to shop owner                           | Store owner receives an email when an order is placed.                                                                   | Works as expected  |

---

### Could Have (Future Development)

| User Story                                                                                                        | Feature or Page / Area                                | Test Description                                                                                          |   Works?                             |
|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|--------------------------------------|
| As a customer, I want to leave reviews on products so that I can share my experience with others.                 | Product reviews                                       | Would allow logged-in customers who purchased a product to leave a rating and review on its page.         | Future enhancement (not implemented) |
| As a customer, I want to filter products (price, popularity, category) so that I can refine my shopping.          | Advanced product filtering                            | Would add additional filters (price range, popularity) alongside existing category filters.               | Future enhancement (not implemented) |
| As a store owner, I want to view basic sales reports so that I can track performance.                             | Admin reporting / dashboard                           | Would provide a simple reporting view of orders, totals and popular products.                             | Future enhancement (not implemented) |
| As a customer, I want to add items to a Wishlist so that I can purchase them later.                               | Wishlist (product detail, My Wishlist, My Account)    | Logged-in users can toggle wishlist on product detail and view/remove items via My Wishlist/My Account.   | Works as expected                    |  
| As a customer, I want to customise pet supplies (e.g. engrave tags) so that I can personalise my order.           | Customisation options                                 | Would add product options for custom text/engraving, applied at checkout and stored with the order.       | Future enhancement (not implemented) |
| As a customer, I want to book grooming appointments online so that I can schedule services as well as products.   | Appointment booking                                   | Would add a booking system for grooming appointments with date/time selection and confirmation.           | Future enhancement (not implemented) |

---

## Lighthouse Testing

Pages were tested using [Google Chrome Lighthouse](https://developers.google.com/web/tools/lighthouse) to assess performance, accessibility, best practices, SEO, and PWA readiness.

### Home Page

![Home Lighthouse Report](/documentation/lighthouse/home_lighthouse.png)

### Products Page

![Products Lighthouse Report](/documentation/lighthouse/products_lighthouse.png)

### Product Detail Page

![Product Detail Lighthouse Report](/documentation/lighthouse/product_detail_lighthouse.png)

### Basket Page

![Basket Lighthouse Report](/documentation/lighthouse/basket_lighthouse.png)

### Checkout Page

![Checkout Lighthouse Report](/documentation/lighthouse/checkout_lighthouse.png)

### My Account Page

![My Account Lighthouse Report](/documentation/lighthouse/account_lighthouse.png)


Overall, scores were consistently high across all categories. Minor accessibility suggestions were already addressed manually, such as ARIA labels and semantic headings. 

Lighthouse raised some advanced security suggestions (CSP, HSTS, Trusted Types). These relate to server configuration rather than the site code.

## Validator Testing

### HTML

All key templates were tested using the [W3C HTML Validator](https://validator.w3.org/). No errors were found.

#### Home Page
<details>
<summary>Click to view validation result (no Errors)</summary>

![Home Page HTML Validation](/documentation/validation/html_home.png)

</details>

#### Products Page
<details>
<summary>Click to view validation result</summary>

![Product Page HTML Validation](/documentation/validation/html_products.png)

</details>

#### Product Detail Page
<details>
<summary>Click to view validation result</summary>

![Product Detail HTML Validation](/documentation/validation/html_product_detail.png)

</details>

#### Basket Page
<details>
<summary>Click to view validation result</summary>

![Basket Page HTML Validation](/documentation/validation/html_basket.png)

</details>

#### Checkout Page
<details>
<summary>Click to view validation result</summary>

![Checkout Page HTML Validation](/documentation/validation/html_checkout.png)

</details>

#### My Account Page
<details>
<summary>Click to view validation result</summary>

![My Account Page HTML Validation](/documentation/validation/html_account.png)

</details>

#### Wishlist Page
<details>
<summary>Click to view validation result</summary>

![Wishlist Page HTML Validation](/documentation/validation/html_wishlist.png)

</details>

#### My Orders Page
<details>
<summary>Click to view validation result</summary>

![My Orders Page HTML Validation](/documentation/validation/html_my_orders.png)

</details>

#### Order Detail Page
<details>
<summary>Click to view validation result</summary>

![Order Detail Page HTML Validation](/documentation/validation/html_order_detail.png)

</details>

#### Checkout Success Page
<details>
<summary>Click to view validation result</summary>

![Checkout Page HTML Validation](/documentation/validation/html_success.png)

</details>

#### Terms & Conditions Page
<details>
<summary>Click to view validation result</summary>

![Terms & Conditions Page HTML Validation](/documentation/validation/html_terms.png)

</details>

#### 404 Page
<details>
<summary>Click to view validation result</summary>

![Error 404 Page HTML Validation](/documentation/validation/html_404.png)

</details>

### CSS Validation

The custom CSS file was tested using the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) and no errors were found.

<details>
<summary>Click to view validation result - No issues</summary>

![CSS Validation Result](/documentation/validation/css_stylesheet.png)

</details>

---

### JavaScript Validation

Custom JavaScript was tested using [JSHint](https://jshint.com/). The following files were validated:

- `base.js`
- `basket.js`
- `product_stock.js`

| File              | Tool    | Result   |
|-------------------|---------|----------|
| `base.js`         | JSHint  | No errors|
| `basket.js`       | JSHint  | No errors|
| `product_stock.js`| JSHint  | No errors|

<details>
<summary><strong>Click Here</strong> to view screenshots for JavaScript validation.</summary>

**Base JS**

![Base.js JSHint Validation](/documentation/validation/js_base.png)

**Basket JS**

![Basket.js JSHint Validation](/documentation/validation/js_basket.png)

**Product Stock JS**

![Product_Stock.js JSHint Validation](/documentation/validation/js_product_stock.png)
</details>

### Python (PEP8)

The Python codebase was validated using the [CI Python Linter](https://pep8ci.herokuapp.com/) provided by Code Institute. All files passed without issues.

| Area / App        | Notes                                      | Status  |
|-------------------|--------------------------------------------|---------|
| `store` app       | models, views, urls, forms, signals        | Passed  |
| `basket` app      | views and helpers                          | Passed  |
| `checkout` app    | models and views                           | Passed  |
| `profiles` app    | models and views                           | Passed  |

## Bugs

The following bugs were discovered and resolved during development and testing:

---

### Bug: Duplicate error messaage when invalid sign in details

**Issue:**  
When user enters an invalid password there are two error messages instead of one.

![Duplicate error message](/documentation/bugs/bug_duplicate.png)

**Solution:**  


![Duplicate solution](/documentation/bugs/bug_duplicate_solution.png)

[See issue #63 for more details.](https://github.com/TheRealMcCall/happy_tails/issues/63)

### Bug: User can add variants with zero stock to basket

**Issue:**  
User is able to add out of stock items to basket.

**Solution:**  

![Zero Stock basket solution](/documentation/bugs/bug_zero_stock_basket_solution.png)

[See issue #56 for more details.](https://github.com/TheRealMcCall/happy_tails/issues/56)


```md
### Known Issues

At the time of final testing, no critical unresolved bugs were identified.
```
---


* [Back To Top](#testing)