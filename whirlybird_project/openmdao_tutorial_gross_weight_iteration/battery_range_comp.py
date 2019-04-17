from openmdao.api import ExplicitComponent

L_D = 13.*1.5 # General aviation L/D ratio with a 50 percent incrase in L/D
ada = 0.7
# R = ada*(E/mb)*(L/D)*(mb/W0) 'electric aircaft range equation'

class BatteryRangeComp(ExplicitComponent):
    def setup(self):
        self.add_input('E/mb')
        # self.add_input('L/D', val = 1.5*L_D)
        # self.add_input('ada',)
        self.add_output('R')
        self.declare_partials('R','E/mb')

    def compute(self, inputs, outputs):
        outputs['R'] = ada*L_D* inputs['E/mb']*0.05

    def compute_partials(self, inputs, partials):
        partials['R', 'E/mb'] = ada*L_D*0.05

