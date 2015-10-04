# ======================================
#
# 1章コード写経
#
# ======================================

import os
from utils import DATA_DIR, CHART_DIR
import scipy as sp
import matplotlib.pyplot as plt

# データの読み込み
data = sp.genfromtxt(os.path.join(DATA_DIR, "web_traffic.tsv"), delimiter="\t")

# データの確認
print(data[:10])
print(data.shape)

# このファイルにあるすべての例は3つのクラスを持っている
colors = ['g', 'k', 'b', 'm', 'r']
linestyle = ['-', '-.', '--', ':', '-']
