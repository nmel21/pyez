import numpy as numpy

from openmdao.api import ExplicitComponent

g = -9.81


class TComp(ExplicitComponent):
    def setup(self):
        self.add_input('vy')
        self.add_output('tf')
        self.declare_partials('tf','vy')


    
    def compute(self, inputs, outputs):
        vy = inputs['vy']
        outputs['tf'] = -2*vy/g
    
    def compute_partials(self, inputs, partials):
        #vy = inputs('vy')

        partials['tf', 'vy'] = -2/g

    


