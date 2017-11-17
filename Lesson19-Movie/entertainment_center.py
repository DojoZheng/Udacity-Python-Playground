import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys that come to life",
						"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=vwyZH85NQC4")
# print(toy_story.storyline)

avatar = media.Movie("Avatar",
					"A marine on an alien planet",
					"http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
					"http://v.youku.com/v_show/id_XMTg5MDk1NDA4.html?spm=a2h0k.8191407.0.0&from=s1.8-3-1.1")
# print(avatar.storyline)
# avatar.show_trailer()

movies = [toy_story, avatar]
# fresh_tomatoes.open_movies_page(movies)
print (media.Movie.VALID_RATINGS)
print (media.Movie.__doc__)
print (media.Movie.__name__)
print (media.Movie.__module__)