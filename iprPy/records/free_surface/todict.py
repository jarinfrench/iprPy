# Standard Python libraries
from __future__ import (absolute_import, print_function,
                        division, unicode_literals)

# https://github.com/usnistgov/DataModelDict
from DataModelDict import DataModelDict as DM

def todict(record, full=True, flat=False):
    """
    Converts the XML content of a record to a dictionary.
    
    Parameters
    ----------
    record : iprPy.Record
        A record of the record style associated with this function.
    full : bool, optional
        Flag used by the calculation records.  A True value will include
        terms for both the calculation's input and results, while a value
        of False will only include input terms (Default is True).
    flat : bool, optional
        Flag affecting the format of the dictionary terms.  If True, the
        dictionary terms are limited to having only str, int, and float
        values, which is useful for comparisons.  If False, the term
        values can be of any data type, which is convenient for analysis.
        (Default is False).
        
    Returns
    -------
    dict
        A dictionary representation of the record's content.
    """
    
    model = DM(record)

    proto = model['free-surface']
    params = {}
    params['key'] = proto['key']
    params['id'] = proto['id']
    params['family'] = proto['system-family']
    
    calcparam = proto['calculation-parameter']
    params['x_axis'] = calcparam['x_axis']
    params['y_axis'] = calcparam['y_axis']
    params['z_axis'] = calcparam['z_axis']
    params['atomshift'] = calcparam['atomshift']
    params['cutboxvector'] = calcparam['cutboxvector']
    
    return params