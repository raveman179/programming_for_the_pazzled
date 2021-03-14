word = "BWWWWWBWWW"
run = "1B5W1B3W"

def runlength(word: str) -> str:
    result = ""
    if word[0].isalpha():
        start = word[0]      
        count = 1
        for i in range(1, len(word)):
            if word[i] == word[i-1]:
                count += 1
            else:
                result += str(count) + start
                start = word[i]
                count = 1
        else:
            result += str(count) + start
    else:
        for i in range(0, len(word), 2):
            w = word[i:i+2]
            result += w[1]*int(w[0])
            
    return result

print(runlength(run))