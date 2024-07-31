current_movies = {'Terminator': '11:00am',
                  'Robocop': '1:00pm',
                  'Transformers': '3:00pm',
                  'Aliens': '5:00pm'}

print ('We are showing the following movies:')
for key in current_movies:
    print(key)  
movie = input('What movie would you like the showtime for?\n') 

showtime = current_movies.get(movie)
if showtime == None:
    print('Requested movie is not available')
else:
    print(movie, 'is playing at', showtime) 