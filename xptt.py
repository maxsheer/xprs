from xml.etree import ElementTree as et

tree = et.parse("t2.xml")
a = tree.findall('Document/MtgRsltDssmntn/voting/VoteRslt/For')
for i in a:
    i.text = '111111'
    print(i.text)
tree.write("lolkek.xml", encoding="windows-1251")
