# Polinomios
from lista import MyList
polinomios_a_list = MyList()
polinomios_b_list = MyList()
polinomio_result = MyList()
polinomios_a_list.append('3x^2+18x-10')
polinomios_b_list.append('-17x^3+4x^2+0x-25')

def main():
    new_component_a = '^', 2 + 1
    new_component_b = '^', 3 + 1 
    while True:
        user_choice = int(input('1. Ingrese componentes a un polinomio \n'
                                '2. Adicion y Sustraccion \n'
                                '3. Evaluar polinomios \n'
                                '4. Salir \n'))
        if user_choice == 1:
            user_choice = int(input('A que polinomio desea ingresar un nuevo componente '
                                    'y el coeficiente \n'
                                    '1. a = 3x^2+18x-10 \n'
                                    '2. b = -17x^3+4x^2+0x-25\n'))
            if user_choice == 1:
                new_component = input('Ingrese un componente ')
                new_number = input('Ingrese un coeficiente: ')
                polinomios_a_list.prepend(new_component_a)
                polinomios_a_list.prepend(new_component)
                polinomios_a_list.prepend(new_number)
                print(polinomios_a_list.transversal())
            elif user_choice == 2:
                new_component = input('Ingrese un componente ')
                new_number = input('Ingrese un coeficiente: ')
                polinomios_b_list.prepend(new_component_b)
                polinomios_b_list.prepend(new_component)
                polinomios_b_list.prepend(new_number)
                print(polinomios_b_list.transversal())
            
        elif user_choice == 2:
            print(f'{polinomios_a_list.transversal()} \n'
                  f'{polinomios_b_list.transversal()}')
            
            user_choice = int(input('Que desea hacer? \n'
                                    '1. Sumar polinomios\n'
                                    '2. Restar polinomios \n'))
            if user_choice == 1:
                pass
            elif user_choice == 2:
                pass
        elif user_choice == 3:
            pass
        else:
            break

main()