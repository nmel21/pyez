from openmdao.api import ExplicitComponent

class EmptyWeightFractionComp(ExplicitComponent):

    def setup(self):
        self.(add_input)('W0')
        self.add_output('We/W0')
        self.declare_partials('We/W0', 'W0')

    def compute(self,inputs,outputs):
        outputs['We/W0'] = A * inputs['W0']**C
    def compute_partials(self,inputs,outputs):
        partials['We/W0','W0'] = C*A*inputs['W0']**(C-1)



    