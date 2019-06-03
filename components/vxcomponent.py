import numpy as numpy
from openmdao.api import ExplicitComponent 


class VxComp(ExplicitComponent):
    def setup(self):
        self.add_input('V')
        self.add_input('theta')
        self.add_output('vx')
        self.declare_partials('vx', 'V')
        self.declare_partials('vx','theta')


    
    def compute(self, inputs, outputs):
        v = inputs['V']
        theta = inputs['theta']
        outputs['vx'] = v*numpy.cos(theta)
    
    def compute_partials(self, inputs, partials):
        v = inputs['V']
        theta = inputs['theta']

        partials['vx', 'V'] = numpy.cos(theta)
        partials['vx', 'theta'] = -v*numpy.sin(theta)

    
