The objective of this webpage is to provide users with a way to search for their favourite movies, movies that they might be interested in or movies that they have been recommended, read the reviews of others or leave a review of their own, they should also be able to delete that review or edit it afterwards.

## UX

The website is aimed at people of any age who have an interest in movies of any genre who would like to read the reviews of others to see if they might like the movie or to leave reviews for others to read. 

### User Stories

#### User who would like to read reviews to see if they like the sound of a movie
As someone who enjoys watching movies, I would like to search for a movie that I have heard of, read something about it and also read what other people who have already watched it think.

#### User who has watched a movie and would like to give their opinion of that movie
As someone who has recently watched a movie, I would like to leave a review of that movie so that others can make an informed choice as the weather they want to watch it or not.

### Wireframes

Below are my first drafted ideas of how the web app would look and work, these were originally made using Balsamiq Mock-ups.

- [Home page for Desktop](wireframes/Index.html_Desktop.png)
- [Home page for Tablet](wireframes/Index.html_Tablet.png)
- [Home page for Mobile](wireframes/Index.html_Mobile.png)
- [Registration page for Desktop](wireframes/Register.html_Desktop.png)
- [Registration page for Tablet](wireframes/Register.html_Tablet.png)
- [Registration page for Mobile](wireframes/Register.html_Mobile.png)
- [Login page for Desktop](wireframes/Login.html_Desktop.png)
- [Login page for Tablet](wireframes/Login.html_Tablet.png)
- [Login page for Mobile](wireframes/login.html_Mobile.png)
- [Profile page for Desktop](wireframes/Profile.html_Desktop.png)
- [Profile page for Tablet](wireframes/Profile.html_Tablet.png)
- [Profile page for Mobile](wireframes/Profile.html_Mobile.png)
- [Search Results page for Desktop](wireframes/Results.html_Desktop.png)
- [Search Results page for Tablet](wireframes/Results.html_Tablet.png)
- [Search Results page for Mobile](wireframes/Results.html_Mobile.png)
- [Movie page for Desktop](wireframes/Movie.html_Desktop.png)
- [Movie page for Tablet](wireframes/Movie.html_Tablet.png)
- [Movie page for Mobile](wireframes/Movie.html_Mobile.png)

The Registration, Login and Profile were later dropped due to the complexity involved in creating them.
The ability to add, edit and delete reviews was added later to showcase CRUD operations.

## Features

#### Theme
The original **Theme** was taken from the **Bootswatch** themes library, the theme **Journal** was used and then styled with **CSS** to customize it further such as the font used and also the dark background. 

#### Navbar
The **Navbar** used in this project was taken from the **Bootswatch** themes library and edited to fit the needs of the page, it holds a home button in the form of a **FontAwesome** icon and a **Search Bar**.
The Navbar is fully **responsive** and on smaller devices, changes to a burger icon which holds the home button and Search Bar.

#### Search Bar
The **Search Bar** came as part of the **Navbar** taken from **Bootswatch**, when a user inputs a movie name and clicks search or presses enter the input is passed through the `search_result()` function, which is added to the **OMDb API** url along with the **API key** and fired through to the **API**, the response is then iterated through and added to an empty list called `result_list` which is passed to the template **results.html**, this will check if `result_list` is an empty list, if it is it will display a message, if it isn't `result_list` is iterated through in batches of 2 to allow a `<div>` with the class of **row** to be rendered between each result.  

#### Movie Information
When a **result** is selected by the user the **imdbID** value is taken from the variable **imdb_id** which is passed to the `movie()` function, this is then added to a new query url for the **OMDb API** which returns the information about the movie and stores it in the variable **info** which is passed to the template `movie.html` as **movie_info** where select pieces of data are rendered on to the page.

#### Reviews
When a **result** is selected by the user and the movie information is rendered the **Mongo Database** is also queried to search for any **documents** containing the **key** `movieID` with the value of the variable `imdb_id`, this is then iterated through and added to an empty list called `review_list` which is passed to the template `movie.html` which is then passed through a **for loop** to render each review individually.

#### Submitting Reviews
When the **Review** button is selected below the movie information on `movie.html` the `imdbID` from the variable `movie_info` is stored in the variable `imdb_id` and passed as a python variable to the `add_review()` function and renders the template `review.html`. When the **form** is filled in and the **submit** button is selected the `imdbID` is passed to the `submit_review()` function which stores all of the form data in the variable `review` and then passes the variable to the **Mongo Database** to `insert_one` and store the data in its key value pairs.

#### Edit Reviews
When the **Edit** button is pressed underneath the rendered review the value `_id` is taken from the variable review and stored as `review_id` which is passed as a python variable to the `edit_review()` function which passes the id to the** Mongo Database** as a query to `find_one` with the unique id created for the review by the Mongo Database that's **key** is `_id` and renders the template `edit-review.html`. When the **form** that is rendered is filled in and **submitted** the previous review is stored in a variable `old_review` and it's `movieID` is stored in a variable `movie_id`, the form is then requested for the username, comments and score and the `movieID` is set to the variable `movie_id` which is all stored in the variable `new_review`. The Database is then requested to `find_one_and_update` with the variable `old_review` being replace by the variable `new_review`.

