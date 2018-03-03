from .tmdbbase import TMDBBase


class TMDBMovie(TMDBBase):
    def __init__(self, id):
        self.id = id

    def info(self):
        return TMDBMovie.api_call(str(self.id))

    def videos(self):
        return TMDBMovie.api_call(str(self.id)+'/videos')

    @staticmethod
    def popular():
        return TMDBMovie.api_call('popular')

    @staticmethod
    def top_rated():
        return TMDBMovie.api_call('top_rated')

    @staticmethod
    def upcoming():
        return TMDBMovie.api_call('upcoming')
