class Song:
    # Class attributes
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Increment song count
        Song.add_to_count()
        
        # Add artist and genre to respective class attributes
        Song.add_to_artists(artist)
        Song.add_to_genres(genre)
        
        # Update the song count for the genre and artist
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
    
    @classmethod
    def add_to_count(cls):
        cls.count += 1
    
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
    
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
    
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    
    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
    
    @classmethod
    def artists(cls):
        return cls.artists
    
    @classmethod
    def genres(cls):
        return cls.genres
    
    @classmethod
    def genre_count(cls):
        return cls.genre_count
    
    @classmethod
    def artist_count(cls):
        return cls.artist_count
