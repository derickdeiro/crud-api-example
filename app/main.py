import os
import random
import sys
import time

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__name__), '..'))
)

from src.controller import add_pokemon_to_db, catch_pokemon


def main():
    while True:
        pokemon_id = random.randint(1, 150)
        pokemon_schema = catch_pokemon(pokemon_id)
        if pokemon_schema:
            add_pokemon_to_db(pokemon_schema)
        else:
            time.sleep(10)


if __name__ == '__main__':
    main()
