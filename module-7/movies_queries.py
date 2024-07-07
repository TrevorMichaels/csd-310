import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "localhost",  
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    print("\nDatabase user {} connected to MySQL on host {} with database {}".format(
        config["user"], config["host"], config["database"]))
    
    cursor = db.cursor()

    # Query 1: Select all fields for the studio table
    cursor.execute("SELECT * FROM studio")
    print("\nStudios:")
    for (studio_id, studio_name) in cursor:
        print(f"Studio ID: {studio_id}, Studio Name: {studio_name}")

    # Query 2: Select all fields for the genre table
    cursor.execute("SELECT * FROM genre")
    print("\nGenres:")
    for (genre_id, genre_name) in cursor:
        print(f"Genre ID: {genre_id}, Genre Name: {genre_name}")

    # Query 3: Select movie names for movies with runtime less than 120 minutes
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    print("\nMovies with runtime less than 2 hours:")
    for (film_name, film_runtime) in cursor:
        print(f"Movie Name: {film_name}, Runtime: {film_runtime} minutes")

    # Query 4: List of film names and directors, grouped by director
    cursor.execute("SELECT film_director, film_name FROM film GROUP BY film_director, film_name")
    print("\nFilm names and directors:")
    for (film_director, film_name) in cursor:
        print(f"Director: {film_director}, Movie: {film_name}")

    input("\n\nPress any key to continue...")  

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)  

finally:
    # It's safer to check if 'db' is defined and is open before trying to close it
    if 'db' in locals() and db.is_connected():
        db.close()