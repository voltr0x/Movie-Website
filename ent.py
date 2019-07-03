import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life.","https://en.wikipedia.org/wiki/File:Toy_Story.jpg","https://www.youtube.com/watch?v=tN1A2mVnrOM")

tintin = media.Movie("Adventures of Tintin","Intrepid reporter Tintin and Captain Haddock set off on a treasure hunt for a sunken ship commanded by Haddock's ancestor.",
"https://www.youtube.com/watch?v=7NWtW699XME","http://www.imdb.com/video/imdb/vi2415828505?ref_=tt_ov_vi")

cars = media.Movie("Cars","A hot-shot race-car named Lightning McQueen gets waylaid in Radiator Springs, where he finds the true meaning of friendship and family.",
"http://www.imdb.com/title/tt0317219/mediaviewer/rm3794114560?ref_=tt_ov_i","https://www.youtube.com/watch?v=SbXIj2T-_uk")

incredibles = media.Movie("The Incredibles","A family of undercover superheroes, while trying to live the quiet suburban life, are forced into action to save the world.",
"http://www.imdb.com/title/tt0317705/mediaviewer/rm915381504?ref_=tt_ov_i","https://www.youtube.com/watch?v=eZbzbC9285I")


movies = [toy_story, tintin, cars, incredibles]
fresh_tomatoes.open_movies_page(movies)
