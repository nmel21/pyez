from openmdao.api import ExplicitComponent

class GrossWeightComp(ExplicitComponent):

    def setup(self):
        self.add_input('Wp')
        self.add_input('Wc')
        self.add_output('W0')
        self.declare_partials('*','*')

    def compute(self,inputs,outputs):
        Wp = inputs['Wp']
        Wc = inputs['Wc']
        We_W0 = inputs['We/W0']


        outputs['We/W0'] = A * inputs['W0']**C



    def compute_partials(self,inputs,outputs):
        partials['We/W0','W0'] = C*A*inputs['W0']**(C-1)
