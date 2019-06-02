from openmdao.api import ExplicitComponent

import numpy as np 

class MeanAeroChord(ExplicitComponent):
    def setup(self):
        self.add_input('Croot')
        self.add_input('lamda')
        self.add_output('C_bar')
        self.declare_partials('C_bar', 'Croot', method = 'fd')
        self.declare_partials('C_bar', 'lamda', method = 'fd')

    def compute(self, inputs, outputs):
        Croot = inputs['Croot']
        lamda = inputs['lamda']
        outputs['C_bar'] = (2./3.)*Croot*((1.+lamda+(lamda**2.))/(1.+lamda))    