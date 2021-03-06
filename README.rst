shared\_ndarray
===============

A pickleable wrapper for sharing NumPy ndarrays between processes using
Python 3.8 shared memory.

SharedNDArrays are designed to be sent over multiprocessing.Pipe and Queue
without serializing or transmitting the underlying ndarray or buffer. While the
associated file descriptor is closed when the SharedNDArray is garbage
collected, the underlying buffer is not released when the process ends: you
must manually call the ``unlink()`` method from the last process to use it.

Usage
-----

.. code:: python

    import multiprocessing as mp

    import numpy as np
    from shared_ndarray import SharedNDArray

    def child(shm):
        print(shm.array)

    if __name__ == '__main__':
        try:
            shm = SharedNDArray((4, 4))
            shm.array[0, 0] = 1
            p = mp.Process(target=child(shm))
            p.start()
            p.join()
        finally:
            shm.unlink()

This should print::

    [[ 1.  0.  0.  0.]
     [ 0.  0.  0.  0.]
     [ 0.  0.  0.  0.]
     [ 0.  0.  0.  0.]]

There are also convenience methods to create a new SharedNDArray from an
existing NumPy array:

.. code:: python

    arr = np.array([0, 0])
    shm1 = SharedNDArray.copy(arr)
    shm2 = SharedNDArray.zeros_like(arr)
    shm1.unlink()
    shm2.unlink()

Dependencies
------------

- `numpy <http://www.numpy.org>`_
- Requires Python >= 3.8
