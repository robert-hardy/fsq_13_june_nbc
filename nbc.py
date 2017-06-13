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


def trained_stacked():
    df = pd.DataFrame(
        data = [
            ['nice', 'John'],
            ['nice', 'is'],
            ['nice', 'good'],
            ['not_nice', 'John'],
            ['not_nice', 'is'],
            ['not_nice', 'bad']
        ],
        columns = ['cat', 'feature']
    )
    return df


def prob(f, c, trained):
    cat = trained['cat']
    feature = trained['feature']
    if f not in feature.values:
        return 0.5

    prob_f_given_c_num = ((cat == c) & (feature == f)).sum()
    prob_f_given_c_den = (cat == c).sum()
    prob_f_given_c = float(prob_f_given_c_num)/prob_f_given_c_den

    prob_c_num = (cat == c).sum()
    prob_c_den = len(cat)
    prob_c = float(prob_c_num)/prob_c_den

    prob_f_num = (feature == f).sum()
    prob_f_den = len(feature)
    prob_f = float(prob_f_num)/prob_f_den

    return prob_f_given_c * prob_c / prob_f


def prob_f_given_c(f, c, trained):
    cat = trained['cat']
    feature = trained['feature']
    prob_f_given_c_num = ((cat == c) & (feature == f)).sum()
    prob_f_given_c_den = (cat == c).sum()
    prob_f_given_c = float(prob_f_given_c_num)/prob_f_given_c_den
    return prob_f_given_c


def docprob(doc, c, trained):
    ff = doc.split()
    p = 1.0
    for f in ff:
        p = p * prob_f_given_c(f, c, trained)

    cat = trained['cat']
    prob_c_num = (cat == c).sum()
    prob_c_den = len(cat)
    prob_c = float(prob_c_num)/prob_c_den

    return p * prob_c
