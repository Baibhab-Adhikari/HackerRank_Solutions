def minion_game(string):
    
    vowels = "AEIOU"  # string of vowels
    kevin_scores = stuart_scores = 0  # initialize player scores
    length = len(string)  # length of the string
    
    # iterate through the given string
    for i in range(length):
        if string[i] in vowels:
            kevin_scores += length - i  # after every iteration, letter combinations reduce
        else:
            stuart_scores += length - i  # after every iteration, letter combinations reduce
    
    # winning scenarios
    if kevin_scores > stuart_scores:
        print(f"Kevin {kevin_scores}")
            
    elif kevin_scores < stuart_scores:
        print(f"Stuart {stuart_scores}")
        
    else:
        print("Draw")  # scores are tied    

if __name__ == "__main__":
    s = input()
    minion_game(s)