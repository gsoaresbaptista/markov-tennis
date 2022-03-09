from tennis import TenisSimulation


if __name__ == "__main__":
    #
    tennis_df = TenisSimulation.generate_dataset(0.75, 1000)
    # print(tennis_df.mean())

    a_points = tennis_df.loc[:, 'A points'].sum()
    b_points = tennis_df.loc[:, 'B points'].sum()

    a_points = a_points/(a_points + b_points)

    print(a_points)
    # print(tennis_df.loc[:, 'B points'])
