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
| Login Page | Warning: Section lacks h2-h6 heading. | Due to the design structure of this page again a h2 header isn't warranted however it is still more semantically correct to keep the section element instead of a DIV. | <img src="./documentation/validators/html/login.webp" alt="HTML validator results for welcome page"> |
| Register Page | Warning: Section lacks h2-h6 heading. | Due to the design structure of this page again a h2 header isn't warranted however it is still more semantically correct to keep the section element instead of a DIV. | <img src="./documentation/validators/html/register.webp" alt="HTML validator results for welcome page"> |
| Budget Page | N/A | N/A | <img src="./documentation/validators/html/budget.webp" alt="HTML validator results for welcome page"> |
| Budgets Page | Warning: Section lacks h2-h6 heading. | Due to the design structure of this page h2 header falls outside of the section element on this page. It would still be semantically correct to keep the section element instead of a DIV. | <img src="./documentation/validators/html/budgets.webp" alt="HTML validator results for welcome page"> |
| Profile Page | N/A | N/A | <img src="./documentation/validators/html/profile.webp" alt="HTML validator results for welcome page"> |
| 404 Page | N/A | N/A | <img src="./documentation/validators/html/404page.webp" alt="HTML validator results for welcome page"> |


#### CSS Validator - [W3C](https://jigsaw.w3.org/css-validator/)

- ##### styles.css

<img src="#" alt="#">

### JavaScript Validator

#### JSHint Validator - [JSHint](https://jshint.com/)

- ##### script.js

<img src="#" alt="#">

### Python Validator

#### Python Validator?? - [#](#)

- ##### run.py

<img src="#" alt="#">

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