import pytest
import aiohttp
from app.routes.main import get_all_pokemons


@pytest.mark.asyncio
async def test_get_all_pokemons():
    pokemon_data = await get_all_pokemons(1)

    assert pokemon_data['name'] == 'bulbasaur'
    assert 'abilities' in pokemon_data

    with pytest.raises(aiohttp.ClientError):
        await get_all_pokemons(10000)

