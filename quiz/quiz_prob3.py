def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    availsize = max_size    
    songlist = songs[:]    
    playlist = []   

    if songlist[0][2] > availsize:
        return playlist
    else:
        playlist.append(songlist[0][0])
        availsize -= songlist[0][2]
        songlist.remove(songlist[0])
    
    songlist.sort(key=lambda x:x[2])
    for i in range(len(songlist)):
        if songlist[i][2] < availsize:
            playlist.append(songlist[i][0])
            availsize -= songlist[i][2]
    
    return playlist                
