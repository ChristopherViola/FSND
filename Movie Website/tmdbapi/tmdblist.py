from .tmdbbase import TMDBBase


class TMDBList(TMDBBase):
    def __init__(self, id):
        self.id = id

    def info(self):
        return TMDBList.api_call(str(self.id))
