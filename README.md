<h1 align="center" id="title"><img src="./budgify/static/images/logo.webp" height="125" alt="Title -  Budgify"></h1>

A simple, yet powerful budgeting app. Create as many budgets as you like for the changing months, seasons and life events, and get insights into your spending.

Budgify was created as my third milestone project for the Code Institutes Level 5 Diploma in Web Application Development.

[View the live project here.](https://budgify-app-a7b562a0c28c.herokuapp.com/)

<img src="./documentation/features/responsivescreenshot.webp" alt="Image of Budgify website on different devices">

## User Experience (UX) 

### User stories

#### First Time Visitor Goals

-   As a first time visitor, I want to easily understand the purpose and features of the Budgify app without any prior knowledge.
-   As a first time visitor, I want to quickly create a new budget and explore the app's functionalities.
-   As a first time visitor, I don't want to be overwhelmed with complex instructions or processes to start using the app.
-   As a first time visitor, I want to be able to contact budgify easily with any issues or questions I have about the app.
-   As a first time visitor I want to be able to register easily and use the app straight away.

#### Returning Visitor Goals

-   As a returning visitor, I want to easily log in to my existing account and access my saved budgets.
-   As a returning visitor, I want to be able to modify or delete existing budgets and view insights on my spending habits.
-   As a returning visitor, I want to be able to modify or delete existing transactions within my budgets.


#### Frequent User Goals
       
-   Frequent would users have similar needs to returning visitors due to the app's straightforward nature.

### Design

#### Colour Scheme
The colour scheme was primarily crafted with a focus on aesthetics and accessibility. Following the contemporary trend observed in web apps, simplicity and minimalism guided the design approach. A notable source of design inspiration for this application was Calendly, known for its clean and uncomplicated design.

Given these considerations, I opted for a white background and mainly utilised colours from the main Bootstrap colour palette. This choice not only aligns with the minimalist design trend but also ensures ease of implementation in various sections by simply applying specific classes such as `primary`, `success`, or `danger`.

-   ##### Colours Used
    - Text colour 1 - `rgba(0, 0, 0, 0.65)`
    - Text colour 2 - `#0d6efd`
    - Background colour - `#ffffff`
    - Button colour 1 - `#0d6efd` / Bootstrap `primary` class
    - Button colour 2 - `#198754` / Bootstrap `success` class
    - Button colour 3 - `#dc3545` / Bootstrap `danger` class
    - Button text colour - `#ffffff`
    - Budget card colour - `rgba(0, 0, 0, 0.45)`

#### Colour Accessibility
			
To ensure the colours chosen met the WCAG 2.1 AA guidelines as minimum and AAA guidelines where possible as with previous projects I used Coolors Contrast Checker which can be found [here](https://coolors.co/contrast-checker/000000-ffffff). However Coolors doesn't support `rgba` so for these colours I used Siege Media which can be found [here](https://www.siegemedia.com/contrast-ratio).

For further information on these guidelines, you can visit the following link. [Web Content Accessibility Guidelines (WCAG) 2.1 (w3.org)](https://www.w3.org/TR/WCAG21/).
        

- ##### Colour Palette and Results
    - Text Colour 1 - [Siege Media Contrast Checker](https://www.siegemedia.com/contrast-ratio#rgba%280%2C%200%2C%200%2C%200.65%29-on-white)<br>
    <img src="./documentation/contrast/text1contrast.webp" alt="Contrast check of main text against white background">  

    - Text Colour 2 - [Coolors Contrast Checker](https://coolors.co/contrast-checker/0d6efd-ffffff)<br>
    <img src="./documentation/contrast/text2contrast.webp" alt="Contrast check of text colour 2 against white background">
  
    - Button Colour 1 - [Coolors Contrast Checker](https://coolors.co/contrast-checker/0d6efd-ffffff)<br>
    <img src="./documentation/contrast/button1contrast.webp" alt="Contrast check of button 1 colour against white background">

    - Button Colour 1 Text - [Coolors Contrast Checker](https://coolors.co/contrast-checker/ffffff-0d6efd)<br>
    <img src="./documentation/contrast/button1textcontrast.webp" alt="Contrast check of white text against button 1 colour">

    - Button Colour 2 - [Coolors Contrast Checker](https://coolors.co/contrast-checker/198754-ffffff)<br>
    <img src="./documentation/contrast/button2contrast.webp" alt="Contrast check of button 2 colour against white background">

    - Button Colour 2 Text - [Coolors Contrast Checker](https://coolors.co/contrast-checker/ffffff-198754)<br>
    <img src="./documentation/contrast/button2textcontrast.webp" alt="Contrast check of white text against button 2 colour">

    - Button Colour 3 - [Coolors Contrast Checker](https://coolors.co/contrast-checker/dc3545-ffffff)<br>
    <img src="./documentation/contrast/button3contrast.webp" alt="Contrast check of button 3 colour against white background">

    - Button Colour 3 Text - [Coolors Contrast Checker](https://coolors.co/contrast-checker/ffffff-dc3545)<br>
    <img src="./documentation/contrast/button3textcontrast.webp" alt="Contrast check of white text against button 3 colour">

    - Budget Card Colour - [Siege Media Contrast Checker](https://www.siegemedia.com/contrast-ratio#rgba%280%2C%200%2C%200%2C%200.45%29-on-white)<br>
    <img src="./documentation/contrast/budgetcardcontrast.webp" alt="Contrast check of budget card colour against white background">
    Passes as AA for large or bold text or graphical objects which this would fall under.


#### Typography
The main considerations for the font were aesthetics and accessibility. I chose the Roboto font as a personal preference as I like the way it looks on the page. It is also a very widely used font developed by Google and is actually used as the default font for the Android operating system, this ensure a fairly wide availability across devises.

 - ##### Fallback Font

    For my fallback font I have opted to stick with the Google recommended fonts when downloading the Roboto font, if no fonts can be found on the user system is will default to the sans-serif family which has many widely used fonts including Arial. Arial is the most widely used font for both online and printed media. Arial is said to be one of the safest web fonts, and is available on all major operating systems.  


#### Imagery

 - ##### Logo
    The Budgify logo was created using Logo.com which can be found [here](https://logo.com/).
    <img src="./budgify/static/images/logo.webp" alt="Budgify Logo">

- ##### Welcome Image
    The welcome image was created by taking screenshots of the main budget table on the website and editing them using Pixlr the website for which can be found [here](https://pixlr.com/)
    <img src="./budgify/static/images/budgettable.webp" alt="Welcome image">

- ##### 404 Image
    The image used on the 404 page was found at Freepiks [here](https://www.freepik.com/free-vector/oops-404-error-with-broken-robot-concept-illustration_8030430.htm#query=404&position=2&from_view=search&track=sph) and was created by storyset.
    <img src="./budgify/static/images/404.webp" alt="404 Image">
<br>

All other imagery on the website are basic icons obtained from Font Awesome which can be found [here](https://fontawesome.com/).


### Wireframes
The wireframes were creates using [Figma](https://www.figma.com/). For most pages there isn't much difference to the layout as the design is very much aimed at mobile first. 

When building the site I deviated slightly from the original wireframes to make the site look less busy on mobile devises, for example instead of adding a button to add or delete a transaction you now simply click on any existing transaction to edit or delete it. 

- ##### Desktop & Tablet Wireframes
<img src="./documentation/wireframes/desktopwireframes1.webp" alt="Website desktop and tablet wireframes">
<img src="./documentation/wireframes/desktopwireframes2.webp" alt="Website desktop and tablet wireframes">

- ##### Mobile Wireframes
<img src="./documentation/wireframes/mobilewireframes.webp" alt="Website mobile wireframes">

### User Journey
The user journey flow charts where created using [Figma](https://www.figma.com/).

- ##### User Journey Key
<img src="./documentation/userjourney/userjourneyskey.webp" alt="User journey flowchart key" height="300">

- ##### User Journey Flow Charts
<img src="./documentation/userjourney/userjourneys1.webp" alt="User journey flowchart 1">
<img src="./documentation/userjourney/userjourneys2.webp" alt="User journey flowchart 2">
<img src="./documentation/userjourney/userjourneys3.webp" alt="User journey flowchart 3">

### Database Schema
The database schema flow charts were created using [Figma](https://www.figma.com/).
<img src="./documentation/dbschema/dbschema.webp" alt="Database schema chart">


[Back to top](#title)  

### Features

-   Fully responsive across all screen sizes.

    -   Laptop / Desktop

    <img src="#" alt="#">

    <img src="#" alt="#">

    <img src="#" alt="#">

    -   Tablet
    <img src="#" alt="#">

    <img src="#" alt="#">

    <img src="#" alt="#">

    -   Mobile
    <img src="#" alt="#">

    <img src="#" alt="#">

    <img src="#" alt="#">

-   Intuitive and easy to navigate using...

    <img src="#" alt="#">

    <img src="#" alt="#">

    <img src="#" alt="#">

### Future Features

-   Feature 1
-   Feature 2
-   Feature 3

### Accessibility
-   The use of semantic HTML.
-   Ensuring the colours and text use meet accessibility standards set by [w3.org](https://www.w3.org/TR/WCAG21/).
-   Ensuring all clickable buttons and links are tabbable using the keyboard.
-   Using descriptive alt tags on all images.
-   Using correct aria labels where necessary.
-   Being mindful in the creation of the design to ensure it is intuitive and as easy to navigate as possible.



[Back to top](#title)  

## Technologies Used

### Languages Used
-   HTML
-   CSS
-   Vanilla javaScript
-   Python

### Frameworks, Libraries & Programs Used

-   [Bootstrap](https://getbootstrap.com/) Version 5.3.0 - For the layout and framework of the website, it was also used to create the various modals which were then restyled to match the rest of the website.


[Back to top](#title)  

## Testing

Please see [TESTING.md](TESTING.md) for all testing performed


## Deployment

### Heroku

The project was deployed to Heroku using the following steps...

1. Step 1
1. Step 2

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Login to GitHub.
2. Locate the repository, you can use a link you have been provided with or use the search function in the top left of the screen.
3. In the top right hand corner of the page locate and click the 'fork' button.
4. Near the bottom of the page click the green button that says 'Create Fork'.
5. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Login to GitHub.
2. Locate the repository, you can use a link you have been provided with or use the search function in the top left of the screen.
3. Near the top of the repository click the green 'Code' button.
4. To clone the repository using HTTPS, under HTTPS copy the link provided.
5. Open the terminal in your code editor. 
6. Change the current working directory to the location where you want the cloned directory to be made.
7. Type git clone, and then paste the URL you copied in Step 3.
8. Press Enter. Your local clone should be created.

[Back to top](#title)  

## Credits

### Code

-   Social Media Integration for Facebook, LinkedIn & Google - Code from [Abi Harrison Meta Tags Webinar](https://www.youtube.com/watch?v=t-4qqmikIqk).

All other code was written by the developer.

### Content

-   Static content for this website was all written by the developer.
 

### Media

-   Logo - The logo was created using...

### Acknowledgements

...

[Back to top](#title)  