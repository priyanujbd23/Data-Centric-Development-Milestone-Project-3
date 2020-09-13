
# CityCabs Agency

CityCabs Agency is a small but reliable cab service. The project is inspired by the cabby service concept. Users can book cabs 
for different destinations nationwide. 

There's also opportunity for new drivrs to join the company by signing up and adding their vehiclesas part of the collection. Services range from city tours, to out of town escurtions, from airport service to camper vans for those who wish to go aay on holidays.
we try to put some emphasis in our drivers who join our company. That way, set forth our reputation as being a reputable company.
The site contains basic information for anyone who wants to book a cab or drive for a cab agency and be their own boss.


## UX

This project is for anyone who mihgt need to book a cab for different servces. Salad. Owing to the busy schedules people often have, 

The site is comprised of seven main sections. Each of these section is made up of sub sctions which are the pages for the website.
These consists primarily of Cab, Brands,, Models, Types, Bookings, Users and Admin sections.

The Home page contains information about the services on offer.
The navigation bar contains the following links:
 Cabs - here users can see all availabe cabs which they can click and book.
 Book Cab - users can book a cab directly using this link.
 View Booking - users can view booked cabs. 
 Log In -  registered users can login to the cab agency
 Sign Up - new users can sign up here . 

For consistency of user experience the site's logo, navigation links and social
media links on the page footer are repeated across the site's pages. The design and layout is also consistent when viewed on desktop, tablet or mobile
devices. The use of Materialize enables the site elements to rearrange themselves according to the current browser screen width in use.

- As a user I want to book a cab for a particular destination or a city tour
- By registering as a member, I can submit or add my on vehicle to the collection a d drive for CityCabs.

- As a user I want to be able to visit or discover new and interesting destinations
  - As a user I want to book a cab for a destinations based on the services on the home page
  - As a user I want to be recommended services based on my requests.
  
- As a user I want to register to a website that gives me the opportunity to work as a cab driver and add my own vehicle 
  - As a user  i want to be able to add a specific vehicle type, brand and model 
  - As a user I want to able to explore a variety of added vehicles

- As a user I want to be able to create an experience by actually taking part in a driver program
  - As a user I want to be recommended administrative options to add and edit cabs and bookings 
  - As a user I want to be able to browse through the cars and bookings sections 
  
- Link to Mockups 
  - assets/mockup/User Centric MileStone  Project 1.pdf
  - assets/mockup/User Centric MileStone  Project 1- Smartphone.pdf

- website
  - https://dop-dd.github.io/User-Centric-MileStone-Project-1/index.html


## Demo 

- Screen shot
  - ![Image of website](/assets/img/website-demo.png) 


## Features

The website is made up of 23 pages. 
-Navigation:
  -The website is easy to navigate through the various pages. The navigation is fixed to the top and is consistent on all web pages.
- Visuals: 
  -The pictures are inserted into materialize cards clear and properly described
- Cabs page:
  -Users can use the cabs link to view all available cabs.
  -Users can search for a cab randomly using the search form
- Book Cab page:
  -Users can use the book cabs link to book a cab directl. Users cannot change the vehicle, brand or model type. 
  -They're offered a selction to choose from.  
- View Bookings page:
  -Users can use the this link to view all booked cabs. These booked cars are no longer avalable on the cabs page for booking.
  -Users can search for a booked cab by type or model using the search form
- Log In page:
  -Registered users can log in. Once logged in, they get a flash message informing them with their username when thy're logged in.
  -They get a welcome message with a link to the admin section.
- Register page:
  -New users can use this link to register for membership.
- Admin:
  -The admin section offers four options
- Add Type:
  -Users can add a vehicle type. Vehicle types include Sedan, Station Wagon, Van, etc.
- Add Brand:
  -Users can add a vehicle brand. Vehicle brands include Fiat, Nissan, Renault, etc.
- Add Model:
  -Users can add a vehicle model. Vehicle types include Sedan, Station Wagon, Van, etc.
- Add Cab:
  -Users can add a cab. Their admin privileges give them the options to add a type, brand or model of their choice.
  -The added cab gets diplayed on the cabs page among existing cabs.
- MongoDB:
  -Users can store their selection in the database. The database has records for cabs, types, brands, models and users. 
