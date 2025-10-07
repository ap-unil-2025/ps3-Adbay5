def find_longest_word(filename):

    with open("test.txt", 'r') as f:
        text = f.read().replace(",","").replace(".","")
        words =text.split()
        element =words[0]
        for i in range(len(words)):
            if len(words[i])>len(element):
                element = words[i]
        return element



print(find_longest_word("test.txt"))