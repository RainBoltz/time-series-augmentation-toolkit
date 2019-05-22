# Time series Augmentation Toolkit
A simple toolkit that helps researchers or specialists to generate more training dataset by augmentation!

## Requirements
  - numpy>=1.12
    
## Implementations
  1. **Distributed Noise (DN)**: adding a noise with defined distribution
  2. **Window Slicing (WS)**: extracting slices from time series and performing classification at the slice level
  3. **Window Warping (WW)**: warping a randomly selected slice of a time series by speeding it up or down
  4. **Extrapolating (EXP)**: extrapolating between samples in feature space
  
    
## Functions
  ```python
  def DN():
    ...
  
  def WS():
    ...
  
  def WW():
    ...
    
  def EXP():
    ...
  ```  
  
## References
  1. Le Guennec, Simon Malinowski, and Romain Tavenard: [Data Augmentation for Time Series Classification using Convolutional Neural Networks](https://aaltd16.irisa.fr/files/2016/08/AALTD16_paper_9.pdf)
  2. Terrance DeVries and Graham W. Taylor: [Dataset Augmentation in Feature Space](https://arxiv.org/pdf/1702.05538.pdf)