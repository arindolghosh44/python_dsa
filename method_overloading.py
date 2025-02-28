class methodLoading:
    def math(self,a=0,b=0,c=0):
        return a+b+c

method1=methodLoading()

print(method1.math(1,2))
print(method1.math(1,2,3))

print(method1.math(1))
