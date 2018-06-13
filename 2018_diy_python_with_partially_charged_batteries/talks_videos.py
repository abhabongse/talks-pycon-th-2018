from IPython.display import HTML

class YouTubeVideo(object):
    def __init__(self, video_id):
        self.video_id = video_id
    def _repr_html_(self):
        return f"""
            <iframe width="1120" height="630" 
                src="https://www.youtube.com/embed/{self.video_id}?rel=0&amp;showinfo=0"
                frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
            </iframe>
        """


NO_BATTERIES = YouTubeVideo('uCQG5Hb6Gew')
