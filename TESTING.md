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
Responsiveness was also demonstrated using short video recordings of real device testing:

- [Google Pixel 8 Pro – Portrait Test](https://drive.google.com/file/d/10eUMt4fQAiNPTXftHLw7Ml7OJQt9P0Wp/view?usp=drive_link)  
- [Google Pixel 8 Pro – Landscape Test](https://drive.google.com/file/d/1Q2A0s3Khq_xtYin5kUAfGEvWzmfDBPma/view?usp=drive_link)

All navigation menus, forms, buttons, summaries, and tables were confirmed to be usable at small screen widths. The layout adapts seamlessly.

## Manual Testing

Thorough manual testing was done for all critical user interactions across pages.

### Global Navigation

| Feature        | Action | Expected Result                                                                          | Works?              |
|----------------|--------|------------------------------------------------------------------------------------------|---------------------|
| Brand Name     | Click  | Goes to homepage                                                                         | Works as expected   |

### Home Page

| Feature           | Action    | Expected Result                       | Works?              |
|-------------------|-----------|---------------------------------------|---------------------|
| Introduction Text | View      | Clear site intro                      | Works as expected   |

### Login Page

| Feature         | Action              | Expected Result                                      | Works?             |
|-----------------|---------------------|------------------------------------------------------|---------------------|
| Login form      | View                | Form is visible with username/email and password fields | Works as expected   |

### Logout Page

| Feature                    | Action     | Expected Result                                        | Works?              |
|----------------------------|------------|--------------------------------------------------------|---------------------|

### Register Page

| Feature             | Action                  | Expected Result                                         | Works?             |
|---------------------|-------------------------|---------------------------------------------------------|---------------------|
| Register form       | View                    | Form with required fields (username, email, password) is visible | Works as expected   |


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

### Test Coverage

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

![Home Lighthouse Report]()

### Products Page

![Products Lighthouse Report]()

### Product Detail Page

![Product Detail Lighthouse Report]()

### Basket Page

![Basket Lighthouse Report]()

### Checkout Page

![Checkout Lighthouse Report]()

Overall, scores were consistently high across all categories. Minor accessibility suggestions were already addressed manually, such as ARIA labels and semantic headings.

## Validator Testing

### HTML

All key templates were tested using the [W3C HTML Validator](https://validator.w3.org/).

#### Home Page
<details>
<summary>Click to view validation result (no Errors)</summary>

</details>

#### Products Page
<details>
<summary>Click to view validation result</summary>

</details>

#### Product Detail Page
<details>
<summary>Click to view validation result</summary>

</details>

#### Basket Page
<details>
<summary>Click to view validation result</summary>

</details>

#### Checkout Page
<details>
<summary>Click to view validation result</summary>

</details>

#### Profile Page
<details>
<summary>Click to view validation result</summary>

</details>

#### Wishlist Page
<details>
<summary>Click to view validation result</summary>

</details>

#### My Orders Page
<details>
<summary>Click to view validation result</summary>

</details>

#### Order Detail Page
<details>
<summary>Click to view validation result</summary>

</details>

#### Checkout Success Page
<details>
<summary>Click to view validation result</summary>

</details>

#### Terms & Conditions Page
<details>
<summary>Click to view validation result</summary>

</details>

#### 404 Page
<details>
<summary>Click to view validation result</summary>

</details>

### CSS Validation

The custom CSS file was tested using the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) and no errors were found.

<details>
<summary>Click to view validation result - No issues</summary>

![CSS Validation Result]()

</details>

---

### JavaScript Validation

Custom JavaScript was tested using [JSHint](https://jshint.com/). The following files were validated:

- `base.js`
- `basket.js`
- `product_stock.js`

| File              | Tool    | Result |
|-------------------|---------|--------|
| `base.js`         | JSHint  |        |
| `basket.js`       | JSHint  |        |
| `product_stock.js`| JSHint  |        |

### Python (PEP8)

The Python codebase was validated using the [CI Python Linter](https://pep8ci.herokuapp.com/) provided by Code Institute. All files passed without issues. 

## Bugs

The following bugs were discovered and resolved during development and testing:

---


* [Back To Top](#testing)