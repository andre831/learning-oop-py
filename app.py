from time import sleep
from dogs import chiuaua, pit_bull, pastor_alemao

#Welcome
print('Olá, bem-vindo ao Canino, casa de adoção de cachorros!')
sleep(2)
print(' ' * 20)

option = 0
optionDog = 0

while option <= 1:
    print('''
    [1]Hoje não posso =(
    [2]Sim, quero muito! ''')
    
    option = int(input('Deseja adotar um amiguinho?'))
    print(' ' * 20)

    if option == 1:
        sleep(1)
        print(' ' * 20)
        print('Okay, obrigado pela visita :D')
        break

    elif option == 2:
        print('Legal, vamos lá')
        sleep(2)
        print('''Hoje temos apenas três doguinhos conosco:
        [1]Chiuaua
        [2]Pitbull
        [3]Pastor Alemão  ''')
        
        optionDog = int(input('Qual quer levar com você hoje?'))
        if optionDog == 1:
            print(' ' * 20)
            print('Legal, vamos preencher a ficha, ok?')
            c1 = chiuaua( 
                nome = input('Qual será o nome dele?'),
                raca= 'Chiuaua',
                cor = 'caramelo',
                sex = 'masc'
            )
            print('Legal, aqui está a ficha do seu novo companheiro:', c1.__dict__ )
            print(' ' * 20)
            c1.latir()
            sleep(1)
            print('Acho que', c1.nome, 'gostou de você')
            break
        
        elif optionDog == 2:
            print(' ' * 20)
            print('Legal, vamos preencher a ficha, ok?')
            pb1 = pit_bull( 
                nome = input('Qual será o nome dele?'),
                raca= 'Pitbull',
                cor = 'malhado',
                sex = 'fêmea'
            )
            print('Legal, aqui está a ficha do seu novo companheiro:', pb1.__dict__ )
            print(' ' * 20)
            pb1.latir()
            sleep(1)
            print('Acho que', pb1.nome, 'gostou de você')
            break
        
        if optionDog == 3:
            print(' ' * 20)
            print('Legal, vamos preencher a ficha, ok?')
            pa1 = pastor_alemao( 
                nome = input('Qual será o nome dele?'),
                raca= 'Pastor Alemão',
                cor = 'preto',
                sex = 'masc'
            )
            pa1['endereço'] = input('Endereço do novo lar?')
            print('Legal, aqui está a ficha do seu novo companheiro:', pa1.__dict__ )
            print(' ' * 20)
            pa1.latir()
            sleep(1)
            print('Acho que', pa1.nome, 'gostou de você')
            break


print('Obrigado por ')