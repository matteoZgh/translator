def Read(func) :
    def read(*args, **kwarg) :
        with open(kwarg['path'],'r') as f :
            del kwarg['path']
            kwarg['file'] = f
            return func(*args, **kwarg)
    return read

def Add(func) :
    def add(*args, **kwarg) :
        with open(kwarg['path'],'a') as f :
            del kwarg['path']
            kwarg['file'] = f
            return func(*args, **kwarg)
    return add

def Write(func) :
    def write(*args, **kwarg) :
        with open(kwarg['path'],'w') as f :
            del kwarg['path']
            kwarg['file'] = f
            return func(*args, **kwarg)
    return write
