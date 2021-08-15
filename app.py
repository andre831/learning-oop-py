from time import sleep
from dogs import chiuaua, pit_bull, pastor_alemao
from donoCachorro import dono_de_cachorro

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
        sleep(2)
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
            print(' ' * 20)
            print('Certo, agora preciso dos seus dados')

            dono_c1 = dono_de_cachorro(
                nome = input('Qual seu nome?'),
                idade = int(input('Diga sua idade:')),
                cpf = int(input('Por favor, me informe seu cpf:')),
                endereco = input('Para terminar, diga o endereço onde você mora:')
            )

            print('''Legal, aqui está a ficha do seu novo companheiro: Aqui você verá os dados do bichinho''',c1.__dict__, 'E aqui estão dos seus:',
            dono_c1.__dict__)

            print(' ' * 20)
            c1.latir()
            sleep(1)
            print(' ' * 20)
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
            print(' ' * 20)
            print('Certo, agora preciso dos seus dados')

            dono_pb1 = dono_de_cachorro(
                nome = input('Qual seu nome?'),
                idade = int(input('Diga sua idade:')),
                cpf = int(input('Por favor, me informe seu cpf:')),
                endereco = input('Para terminar, diga o endereço onde você mora:')
            )

            print('''Legal, aqui está a ficha do seu novo companheiro: Aqui você verá os dados do bichinho''', pb1.__dict__, 'E aqui estão dos seus:', dono_pb1.__dict__)
            
            pb1.latir()
            sleep(1)
            print(' ' * 20)
            print('Acho que', pb1.nome, 'gostou de você')
            break
        
        elif optionDog == 3:
            print(' ' * 20)
            print('Legal, vamos preencher a ficha, ok?')
            pa1 = pastor_alemao( 
                nome = input('Qual será o nome dele?'),
                raca= 'Pastor Alemão',
                cor = 'preto',
                sex = 'masc'
            )
            print(' ' * 20)
            print('Certo, agora preciso dos seus dados')

            dono_pa1 = dono_de_cachorro(
                nome = input('Qual seu nome?'),
                idade = int(input('Diga sua idade:')),
                cpf = int(input('Por favor, me informe seu cpf:')),
                endereco = input('Para terminar, diga o endereço onde você mora:')
            )

            print('''Legal, aqui está a ficha do seu novo companheiro: Aqui você verá os dados do bichinho''', pa1.__dict__, 'E aqui estão dos seus:', dono_pa1.__dict__)
            
            pa1.latir()
            sleep(1)
            print(' ' * 20)
            print('Acho que', pa1.nome, 'gostou de você')
            break


print('Obrigado pela visita você será sempre bem vindo!')