# Regular Expressions

# Regular Expressions (sometimes shortened to regexp, regex, or re) are a tool for matching patterns in text. In Python, we have the re module. The applications
#  for regular expressions are wide-spread, but they are fairly complex, so when contemplating using a regex for a certain task, think about alteranatives, and
#  come to regexes as a last resort

# An example regex is r"^(From|To|Cc).*?python-list@python.org" Now for an explanation
# 1. The caret ^ matches text at the beginning of a line.
# 2. The following group, the part with (From|To|Cc) means, that the line has to start with one of the words that are separated by the pipe | which is the OR 
#  operator, and the regex will match if the line starts with any of the words in the group.
# 3. The .*? means to un-greedily match any number of characters, except the newline \n character. 
    # 3. i. Un-greedy here means to match as few repetitions as possible. 
# 3. ctd: The . character means any non-newline character, the * means to repeat 0 or more times, and the ? character makes it un-greedy

# So, the following lines would be matched by that regex: From: python-list@python.org To: !asp]<,. python-list@python.org

# A complete reference for the syntax is available at https://docs.python.org/3/library/re.html#regular-expression-syntax%22RE%20syntax

# As an example of a "proper" email-matching regex (like the one in this exercise), see the following example:

# import re
# pattern = re.compile(r"\[(on|off)\]") # Slight optimisation
# print(re.search(pattern, "Mono: Playback 65 [75%] [-16.50dB] [on]")) # Returns a Match object! (because the phrase on is there)
# print(re.search(pattern, "Nada...:-(")) # Doesn't return anything.

# Exercise
# Make a regular expression that will match an email

import re

def test_mail(your_pattern):
    pattern = re.compile(your_pattern)
    emails = ["jogn@example.com", "python-list@python.org", "wha.t`1an?ug{}ly@email.com"]
    for email in emails:
        if not re.match(pattern, email):
            print("You failed to match %s" % (email))
        elif not your_pattern:
            print("Forgot to enter a pattern!")
        else:
            print("Pass")

pattern = r"^.*@(?=[^<>()\[\]\.,;:\s@\"])[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$" # Your pattern here!
# Note: The following comments show the selection of operators being used in the regex and their purpose. The most noteable ideas here is the stacking of 
# operators, and conditions in the sequence of the string, as well as positive lookahead (looking for stuff to match and stuff that, if there, means not a match)
# ^.* matches anything before the @ from the start of the string
# The @ after means to match an @ after any characters
# The (?=[^ . . . .]) means the positive lookahead of not containing any of the characters enclosed in [] immediately after the @
# The following [. . .]+ is all acceptable characters expected, and it allows dots
# The \. allows us to look for the "." character which is an operator but the \ lets us search for it. This is after the previous searches
# The last box is all the acceptable characters after the dot
# The {2,} means it has to be a minimum of two letters long
# The $ means end of string

test_mail(pattern)