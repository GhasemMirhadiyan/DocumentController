

# Receive Data include Tags File in List to Checking
def verification(tags):
    a = []
    b = []
    FileHoldTag = ''
    length = 0
    count = 0
    for item in tags:

        # delete first number such as 1074-TGD-158 >> 074-TGD-158
        if str(item[0]) == '':
            print(item)
            item = str(item)
            item = item[1:]
            a.append(item)
        # delete 074-TGD-1340 >> 074-TGD-134
        elif len(item) == 12 and str(item[3]) == '-' and str(item[0:2]).isdigit():
            item = item[:11] + item[11 + 1:]
            a.append(item)
        # 01-JCF-A0230 >> 01-JCF-A023
        elif len(item) == 12 and str(item[11:12]).isdigit() and str(item[11:12]) == '0':
            item = item[:11] + item[11 + 1:]
            a.append(item)
        # 074-GD-1370 >> 074-GD-137
        elif len(item) == 11 and str(item[10:11]).isdigit() and str(item[10:11]) == '0':
            item = item[:10] + item[10 + 1:]
            a.append(item)
        elif len(item) == 13 and str(item[12:13]).isdigit() and str(item[12:13]) == '0':
            item = item[:12] + item[12 + 1:]
            a.append(item)
        elif len(item) >= 15:
            b.append(item)
        else:
            a.append(item)
    # Sort and Delete Duplicate Tag

    result = [*set(a)]
    for item in result:
        count += length
        FileHoldTag += (str(item) + ', ')
    return count, result, FileHoldTag


