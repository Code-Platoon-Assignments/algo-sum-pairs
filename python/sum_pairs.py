def sum_pairs(intArr, target):
    '''takes a list of ints and a target. returns a list of all pairs of values within in the list that add up to target (compliment eachother). Return a string if none are found'''
    hash_map = {} # initilize a dict to store hash map (number index pairs)
    answer_pairs = [] # initilize a list to store complimentary number pairs
    for i, number in enumerate(intArr): # for each index number pair in enumerate intArr
        compliment = target - number # calculate the compliment
        if compliment in hash_map: # if the compliment is already in the hash map
            answer_pairs.append([compliment, number]) # append the number and compliment into the answer_pairs array
        hash_map[number] = i # update the hash map with a number index pair

    if len(answer_pairs)>0: # if there are any answers in the answer_pairs array
        return answer_pairs # return the array
    return 'unable to find pairs' # else return string