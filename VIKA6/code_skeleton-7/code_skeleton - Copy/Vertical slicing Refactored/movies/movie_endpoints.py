from contextlib import AbstractContextManager
from typing import Callable
from fastapi import APIRouter, Depends, status
from common.infrastructure.get_service import get_service
from movies.create_movie_dto import CreateMovieDto
from movies.movie import Movie
from sqlalchemy.orm import Session


router = APIRouter(
    prefix='/movies',
)

# session_factory: Callable[..., AbstractContextManager[Session]] = Depends(get_service)
# session_factory: Callable[..., AbstractContextManager[Session]] = Depends(get_service())
# session_factory: Callable[..., AbstractContextManager[Session]] = Depends(get_service(Callable[..., AbstractContextManager[Session]]))

@router.get('/')
def get_movies(session_factory: Callable[..., AbstractContextManager[Session]] = Depends(get_service(Callable[..., AbstractContextManager[Session]]))):
    with session_factory() as session:
        return session.query(Movie).all()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_movie(request: CreateMovieDto, session_factory: Callable[..., AbstractContextManager[Session]] = Depends(get_service(Callable[..., AbstractContextManager[Session]]))):
    movie = Movie(
        name=request.name,
        description=request.description,
        imdb_url=request.imdb_url,
    )

    with session_factory() as session:
        session.add(movie)
        session.commit()
        session.refresh(movie)

    return movie
