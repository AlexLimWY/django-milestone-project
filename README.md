# Online Cookbook
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
- Allowing users to upload image(s) of their respective book(s).
## Technologies Used
1. HTML
- For structuring the website, e.g. adding content to the website.
2. CSS
- For styling the website, e.g. text alignment.
3. [Bootstrap (Version 4)](https://getbootstrap.com/)
 - The project uses Bootstrap to create mobile-responsive web pages.
## Testing
Python assertions were used to test the models created. The Python assert statements can be found in the ‘tests.py’ file in the ‘book’ folder of this ‘django-milestone-project’ Cloud9 workspace.

