from openmdao.api import ExplicitComponent
import numpy

class XcgWingComp(ExplicitComponent):
    def setup(self):
        self.add_input('lamda')
        self.add_input('xcg_w_o')
        self.add_output('xcg_w')
        self.declare_partials('xcg_w','lamda')

    def compute(self, inputs, outputs):
        lamda = inputs['lamda']
        xcg_w_o = inputs['xcg_w_o']
        outputs['xcg_w'] = xcg_w_o * numpy.cos(lamda)

    def compute_partials(self, inputs, partials):
        lamda = inputs['lamda']
        xcg_w_o = inputs['xcg_w_o']
        partials['xcg_w','lamda'] = - xcg_w_o * numpy.sin(lamda)


