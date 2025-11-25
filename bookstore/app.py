from flask import Flask, render_template, request, redirect, url_for, make_response


# instantiate the app
app = Flask(__name__)

# Create a list called categories. The elements in the list should be lists that contain the following information in this order:
#   categoryId
#   categoryName
#   An example of a single category list is: [1, "Biographies"]
categories = [
    [1, "Biographies"],
    [2, "Learn to Play"],
    [3, "Music Theory"],
    [4, "Scores and Charts],
    ]

# Create a list called books. The elements in the list should be lists that contain the following information in this order:
#   bookId     (you can assign the bookId - preferably a number from 1-16)
#   categoryId (this should be one of the categories in the category dictionary)
#   title
#   author
#   isbn
#   price      (the value should be a float)
#   image      (this is the filename of the book image.  If all the images, have the same extension, you can omit the extension)
#   readNow    (This should be either 1 or 0.  For each category, some of the books (but not all) should have this set to 1.
#   An example of a single category list is: [1, 1, "Madonna", "Andrew Morton", "13-9780312287863", 39.99, "madonna.png", 1]

books = [
    # Biographies (categoryId = 1)
    [1, 1, "Beethoven", "David Jacobs",
     "13-9780304936588", 9.99, "beethoven.gif", 0],
    [2, 1, "Madonna", "Andrew Morton",
     "13-9780312287863", 12.99, "madonna.jpg", 1],
    [3, 1, "Clapton: The Autobiography", "Eric Clapton",
     "13-9780767925365", 10.99, "clapton.jpg", 1],
    [4, 1, "Music is My Mistress", "Edward Kennedy Ellington",
     "13-9780306800037", 68.99, "music-is-my-mistress.jpg", 0],

    # Learn to Play (categoryId = 2)
    [5, 2, "Piano for Beginners", "Lisa Brown",
     "13-9780000000001", 19.99, "piano-beginners.jpg", 1],
    [6, 2, "Guitar Chords Made Easy", "Mark Davis",
     "13-9780000000002", 15.99, "guitar-chords.jpg", 0],
    [7, 2, "Drums 101", "Samantha Lee",
     "13-9780000000003", 17.99, "drums-101.jpg", 0],
    [8, 2, "Voice Training Basics", "Caroline Smith",
     "13-9780000000004", 14.99, "voice-training.jpg", 1],

    # Music Theory (categoryId = 3)
    [9, 3, "Essential Music Theory", "John Carter",
     "13-9780000000011", 21.99, "essential-theory.jpg", 1],
    [10, 3, "Harmony and Form", "Maria Russo",
     "13-9780000000012", 24.99, "harmony-form.jpg", 0],
    [11, 3, "Jazz Theory Explained", "Ben Martinez",
     "13-9780000000013", 23.50, "jazz-theory.jpg", 1],
    [12, 3, "Rhythm and Meter", "Olivia Cheng",
     "13-9780000000014", 18.75, "rhythm-meter.jpg", 0],

    # Scores and Charts (categoryId = 4)
    [13, 4, "Classical Piano Favorites", "Various",
     "13-9780000000021", 16.99, "classical-piano.jpg", 0],
    [14, 4, "Pop Hits: Easy Piano", "Various",
     "13-9780000000022", 19.50, "pop-hits.jpg", 1],
    [15, 4, "Jazz Standards Real Book", "Various",
     "13-9780000000023", 29.99, "jazz-standards.jpg", 1],
    [16, 4, "Broadway Songbook", "Various",
     "13-9780000000024", 22.00, "broadway-songbook.jpg", 0],
]



# set up routes
@app.route('/')
def home():
       """
    Home page: show welcome text + categories.
    We pass the categories list so index.html can loop over it.
    """
    return render_template('index.html', categories=categories)
   

@app.route('/category')
def category():
        """
    Category page.
    URL will look like: /category?category=1
    """
    cat_id_str = request.args.get('category')

    if cat_id_str is None:
        # if no category passed, just go back to home
        return redirect(url_for('home'))

    try:
        cat_id = int(cat_id_str)
    except ValueError:
        return redirect(url_for('home'))

    # filter books that belong to this category
    selected_books = [b for b in books if b[1] == cat_id]

    return render_template(
        'category.html',
        categories=categories,
        selectedCategory=cat_id,
        books=selected_books
    )

@app.route('/search')
def search():
    #Link to the search results page.
    return redirect(url_for('home'))

@app.errorhandler(Exception)
def handle_error(e):
    """
    Output any errors - good for debugging.
    """
    return render_template('error.html', error=e) # render the edit template


if __name__ == "__main__":
    app.run(debug = True)
