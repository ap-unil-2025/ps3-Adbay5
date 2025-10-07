def count_characters(filename, include_spaces=True):

     with open(filename, 'r') as f:
        text = f.read()
        if include_spaces :
            return len(text)
        else :
            return len(text.replace(" ",""))


print(count_characters("test.txt",False))