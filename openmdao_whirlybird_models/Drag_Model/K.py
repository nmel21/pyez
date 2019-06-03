from openmdao.api import ExplicitComponent

class K(ExplicitComponent):
    def setup(self):
        self.add_input('b')
        self.add_input('S')
        self.add_output('K')
        self.declare_partials('*', '*', method = 'fd')


    def compute(self, inputs, outputs):
        b = inputs['b']
        S = inputs['S']
        outputs['K'] = 1/(pi*((4.61*(1-(0.045*(((b^2)/S)^0.68)))*(cosd(30)^0.15)) - 3.1)*((b^2)/S))