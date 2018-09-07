from xml.dom.minidom import *
from tkinter import *


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("lolkek")

    def close_window(self, master):
        master.quit()





class xprs:
    def __init__(self, dpath):
        self.path = dpath
        self.votesfr = []
        self.questions = []
        self.descs = []
        self.votesag = []
        self.votesab = []
        self.votesna = []
        self.labls = []

    def getDoc(self, dpath):
        f = open(dpath)
        doc = xml.dom.minidom.parse(f)
        return doc

    def getNode(self, eldoc):
        node = eldoc.documentElement
        if node.nodeType == xml.dom.Node.ELEMENT_NODE:
            print(node.nodeName)
        return node

    def getQs(self, node):
        votes = node.getElementsByTagName('VoteRslt')
        for q in votes:
            e = q.getElementsByTagName('IssrLabl')[0]
            for i in e.childNodes:
                if i.nodeType == i.TEXT_NODE:
                    self.labls.append(i.data)

    def getVotesFor(self, node):
        votes = node.getElementsByTagName('VoteRslt')
        for q in votes:
            try:
             e = q.getElementsByTagName('For')[0]
             for i in e.childNodes:
                if i.nodeType == i.TEXT_NODE:
                    self.votesfr.append(int(i.data))
            except:
             self.votesfr.append(0)

    def getVotesAgnst(self, node):
        votes = node.getElementsByTagName('VoteRslt')
        for q in votes:
            try:
             e = q.getElementsByTagName('Agnst')[0]
             for i in e.childNodes:
                if i.nodeType == i.TEXT_NODE:
                    self.votesag.append(int(i.data))
            except:
             self.votesag.append(0)

    def getVotesAbstn(self, node):
        votes = node.getElementsByTagName('VoteRslt')
        for q in votes:
            try:
             e = q.getElementsByTagName('Abstn')[0]
             for i in e.childNodes:
                if i.nodeType == i.TEXT_NODE:
                    self.votesab.append(int(i.data))
            except:
             self.votesab.append(0)

    def getVotesNoActn(self, node):
        votes = node.getElementsByTagName('VoteRslt')
        for q in votes:
            try:
                e = q.getElementsByTagName('NoActn')[0]
                for i in e.childNodes:
                    if i.nodeType == i.TEXT_NODE:
                        self.votesna.append(int(i.data))
            except:
                self.votesna.append(0)


root = Tk()
root.geometry("800x800")
M = MyFirstGUI(root)

my_list_of_entriesf = []
my_list_of_entriesa = []
my_list_of_entriesab = []
my_list_of_entriesn = []
my_list_of_labelsf = []
my_list_of_labelsab = []
my_list_of_labelsn = []
my_list_of_labelsa = []
my_list_of_entries = []
my_list_of_labels = []

D = xprs('t2.xml')
D.getQs(D.getNode(D.getDoc(D.path)))

print(D.labls)
print('votesfor')
D.getVotesFor(D.getNode(D.getDoc(D.path)))
print(D.votesfr)
print('votesab')
D.getVotesAbstn(D.getNode(D.getDoc(D.path)))
print(D.votesab)
print('votesag')
D.getVotesAgnst(D.getNode(D.getDoc(D.path)))
print(D.votesag)
print('votesna')
D.getVotesNoActn(D.getNode(D.getDoc(D.path)))
print(D.votesna)

C = len(D.votesna)

N1 = Label(root, text="for")
N1.grid(row=0, column=1)

N2 = Label(root, text="Labls")
N2.grid(row=0, column=0)

N3 = Label(root, text="Against")
N3.grid(row=0, column=2)

N4 = Label(root, text="Abstained")
N4.grid(row=0, column=3)

N5 = Label(root, text="No Action")
N5.grid(row=0, column=4)

r1 = 1

for i in D.labls:
    my_list_of_entries.append(Entry(root))
    my_list_of_entries[-1].insert(0, i)
    my_list_of_entries[-1].grid(row=r1, column=0)
    r1 += 1

r2 = 1
for i in D.votesfr:
    my_list_of_entries.append(Entry(root))
    my_list_of_entries[-1].insert(0, i)
    my_list_of_entries[-1].grid(row=r2, column=1)
    r2 += 1

r3 = 1
for i in D.votesag:
    my_list_of_entries.append(Entry(root))
    my_list_of_entries[-1].insert(0, i)
    my_list_of_entries[-1].grid(row=r3, column=2)
    r3 += 1

r4 = 1
for i in D.votesab:
    my_list_of_entries.append(Entry(root))
    my_list_of_entries[-1].insert(0, i)
    my_list_of_entries[-1].grid(row=r4, column=3)
    r4 += 1

r5 = 1
for i in D.votesna:
    my_list_of_entries.append(Entry(root))
    my_list_of_entries[-1].insert(0, i)
    my_list_of_entries[-1].grid(row=r5, column=4)
    r5 += 1

close_button = Button(root, text="Close", command=M.close_window(root))
close_button.grid(row=r5, column=2)

root.mainloop()
