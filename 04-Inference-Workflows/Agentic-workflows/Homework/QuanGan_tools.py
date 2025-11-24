from typing import Any, Dict, Literal
import os
from langchain_core.tools import tool

from ase.io import write as ase_write
from ase import Atoms
import numpy as np


@tool
def calc_CCRF_amplifier_wavenumber(frequency: float) -> Dict[str, Any]:
    """Calculate CCRF_Amplifier wavenumber under certain frequency.

    Parameters
    ----------
    frequency : float
        The frequency of the input signal (GHz) 

    Returns
    -------
    dict
        postitive propagation statu,wavenumber of the CCRF_Amplifier (m^(-1)), input frequency 
    
    """
    
    c = 3e8;
    pi = 3.14;
    D = 2.5e-2;
    omega = 2*pi*frequency*1e9; 
    xg = 4e-2;
    kn=0.4*omega/c*np.tan(omega*D/c)/xg;
    
    if kn>0:
        stat = True;
    else:
        stat = False;

    return {
        "postitive propagation status": stat,
        "wavenumber": kn,
        "frequency": frequency,
    }