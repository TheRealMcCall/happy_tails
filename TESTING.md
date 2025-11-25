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

![Chrome Screenshot](/documentation/compatability/chrome.png)

</details>

<details>
<summary>Click here to view Firefox screenshot - <strong>Working as Expected</strong></summary>

![Firefox Screenshot](/documentation/compatability/firefox.png)

</details>

<details>
<summary>Click here to view Edge screenshot - <strong>Working as Expected</strong></summary>

![Edge Screenshot](/documentation/compatability/edge.png)

</details>

<details>
<summary>Click here to view Opera screenshot - <strong>Working as Expected</strong></summary>

![Opera Screenshot](/documentation/compatability/opera.png)

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
Responsiveness was also demonstrated using a short video recordings of real device testing:

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

| Feature                    | Action     | Expected Result                                        | Works?              |
|----------------------------|------------|--------------------------------------------------------|---------------------|
| View Product List Grid     | View       | Displays a grid of available products                  | Works as expected   |

### Products Details Page

| Feature                    | Action     | Expected Result                                        | Works?              |
|----------------------------|------------|--------------------------------------------------------|---------------------|

### My Account Page

| Feature                    | Action     | Expected Result                                        | Works?              |
|----------------------------|------------|--------------------------------------------------------|---------------------|

### My Orders Page

| Feature                    | Action     | Expected Result                                        | Works?              |
|----------------------------|------------|--------------------------------------------------------|---------------------|

### Edit Profile Page

| Feature                    | Action     | Expected Result                                        | Works?              |
|----------------------------|------------|--------------------------------------------------------|---------------------|

### Add Address Page

| Feature                    | Action     | Expected Result                                        | Works?              |
|----------------------------|------------|--------------------------------------------------------|---------------------|

### Edit Address Page

| Feature                    | Action     | Expected Result                                        | Works?              |
|----------------------------|------------|--------------------------------------------------------|---------------------|

### Wishlist Page

| Feature                    | Action     | Expected Result                                        | Works?              |
|----------------------------|------------|--------------------------------------------------------|---------------------|

### Basket Page

| Feature         | Action           | Expected Result                     | Works?              |
|-----------------|------------------|-------------------------------------|---------------------|

---

### Checkout Page

| Feature                    | Action     | Expected Result                                        | Works?              |
|----------------------------|------------|--------------------------------------------------------|---------------------|

### Terms & Conditions Page

| Feature                    | Action     | Expected Result                                        | Works?              |
|----------------------------|------------|--------------------------------------------------------|---------------------|

### Product Management Pages (Store owner / Admin Only)

| Feature                    | Action     | Expected Result                                        | Works?              |
|----------------------------|------------|--------------------------------------------------------|---------------------|

### Error 404 Page

| Feature                    | Action     | Expected Result                                        | Works?              |
|----------------------------|------------|--------------------------------------------------------|---------------------|

### Email function tests

| Feature                    | Action     | Expected Result                                        | Works?              |
|----------------------------|------------|--------------------------------------------------------|---------------------|

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

All key user stories were implemented and tested. Screenshots demonstrating the implementation of each user story can be found in the [README User Stories section](/README.md#user-stories).

### Must Have

| User Story                                                                 | Feature or Page           | Test Description                                                                 | Works?             |
|----------------------------------------------------------------------------|----------------------------|----------------------------------------------------------------------------------|---------------------|


### Should Have

| User Story                                                                 | Feature or Page           | Test Description                                                                 | Works?             |
|----------------------------------------------------------------------------|----------------------------|----------------------------------------------------------------------------------|---------------------|

### Could Have (Future Development)

| User Story                                                                 | Feature or Page           | Test Description                                                                 | Works?             |
|----------------------------------------------------------------------------|----------------------------|----------------------------------------------------------------------------------|---------------------|

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

![Checkout Page HTML Validation](/documentation/validation/html_checkout.png)

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

![Coverage Report](/documentation/validation/js_base.png)

**Basket JS**

![HTML Coverage Report](/documentation/validation/js_basket.png)

**Product Stock JS**

![HTML Coverage Report](/documentation/validation/js_product_stock.png)
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


* [Back To Top](#testing)