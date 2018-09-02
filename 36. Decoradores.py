def protected(func):

    def wrapper(password):

        if password == 'strigidae':
            return func()
        else:
            print('La contraseña es incorrecta.')

    return wrapper


@protected
def protected_function():
    print('Tu contraseña es correcta.')


if __name__ == '__main__':
    password = str(input('Ingresa tu contraseña: '))
    
    protected_function(password)
