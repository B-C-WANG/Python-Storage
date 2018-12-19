import traceback

def check(input,output):
    def w1(func):
        def inner(*args):

            assert len(args) == len(input) ,"Input args number not match"
            for i in range(len(input)):
                assert isinstance(args[i],input[i]),"the %s th args do not match except %s, got %s"%(i,str(input[i]),type(args[i]))

            results = func(*args)
            assert len(results) == len(output), "Input args number not match"
            for i in range(len(output)):
                assert isinstance(results[i], output[i]), "the %sth args do not match except %s, got %s" % (
                i, str(output[i]), type(results[i]))

        return inner
    return w1

@check(input=(str,int),output=(int))
def a(abc,defg):
    print(abc,defg)


a("122",12)





