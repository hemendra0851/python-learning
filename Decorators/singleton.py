
'''The basic idea is that we will define a dictionary and store the instance into it. 
Whenever we’re trying to instantiate the class, the dictionary is checked. 
If there is no instance, instantiate the class and return the instance. 
Otherwise, do not instantiate the class again, just return the existing instance.'''


def singleton(_class):
    instances = {}
    
    def get_instance(*args, **kwargs):
        if _class not in instances:
            print('Connecting to DB...')
            instances[_class] = _class(*args, **kwargs)
            print('Connected')
        else:
            print('Already has a connection, will reuse it.')
        return instances[_class]
    return get_instance

@singleton
class DBConnection:
    def connect_to_db():
        pass