import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "localhost",  
    "database": "movies",
    "raise_on_warnings": True
}

def show_films(cursor, title):
    """ Method to execute an inner join on all tables, iterate over the dataset, and output the results to the terminal window. """
    cursor.execute("""
    SELECT 
        film.film_name AS 'Name', 
        film.film_director AS 'Director', 
        genre.genre_name AS 'Genre', 
        studio.studio_name AS 'Studio Name' 
    FROM 
        film 
    INNER JOIN 
        genre ON film.genre_id = genre.genre_id
    INNER JOIN 
        studio ON film.studio_id = studio.studio_id
    """)
    films = cursor.fetchall()
    print("\n -- {} --".format(title))
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    
    # Perform INSERT
    cursor.execute("INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) VALUES ('Inception', '2010', 148, 'Christopher Nolan', (SELECT studio_id FROM studio WHERE studio_name = 'Universal Pictures'), (SELECT genre_id FROM genre WHERE genre_name = 'SciFi'));")
    show_films(cursor, "DISPLAYING FILMS AFTER INSERTING INCEPTION")
    
    # Perform UPDATE
    cursor.execute("UPDATE film SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror') WHERE film_name = 'Alien';")
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATING ALIEN TO HORROR")
    
    # Perform DELETE
    cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator';")
    show_films(cursor, "DISPLAYING FILMS AFTER DELETING GLADIATOR")
    
    db.commit()
    
    input("\n\nPress any key to continue...")  

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)

finally:
    # Ensure the database connection is closed
    if db.is_connected():
        db.close()