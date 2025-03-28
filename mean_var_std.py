import numpy as np # type: ignore

def calculate(list):
    mean =[]
    variance = []
    standardDeviation = []
    maximum = []
    minimum = []
    total = []

    try:

        arr = np.reshape(list, (3, 3))
    except:
      raise ValueError( "List must contain nine numbers.")    
    
    mean.append(np.mean(arr, axis=0).tolist())
    mean.append(np.mean(arr, axis=1).tolist())
    mean.append(np.mean(arr).tolist())

    variance.append(np.var(arr, axis=0).tolist())
    variance.append(np.var(arr, axis=1).tolist())
    variance.append(np.var(arr).tolist())

    standardDeviation.append(np.std(arr, axis=0).tolist())
    standardDeviation.append(np.std(arr, axis=1).tolist())
    standardDeviation.append(np.std(arr).tolist())

    maximum.append(np.amax(arr, axis=0).tolist())
    maximum.append(np.amax(arr, axis=1).tolist())
    maximum.append(np.amax(arr).tolist())

    minimum.append(np.amin(arr, axis=0).tolist())
    minimum.append(np.amin(arr, axis=1).tolist())
    minimum.append(np.amin(arr).tolist())

    total.append(np.sum(arr, axis=0).tolist())
    total.append(np.sum(arr, axis=1).tolist())
    total.append(np.sum(arr).tolist())

    calculations = {
    'mean': mean,
    'variance': variance,
    'standard deviation': standardDeviation,
    'max': maximum,
    'min': minimum,
    'sum': total
  }
    
    return calculations