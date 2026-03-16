#Function
def hello_func():
    return 'Hi'
print(hello_func())


#e2
def hf(greeting):
    return '{} Bhusal.'.format(greeting)
print(hf("My name is prasid"))

#e3
def std(*args, **kwargs):
    print(args)
    print(kwargs)
std("Math","Art", name="Prasid", Age=20)
