<h1>Weather Checker</h1>

Maybe it's a business trip or a vacation trip or a picnic trip, if you are traveling somewhere and want to know the weather forecast of your destination. Weather Checker will help you. What's more, you can send this information to your email address or a friend's email address!

All you have to do is specify the locations you want to go to. Weather Checker will do everything else for you with its user-friendly screens. The locations you want to go to are easily and safely determined thanks to the Google Maps infrastructure. You get real information thanks to Openweather api support. 

<h1 style="color:red;"> Live link here</h1>

<img src="docs/images/welcome.webp" alt="Welcome Screen">

<h2> How to Use </h2>

<ul>
<li>The user must have an email address to receive reports.</li>
<li>The user needs to set the targets (latitude and longitude).</li>
<li>The user must specify the date of departure.</li>
</ul>

<h2>Site Owners Goal</h2>

<ul>
<li>To enable its users to easily access the information they want.</li>
<li>Providing users with an easy-to-use application.</li>
</ul>

<h2>User Benefits</h2>

This program significantly simplifies travel planning for users. They can better plan their travel dates and destinations by getting weather information while determining the route they will travel. In this way, they can take precautions against adverse weather conditions they may encounter while traveling and make their travel experience more enjoyable.

In addition, this program helps users determine their travel routes. Users can identify the cities they want to visit and the activities they will do in those cities. Using weather information, they can plan which activities are more suitable for the dates they will be traveling and what kind of clothes they should wear.

The program helps users save time and resources. They can create their travel routes on a single platform, without the need for external weather apps or websites. This allows users to make travel plans more efficiently and prevents unnecessary time wastage.

Users receive personalized services through the program. They can easily manage their travel plans by receiving travel route and weather information via email. This helps users keep their travel plans updated and makes their travel experience smoother.

<h2>Logic Flow</h2>

Starting to design my project with a flowchart has helped me a lot. First, these diagrams helped me understand my code better and simplify complex logic. The flow of logic with visually represented figures helped me to see the operations more clearly and better understand how the code works. Secondly, the flowcharts made it easier for me to identify potential error points and get through the debugging process more easily.

**There may be some differences because I drew the flowchart before I started my project.**

<img src="docs/images/charts.webp" alt="Weather Checker Flow Charts">

## Features

### Welcome Section

When the user enters the application they are greeted with a very simple page welcoming them to the game and asking them for their name. The welcome text was created using Pyfiglet which takes ASCII text and renders it into ASCII art fonts.

<img src="docs/images/welcome.webp" alt="Introduction">

### Name Validation

User name entry has strong data validation. The user cannot enter a name with numbers or spaces in it. If they do not enter valid data, the message "Please enter valid name (only alpha characters) and one word!" is displayed.   

<img src="docs/images/name_validation.webp" alt="Name Validation">

### Email Validation

Once the user has entered their name correctly, they are asked to enter their email address.

<img src="docs/images/email.webp" alt="Email Enter">

The email address entered by the user is checked with a regex structure. In case the mail expression is incorrect, the user will be asked to enter this data again.

<img src="docs/images/email_validation.webp" alt="Email Validation">

When you enter your name and email address correctly, the user object will be created and then it will continue its process. 

### Maps Help Section

After the user has provided the required information, he/she has to report his/her location in order to get the weather information of the destination, which is the main purpose of the program. If he/she does not have this information, we provide information on how to access this information. If he indicates that he would like to get help: 

<img src="docs/images/maps_tip.webp" alt="Maps Tip">

If the user asks for help, an explanation of how to use the Google Maps service and a link to help will be displayed.

<img src="docs/images/help_screen.webp" alt="Maps Tip">

### Add location

If the user does not ask for help, the program will ask how many cities they would like to receive a report about.

<img src="docs/images/no_help.webp" alt="Maps Tip">

At this point we expect our user to specify how many cities to add with a number. And of course we need to check the entered expression. If it is entered incorrectly: 

<img src="docs/images/loc_val.webp" alt="Location Validation">

As many locations as the user enters, it is requested to enter latitude and longitude information first, respectively.

<img src="docs/images/lat_long_enter.webp" alt="Latitude longitude enter">

The entered coordinate information is queried with the api service of Geopy service and the registered address information is displayed to the user.

<img src="docs/images/lat_long_validation.webp" alt="Latitude longitude validation">

If the user thinks that the address information is incorrect, he/she can type N and re-enter the information or Y to continue the program execution. If the user has specified that he/she wants to go to more than one location, the coordinate information of all cities and the date to be traveled are asked on this screen. 






isalpha -> https://www.codecademy.com/resources/docs/python/strings/isalpha

regex -> fullmatch -> https://www.geeksforgeeks.org/re-fullmatch-function-in-python/


GeoLocation -> geopy 2.4.1  https://pypi.org/project/geopy/

Adresler ülkelere göre farkliliklar gösterdigi icin adresler tam olarak gösterilmektedir.

city name -> https://www.geeksforgeeks.org/get-the-city-state-and-country-names-from-latitude-and-longitude-using-python/