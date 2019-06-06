# Online Bookstore
This is a website for user-generated content. Specifically, users or authors can upload books and the combination of all these uploads will form an online bookstore. In addition, the users can update or delete recipes on this website.

## Demo
A live demo can be found [here](https://alwy-django-assignment.herokuapp.com/).

## UX
My goal in the design was an online bookstore using e-commerce for transactions. Users could register for a new account and log in to the ‘shopping’ section of this website. Users who do not have an account in this website cannot purchase items and can only read information about books uploaded by the administrator or other users who have accounts.
In the ‘shopping’ section, users could add items which they wished to purchase to their shopping cart and check them out by making payments with Stripe. These users could also remove items from their shopping cart if they ultimately decided not to purchase those items. In addition, these users could upload new books to the website, or delete or edit existing books on the website.
Regardless of having an account, users can search for books by title using the search bar in the ‘shopping’ and ‘non-shopping’ sections of this website.
The information to be presented to the user and the database relations is based on the ‘Online_Bookstore_ER_Diagramme.jpg’ file in the main directory of this ‘django-milestone-project’ Cloud9 workspace.
### Existing Features
-There is a modal button for each book, called ‘More Information’ so that the user can click on it to open up a pop-up box to show more information about the book.
- There is a search bar at the top of every page for the user to key in a book title which he or she wants to find. The user will be able to see the search results after keying in and clicking on the ‘Search’ button below the search bar.

### Features Left to Implement
- Allowing users to upload samples/excerpts of their books.

## Technologies Used
1. HTML
- For structuring the website, e.g. adding content to the website.
2. CSS
- For styling the website, e.g. text alignment.
3. [Bootstrap (Version 4)](https://getbootstrap.com/)
 - The project uses Bootstrap to create mobile-responsive web pages.
## Testing
Python assertions were used to test the models created. The Python assert statements can be found in the ‘tests.py’ file in the ‘book’ folder of this ‘django-milestone-project’ Cloud9 workspace.
Where Python assertions were not done, manual tests were done. For example, to test the mobile responsiveness of this website, different screen sizes were used to view the website. For example, a mobile phone screen size was used to test a small view and a desktop computer screen size was used to test a big view. 
In another example, a user trying to add a book on the website would need to key in information for the blank fields such as ‘Title’ because they are required fields. Submitting the recipe without filling in the blank fields would cause an error message to appear. Successful submission of the recipe will redirect the user to the ‘Home’ page of the website.

## Deployment
This project was deployed to Heroku.
A person who wants to run this code locally can clone or download this repository from https://github.com/AlexLimWY/django-milestone-project.git and paste it into their editor terminal.

## Credits
### Content
- The text for The Hobbit was taken from [Amazon]( https://www.amazon.com/Hobbit-J-R-R-Tolkien/dp/0345339681/ref=sr_1_5?keywords=the+lord+of+the+rings+the+hobbit&qid=1559528811&s=books&sr=1-5)
- The text for Ready Player One was taken from [Amazon](https://www.amazon.com/Ready-Player-One-Ernest-Cline/dp/0307887448/ref=sr_1_1?crid=2J1NJU4FS59BW&keywords=ready+player+one&qid=1559528918&s=books&sprefix=ready+player+one%2Cstripbooks-intl-ship%2C412&sr=1-1)
- The text for Redemption was taken from [Amazon](https://www.amazon.com/Redemption-Memory-Man-Book-5-ebook/dp/B07G87BTJQ/ref=tmm_kin_swatch_0?_encoding=UTF8&qid=1559529075&sr=1-1)
- The text for The Notebook was taken from [Amazon](https://www.amazon.com/Notebook-Nicholas-Sparks/dp/0446676098)
- The text for The Good Fight was taken from [Amazon]( https://www.amazon.com/Good-Fight-Novel-Danielle-Steel/dp/1101884142/ref=sr_1_3?keywords=the+good+fight&qid=1559530787&s=books&sr=1-3)
- The text for The Purpose Driven Life: What on Earth Am I Here For? was taken from [Amazon]( https://www.amazon.com/Purpose-Driven-Life-What-Earth/dp/031033750X/ref=sr_1_1?keywords=the+purpose+driven+life&qid=1559530945&s=books&sr=1-1)

### Media
- The image for The Hobbit was taken from [Amazon]( https://www.amazon.com/Hobbit-J-R-R-Tolkien/dp/0345339681/ref=sr_1_5?keywords=the+lord+of+the+rings+the+hobbit&qid=1559528811&s=books&sr=1-5)
- The image for Ready Player One was taken from [Amazon](https://www.amazon.com/Ready-Player-One-Ernest-Cline/dp/0307887448/ref=sr_1_1?crid=2J1NJU4FS59BW&keywords=ready+player+one&qid=1559528918&s=books&sprefix=ready+player+one%2Cstripbooks-intl-ship%2C412&sr=1-1)
- The image for Redemption was taken from [Amazon](https://www.amazon.com/Redemption-Memory-Man-Book-5-ebook/dp/B07G87BTJQ/ref=tmm_kin_swatch_0?_encoding=UTF8&qid=1559529075&sr=1-1)
- The image for The Notebook was taken from [Amazon](https://www.amazon.com/Notebook-Nicholas-Sparks/dp/0446676098)
- The image for The Good Fight was taken from [Amazon]( https://www.amazon.com/Good-Fight-Novel-Danielle-Steel/dp/1101884142/ref=sr_1_3?keywords=the+good+fight&qid=1559530787&s=books&sr=1-3)
- The image for The Purpose Driven Life: What on Earth Am I Here For? was taken from [Amazon]( https://www.amazon.com/Purpose-Driven-Life-What-Earth/dp/031033750X/ref=sr_1_1?keywords=the+purpose+driven+life&qid=1559530945&s=books&sr=1-1)

### Acknowledgements
- I was inspired to create an online bookstore because the number of people reading books on their electronic devices is increasing. I also believe that people from all over the world should share their knowledge with one another through books.



