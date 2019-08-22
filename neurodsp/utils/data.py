"""Data related utility functions."""

import numpy as np

###################################################################################################
###################################################################################################

def create_freqs(freq_start, freq_stop, freq_step=1):
    """Create an array of frequencies.

    Parameters
    ----------
    freq_start : float
        Starting value for the frequency definition.
    freq_stop : float
        Stopping value for the frequency definition, inclusive.
    freq_step : float, optional, default=1
        Step value, for linearly spaced values between start and stop.

    Returns
    -------
    1d array
        Frequency indices.
    """

    return np.arange(freq_start, freq_stop + freq_step, freq_step)


def create_times(n_seconds, fs, start_val=0.):
    """Create an array of time indices.

    Parameters
    ----------
    n_seconds : float
        Signal duration, in seconds.
    fs : float
        Signal sampling rate, in Hz.
    start_val : float, optional, default=0.
        Starting value for the time definition.

    Returns
    -------
    1d array
        Time indices.
    """

    return np.arange(start_val, n_seconds, 1/fs)


def create_samples(n_samples, start_val=0):
    """Create an array of sample indices.

    Parameters
    ----------
    n_seconds : int
        Number of sample.
    start_val : int, optional, default=0
        Starting value for the samples definition.

    Returns
    -------
    1d array
        Sample indices.
    """

    return np.arange(start_val, n_samples, 1)
