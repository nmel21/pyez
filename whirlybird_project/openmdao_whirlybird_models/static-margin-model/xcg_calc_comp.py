from openmdao.api import ExplicitComponent

import numpy as np 


class XcgCalcComp(ExplicitComponent):
    def setup(self):
        self.add_input('W_xcg_b')
        self.add_input('xcg_w')
        self.add_input('Ww', val = .114)
        self.add_output('xcg')
        self.declare_partials('xcg','xcg_w')

    def compute(self, inputs, outputs):
        W_xcg_b = inputs['W_xcg_b']
        xcg_w = inputs['xcg_w']
        Ww = inputs['Ww']
        outputs['xcg'] = (W_xcg_b + xcg_w * Ww) / 5.605

    def compute_partials(self, inputs, partials):
        # W_xcg_b = inputs['W_xcg_b']
        # xcg_w = inputs['xcg_w']
        Ww = inputs['Ww']
        partials['xcg','xcg_w'] = Ww / 5.605


