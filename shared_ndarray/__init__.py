"""A pickleable wrapper for sharing NumPy ndarrays between processes using POSIX shared memory."""

try:
    import multiprocessing.shared_memory
except ModuleNotFoundError as e:
    print('requires Python >= 3.8 shared_memory')
    raise e

from .shared_ndarray import SharedNDArray

SharedNDArrayError = Exception

__all__ = ['SharedNDArray', 'SharedNDArrayError']

__author__ = 'Katherine Crowson'
__copyright__ = 'Copyright 2017, Katherine Crowson, 2020 Gerd Langer converted to Python 3.8 shared_memory'
__credits__ = ['Katherine Crowson']
__license__ = 'MIT'
__maintainer__ = 'Katherine Crowson'
__email__ = 'crowsonkb@gmail.com'
