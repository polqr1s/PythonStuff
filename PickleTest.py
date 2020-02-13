import pickle


#pickling a list
'''
savelist = ["spam", "eggs"]

#save
savelist = pickle.dump(savelist, open("savefile.dat", "wb"))

#load
savelist = pickle.load(open("savefile.dat", "rb"))


print(savelist)
'''

#pickling a class

class obj():
    def __init__(self):
        self.attr = 5

class why(obj):
    def __init__(self):
        self.attr = 3
    def value(self):
        print (thing.attr)

thing = why()

#save
#thing = pickle.dump(thing, open("save.dat", "wb"))

#load
thing = pickle.load(open("save.dat", "rb"))

thing.value()



