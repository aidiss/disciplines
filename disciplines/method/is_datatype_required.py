# -*- coding: utf-8 -*-
def is_datatype_required(data, datatype, theory, complete=False):
    """Checks whether datatype is 

    Args:
            data : link to database, dataframe or to ontology (networkx) object.
            datatype (: (persons, events, texts, citations ) # Or combined
            complete (Boolean) : True for complete info.

    Returns:
            result (int[0:5]) : where the higher int the bigger importance """
    result = ''

    def is_required(data):
        return

    for data in theory:
        if is_required(data):
            result[data] = True  # Or details
            if complete == True:
                result[data] = "more info about how it is required"
    return False
