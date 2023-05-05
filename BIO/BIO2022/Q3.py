[s,ith] = [x for x in input().split(' ')]
ith = int(ith) #input

def getLetters(pos): #gets all possible letters for each position
    pos = s.index(chr(pos+97))
    possible = [chr(pos+65)]
    for i in range(pos,0,-1):
        if ord(s[i])<ord(s[pos]):
            possible.append(chr(i+65))
    return ''.join(reversed(possible))

firstLetter = getLetters(0)
prefList = [firstLetter]

def solve(i):
    global ith
    if len(s)==len(prefList):#base case if all letters of preferred list are used.
        return
    else:#gets the total number of combinations for each starting letter and then adds the next letter if the combination count exceeds the
        possibleLetters = getLetters(i)
        for k in range(len(possibleLetters)):
            combs = 1
            for j in range(i+1,len(s)):
                combs *= len(getLetters(j))
            if combs>=ith:
                prefList.append(possibleLetters[k])
                return solve(i+1) #recurseion to find all the possible third letters from the first 2 letters (and so on for all the letters)
            else:
                ith -= combs

solve(1)
print(''.join(prefList)) #prints out all the letters joined together into a string