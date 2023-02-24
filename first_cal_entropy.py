import numpy as np
ori_words = np.load("data_sourse\words_for_version2.npy",allow_pickle=True)
from function import cal_info_entropy
ori_words = cal_info_entropy(ori_words)
np.save("data_sourse/first_cal_entropy.npy",ori_words)