- Responsiveness:
  -The website is developed with the notion of mobile-first and is thus, fully reponsible.
- The website is intuitive and the content is relevant 
-Social Media icons
  -These extend the site's functonality. Users can visit a social media website by clicking onthe appropriate icon  
  
### Existing Features

- Cabs page- User can browse through and choose between different vehicle types and models. 
- Add Booking page- User can book a cab by filling in their information ans slecting a cab. 
- Log in form- A registered user can log in to the admin section 
- Sign up form- A user can sign up fo a free membership by filling in the form on the sign up page.
- Bookings page- User can browse through to find if a particular vehicle has been booked or not. 
- Search form- Users can search for available or booked cabs 
- MongoDB- Users records are stored in the database. cab pictures can be added via url links and inserted in the template on cabs page

### Features left to implement

At the moment the site lacks email confirmationIn. Users who booked a cab are not currently informed about their booking by email.
Confirmation is given to the users via phone. Implementation of this feature is currently in process. 
 
## Technology used
This projet is built using HTML, CSS, Javascript, jQuery and Materialize

- HTML 
  - Html is used the defacto language for the web pages
  - Link: https://www.w3schools.com/html/default.asp
  
- CSS
  - CSS is implemented for styling and layout.
  - Link: https://www.w3schools.com/css/default.asp
    
- Materialize
  - Bootstrap is to make this website responsive and mobile-first websites. Theframework includes HTML and CSS based design templates to help design websites faster and easier. It The Header, Body and Footer are all in Bootstrap containers which creates a very responsive effect on the entire website.
    Link: https://materializecss.com/
  
- MongoDB
  -This is the Database used to store users, vehicle types, models and bookings
  - Link: https://www.mongodb.com/

- jQuery
  - https://jquery.com/
  
## Testing

1. Site Navifation:
   1. from home page navigate to the other pages on the website. The link s work as intended.
   2. clicking on the logo brings you to the home page.

2. Video:
   1. click on the video. It plays on small and full screen sizes. 

3. cover text(Fresh Salad for all):
   1. Open this website on mobile version. This content is set to hide on small screens less than 763px

4. Contact Form:
   1. Go to the "Contact" page
   2. Submit empty form and verify that an error message about the required fields appears
   3. Submit the form with an invalid email and see a message asking you to fill the inromation in the required fields 
   4. Try to click on the map. It opens up in a new tab allowing you to search for a location directly from this website
  
5. Sign up Form:
   1. Go to the "Sign Up" page
   2. Submit empty form and verify that an error message about the required fields appears
   3. Submit the form with an invalid email and see a message asking you to fill the inromation in the required fields 
   4. Try to submit a form by clicking on the social medial icons. They open in separate tabs aalowing you to sign up.

6. Sign up Form:
   1. Go to the "Sign Up" page
 
7. Social Media icons:
   1. Go to the footer section at the bottom of each page
   2. Try clicking on any social icons. They each open in separate tabs 
 
8. Tablets and mobiles:
    1. The website is optimized for mobile viewing. The media queries display the pages correctly.
    2. Try running the page in mobile mode and see how it correctly fits to the size of the screen 
  

## Deployment

The code consist of static website developed using HTML, CSS and Bootstrap. This code does not contain any executable file. The website is hosted
using Github pages. This can be located via:
   - Settings tab on the repository page
   - Github pages
   - Under Github pages select source and choose master branch. This will then use the mastr branch for the Github pages

## Credits

### Content

- Tips for the main-content rows and colums of the home page was taken and edited from:
  - https://websitesetup.org/bootstrap-tutorial-for-beginners/
  
- The code for the contact form was taken and edited from:
  - https://www.w3schools.com/bootstrap4/bootstrap_navbar.asp
  
- The code fpr the Map was taken from:
  - https://www.maps.ie/create-google-map/
  
- The code for the sign up form was taken and edited from: 
  - https://mdbootstrap.com/docs/jquery/forms/basic/?#!
  
### Media
  
- The video was taken from:
  - https://www.pexels.com/video/a-person-tossing-a-vegetable-salad-in-a-bowl-3189049/
  
- The images were taken from the royalty free website at:
  - https://www.pexels.com/search/eating/ 

### Acknowledgements
- I received inspiration for this project from the Love Running project.