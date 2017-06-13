import pandas as pd


def trained():
    df = pd.DataFrame(
        data = [
            ['nice', 1, 1, 1, 0],
            ['not_nice', 1, 1, 0, 1]
        ],
        columns = ['cat', 'John', 'is', 'good', 'bad']
    )
    return df
