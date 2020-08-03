import numpy as np
np.random.seed(9453)
from time_series_augmentation_toolkit import DN
import pickle

with open('labeldata.pkl','rb') as f:
    data = pickle.load(f)
    
output = []    
for d in data:
    this_output = d.copy()
    
    r = np.random.choice([3,5,10,15,20], size=4, p=[0.1,0.5,0.3,0.05,0.05])
    this_output['ohlc_data']['open'] = np.rint(DN(np.array(this_output['ohlc_data']['open']), sigma=r[0])).tolist()
    this_output['ohlc_data']['high'] = np.rint(DN(np.array(this_output['ohlc_data']['high']), sigma=r[1])).tolist()
    this_output['ohlc_data']['low'] = np.rint(DN(np.array(this_output['ohlc_data']['low']), sigma=r[2])).tolist()
    this_output['ohlc_data']['close'] = np.rint(DN(np.array(this_output['ohlc_data']['close']), sigma=r[3])).tolist()
    
    for i in range(this_output['index'][1] - this_output['index'][0] + 1):
        if this_output['ohlc_data']['high'][i] < this_output['ohlc_data']['low'][i]:
            this_output['ohlc_data']['high'][i], this_output['ohlc_data']['low'][i] = \
                this_output['ohlc_data']['low'][i], this_output['ohlc_data']['high'][i]
        
    output.append(this_output)
    
with open('labeldata_aug.pkl','wb') as f:
    pickle.dump(output, f)