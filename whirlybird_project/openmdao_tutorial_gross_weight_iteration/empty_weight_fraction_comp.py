from openmdao.api import ExplicitComponent


A = 1.51
C = -0.1

class EmptyWeightFractionComp(ExplicitComponent):

    def setup(self):
        self.add_input('W0', val=2000)
        self.add_output('We/W0', val=0.5)
        self.declare_partials('We/W0', 'W0')

    def compute(self, inputs, outputs):
        outputs['We/W0'] = A * inputs['W0'] ** C


    def compute_partials(self, inputs, partials):
        partials['We/W0', 'W0'] = C * A * inputs['W0'] ** (C - 1)
