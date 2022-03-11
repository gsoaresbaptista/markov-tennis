from .markov import Markov


def get_tennis_machine() -> Markov:
    # Create the machine nodes
    node_0_0 = Markov("0-0")
    node_15_love = Markov("15-Love")
    node_15_15 = Markov("15-15")
    node_15_30 = Markov("15-30")
    node_15_40 = Markov("15-40")
    node_30_love = Markov("30-Love")
    node_30_15 = Markov("30-15")
    node_30_30 = Markov("30-30")
    node_30_40 = Markov("30-40")
    node_40_love = Markov("40-Love")
    node_40_15 = Markov("40-15")
    node_40_30 = Markov("40-30")
    node_a_wins = Markov("A-Wins")
    node_b_wins = Markov("B-Wins")
    node_deuce = Markov("Deuce")
    node_adv_a = Markov("Adv. A")
    node_adv_b = Markov("Adv. B")
    node_love_15 = Markov("Love-15")
    node_love_30 = Markov("Love-30")
    node_love_40 = Markov("Love-40")

    # Linking the nodes states
    node_0_0.left = node_15_love
    node_0_0.right = node_love_15

    node_15_love.left = node_30_love
    node_15_love.right = node_15_15

    node_15_15.left = node_30_15
    node_15_15.right = node_15_30

    node_15_30.left = node_30_30
    node_15_30.right = node_15_40

    node_15_40.left = node_30_40
    node_15_40.right = node_b_wins

    node_30_love.left = node_40_love
    node_30_love.right = node_30_15

    node_30_30.left = node_40_30
    node_30_30.right = node_30_40

    node_40_30.left = node_a_wins
    node_40_30.right = node_deuce

    node_30_40.left = node_deuce
    node_30_40.right = node_b_wins

    node_30_15.left = node_40_15
    node_30_15.right = node_30_30

    node_40_love.left = node_a_wins
    node_40_love.right = node_40_15

    node_40_15.left = node_a_wins
    node_40_15.right = node_40_30

    node_deuce.left = node_adv_a
    node_deuce.right = node_adv_b

    node_adv_a.left = node_a_wins
    node_adv_a.right = node_deuce

    node_adv_b.left = node_deuce
    node_adv_b.right = node_b_wins

    node_love_15.left = node_15_15
    node_love_15.right = node_love_30

    node_love_30.left = node_15_30
    node_love_30.right = node_love_40

    node_love_40.left = node_15_40
    node_love_40.right = node_b_wins

    return node_0_0
