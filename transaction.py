import pandas as pd
import numpy as np

df = pd.read_csv("mempool.csv")

#sorting in descending order of fee
sorted_df = df.sort_values(by=["fee"], ascending=False)

a_dataframe = pd.DataFrame(sorted_df['tx_id'])
#displaying the tx_id in a text file
numpy_array = a_dataframe.to_numpy()
np.savetxt("block.txt", numpy_array, fmt = " %s")