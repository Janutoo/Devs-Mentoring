


#Użycie @staticmethod i @classmethod
# Cel: Ćwiczenie dekoratorów wbudowanych w Pythonie (@staticmethod, @classmethod).
# Opis: Stworzyć klasę MathUtils z dwiema metodami. @staticmethod nie korzysta z obiektu klasy,
#  a @classmethod operuje na samej klasie.

class MathUtils:

    @classmethod
    def multiply(cls, a, b):
        return a * b

    @staticmethod
    def add(a, b):
        return a + b
    
print(MathUtils.multiply(3, 4))
print(MathUtils.add(5, 10))

# class MathUtils
#     public:
#     static void add(int a int b)
#     {
#         return a + b 
#     }
