import xml.dom.minidom
import urllib.request


class ApptParser(object):

    def __init__(self, url, flag='url'):
        self.list = []
        self.appt_list = []
        self.flag = flag
        self.rem_value = 0
        xml = self.getXml(url)
        self.handleXml(xml)



    def getXml(self, url):
        try:
            print(url)
            f = urllib.request.urlopen(url)
        except:
            f = url

        doc = xml.dom.minidom.parse(f)
        node = doc.documentElement
        if node.nodeType == xml.dom.Node.ELEMENT_NODE:
            print('Элемент: %s' % node.nodeName)
            for (name, value) in node.attributes.items():
                print(' Attr -- имя: %s значение: %s' % (name, value))

        return node

    def handleXml(self, xml):
        rem = xml.getElementsByTagName('zAppointments')
        appointments = xml.getElementsByTagName("appointment")
        self.handleAppts(appointments)

    def getElement(self, element):
        return self.getText(element.childNodes)

    def handleAppts(self, appts):
        for appt in appts:
            self.handleAppt(appt)
        self.list = []

    def handleAppt(self, appt):
        begin = self.getElement(appt.getElementsByTagName("begin")[0])
        duration = self.getElement(appt.getElementsByTagName("duration")[0])
        subject = self.getElement(appt.getElementsByTagName("subject")[0])
        location = self.getElement(appt.getElementsByTagName("location")[0])
        uid = self.getElement(appt.getElementsByTagName("uid")[0])

        self.list.append(begin)
        self.list.append(duration)
        self.list.append(subject)
        self.list.append(location)
        self.list.append(uid)
        print(self.list)
        if self.flag == 'file':
            try:
                state = self.getElement(appt.getElementsByTagName("state")[0])
                self.list.append(state)
                alarm = self.getElement(appt.getElementsByTagName("alarmTime")[0])
                self.list.append(alarm)
            except Exception as e:
                print(e)

        self.appt_list.append(self.list)

    def getText(self, nodelist):
        rc = ""
        for node in nodelist:
            if node.nodeType == node.TEXT_NODE:
                rc = rc + node.data
        return rc
appt = ApptParser("appt.xml")
print(appt.list)