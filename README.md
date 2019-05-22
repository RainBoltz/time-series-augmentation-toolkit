# Time series Augmentation Toolkit
A simple toolkit that helps researchers or specialists to generate more training dataset by augmentation!

## Requirements
  - numpy>=1.12
    
## Implementations
  1. **Distributed Noise (DN)**:
    | adding a noise with defined distribution
  2. **Window Slicing (WS)**:
    | extracting slices from time series and recombine the them together in orders
  3. **Window Warping (WW)**:
    | warping a randomly selected slice of a time series by speeding it up or down
  4. **Dataset Mixing (DM)**:
    | tune the extrapolating between time series in feature space
  
    
## Functions
  ```python
  def DN(ts, sigma=0.0, mu=1.0, alpha=1.0, random_seed=None):
    '''
    ts: np.array, time series data
    sigma: float, standard deviation of the noise distribution
    mu: float, mean of the noise distribution
    alpha: float, the ratio of changes (new_value = alpha * delta + original_value)
    random_seed: int, set numpy random seed
    '''
  
  ################ TODO BELOW ################
  def WS(ts_set, n=None, random_seed=None):
    '''
    ts_set: np.ndarray, time series dataset
    slicing_size: int, size of the sliced series, if None then default to 1/4 data length
    random_seed: int, set numpy random seed
    '''
  
  def WW(ts, n=None, alpha=0.5, random_seed=None):
    '''
    ts: np.array, time series data
    n: int, influence range (+/-n values), if None then default to 1
    alpha: float, the ratio of streching
    random_seed: int, set numpy random seed
    '''
    
  def DM(ts_set, random_seed=None):
    '''
    ts_set: np.ndarray, time series dataset
    
    //TODO
    
    random_seed: int, set numpy random seed
    '''
  ```  
  
## References
  1. Le Guennec, Simon Malinowski, and Romain Tavenard: [Data Augmentation for Time Series Classification using Convolutional Neural Networks](https://aaltd16.irisa.fr/files/2016/08/AALTD16_paper_9.pdf)
  2. Terrance DeVries and Graham W. Taylor: [Dataset Augmentation in Feature Space](https://arxiv.org/pdf/1702.05538.pdf)