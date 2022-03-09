import pandas as pd
from tqdm.autonotebook import tqdm
from .markov import Markov
from .tennis_machine import get_tennis_machine
from random import random
from typing import Dict, List


class TenisSimulation:
    @staticmethod
    def generate_dataset(
            probability: float,
            n_simulations: int) -> pd.DataFrame:
        #
        matches: List[pd.DataFrame] = []

        for i in tqdm(range(n_simulations)):
            #
            game_end: bool = False

            #
            match: Dict = {
                'A points': 0,
                'B points': 0,
                'sets A-Wins': 0,
                'sets B-Wins': 0,
                'games A-Wins': 0,
                'games B-Wins': 0,
            }

            while not game_end:
                current_node: Markov = get_tennis_machine()
                set_end = False

                game_results: Dict = {
                    'games A-Wins': 0,
                    'games B-Wins': 0,
                }

                while not set_end:
                    while not current_node.is_over():
                        number: float = random()

                        # Compute point
                        p = number < probability
                        match['A points' if p else 'B points'] += 1

                        # Update simulation state
                        current_node.process(p)

                    game_results['games ' + current_node.name] += 1
                    match['games ' + current_node.name] += 1

                    if (game_results['games A-Wins'] == 6 and
                       game_results['games B-Wins'] <= 4):
                        match['sets A-Wins'] += 1
                        set_end = True

                    elif (game_results['games B-Wins'] == 6 and
                          game_results['games A-Wins'] <= 4):
                        match['sets B-Wins'] += 1
                        set_end = True

                    elif game_results['games A-Wins'] == 7:
                        match['sets A-Wins'] += 1
                        set_end = True

                    elif game_results['games B-Wins'] == 7:
                        match['sets B-Wins'] += 1
                        set_end = True

                if match['sets A-Wins'] == 2:
                    match['Winner'] = 'A'
                    game_end = True

                elif match['sets B-Wins'] == 2:
                    match['Winner'] = 'B'
                    game_end = True

            matches.append(match)

        return pd.DataFrame(matches)
