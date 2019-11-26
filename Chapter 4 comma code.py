def stringify(spam):
    new_string = ''
    for i in range(0,len(spam)-2):
        new_string += spam[i] + ', '
    new_string += 'and ' + spam[-1]
    print(new_string)
    return new_string

eggs = ['spork', 'spoon', 'fork', 'knife']
stringify(eggs)
    
bacon = ['dasher', 'dancer', 'prancer', 'vixen', 'comet', 'cupid', 'donner', 'blitzen', 'rudolph']
stringify(bacon)
