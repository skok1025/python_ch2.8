# class Point


class Point:
    count_of_instance = 0

    def setx(self,x):
        self.x = x

    def getx(self):
        return self.x

    def sety(self,y):
        self.y = y

    def gety(self):
        return self.y

    def show(self):
        print('점: ',self.x,',',self.y)

        @classmethod
        def class_method(cls):
            return cls.count_of_instance

        @staticmethod
        def static_method():
            print('static method called')
