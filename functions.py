from recommendation import recommend_songs_by_cluster, DEFAULT_FEATURE_COLS





def list_of_recommendations(recommended_song_string, number_of_recommendations):
    
    # Declaration of used variables
    liked_songs_input = recommended_song_string
    feature_cols = DEFAULT_FEATURE_COLS
    n_recommendations = number_of_recommendations


    liked_song_names = [song.strip() for song in liked_songs_input.split("\n") if song.strip()]
    
    dictionary_to_return = [[2]]       
    
    if len(liked_song_names) == 0:
        print("warning: song is less than 1")
    elif len(feature_cols) < 4:
        print("Please select at least 4 features.")
    else:
        final_recommendations, songs_not_in_db = recommend_songs_by_cluster(liked_song_names, n_recommendations, feature_cols)        

        i = 0     
        for song_info in final_recommendations.items():
            chars = [',', '.','#','(',')','?','!']
            
            
            # TODO: values(artist name, link) need to be appended into a dictionary or a similar data structure
                
            song_name = song_info[1]['Name'].translate({ord(k): None for k in chars})
            song_artist = song_info[1]['Artists'].translate({ord(k): None for k in chars})

            url ="https://music.youtube.com/search?q="+song_name.replace(" ","+")+"+" +song_artist.replace(" ","+")+""
            dictionary_to_return[i][0] = f"{song_info[1]['Name']} by {song_info[1]['Artists']}"
            dictionary_to_return[i][1] = url
            i+1
            print(url)

         
         
dictionary = list_of_recommendations("Thunder",5)