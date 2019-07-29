"""open for extention and closed for modification. You should design things in a way that while you need to add more
features to your product, more implementation might be added rather than changed """


class Logger:
    def __init__(self, path):
        self.path = path
        pass

    def connect(self, destination):
        if destination == 'mongo':
            Mongo().connect(self.path)

        if destination == 'elastic':
            Elastic().connect(self.path)


"""
In above case for each new logging destination  we ll have to change connect function of Logger class. This voilates ocp
"""


class Logger:
    def __init__(self, path):
        self.path = path
        pass

    def connect(self, destination):
        destination.connect(self.path)


class LoggerStores:
    def connect(self, path):
        raise NotImplementedError


class MongoLoggerStore(LoggerStores):
    def connect(self, path):
        pass


class ElasticLoggerStore(LoggerStores):
    def connect(self, path):
        pass


"""Above is correction where for each new logger store we just have to extend our code by including  implementation 
new logger. General way is to have interfaces in place and let the implementation handle the adding features. """
