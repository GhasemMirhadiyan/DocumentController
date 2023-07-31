import re


# Receive PlainText From Pdf Document for Process with Regex
def TextProcess(message, file):
    test_str = message
    l: list = []
    regex = r"(\S{1,4}[--—]\w{1,4}[--—]\S{1,6}[--—]\S{1,4}[--—]\S{1,3}[--—]\S{1,3}[-]\S{1,3})|(\S{1,4}[-]\w{1,4}[-]\S{1,6}[-]\S{1,4}[-]\S{1,3}[-]\S{1,3})|(\S{1,4}[--—]\w{1,4}[--—- ]\S{1,6}[-]\S{1,4}[--—- ]\S{1,4})|(\S{1,5}[-]\w{1,4}[--—]\S{1,6}[-]\S{1,4})|(\d{1,4}[-]\w{1,4}[-]\S{1,6})|(\S{3,4}[-]\w{3,7})"
    #regex = '(^\S{1,4}[-]\w{1,4}[-]\S{1,6}[-]\S{1,4}$)|(^\d{1,4}[-]\w{1,4}[-]\S{1,6}$)|(^\S{3,4}[-]\w{3,7}\$)|(0\d{2}[-]\w{1,2}[-]\w{2,4})'

    matches = re.finditer(regex, test_str, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        a = match.group()
        l.append(a)

    return l
