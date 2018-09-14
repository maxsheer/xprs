from xml.dom.minidom import *
from tkinter import *


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("lolkek")

    def cbutton(self, master):
        c = Button(master, text="close")
        c['command'] = master.destroy
        c.grid(row=r5, column=2)

    def ebutton(self, master):
        e = Button(master, text="edit")
        e['command'] = master.destroy
        e.grid(row=r5, column=3)

    def sbutton(self, master):
        e = Button(master, text="save")
        e['command'] = master.destroy
        e.grid(row=r5, column=4)


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
        self.accepts = []

    def getDoc(self, dpath):
        f = open(dpath)
        doc = xml.dom.minidom.parse(f)
        return doc

    def getNode(self, eldoc):   # get rootnode elements
        node = eldoc.documentElement
        if node.nodeType == xml.dom.Node.ELEMENT_NODE:
            print(node.nodeName)
        return node

    def getQs(self, node):    # get subobjects by tagname
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

    def getAccepted(self, node):
        votes = node.getElementsByTagName('VoteRslt')
        for q in votes:
            e = q.getElementsByTagName('Accptd')
            for i in e.childNodes:
                if i.nodeType == i.TEXT_NODE:
                    self.accepts.append(i.data)


root = Tk()
root.geometry("800x800")
M = MyFirstGUI(root)

my_list_of_entriesf = []
my_list_of_entriesa = []
my_list_of_entriesab = []
my_list_of_entriesn = []
my_list_of_labels = []
my_list_of_accepts = []
acvar = []

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
print('accepts')
D.getAccepted(D.getNode(D.getDoc(D.path)))
print(D.accepts)

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
    my_list_of_labels.append(Entry(root))
    my_list_of_labels[-1].insert(0, i)
    my_list_of_labels[-1].grid(row=r1, column=0)
    my_list_of_labels[-1].config(state="readonly")
    r1 += 1

r2 = 1
for i in D.votesfr:
    my_list_of_entriesf.append(Entry(root))
    my_list_of_entriesf[-1].insert(0, i)
    my_list_of_entriesf[-1].grid(row=r2, column=1)
    my_list_of_entriesf[-1].config(state="readonly")
    r2 += 1

r3 = 1
for i in D.votesag:
    my_list_of_entriesa.append(Entry(root))
    my_list_of_entriesa[-1].insert(0, i)
    my_list_of_entriesa[-1].grid(row=r3, column=2)
    my_list_of_entriesa[-1].config(state="readonly")
    r3 += 1

r4 = 1
for i in D.votesab:
    my_list_of_entriesab.append(Entry(root))
    my_list_of_entriesab[-1].insert(0, i)
    my_list_of_entriesab[-1].grid(row=r4, column=3)
    my_list_of_entriesab[-1].config(state="readonly")
    r4 += 1

r5 = 1
for i in D.votesna:
    my_list_of_entriesn.append(Entry(root))
    my_list_of_entriesn[-1].insert(0, i)
    my_list_of_entriesn[-1].grid(row=r5, column=4)
    my_list_of_entriesn[-1].config(state="readonly")
    r5 += 1

r6 = 1
for i in D.accepts:
    my_list_of_accepts.append(Checkbutton(root))
    acvar.append()
    my_list_of_accepts[-1].grid(row=r6, column=5)
    my_list_of_accepts[-1].config(state="readonly")
    r6 += 1

M.cbutton(root)
M.ebutton(root)
M.sbutton(root)
root.mainloop()
