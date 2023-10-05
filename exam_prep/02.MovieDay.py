time = int(input())
scenes = int(input())
scene_time = int(input())

movie = time - (scene_time*scenes) - 0.15*time

if movie>=0:
    print(f"You managed to finish the movie on time! You have {movie:.0f} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {abs(movie):.0f} minutes.")