from openmdao.api import ExplicitComponent
import numpy as np
#' lift curve slope component of static margin model
# ' 5.605 Kg' for the initial gross weight
class LiftCurveComp(ExplicitComponent):
    def setup(self):
        self.add_input('lamda')
        # self.add_input('t/c', val = .12)
        self.add_input('b',)
        self.add_input('S', val = 0.18)
        self.add_output('Cl_alpha_inf')
        self.add_output('Cl_alpha')
        self.declare_partials('Cl_alpha', 'lamda')
        self.declare_partials('Cl_alpha', 'b')
    
    def compute(self, inputs, outputs):
        lamda = inputs['lamda']
        b = inputs['b']
        S = inputs['S']
        outputs['Cl_alpha_inf'] = 1.8 * np.pi * ( 1+ 0.8 * .12) * np.cos(lamda -1.0) #'double check'
        Cl_alpha_inf = outputs['Cl_alpha_inf']

        outputs['Cl_alpha'] = Cl_alpha_inf * (1 + Cl_alpha_inf * np.pi * (b**2 / S))
    
    def compute_partials(self, inputs, outputs, partials):
        lamda = inputs['lamda']
        b = inputs['b']
        S = inputs['S']
        outputs['Cl_alpha_inf'] = 1.8 * np.pi * ( 1+ 0.8 * .12) * np.cos(lamda -1.0) #'double check'

        Cl_alpha_inf = outputs['Cl_alpha_inf']
        diff_Cl_alpha_inf = -1.8 * np.pi * (1 + 0.8*0.12) * np.sin(lamda -1)

        partials['Cl_alpha', 'lamda'] = diff_Cl_alpha_inf + 2 * Cl_alpha_inf * diff_Cl_alpha_inf * np.pi * b**2 / S
        partials['Cl_alpha', 'b'] = 2 * (Cl_alpha_inf ** 2) * np.pi * b /S
