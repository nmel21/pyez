from openmdao.api import ExplicitComponent


class GrossWeightComp(ExplicitComponent):

    def setup(self):
        self.add_input('Wp')
        self.add_input('Wc')
        self.add_input('We/W0', val=0.5)
        # self.add_input('Wb/W0', val = .05) # battery to gross ratio, inital guess made from whirlybird bill of materials
        self.add_output('W0', val=2000)
        self.declare_partials('*', '*')

    def compute(self, inputs, outputs):
        Wp = inputs['Wp']
        Wc = inputs['Wc']
        We_W0 = inputs['We/W0']
        # Wb_W0 = inputs['Wb/W0'] # newly added battery to gross weight ratio
        outputs['W0'] = (Wp + Wc) / (1 - We_W0 )
        # outputs['W0'] = (Wp + Wc) / (1 - We_W0 - 0.05) # added the Wb_W0 term

    def compute_partials(self, inputs, partials):
        Wp = inputs['Wp']
        Wc = inputs['Wc']
        We_W0 = inputs['We/W0']
        # Wb_W0 = inputs['Wb/W0']
        partials['W0', 'Wp'] = 1. / (1 - We_W0)
        partials['W0', 'Wc'] = 1. / (1 - We_W0)
        partials['W0', 'We/W0'] = (Wp + Wc) / (1 - We_W0) ** 2

        # partials['W0', 'Wp'] = 1. / (1 - We_W0 - 0.05)
        # partials['W0', 'Wc'] = 1. / (1 - We_W0 - 0.05)
        # partials['W0', 'We/W0'] = (Wp + Wc) / (1 - We_W0 - 0.05) ** 2
        # partials['W0', 'Wb/W0'] = (Wp + Wc) / ( 1 - We_W0 - 0.05)** 2