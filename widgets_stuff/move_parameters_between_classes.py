class Class_1():
    def __init__(self, parameter_1):
        """
        this is the class initiation
        it receives parameter when you create it
        """
        print(parameter_1)
        self.param_1 = parameter_1
        self.just_something = "text"

    def get_parameter_from_outside(self, outer_param):
        self.param_2 = outer_param

    def get_param_1(self):
        return self.param_1

    def get_param_2(self):
        return self.param_2