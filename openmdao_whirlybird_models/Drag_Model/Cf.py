from openmdao.api import ExplicitComponent


class Cf(ExplicitCOmponent): 

    def setup(self):
        self.add_input('R')
        self.add_input('M', val =0.0676)
        self.add_output('Cf')
        self.declare_partials('*', '*', method = 'fd')

    def compute(self, inputs, outputs):
        R = inputs['R']
        M = inputs['M']

        outputs['Cf'] = 0.455/( log10(R^2.58) * ((1 + (0.144*(M^2)) )^0.65))