#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    
    res_error = abs(predictions - net_worths)
    zipped_out = zip(ages, net_worths, res_error)
    from operator import itemgetter
    zipped_out.sort(key = itemgetter(2))
    cleaned_data =  zipped_out[:(len(zipped_out)*9/10)]

    
    return cleaned_data

