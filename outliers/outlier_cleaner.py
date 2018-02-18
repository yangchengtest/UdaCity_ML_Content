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
    sortlist=[]
    ### your code goes here
    for index in range(len(predictions)):
        dap=abs(predictions[index]-net_worths[index])
        sortlist.append((index,dap))
    newsortlist=sorted(sortlist, key = lambda sortlist:sortlist[1], reverse = True)
    print newsortlist
    for index1 in range(len(predictions)):
        isClean=False
        for index2 in range(len(newsortlist)/10):
            if (index1==newsortlist[index2][0]):
                isClean=True
        if (not isClean):
            cleaned_data.append((ages[index1],net_worths[index1],None))
    print cleaned_data
    return cleaned_data

