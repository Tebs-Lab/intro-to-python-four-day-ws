# The prefered way to open a text file in Python looks like this:
# The long string is the path to the file, the 'r' means "read mode" which can also be "w" for write mode
# 'rb' and 'wb' are available for "raw byte" mode, which you may eventually have reason to use but for now 
# we're going to ignore those options.
with open('book-texts/frankenstein-no-header-footer.txt', 'r') as franken_reader:
    # The type of franken_reader is a <class '_io.TextIOWrapper'>
    print(type(franken_reader))
    
    # This type has some interesting methods.
    ## .read() will process the whole file and we can put it in a string
#     whole_text = franken_reader.read()
#     print(whole_text)

    # NOTE: Once the file has been "read" it cannot be read a second time
    # in fact reading any part of the file "consumes" that section. So if you run the followingg
    # code without commenting out the above call to "read()" nothing will be output.

    # Read, with a parameter, will read the specified number of bytes
#     first_50_bytes = franken_reader.read(50)
#     print(first_50_bytes)
    
    # Readline can be used to read one line at a time. 
    first_line = franken_reader.readline()
    print(first_line)


# A counter is a dictionary where the default value for every key is 0.
from collections import Counter

word_counts = Counter()

with open('book-texts/frankenstein-no-header-footer.txt', 'r') as franken_reader:
    line = franken_reader.readline()
    
    # The final line will be an empty string
    # No other lines (even blank ones) will be the empty string
    # An empty line will instead be the newline character "\n"
    while line != '':
        # The split function turns a string into an array of words based on 
        # where the whitespace characters are. You can split on other characters too!
        words = line.split() 
        
        for word in words:
            word_counts[word] += 1
            
        line = franken_reader.readline()
        
        
# Now that we have the word counts... Lets check them out!
for count in word_counts.most_common():
    print(count)
    
# If you look carefully there are some odd ones that we'd need better processing
# # to handle. Here are some examples:
#     ('contumely?', 1)
#     ('at,', 1)
#     ('“Fear', 1)
#     ('“Farewell!', 1)

# It turns out, python has a lot of great stuff built in, including a solution to this problem...
import string
word_counts = Counter()

with open('book-texts/frankenstein-no-header-footer.txt', 'r') as franken_reader:
    line = franken_reader.readline()
    
    # The final line will be an empty string
    # No other lines (even blank ones) will be the empty string
    # An empty line will instead be the newline character "\n"
    while line != '':
        # Lets lowercase everything so we don't count A and a separately.
        line = line.lower()
        
        # explaination of maketrans: https://www.geeksforgeeks.org/python-maketrans-translate-functions/
        # replace hyphen (EM AND EN DASH) with space, 
        line = line.translate(str.maketrans('-—', '  '))
        
        # remove anything in string.punctuation and the two weird quotes
        line = line.translate(str.maketrans('', '', string.punctuation + '“' + '”'))
        
        # The split function turns a string into an array of words based on 
        # where the whitespace characters are. You can split on other characters too!
        words = line.split() 
        "hello--world"
        for word in words:
            word_counts[word] += 1
            
        line = franken_reader.readline()
        
        
# Now that we have the word counts... Lets check them out!
for count in word_counts.most_common():
    print(count)

# Regular Expressions

# When working with text, especially when searching for patterns in text, regex is incredibly useful. Lets look at some of the basics.

# * Regex offers some very fancy features that can be very helpful...
#     * `.` is regex's version of `_` — it matches any one character.
#     * `*` and `+` are quantitative operations that modify the previous character:
#         * `.*` means "0 or more of any character"
#         * `.+` means "one or more of any character"
#         * `a+` means "one or more a's in a row"
#     * More specific quantitive operations use `{}`
#         * `a{1,3}` means between 1 and 3 a's in a row.
#         * The `?` can modify any other of these quantifiers to make it "greedy" which means it matches the shortest possible match. By default regex matches the longest possible match 
        
# * Character classes are grouped in `[]`
#     * A character class is a set of characters to match.
#     * The `-` is used to specify characters "between" each other, which has to do with the `ASCII` and `Unicode` formats and their lookup tables.
#     * But simply, `[a-z]` means all the lowercase letters from a to z. `[a-zA-Z] means all lower and uppercase letters.
#     * `[aeiou]` means any of the vowels. 
# * Character classes can be combined with the numerical operators!
    
# * `^` matches the start of a string and `$` matches the end of a string.

# Lets see some examples in action:
import re # this is the regular expression library built into python

book_text = ''

with open('book-texts/frankenstein-no-header-footer.txt', 'r') as franken_reader:
    # This code reads the book line by line, and strips out newlines unless
    # they appear on a line by themselves. Essentially leaving in only line breaks
    # that are paragraph breaks!
    line = franken_reader.readline()
    while line != '':
        if line == '\n':
            book_text += line
        else:
            book_text += line.replace("\n", ' ')

        line = franken_reader.readline()
        
print(book_text)

# Find words with two vowels in a row in them
dual_vowel_words = ' [a-zA-Z]*[aeiouyAEIOUY]{2}[a-zA-Z]* '

double_vowel_instances = re.findall(dual_vowel_words, book_text)
for dv in double_vowel_instances:
    print(dv)

# Finally, for completeness, lets also write back some data to a file. 
# Specifically, lets make a CSV from the word counts we computed above:
with open('book-texts/fs-word-counts.csv', 'w') as wc_csv:
    # This line is the CSV header
    line = 'word,count\n'
    wc_csv.write(line)
    
    for word, count in word_counts.items():
        # This is a "string interpolation" syntax. Variables inside {}'s get replaced with
        # The value of the variable.
        line = f'{word},{count}\n'
        wc_csv.write(line)