from collections import Counter

def most_frequent(data):
    """
        determines the most frequently occurring string in the sequence.
    """
    # your code here
    
    counter = Counter(data)
    max_value = max(counter.values())
    
    x = counter.keys()
    for i in x:
        y = counter[i]
        if y == max_value:
            ans = i
            print(ans)
    
    
    return ans


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')