#### Delete Reviews
When the **Delete** button is pressed underneath the rendered review the value `_id` is taken from the variable review and stored as `review_id` which is passed as a python variable to the `delete_review()` function which passes the unique id to the **Mongo Database** to `delete_one`. 

### Possible Features To Implement
- A Registration and Login for users would ideally be implemented so that users have a fixed username and are the only ones who can edit or delete their reviews.
- An Amazon affiliate link so that users can choose to buy the movies they like or are interested in watching.

## Technologies Used

- This project uses **HTML**, **CSS** and **Python** programming languages
- [**Visual Studio Code**](https://code.visualstudio.com/) was used as the development IDE
- [**Bootstrap**](https://getbootstrap.com/)
- [**FontAwesome**](https://fontawesome.com/)
- [**Google Fonts**](https://fonts.google.com/)
- [**Popper.js**](https://popper.js.org/)
- this projects wireframes were created on [**Balsamiq**](https://balsamiq.com/)
- The HTML and CSS code were validated using the [**W3C Markup Validation Service**](https://validator.w3.org/) website

## Testing

- The HTML and CSS code were validated using the [**W3C Markup Validation Service**](https://validator.w3.org/) website

### User Stories Tested

#### User who would like to read reviews to see if they like the sound of a movie
As someone who enjoys watching movies, I would like to search for a movie that I have heard of, read something about it and also read what other people who have already watched it think.

- The Home Page gives a quick explenation of what the website is used for and how to use it
- searching for a movie returns that movie and any related titles
- selecting a movie opens a page with information about the movie
- underneath the movies information are reviews left by other users

#### User who has watched a movie and would like to give their opinion of that movie
As someone who has recently watched a movie, I would like to leave a review of that movie so that others can make an informed choice as the weather they want to watch it or not.

- The Home Page gives a quick explenation of what the website is used for and how to use it
- searching for a movie returns that movie and any related titles
- selecting a movie opens a page with information about the movie
- underneath the movies information is a button labeled Review and reviews left by other users
- Pressing the Review button opens a page with a form on it to give a username, comments and score for the movie
- Returning to the movies page displays other users reviews and the one just entered
- selecting edit review will allow the review to be edited
- selecting delete review will remove the review

### Manual Testing

#### Navbar

- Open the page in a new browser window
- right click and select inspect
- select toggle device toolbar or press Ctrl+shift+M
- set the device to responsive
- move the slider in and out to see that the Navbar changes to have a burger icon at 991px
- press the home button to see that the page reloads on to index.html
- press the title "MOVIESTORE" to see that the page reloads on to index.html

#### Search Bar

- Open the page in a new browser window
- select the search bar
- type in a move title (for example: Star Wars)
- select the button labelled Search or press enter
- see that a list of movies relating to the search has been rendered on to the page

#### Movie Information

- Open the page in a new browser window
- select the search bar
- type in a move title (for example: Star Wars)
- select the button labelled Search or press enter
- see that a list of movies relating to the search has been rendered on to the page
- select the movie you were looking for
- see that the movies poster has been rendered in the centre of the page and information about the movie has been rendered underneath




**Testing was carried out on a desktop computer**

### Code Validation

- The **HTML** code was validated using [**W3C Markup Validation**](https://validator.w3.org/)
- The **CSS** code was validated using [**W3C CSS Validation**](https://jigsaw.w3.org/css-validator/)

### Further Testing

The page was shared with family and friends to gather any feedback on any issues found


## Deployment

The Visual Studio Code IDE was used to develop this project and all work was added, committed and pushed to a GitHub repository which was linked with Heroku.

**To deploy on GitHub Pages**

1. **Login** to GitHub
2. Select the **Repositories** tab
3. Select the **MilestoneProject2** repository
4. From the options near the top of the page select **Settings**
5. Scroll down to the section titled **GitHub Pages**
6. Under **Source** select the drop down menu and select **Master Branch**
7. The page will automatically refresh and the page is now **deployed**
8. Scroll back down to the GitHub Pages section to find the **URL**

**How to run the project locally**

1. Use [**this**](https://github.com/OwenCookman/milestoneproject3) link to go to the **repository**
2. Above the repository files select the green button that says **Clone or download**
3. Select the **copy to clip board** image next to the URL to copy the URL to your clip board
4. Using your **local IDE** open a **Git terminal**
5. Change the directory to the location that you want to create the **cloned directory**
6. Type **git clone** and **paste** the URL you copied from GitHub

## Credits

Credit for the Login and Register forms and validation goes to Corey Schafer and his Python Flask Tutorial: Forms and user input series on [**Youtube**](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g)


## Acknowledgements

I would like to thank my family and friends for testing this project and reporting back to me with any issues. 
I would also like to thank my mentor Simen Daehlin for his brilliant tutelage.

This project was created for educational purposes only.
