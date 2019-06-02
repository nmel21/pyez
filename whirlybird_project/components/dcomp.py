import numpy as np

from openmdao.api import ExplicitComponent

class dComp(ExplicitComponent):
    def setup(self):
        self.add_input('vx')
        self.add_input('tf')
        self.add_output('d')
        self.declare_partials('d','vx')
        self.declare_partials('d','tf')


    
    def compute(self, inputs, outputs):
        vx = inputs['vx']
        tf = inputs['tf']
        outputs['d'] = vx*tf
    
    def compute_partials(self, inputs, partials):
        vx = inputs['vx']
        tf = inputs['tf']

        partials['d', 'vx'] = tf
        partials['d', 'tf'] = vx

    
