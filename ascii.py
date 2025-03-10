start = 97
end = 122

def ascii_to_alpha(start, end):
    for i in range(start, end+1):
        print(chr(i), end=",")
        
ascii_to_alpha(start=start, end=end)