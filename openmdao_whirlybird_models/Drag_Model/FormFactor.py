from openmdao.api import ExplicitComponent


class FormFactors(ExplicitComponent):
    
    def setup(self):
        self.add_input('tc1',val = .12)
        self.add_input('xc1', val = .3)
        self.add_input('M', val = .0676)
        self.add_input('sweep')
        self.add_output('FF')
        self.declare_partial('*', '*', method = 'fd')

    def compute(self, inputs, outputs):
        tc1 = inputs['tc1']
        xc1 = inputs['xc1']
        M = inputs['M']
        sweep = inputs['sweep']

        outputs['FF'] = ((0.6*tc1/xc1) + (100*(tc1^4)) + 1)*(1.34*(M^.18))*(cosd(sweep)^.28)


