

from py2neo import Graph, Node, Relationship
import os
import xlrd

def getIndex(L,value):
    a=0
    for i in range(len(L)):
            if L[i][1] == value:
                a = i
    return a
def data_preparation(bcow_file):
    txt = open(bcow_file)
    txt_data = txt.readlines()
    prepared_data = []
    pre_data2=[]
    pre_data3 = []
    for line in txt_data:
        datalist = [line[0:1].replace(' ', ''), line[1:5].replace(' ', ''), line[5:6].replace(' ', ''), line[6:13],
                    line[13:16].replace(' ', ''), line[16:19].replace(' ', ''), line[19:22].replace(' ', ''), line[22:23].replace(' ', ''),
                    line[23:24].replace(' ', ''), line[24:25].replace(' ', ''), line[25:26].replace(' ', ''), line[26:29].replace(' ', ''),
                    line[30:37], line[37:40].replace(' ', ''), line[40:43].replace(' ', ''), line[43:46].replace(' ', ''),
                    line[46:47].replace(' ', ''), line[47:48].replace(' ', ''), line[48:49].replace(' ', ''), line[49:50].replace(' ', ''),
                    line[50:53].replace(' ', ''), line[54:61], line[61:64].replace(' ', ''), line[64:67].replace(' ', ''),
                    line[67:70].replace(' ', ''), line[70:71].replace(' ', ''), line[71:72].replace(' ', ''), line[72:73].replace(' ', ''),
                    line[73:74].replace(' ', ''), line[74:77].replace(' ', ''), line[77:80].replace(' ', '')]
        if datalist[3] != '9999999' and datalist[3] != '       ':
            datalist[3] = '1' + datalist[3].replace(' ', '0')
        if datalist[12] != '9999999' and datalist[12] != '       ':
            datalist[12] = '1' + datalist[12].replace(' ', '0')
        if datalist[21] != '9999999' and datalist[21] != '       ':
            datalist[21] = '1' + datalist[21].replace(' ', '0')
        pre_data2.append(datalist)
    for line_2 in pre_data2:
        if line_2[3] =='9999999':
            value=str(int(line_2[1])-1)
            d=getIndex(pre_data2, value)
            line_2[3]=pre_data2[d][3]
        pre_data3.append(line_2)
    for line_3 in pre_data3:
        if line_3[3] =='9999999':
            value=str(int(line_3[1])-1)
            d=getIndex(pre_data3, value)
            line_3[3]=pre_data3[d][3]
        prepared_data.append(line_3)
    return prepared_data


def match(p_dict, k, ev):
    try:
        pr = p_dict[k][ev]
    except BaseException:
        if k in [1, 2]:
            try:
                pr=p_dict[14][ev]
            except BaseException:
                pr = 'Null'
        else:
            if k == 6:
                try:
                    print(ev[1:])
                    pr = p_dict[15][ev[1:]]
                except BaseException:
                    pr = 'Null'
            else:
                pr = 'Null'
    return pr


def phy_pro1(p_dict, event):
    phy_properties1 = [int(event[1]), match(p_dict, 0, event[0]), event[3], match(p_dict, 1, event[4]), match(p_dict, 1, event[5]),
                       match(p_dict, 2, event[6]), match(p_dict, 3, event[8]),match(p_dict, 4, event[9]), match(p_dict, 5, event[10]),
                       match(p_dict, 6, event[9] + event[10] + event[11])]
    return phy_properties1


def phy_pro2(p_dict, event):
    phy_properties2 = [event[12], match(p_dict, 1, event[13]), match(p_dict, 1, event[14]), match(p_dict, 2, event[15]),
                       match(p_dict, 3, event[17]), match(p_dict, 4, event[18]), match(p_dict, 5, event[19]),
                       match(p_dict, 6, event[18] + event[19] + event[20])]
    return phy_properties2


def phy_pro3(p_dict, event):
    phy_properties3 = [event[21], match(p_dict, 1, event[22]), match(p_dict, 1, event[23]), match(p_dict, 2, event[24]),
                       match(p_dict, 3, event[26]), match(p_dict, 4, event[27]), match(p_dict, 5, event[28]),
                       match(p_dict, 6, event[27] + event[28] + event[29])]
    return phy_properties3


def com_pro1(p_dict, event):
    com_properties1 = [int(event[1]), match(p_dict, 0, event[0]), event[3], match(p_dict, 1, event[4]), match(p_dict, 1, event[5]),
                       match(p_dict, 2, event[6]), match(p_dict, 3, event[8]),match(p_dict, 4, event[9]), match(p_dict, 7, event[10]),
                       match(p_dict, 8, event[11][0]) + '/' + match(p_dict, 9, event[11][1]) + '/' + match(p_dict, 10, event[11][2])]
    return com_properties1


