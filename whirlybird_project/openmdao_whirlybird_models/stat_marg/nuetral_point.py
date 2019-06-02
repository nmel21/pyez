from openmdao.api import ExplicitComponent

import numpy as np 

class NuetralPoint(ExplicitComponent):
    def setup(self):
        self.add_input('Cl_alpha')
        self.add_input('S') 
        self.add_input('Xac_wing')        
        self.add_output('Xnp_wing')
        self.declare_partials('*', '*', method = 'fd')

    def compute(self, inputs, outputs):
        Cl_alpha = inputs['Cl_alpha']
        S = inputs['S']
        Xac_wing = inputs['Xac_wing']
        outputs['Xnp_wing'] =  (Cl_alpha*S*Xac_wing)/(Cl_alpha*S)