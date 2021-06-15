word = input("Enter a Word or number to see all their possible permutations: ")

def permutation(word):
    # when length is only one
    if len(word) == 1:
        return [word]
    
    #when length greater than one
    permutations = permutation(word[1:])
    char = word[0]
    result = []

    for perm in permutations:
        for i in range(len(perm) +1) :
            result.append(perm[:i] + char + perm[i:])

    return result

print(permutation(word))