def com_pro2(p_dict, event):
    com_properties2 = [event[12], match(p_dict, 1, event[13]), match(p_dict, 1, event[14]), match(p_dict, 2, event[15]),
                       match(p_dict, 3, event[17]), match(p_dict, 4, event[18]), match(p_dict, 7, event[19]),
                       match(p_dict, 8, event[20][0]) + '/' + match(p_dict, 9, event[20][1]) + '/' + match(p_dict,10, event[20][2])]
    return com_properties2


def int_req_pro1(p_dict, event):
    int_req_properties1 = [int(event[1]), match(p_dict, 0, event[0]), event[3], match(p_dict, 1, event[4]), match(p_dict, 1, event[5]),
                           match(p_dict, 2, event[6]), match(p_dict, 3, event[8]), match(p_dict, 4, event[9]), match(p_dict, 7, event[10]),
                           match(p_dict, 11, event[11][0])]
    return int_req_properties1


def int_req_pro2(p_dict, event):
    int_req_properties2 = [event[12], match(p_dict, 1, event[13]), match(p_dict, 1, event[14]), match(p_dict, 2, event[15]),
                           match(p_dict, 3, event[17]), match(p_dict, 4, event[18]), match(p_dict, 7, event[19]),
                           match(p_dict, 11, event[20][0])]
    return int_req_properties2


def data_conversion(m, prepared_data):
    property_dict = './CodeDictionary.xlsx'
    data1 = xlrd.open_workbook(property_dict)
    p_dict = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
    for i in range(0, 15):
        if i in [1, 2]:
            table = data1.sheets()[i]
            nol = table.ncols
            for j in range(nol):
                if table.cell_value(0 + 2 * m, j) == '':
                    break
                title = str(int(table.cell_value(0 + 2 * m, j)))
                value = table.cell_value(1 + 2 * m, j)
                p_dict[i][title] = value
        else:
            table = data1.sheets()[i]
            nol = table.ncols
            for j in range(nol):
                if table.cell_value(0, j) == '':
                    break
                title = str(int(table.cell_value(0, j)))
                value = table.cell_value(1, j)
                p_dict[i][title] = value

    bcow_conversion = []
    ev = []
    for event in prepared_data:
        if event[2] == '1':
            ev = phy_pro1(p_dict, event)
        if event[2] == '2':
            if event[10] == '1':
                ev = com_pro1(p_dict, event)+phy_pro2(p_dict, event)
            if event[10] in ['2', '3']:
                ev = int_req_pro1(p_dict, event)+phy_pro2(p_dict, event)
        if event[2] == '3':
            if event[10] == '1':
                if event[19] == '1':
                    ev = com_pro1(p_dict, event)+com_pro2(p_dict, event)+phy_pro3(p_dict, event)
                if event[19] in ['2', '3']:
                    ev = com_pro1(p_dict, event)+int_req_pro2(p_dict, event)+phy_pro3(p_dict, event)
                    print(ev)
            if event[10] in ['2', '3']:
                if event[19] == '1':
                    ev = int_req_pro1(p_dict, event) + com_pro2(p_dict, event) + phy_pro3(p_dict, event)

                if event[19] in ['2', '3']:
                    ev = int_req_pro1(p_dict, event) + int_req_pro2(p_dict, event) + phy_pro3(p_dict, event)
        if ev:
            bcow_conversion.append(ev)
    sorted_bcow_conversion = sorted(bcow_conversion, key=(lambda x: x[2]))
    print(sorted_bcow_conversion)
    return sorted_bcow_conversion

def actor_list(p_dict):
    ev_list = []
    for event in p_dict:
        if event:
            ev = [event[3], event[4]]
            ev_list.extend(ev)
    ev_list.remove('Null')
    ac = list(set(ev_list))
    return ac


def pro1(casename, event, ac_n, root_typenum, general_typenum):
    properties1={
                'CaseName': casename,
                'EventId': int(event[0]),
                'EventImpact': event[1],
                '1Date': int(event[2]),
                '1Actor1': event[3],
                '1Actor2': event[4],
                '1Place': event[5],
                '1EventTempo': event[6],
                '1EventRootType': event[7],
                '1EventGeneralType': event[8],
                '1EventSpecificType': event[9],
                'Actornum': ac_n,
                'RootTypenum': root_typenum,
                'GeneralTypenum':general_typenum}
    return properties1


def pro2(casename, event, ac_n, root_typenum, general_typenum):
    properties2={
                'CaseName': casename,
                'EventId': int(event[0]),
                'EventImpact': event[1],
                '1Date': int(event[2]),
                '1Actor1': event[3],
                '1Actor2': event[4],
                '1Place': event[5],
                '1EventTempo': event[6],
                '1EventRootType': event[7],
                '1EventGeneralType': event[8],
                '1EventSpecificType': event[9],
                '2Date': event[10],
                '2Actor1': event[11],
                '2Actor2': event[12],
                '2Place': event[13],
                '2EventTempo': event[14],
                '2EventRootType': event[15],
                '2EventGeneralType': event[16],
                '2EventSpecificType': event[17],
                'Actornum': ac_n,
                'RootTypenum': root_typenum,
                'GeneralTypenum':general_typenum}
    return properties2


