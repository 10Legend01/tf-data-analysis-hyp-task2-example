import pandas as pd
import numpy as np

from scipy.stats import anderson_ksamp, ks_2samp, cramervonmises_2samp, mannwhitneyu

chat_id = 1379613676 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # 2 из 4
    # return anderson_ksamp([x, y]).significance_level < 0.08

    # 1 из 4
    # return ks_2samp(x, y).pvalue < 0.08

    # 3 из 4
    return cramervonmises_2samp(x, y).pvalue < 0.08

    # 1 из 4
    # return mannwhitneyu(x, y).pvalue < 0.08

    # return anderson_ksamp([x, y]).pvalue < 0.08

# historical_db = pd.read_csv("historical_data.csv", index_col=0)
# db1 = pd.read_csv("modified_data_of_type_1.csv", index_col=0)
# db2 = pd.read_csv("modified_data_of_type_2.csv", index_col=0)
# db3 = pd.read_csv("modified_data_of_type_3.csv", index_col=0)
#
# def test(db1, db2, error):
#     good = 0
#     all = 0
#     for i in range(200):
#         for j in range(200):
#             # if i == j: continue
#             # ma1 = np.array(db1[f'x{i}'])
#             # ma2 = np.array(db2[f'x{j}'])
#             ma1 = np.array(db1.iloc[i])
#             ma2 = np.array(db2.iloc[j])
#             if solution(ma1, ma2):
#                 good += 1
#             all += 1
#     err1 = good / all
#     if db1 is not db2:
#         err1 = 1 - err1
#     print(err1, error, err1 < error)
#
# test(historical_db, historical_db, 0.0705)
# test(historical_db, db1, 0.161)
# test(historical_db, db2, 0.102)
# test(historical_db, db3, 0.108)
