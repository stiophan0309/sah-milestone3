## Steven A. Horne - Web Designer & Full Stack Web Developer

developed by Steven A. Horne

---


The site is the personal portfolio and blog of a web developer and designer.  The site will display information about the the author's skills, education and read their blog page as well as contact them.

The main goals of the site are: 

* Build an online prescence and promote the developer's services/brand
* Encourage people to use the Contact Page with enquiries
* Simple and clear UX for users to navigate
* Provide a blog to share the developer's experiences

---

## UX

The site is intended for anyone who is interested in web design/development and/or those who are looking for assistance with a project/site.

The site is designed with a simple approach in mind and is easy to use and navigate. 


### Admin section

The Admin section can ONLY be accessed by adding **/admin** at the end on the url.  This is to prevent access to unauthorised users.
In the Admin section, adminstrators can create, edit and delete posts in the Blog.

---

## User Stories

* As a user I want to be able to see the developer's skills and/or work.
* As a user I want to be able to visit their website and be able to easily navigate arount and be able to contact the developer.
* As a user I want to be able to see if their own site is professionally designed and easy to use.
* As a user customer I want fo find out information about the developer.
* As a web developer I want to compare the developer's site to my own.
* As a web developer I want to see what the site offers and if it offers anything different.
* As an administrator I want to be able to access the Blog Admin page and be able to create, delete and update blog posts

---

## Wireframes

Wireframe mockups can be found [here](/wireframes)

---

## Features

### Existing Features

The site is navigated by means of the Navbar from where all pages can be accessed and it remains at the top of the page when scrolling.  The user can return to the Home page by either clicking/pressing the Home link of the House icon.

The Education page utilises a timeline to visually show education/employment history and other milestones.

The Experience page displays a list of icons of various technologies/software which the developer has experience.  The user can click each icon which will open a modal popup displaying the number of years of experience and some information about the relevant item.

The Contact page has a simple form the user can contact the developer.

The Blog page shows the developer's stories and experiences. The user can expand each story by means of a button on each post.

The site utilises the CRUD (Create, Read, Update, Delete) in the Blog section. 

### Features to implement

The need or a seperate login facility for administrators is the main requirement outstanding.

---

## Technologies

The site uses the following technologies:

* **HTML5** - Used to structure the site
* **CSS3** - Used to provide styling and visual appearance
* **Bootstrap** - Provides a responsive layout to work across different screen sizes and devices
* **Javascript** - Used to provide user interactivity such as the Contact form
* **Python** - Python is in the background and powers the site
* **Flask** - Used to provide templates to talk to Python
* **Jinja** - Used to provide templating features
* **TinyMCE** - Used to provide WYSIWIG text for creating posts in the Blog
* **EmailJS** - 3rd Party email client enables an email facility without going through a server
* **DevIcons** - Icon library used in the Experience page for the technology icons
* **jQuery** - Used as part of **Bootstrap** to provide some functionality in the Navbar

---

## Testing

Throughout the the development process the testing was done manually including:

* Tesing responsiveness on different devices and browsers
* Checked DevTools for errors and API responses and requests
* Used the MongoDB GUI to check database to make sure entries were added/deleted/updated
* Checked EmailJS GUI to check if emails were being sent OK
* Got family members to check their devices if they could access use the deployed app

---

## Deployment

The development site is located on my GitHub site at:

https://github.com/stiophan0309/sah-milestone3

The live site is deployed to Heroku at:

https://sah-milestone3.herokuapp.com/

---

## Credits

The Timeline on the Education Page was sourced from W3C schools.  [Link](https://www.w3schools.com/howto/howto_css_timeline.asp "here")

---

## Media

The front page image is property of the developer.
The portrait of me in the About page was taken by John Maxwell.