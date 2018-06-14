from IPython.display import HTML

class YouTubeVideo(object):
    """
    Displays YouTube video in Jupyter Notebook.
    
    Attributes:
        video_id: YouTube video ID
        autoplay: Whether to auto-play video on load
        rel: Whether to show suggested videos when finishes
        controls: Whether to show player controls
        showinfo: Whether to show video title and player actions
    """
    
    def __init__(self, video_id, autoplay=False, rel=False, controls=True, showinfo=True):
        self.video_id = video_id
        self.autoplay = autoplay
        self.rel = rel
        self.controls = controls
        self.showinfo = showinfo
        
    def _repr_html_(self):
        options = []
        if self.autoplay:
            options.append("autoplay=1")
        if not self.rel:
            options.append("rel=0")
        if not self.controls:
            options.append("controls=0")
        if not self.showinfo:
            options.append("showinfo=0")
        opt_string = "&amp;".join(options)
        return f"""
            <iframe width="960" height="540"
                src="https://www.youtube.com/embed/{self.video_id}?{opt_string}"
                frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
            </iframe>
        """
