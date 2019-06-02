import numpy as numpy

from openmdao.api import ExplicitComponent

class VyComp(ExplicitComponent):
    def setup(self):
        self.add_input('V')
        self.add_input('theta')
        self.add_output('vy')
        self.declare_partials('vy', 'V')
        self.declare_partials('vy','theta')


    
    def compute(self, inputs, outputs):
        v = inputs['V']
        theta = inputs['theta']
        outputs['vy'] = v*numpy.sin(theta)
    
    def compute_partials(self, inputs, partials):
        v = inputs['V']
        theta = inputs['theta']

        partials['vy', 'V'] = numpy.sin(theta)
        partials['vy', 'theta'] = v*numpy.cos(theta)

    
