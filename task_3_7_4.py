from xml.etree import ElementTree


def traverse(el, level):
    color = el.attrib['color']
    colors[color] += level
    for child in el:
        traverse(child, level + 1)


colors = {
    'red': 0,
    'green': 0,
    'blue': 0
}
try:
    root = ElementTree.fromstring(input())
    traverse(root, 1)
except:
    pass

print(str(colors['red']) + " " + str(colors['green']) + " " + str(colors['blue']))