def pro3(casename, event, ac_n, root_typenum, general_typenum):
    properties3= {
                'CaseName': casename,
                'EventId': int(event[0]),
                'EventImpact': event[1],
                '1Date': int(event[2]),
                '1Actor1': event[3],
                '1Actor2': event[4],
                '1Place': event[5],
                '1EventTempo': event[6],
                '1EventRootType': event[7],
                '1EventGeneralType': event[8],
                '1EventSpecificType': event[9],
                '2Date': event[10],
                '2Actor1': event[11],
                '2Actor2': event[12],
                '2Place': event[13],
                '2EventTempo': event[14],
                '2EventRootType': event[15],
                '2EventGeneralType': event[16],
                '2EventSpecificType': event[17],
                '3Date': event[18],
                '3Actor1': event[19],
                '3Actor2': event[20],
                '3Place': event[21],
                '3EventTempo': event[22],
                '3EventRootType': event[23],
                '3EventGeneralType': event[24],
                '3EventSpecificType': event[25],
                'Actornum': ac_n,
                'RootTypenum': root_typenum,
                'GeneralTypenum':general_typenum}
    return properties3


def create_eventgraph(i, bcow_conversion):
    graph = Graph("http://localhost:7474", auth=("neo4j", '1993071707ZhuKun'))
    file = './BCOWCaseData.xlsx'
    data = xlrd.open_workbook(file)
    table = data.sheets()[0]

    casename=table.cell_value(i + 1, 1)
    case_pro={'CaseId': table.cell_value(i + 1, 0), 'CaseName': casename,'CodedDate':table.cell_value(i + 1, 2),'CaseDescription':table.cell_value(i + 1, 3)}
    case = Node('Case', **case_pro)
    graph.create(case)
    ac = actor_list(bcow_conversion)
    for event in bcow_conversion:
        if event:
            ev = Node()
            ac_n = ac.index(event[3]) + 1
            if len(event) == 10:
                if event[8] == 'Military':
                    properties = pro1(casename, event, ac_n, 1, 0)
                    ev = Node('MilitaryEvent','PhysicalEvent','Event',  **properties)
                    graph.create(ev)
                if event[8] == 'Diplomatic':
                    properties = pro1(casename, event, ac_n, 1, -1)
                    ev = Node('DiplomaticEvent', 'PhysicalEvent','Event' , **properties)
                    graph.create(ev)
                if event[8] == 'Economic':
                    properties = pro1(casename, event, ac_n, 1,-2)
                    ev = Node('EconomicEvent', 'PhysicalEvent', 'Event',  **properties)
                    graph.create(ev)
                if event[8] == 'Unofficial':
                    properties = pro1(casename, event, ac_n,1, -3)
                    ev = Node('UnofficialEvent' , 'PhysicalEvent', 'Event',  **properties)
                    graph.create(ev)
            if len(event) == 18:
                if event[8] == 'Comment':
                    properties = pro2(casename, event, ac_n, 2, 1)
                    ev = Node('CommentEvent', 'VerbalEvent', 'Event',   **properties)
                    graph.create(ev)
                if event[8] == 'Intention':
                    properties = pro2(casename, event, ac_n, 2, 2)
                    ev = Node('IntentionEvent', 'VerbalEvent', 'Event',   **properties)
                    graph.create(ev)
                if event[8] == 'Request':
                    properties = pro2(casename, event, ac_n, 2, 3)
                    ev = Node('RequestEvent', 'VerbalEvent', 'Event',   **properties)
                    graph.create(ev)
            if len(event) == 26:
                if event[8] == 'Comment':
                    properties = pro3(casename, event, ac_n, 2, 1)
                    ev = Node('CommentEvent', 'VerbalEvent', 'Event',   **properties)
                    graph.create(ev)
                if event[8] == 'Intention':
                    properties = pro3(casename, event, ac_n, 2, 2)
                    ev = Node('IntentionEvent', 'VerbalEvent', 'Event',   **properties)
                    graph.create(ev)
                if event[8] == 'Request':
                    properties = pro3(casename, event, ac_n, 2, 3)
                    ev = Node('RequestEvent', 'VerbalEvent', 'Event',   **properties)
                    graph.create(ev)
            re = Relationship(case, 'hasEvent', ev)
            graph.create(re)


path1 = "./BCOWEventData"
BCOW = os.listdir(path1)
for n in range(0, 40, 1):
    f = open('F:\\09-ALTLPT\\01-数据库\\BCOW历史案例集\\重复1.txt', 'a+')
    f.write('案例'+str(n)+'\n')
    b_file = path1 + '\\' + BCOW[n]
    p_data = data_preparation(b_file)
    b_conversion = data_conversion(n, p_data)
    create_eventgraph(n, b_conversion)

