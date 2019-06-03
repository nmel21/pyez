from openmdao.api import ExplicitComponent


class Reynolds(ExplicitComponent): 

    def setup(self):
        self.add_input('rho', val = 1.225)
        self.add_input('V', val = 23.)
        self.add_input('mu', 2.008 * 10 **(-5.0) )
        self.add_input('C_bar') # mean aerodynamic chord
        self.add_output('R')
        self.declare_partials('*', '*', method = 'fd')

    def compute(self, inputs, outputs): 
        rho = inputs['rho']
        V = inputs['V']
        mu = inputs['mu']
        C_bar = inputs['C_bar']

        outputs['R'] = (rho * V * C_bar )/mu