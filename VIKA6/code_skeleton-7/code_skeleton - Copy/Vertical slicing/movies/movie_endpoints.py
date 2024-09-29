from fastapi import APIRouter, Depends, status
from common.infrastructure.get_service import get_service
from movies.create_movie_dto import CreateMovieDto

from movies.movie import Movie
from movies.movie_service import MovieService

router = APIRouter(
    prefix='/movies',
)


@router.get('/')
def get_movies(movie_service: MovieService = Depends(get_service(MovieService))):
    return movie_service.get_all()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_movie(request: CreateMovieDto, movie_service: MovieService = Depends(get_service(MovieService))):
    movie = Movie(
        name=request.name,
        description=request.description,
        imdb_url=request.imdb_url,
    )

    movie_service.create_movie(movie)

    return movie
