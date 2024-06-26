from fastapi import APIRouter, HTTPException
from databases.animes import (get_all_animes,create_anime,get_one_anime,delete_anime)
from models.anime import Anime,UpdateAnime



anime = APIRouter()

@anime.get('/api/animes')  
async def get_anime():
    response = await get_all_animes()
    return response


@anime.post('/api/create_anime', response_model=Anime)
async def save_anime(anime: Anime):
    AnimeFound = await get_one_anime(anime.name)
    if AnimeFound:
        raise HTTPException(409, "Anime already exists")

    response = await create_anime(anime.dict())
    print(response)
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@anime.put('/api/anime/{id}', response_model=Anime)
async def put_bird(id: str, data: UpdateAnime):
    data.id = id
    response = UpdateAnime(**data.dict())
    if response:
        return response
    raise HTTPException(404, f"There is no task with the id {id}")

@anime.delete('/api/anime/{id}')
async def remove_task(id: str):
    response = await delete_anime(id)
    if response:
        return "Successfully delete delete from the database"
    raise HTTPException(404, f"There is no task with the id {id}")