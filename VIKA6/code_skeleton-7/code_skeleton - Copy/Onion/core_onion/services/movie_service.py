from injector import inject

from core_onion.interfaces.IMovieRepository import IMovieRepository
from core_onion.models.movie import Movie


class MovieService:
    @inject
    def __init__(self, repository: IMovieRepository):
        self.__repository = repository

    def get_all(self) -> list[Movie]:
        return self.__repository.get_all()

    def create_movie(self, movie: Movie) -> None:
        self.__repository.create_movie(movie)
