import numpy as np
import pandas as pd
from pymcdm.methods import TOPSIS, SPOTIS
from pymcdm.normalizations import minmax_normalization

matrix = np.array([
    [250, 16, 12],
    [200, 20, 8],
    [300, 11, 10],
    [275, 18, 11]
])

weights = np.array([0.5, 0.3, 0.2])

types = [1, -1, -1]


norm_matrix = minmax_normalization(matrix, types)

bounds = np.array([[np.min(matrix[:, i]), np.max(matrix[:, i])] for i in range(matrix.shape[1])])

topsis = TOPSIS()
topsis_scores = topsis(norm_matrix, weights, types)

spotis = SPOTIS(bounds)
spotis_scores = spotis(matrix, weights, types)

ranking_df = pd.DataFrame({
    'Alternatywa': [f'A{i+1}' for i in range(len(matrix))],
    'TOPSIS': topsis_scores,
    'SPOTIS': spotis_scores
})

ranking_df['TOPSIS_rank'] = ranking_df['TOPSIS'].rank(ascending=False)
ranking_df['SPOTIS_rank'] = ranking_df['SPOTIS'].rank(ascending=True)

print(ranking_df)

ranking_df.to_csv('wyniki.csv', index=False)

