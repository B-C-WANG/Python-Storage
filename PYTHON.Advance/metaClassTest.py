

def make_Class():
    def print_name(self,name):
        print("Hello, %s" % name)

    Hello = type("Hello_World",             # type name
                 (object,),                 # base class
                 dict(say_hello=print_name)) # method dict

    hello = Hello()
    hello.say_hello("wang")

    print(type(hello))

def metaClass():
    class SayMetaClass(type):
        def __new__(cls, name, bases, attrs):
            attrs['say_' + name] = lambda self, value, saying=name: print(saying + ',' + value + '!')
            return type.__new__(cls, name, bases, attrs)# attrs there is in fact method dict!


    class askdjlkasjfl(object,metaclass=SayMetaClass):
        pass
        # if the class with <name>, and the method say_<name> will auto add to it as a method

    hello = askdjlkasjfl() # the __new__ method used
    hello.say_askdjlkasjfl("Wang")


    class Sayolala(object, metaclass=SayMetaClass):
        pass

    s = Sayolala()
    s.say_Sayolala('japan!')

def metaList():

    class ExtendedList(type):
        def __new__(cls, name, bases, attrs):
            attrs["add"] = lambda self,value: self.append(value+"_extend_by_add")
            return type.__new__(cls,name,bases,attrs)

    class Mylist(list,metaclass=ExtendedList):
        pass

    L = Mylist()
    L.add("123")
    L.append(1)
    print(L)


    class ExtendedNameList(type):
        def __new__(cls, name, bases, attrs):
            attrs["add_"+name] = lambda self,value: self.append(value+"_add_by_%s"%name)
            return type.__new__(cls,name,bases,attrs)

    class abcabclist(list,metaclass=ExtendedNameList):
        pass

    L = abcabclist()
    L.add_abcabclist("123")
    L.append(1)
    print(L)





#make_Class()

#metaClass()
metaList()