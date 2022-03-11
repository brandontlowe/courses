movies_watched = {"The Matrix", "Green Book", "Her"}
user_movie = input("Enter something you've watched recently: ")

if user_movie in movies_watched:
    print(f"I've seen {user_movie} too!")
else:
    print(f"I haven't seen {user_movie} yet")