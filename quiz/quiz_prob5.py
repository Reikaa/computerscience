def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    total = sum(L)
    for num in range(1,len(L)):
        for ind in range(0,len(L)):
            if ind+num-1 < len(L):
                temp = sum(L[ind:ind+num])
                if temp > total:
                    total = temp
    return total
