import tornado.web
import tornado.wsgi
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 14:32:15 2016

@author: Usuario
"""



import numpy as np
import skfuzzy as fuzz

#from mpl_toolkits.mplot3d import Axes3D

from skfuzzy import control as ctrl

import json

def aggFuzzy(pesoVal, tempoVal, pasVal):
    peso = np.arange(0.0,6.0,1.0)
    tempo = np.arange(0,30.0001,0.0001)
    opor = np.arange(0,6,1)
    pas = np.arange(0,11,1)
    #Peso
    peso_antecedent = ctrl.Antecedent(peso,'Peso da profissao')
    tempo_antecedent = ctrl.Antecedent(tempo,'Tempo')
    pas_antecedent = ctrl.Antecedent(pas,"Pacientes")
    opor_consequent = ctrl.Consequent(opor,"Oportunidades")

    #Peso

    peso_antecedent['MP'] = fuzz.trimf(peso_antecedent.universe,[0,1,2])
    peso_antecedent['P'] = fuzz.trimf(peso_antecedent.universe,[1,2,3])
    peso_antecedent['M'] = fuzz.trimf(peso_antecedent.universe,[2,3,4])
    peso_antecedent['A'] = fuzz.trimf(peso_antecedent.universe,[3,4,5])
    peso_antecedent['MA'] = fuzz.trimf(peso_antecedent.universe,[4,5,6])
    peso_antecedent.view()
    #Tempo

    tempo_antecedent['MP'] = fuzz.gaussmf(tempo_antecedent.universe,0,np.std(tempo))
    tempo_antecedent['M'] = fuzz.gaussmf(tempo_antecedent.universe,15,np.std(tempo))
    tempo_antecedent['MA'] = fuzz.gaussmf(tempo_antecedent.universe,30,np.std(tempo))
    tempo_antecedent.view()

    #Pessoas

    pas_antecedent['MP'] = fuzz.trapmf(pas_antecedent.universe,[0,0,1,2])
    pas_antecedent['P'] = fuzz.trapmf(pas_antecedent.universe,[0,2,3,5])
    pas_antecedent['M'] = fuzz.trimf(pas_antecedent.universe,[3,5,6])
    pas_antecedent['A'] = fuzz.trapmf(pas_antecedent.universe,[5,6,8,9])
    pas_antecedent['MA'] = fuzz.trapmf(pas_antecedent.universe,[8,9,10,11])

    #Oportunidades

    opor_consequent['MP'] = fuzz.trimf(opor_consequent.universe,[0,1,2])
    opor_consequent['P'] = fuzz.trimf(opor_consequent.universe,[1,2,3])
    opor_consequent['M'] = fuzz.trimf(opor_consequent.universe,[2,3,4])
    opor_consequent['A'] = fuzz.trimf(opor_consequent.universe,[3,4,5])
    opor_consequent['MA'] = fuzz.trimf(opor_consequent.universe,[4,5,6])

    #Regras
    Rule0 = ctrl.Rule(peso_antecedent['MP'] & tempo_antecedent['MP'] & pas_antecedent['MP'],opor_consequent['MP'])
    Rule1 = ctrl.Rule(peso_antecedent['MP'] & tempo_antecedent['MP'] & pas_antecedent['P'],opor_consequent['MP'])
    Rule2 = ctrl.Rule(peso_antecedent['MP'] & tempo_antecedent['MP'] & pas_antecedent['M'],opor_consequent['MP'])
    Rule3 = ctrl.Rule(peso_antecedent['MP'] & tempo_antecedent['MP'] & pas_antecedent['A'],opor_consequent['MP'])
    Rule4 = ctrl.Rule(peso_antecedent['MP'] & tempo_antecedent['MP'] & pas_antecedent['MA'],opor_consequent['MP'])
    Rule5 = ctrl.Rule(peso_antecedent['MP'] & tempo_antecedent['M'] & pas_antecedent['MP'],opor_consequent['MP'])
    Rule6 = ctrl.Rule(peso_antecedent['MP'] & tempo_antecedent['M'] & pas_antecedent['P'],opor_consequent['MP'])
    Rule7 = ctrl.Rule(peso_antecedent['MP'] & tempo_antecedent['M'] & pas_antecedent['M'],opor_consequent['P'])
    Rule8 = ctrl.Rule(peso_antecedent['MP'] & tempo_antecedent['M'] & pas_antecedent['A'],opor_consequent['P'])
    Rule9 = ctrl.Rule(peso_antecedent['MP'] & tempo_antecedent['M'] & pas_antecedent['MA'],opor_consequent['P'])
    Rule10 = ctrl.Rule(peso_antecedent['MP'] & tempo_antecedent['MA'] & pas_antecedent['MP'],opor_consequent['P'])
    Rule11 = ctrl.Rule(peso_antecedent['MP'] & tempo_antecedent['MA'] & pas_antecedent['P'],opor_consequent['M'])
    Rule12 = ctrl.Rule(peso_antecedent['MP'] & tempo_antecedent['MA'] & pas_antecedent['M'],opor_consequent['M'])
    Rule13 = ctrl.Rule(peso_antecedent['MP'] & tempo_antecedent['MA'] & pas_antecedent['A'],opor_consequent['A'])
    Rule14 = ctrl.Rule(peso_antecedent['MP'] & tempo_antecedent['MA'] & pas_antecedent['MA'],opor_consequent['A'])
    Rule15 = ctrl.Rule(peso_antecedent['P'] & tempo_antecedent['MP'] & pas_antecedent['MP'],opor_consequent['P'])
    Rule16 = ctrl.Rule(peso_antecedent['P'] & tempo_antecedent['MP'] & pas_antecedent['P'],opor_consequent['P'])
    Rule17 = ctrl.Rule(peso_antecedent['P'] & tempo_antecedent['MP'] & pas_antecedent['M'],opor_consequent['P'])
    Rule18 = ctrl.Rule(peso_antecedent['P'] & tempo_antecedent['MP'] & pas_antecedent['A'],opor_consequent['P'])
    Rule19 = ctrl.Rule(peso_antecedent['P'] & tempo_antecedent['MP'] & pas_antecedent['MA'],opor_consequent['P'])
    Rule20 = ctrl.Rule(peso_antecedent['P'] & tempo_antecedent['M'] & pas_antecedent['MP'],opor_consequent['P'])
    Rule21 = ctrl.Rule(peso_antecedent['P'] & tempo_antecedent['M'] & pas_antecedent['P'],opor_consequent['P'])
    Rule22 = ctrl.Rule(peso_antecedent['P'] & tempo_antecedent['M'] & pas_antecedent['M'],opor_consequent['M'])
    Rule23 = ctrl.Rule(peso_antecedent['P'] & tempo_antecedent['M'] & pas_antecedent['A'],opor_consequent['M'])
    Rule24 = ctrl.Rule(peso_antecedent['P'] & tempo_antecedent['M'] & pas_antecedent['MA'],opor_consequent['M'])
    Rule25 = ctrl.Rule(peso_antecedent['P'] & tempo_antecedent['MA'] & pas_antecedent['MP'],opor_consequent['M'])
    Rule26 = ctrl.Rule(peso_antecedent['P'] & tempo_antecedent['MA'] & pas_antecedent['P'],opor_consequent['A'])
    Rule27 = ctrl.Rule(peso_antecedent['P'] & tempo_antecedent['MA'] & pas_antecedent['M'],opor_consequent['A'])
    Rule28 = ctrl.Rule(peso_antecedent['P'] & tempo_antecedent['MA'] & pas_antecedent['A'],opor_consequent['MA'])
    Rule29 = ctrl.Rule(peso_antecedent['P'] & tempo_antecedent['MA'] & pas_antecedent['MA'],opor_consequent['MA'])
    Rule30 = ctrl.Rule(peso_antecedent['M'] & tempo_antecedent['MP'] & pas_antecedent['MP'],opor_consequent['M'])
    Rule31 = ctrl.Rule(peso_antecedent['M'] & tempo_antecedent['MP'] & pas_antecedent['P'],opor_consequent['M'])
    Rule32 = ctrl.Rule(peso_antecedent['M'] & tempo_antecedent['MP'] & pas_antecedent['M'],opor_consequent['M'])
    Rule33 = ctrl.Rule(peso_antecedent['M'] & tempo_antecedent['MP'] & pas_antecedent['A'],opor_consequent['M'])
    Rule34 = ctrl.Rule(peso_antecedent['M'] & tempo_antecedent['MP'] & pas_antecedent['MA'],opor_consequent['M'])
    Rule35 = ctrl.Rule(peso_antecedent['M'] & tempo_antecedent['M'] & pas_antecedent['MP'],opor_consequent['M'])
    Rule36 = ctrl.Rule(peso_antecedent['M'] & tempo_antecedent['M'] & pas_antecedent['P'],opor_consequent['M'])
    Rule37 = ctrl.Rule(peso_antecedent['M'] & tempo_antecedent['M'] & pas_antecedent['M'],opor_consequent['A'])
    Rule38 = ctrl.Rule(peso_antecedent['M'] & tempo_antecedent['M'] & pas_antecedent['A'],opor_consequent['A'])
    Rule39 = ctrl.Rule(peso_antecedent['M'] & tempo_antecedent['M'] & pas_antecedent['MA'],opor_consequent['A'])
    Rule40 = ctrl.Rule(peso_antecedent['M'] & tempo_antecedent['MA'] & pas_antecedent['MP'],opor_consequent['A'])
    Rule41 = ctrl.Rule(peso_antecedent['M'] & tempo_antecedent['MA'] & pas_antecedent['P'],opor_consequent['MA'])
    Rule42 = ctrl.Rule(peso_antecedent['M'] & tempo_antecedent['MA'] & pas_antecedent['M'],opor_consequent['MA'])
    Rule43 = ctrl.Rule(peso_antecedent['M'] & tempo_antecedent['MA'] & pas_antecedent['A'],opor_consequent['MA'])
    Rule44 = ctrl.Rule(peso_antecedent['M'] & tempo_antecedent['MA'] & pas_antecedent['MA'],opor_consequent['MA'])
    Rule45 = ctrl.Rule(peso_antecedent['A'] & tempo_antecedent['MP'] & pas_antecedent['MP'],opor_consequent['A'])
    Rule46 = ctrl.Rule(peso_antecedent['A'] & tempo_antecedent['MP'] & pas_antecedent['P'],opor_consequent['A'])
    Rule47 = ctrl.Rule(peso_antecedent['A'] & tempo_antecedent['MP'] & pas_antecedent['M'],opor_consequent['A'])
    Rule48 = ctrl.Rule(peso_antecedent['A'] & tempo_antecedent['MP'] & pas_antecedent['A'],opor_consequent['A'])
    Rule49 = ctrl.Rule(peso_antecedent['A'] & tempo_antecedent['MP'] & pas_antecedent['MA'],opor_consequent['A'])
    Rule50 = ctrl.Rule(peso_antecedent['A'] & tempo_antecedent['M'] & pas_antecedent['MP'],opor_consequent['A'])
    Rule51 = ctrl.Rule(peso_antecedent['A'] & tempo_antecedent['M'] & pas_antecedent['P'],opor_consequent['A'])
    Rule52 = ctrl.Rule(peso_antecedent['A'] & tempo_antecedent['M'] & pas_antecedent['M'],opor_consequent['MA'])
    Rule53 = ctrl.Rule(peso_antecedent['A'] & tempo_antecedent['M'] & pas_antecedent['A'],opor_consequent['MA'])
    Rule54 = ctrl.Rule(peso_antecedent['A'] & tempo_antecedent['M'] & pas_antecedent['MA'],opor_consequent['MA'])
    Rule55 = ctrl.Rule(peso_antecedent['A'] & tempo_antecedent['MA'] & pas_antecedent['MP'],opor_consequent['MA'])
    Rule56 = ctrl.Rule(peso_antecedent['A'] & tempo_antecedent['MA'] & pas_antecedent['P'],opor_consequent['MA'])
    Rule57 = ctrl.Rule(peso_antecedent['A'] & tempo_antecedent['MA'] & pas_antecedent['M'],opor_consequent['MA'])
    Rule58 = ctrl.Rule(peso_antecedent['A'] & tempo_antecedent['MA'] & pas_antecedent['A'],opor_consequent['MA'])
    Rule59 = ctrl.Rule(peso_antecedent['A'] & tempo_antecedent['MA'] & pas_antecedent['MA'],opor_consequent['MA'])
    Rule60 = ctrl.Rule(peso_antecedent['MA'] & tempo_antecedent['MP'] & pas_antecedent['MP'],opor_consequent['MA'])
    Rule61 = ctrl.Rule(peso_antecedent['MA'] & tempo_antecedent['MP'] & pas_antecedent['P'],opor_consequent['MA'])
    Rule62 = ctrl.Rule(peso_antecedent['MA'] & tempo_antecedent['MP'] & pas_antecedent['M'],opor_consequent['MA'])
    Rule63 = ctrl.Rule(peso_antecedent['MA'] & tempo_antecedent['MP'] & pas_antecedent['A'],opor_consequent['MA'])
    Rule64 = ctrl.Rule(peso_antecedent['MA'] & tempo_antecedent['MP'] & pas_antecedent['MA'],opor_consequent['MA'])
    Rule65 = ctrl.Rule(peso_antecedent['MA'] & tempo_antecedent['M'] & pas_antecedent['MP'],opor_consequent['MA'])
    Rule66 = ctrl.Rule(peso_antecedent['MA'] & tempo_antecedent['M'] & pas_antecedent['P'],opor_consequent['MA'])
    Rule67 = ctrl.Rule(peso_antecedent['MA'] & tempo_antecedent['M'] & pas_antecedent['M'],opor_consequent['MA'])
    Rule68 = ctrl.Rule(peso_antecedent['MA'] & tempo_antecedent['M'] & pas_antecedent['A'],opor_consequent['MA'])
    Rule69 = ctrl.Rule(peso_antecedent['MA'] & tempo_antecedent['M'] & pas_antecedent['MA'],opor_consequent['MA'])
    Rule70 = ctrl.Rule(peso_antecedent['MA'] & tempo_antecedent['MA'] & pas_antecedent['MP'],opor_consequent['MA'])
    Rule71 = ctrl.Rule(peso_antecedent['MA'] & tempo_antecedent['MA'] & pas_antecedent['P'],opor_consequent['MA'])
    Rule72 = ctrl.Rule(peso_antecedent['MA'] & tempo_antecedent['MA'] & pas_antecedent['M'],opor_consequent['MA'])
    Rule73 = ctrl.Rule(peso_antecedent['MA'] & tempo_antecedent['MA'] & pas_antecedent['A'],opor_consequent['MA'])
    Rule74 = ctrl.Rule(peso_antecedent['MA'] & tempo_antecedent['MA'] & pas_antecedent['MA'],opor_consequent['MA'])


    opor_ctrl = ctrl.ControlSystem([Rule0	,
        Rule1	,
        Rule2	,
        Rule3	,
        Rule4	,
        Rule5	,
        Rule6	,
        Rule7	,
        Rule8	,
        Rule9	,
        Rule10	,
        Rule11	,
        Rule12	,
        Rule13	,
        Rule14	,
        Rule15	,
        Rule16	,
        Rule17	,
        Rule18	,
        Rule19	,
        Rule20	,
        Rule21	,
        Rule22	,
        Rule23	,
        Rule24	,
        Rule25	,
        Rule26	,
        Rule27	,
        Rule28	,
        Rule29	,
        Rule30	,
        Rule31	,
        Rule32	,
        Rule33	,
        Rule34	,
        Rule35	,
        Rule36	,
        Rule37	,
        Rule38	,
        Rule39	,
        Rule40	,
        Rule41	,
        Rule42	,
        Rule43	,
        Rule44	,
        Rule45	,
        Rule46	,
        Rule47	,
        Rule48	,
        Rule49	,
        Rule50	,
        Rule51	,
        Rule52	,
        Rule53	,
        Rule54	,
        Rule55	,
        Rule56	,
        Rule57	,
        Rule58	,
        Rule59	,
        Rule60	,
        Rule61	,
        Rule62	,
        Rule63	,
        Rule64	,
        Rule65	,
        Rule66	,
        Rule67	,
        Rule68	,
        Rule69	,
        Rule70	,
        Rule71	,
        Rule72	,
        Rule73	,
        Rule74
    ]);
    saida = ctrl.ControlSystemSimulation(opor_ctrl)
    saida.input['Peso da profissao'] = pesoVal
    saida.input['Tempo'] = tempoVal
    saida.input['Pacientes'] = pasVal
    saida.compute()


    return round(saida.output['Oportunidades'])


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        c = 0
        d = json.loads(json.dumps({ k: self.get_argument(k) for k in self.request.arguments }))
        i = d['a'].split(',')
        o = d['b'].split(',')
        p = d['c'].split(',')
        for n in range(len(i)):
            k = aggFuzzy(int(i[n]),int(o[n]),int(p[n]))
            c = c + k
        self.write(str(c))
    def post(self):
        c = 0
        d = json.loads(json.dumps({ k: self.get_argument(k) for k in self.request.arguments }))
        i = d['a'].split(',')
        o = d['b'].split(',')
        p = d['c'].split(',')
        for n in range(len(i)):
            k = aggFuzzy(int(i[n]),int(o[n]),int(p[n]))
            c = c + k
        self.write(str(c))
application = tornado.wsgi.WSGIApplication([
    (r"/", MainHandler),
])
