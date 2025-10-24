# 4.1.2 Reading Local Files

# Basic
f = open ('document .txt ', 'r', encoding ='utf -8 ')
content = f. read ()
print ( len ( content )) # print the length of the text

# Better
with open ('document .txt ', 'r', encoding ='utf -8 ') as f:
    content2 = f. read ()
print ( len ( content2 )) # print the length of the text

# Better: Line-by-line
with open ('document .txt ', 'r', encoding ='utf -8 ') as f:
    for line in f:
        print ( line ) # print the current line