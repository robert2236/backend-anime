from databases.database import coleccion
from models.anime import Anime,UpdateAnime
from bson import ObjectId

async def get_all_animes():
    anime_list = []
    cursor = coleccion.find({})
    async for document in cursor:
        anime_list.append(Anime(**document))
    return anime_list

async def get_one_anime(search):
    anime = await coleccion.find_one({"name": search})
    return anime


async def create_anime(anime):
    new_anime = await coleccion.insert_one(anime)
    created_anime = await coleccion.find_one({"_id": new_anime.inserted_id})
    return created_anime

async def update_anime(id: str, data: UpdateAnime):
    bird = {k: v for k, v in data.dict().items() if v is not None}
    await coleccion.update_one({"_id": ObjectId(id)}, {"$set": bird})
    document = await coleccion.find_one({"_id": ObjectId(id)})
    return document

async def delete_anime(id):
    await coleccion.delete_one({"_id": ObjectId(id)})
    return True