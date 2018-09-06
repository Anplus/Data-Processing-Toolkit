import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

##
data = pd.read_csv("../input/train.csv", header=0)
test = pd.read_csv("../input/test.csv", header=0)

data.shape
