# Budgify -  Testing

<img src="./documentation/features/responsivescreenshot.webp" alt="Image of Budgify website on different devices">

[View the live project here.](https://budgify-app-a7b562a0c28c.herokuapp.com/)


Extensive testing was carried out throughout the life cycle of this project. As well as all of the documented testing below I asked friends and family to use the site and tell me what was and wasn't working. I worked through the game click and checking each feature and function by one and looked for anything that wasn't working or that was logging an error in the console. 

Had I given myself more time I would have liked to have implemented some automated testing using Jest and is certainly something I will look to implement in future projects. 

In practice and for production code a combination of both manual and automated testing is important. Automated testing can provide fast results especially across large applications whilst manual testing adds the human element and is more adept at spotting things like intuitiveness of the design. Utilising both can ensure high levels of quality and reliability of web applications.


## AUTOMATED TESTING

#### HTML Validator - [W3C](https://validator.w3.org/)

| Page | Errors/Warnings | Solution | Image |
| --- | --- | --- | --- |
| Welcome Page | Warning: Section lacks h2-h6 heading. | There is little use for a h2 element on this page, however a section element is still more semantically correct so ignored this warning. | <img src="./documentation/validators/html/welcome.webp" alt="HTML validator results for welcome page"> |
| Login Page | Warning: Section lacks h2-h6 heading. | Due to the design structure of this page again a h2 header isn't warranted however it is still more semantically correct to keep the section element instead of a DIV. | <img src="./documentation/validators/html/login.webp" alt="HTML validator results for login page"> |
| Register Page | Warning: Section lacks h2-h6 heading. | Due to the design structure of this page again a h2 header isn't warranted however it is still more semantically correct to keep the section element instead of a DIV. | <img src="./documentation/validators/html/register.webp" alt="HTML validator results for register page"> |
| Budget Page | N/A | N/A | <img src="./documentation/validators/html/budget.webp" alt="HTML validator results for budget page"> |
| Budgets Page | Warning: Section lacks h2-h6 heading. | Due to the design structure of this page h2 header falls outside of the section element on this page. It would still be semantically correct to keep the section element instead of a DIV. | <img src="./documentation/validators/html/budgets.webp" alt="HTML validator results for budgets page"> |
| Profile Page | N/A | N/A | <img src="./documentation/validators/html/profile.webp" alt="HTML validator results for profile page"> |
| 404 Page | N/A | N/A | <img src="./documentation/validators/html/404page.webp" alt="HTML validator results for 404 page"> |


#### CSS Validator - [W3C](https://jigsaw.w3.org/css-validator/)

| File | Errors/Warnings | Solution | Image |
| --- | --- | --- | --- |
| styles.css | N/A | N/A | <img src="./documentation/validators/css/styles.webp" alt="CSS validator results for styles.css"> |

### JavaScript Validator

#### JSHint Validator - [JSHint](https://jshint.com/)

| File | Errors/Warnings | Solution | Image |
| --- | --- | --- | --- |
| 404.js | N/A | N/A | <img src="./documentation/validators/js/404.webp" alt="JS validator results for 404.js"> |
| add-budget.js | N/A | N/A | <img src="./documentation/validators/js/add-budget.webp" alt="JS validator results for add-budget.js"> |
| budget.js | 1. Do no user 'new' for side effects. 2. Undefined variable - Chart | Both errors are side effects of using the ChartJS library and how they are implemented and not something I can change, so ignored. | <img src="./documentation/validators/js/budget.webp" alt="JS validator results for budget.js"> |
| confirmpwd.js | N/A | N/A | <img src="./documentation/validators/js/confirmpwd.webp" alt="JS validator results for confirmpwd.js"> |
| support.js | Undefined variables - emailjs & sendMail| Both errors are side effects of using the EmailJS service and how they are implemented and not something I can change, so ignored. | <img src="./documentation/validators/js/support.webp" alt="JS validator results for support.js"> |

### Python Validator - [Code Institute Python Linter](https://pep8ci.herokuapp.com/) 

#### Python Validator?? - [#](#)

| File | Errors/Warnings | Solution | Image |
| --- | --- | --- | --- |
| __ init __.py| Module level import not at top of file. | The reason this is being imported last, is because the 'routes' file will rely on using the 'app' and 'db' variables defined above. If we try to import routes before 'app' and 'db' are defined, then we'll get circular-import errors. So I have ignored this error| <img src="./documentation/validators/python/init.webp" alt="Python validator results for __init__.py"> |
| models.py | N/A | N/A | <img src="./documentation/validators/python/models.webp" alt="Python validator results for models.py"> |
| routes.py | N/A | N/A | <img src="./documentation/validators/python/routes.webp" alt="Python validator results for routes.py"> |
| run.py | N/A | N/A | <img src="./documentation/validators/python/run.webp" alt="Python validator results for run.py"> |

### Lighthouse

I used Lighthouse within the Chrome Developer Tools to test the performance, accessibility, best practices and SEO of the website. 

#### Desktop Results

- ##### Homepage

<img src="#" alt="#">

## MANUAL TESTING

### Testing User Stories

| Goals | How are they achieved? | Image |
| --- | --- | --- |
|  |  |  |

### Devices Used For Testing

The site has altogether in one way or another been used and tested on the following devices...

-   Google Pixel 7 - Chrome
-   HP Elitebook (Windows) - Chrome, Edge and Firefox
-   Iphone SE - Safari and Chrome
-   Ipad - Safari and Chrome
-   Macbook Pro - Safari and Chrome
-   Samsung Galaxy Tab S7 - Chrome and Samsung Browser
-   Samsung S23 Ultra - Edge, Chrome, Firefox and Samsung Browser

### Full Manual Testing

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## BUGS

### Solved Bugs

| No. | Bug | How I solved the issue |
| --- | --- | --- |
|  |  |  |

### Unsolved Bugs

| No | Bug | |
| --- | --- | --- |
|  |  |  |