import logging
import aiohttp

from flask import Blueprint, redirect, render_template, request, url_for

main = Blueprint('main', __name__)

async def get_all_pokemons(id: int) -> any:
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://pokeapi.co/api/v2/pokemon/{id}') as resp:
            return await resp.json()

@main.route('/pokemon/<int:id>')
async def poke_app(id):
    logging.info(">>>>>>>>>>>>>> Consumiendo Endpoint: PokeAPI/Pokemon >>>>>>>>>>>>>>")
    pokemon = await get_all_pokemons(1) if id<=0 else await get_all_pokemons(id)
    logging.info(">>>>>>>>>>>>>> Renderizando Pagina: PokeAPI/Pokemon >>>>>>>>>>>>>>")
    return render_template('pokedex.html',pokemon=pokemon)
