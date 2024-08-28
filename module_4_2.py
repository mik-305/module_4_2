def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function() #  Вызов внутри test_function()


test_function()

#inner_function()  Вызов вне test_function() приводит к ошибке

