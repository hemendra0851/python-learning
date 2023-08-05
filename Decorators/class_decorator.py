
# Syntax

def class_decorator(_class):
    def wrapped_class_constructor():
        # Do something before the class is instantiated
        instance = _class()
        # Do something after the class has been instantiated
        return instance
    return wrapped_class_constructor

