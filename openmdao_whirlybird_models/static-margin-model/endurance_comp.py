from openmdao.api import ExplicitComponent

class EnduranceComp(ExplicitComponent):
    def setup(self):
        self.add_input('')
        self.add_input('')
        self.add_output('')
        self.declare_partials('')
    