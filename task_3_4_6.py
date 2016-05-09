import requests as req
import re

# A = 'https://en.wikipedia.org/wiki/Main_Page'  # input()
A = 'https://stepic.org/media/attachments/lesson/24472/sample0.html'  # input()
B = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'  # input()

REGEX = r'<a.*href=[\'"](\S+)[\'"].*>.*<\/a>'

def can_reach(A, B):
    try:
        resA = req.get(A)
        textA = resA.text
        for C in re.findall(REGEX, textA):
            # print(C)
            try:
                resC = req.get(C)
                textC = resC.text
                for link_in_C in re.findall(REGEX, textC):
                    if link_in_C == B:
                        print('Yes')
                        return
            except:
                pass
    except:
        pass
    print('No')
can_reach(A, B)
