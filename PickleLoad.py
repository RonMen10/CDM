import pickle
import pandas as pd

pickle_in = open(r"C:\test\Archives\0.05_0.05_0.05_0.05.pkl","rb")
example_dict = pickle.load(pickle_in)
print(example_dict)
df = pd.DataFrame.from_dict(data=example_dict, orient='index')
df.transpose().to_csv("C:\test\Archives\train_withid.csv")