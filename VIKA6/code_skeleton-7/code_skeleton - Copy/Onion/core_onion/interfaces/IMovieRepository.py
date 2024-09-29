from abc import ABC, abstractmethod
from typing import List
from core_onion.models.movie import Movie


class IMovieRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Movie]:
        """Retrieve all movies."""
        pass

    @abstractmethod
    def create_movie(self, movie: Movie) -> None:
        """Create a new movie."""
        pass
