DOACOES = []
AZUL_CLARO = '\033[94m'
CIANO_CLARO = '\033[96m'
VERMELHO_CLARO = '\033[91m'
AMARELO_CLARO = '\033[93m'
BRANCO = '\033[97m'
RESET = '\033[0m'




def REGISTRAR_DOACAO():
    print(f'{CIANO_CLARO}--- REGISTRAR NOVA DOAÇÃO ---{RESET}')
    NOME = input(f'{AZUL_CLARO}NOME DO DOADOR: {RESET}')
    TIPO = input(f'{AZUL_CLARO}TIPO DE DOAÇÃO (ALIMENTO, ROUPA, BRINQUEDO, ETC.): {RESET} ')
    try:
        QUANTIDADE = int(input(f'{AZUL_CLARO}QUANTIDADE:'))
    except ValueError:
        print(f'QUANTIDADE INVÁLIDA!❌🥵 REGISTRO CANCELADO.')
        return
    DATA = input(f'DATA DA DOAÇÃO (EX: 14/05/2025): ')
    ENTREGUE = input(f'A DOAÇÃO JÁ FOI ENTREGUE? (S/N): {RESET}').lower() == 'sim' or 'nao'

    DOACAO = {
        'id': len(DOACOES) + 1,
        'doador': NOME,
        'tipo': TIPO,
        'quantidade': QUANTIDADE,
        'data': DATA,
        'entregue': ENTREGUE
    }

    DOACOES.append(DOACAO)
    print('\n')
    print(f'{AMARELO_CLARO}✅ DOAÇÃO REGISTRADA COM SUCESSO!✅👌😎{RESET}')
    print('\n')



def VER_TODAS_DOACOES():
    print(f'{CIANO_CLARO}--- LISTA DE TODAS AS DOAÇÕES ---  {RESET}')
    if not DOACOES:
        print(f'{VERMELHO_CLARO}NENHUMA DOAÇÃO REGISTRADA.{RESET}')
        return
    for D in DOACOES:
        print(f"{AZUL_CLARO}ID: {D['id']} | DOADOR: {D['doador']} | TIPO: {D['tipo']} | QTD: {D['quantidade']} | DATA: {D['data']} | ENTREGUE: {'SIM' if D['entregue'] else 'NÃO'}{RESET}")
        print('\n')



def CONSULTAR_POR_TIPO():
    print(f'{CIANO_CLARO}--- CONSULTAR DOAÇÕES POR TIPO ---{RESET}')
    TIPO = input(f'{AZUL_CLARO}DIGITE O TIPO DE DOAÇÃO QUE DESEJA CONSULTAR: {RESET}').lower()
    FILTRADAS = [D for D in DOACOES if D['tipo'].lower() == TIPO]
    if not FILTRADAS:
        print(f'{AMARELO_CLARO}NENHUMA DOAÇÃO DO TIPO "{TIPO.upper()}" ENCONTRADA.{RESET}')
        print('\n')
        return
    for D in FILTRADAS:
        print(f"{AZUL_CLARO}ID: {D['id']} | DOADOR: {D['doador']} | QTD: {D['quantidade']} | DATA: {D['data']} | ENTREGUE: {'SIM' if D['entregue'] else 'NÃO'}{RESET}")
        print('\n')



def MARCAR_COMO_ENTREGUE():
    print(f'{CIANO_CLARO}--- MARCAR DOAÇÃO COMO ENTREGUE ---{RESET}')
    try:
        ID_BUSCA = int(input(f'{AZUL_CLARO}DIGITE O ID DA DOAÇÃO QUE FOI ENTREGUE: '))
        for D in DOACOES:
            if D[f'id'] == ID_BUSCA:
                D[f'entregue{RESET}'] = True
                print(f'{AMARELO_CLARO}✅ DOAÇÃO MARCADA COMO ENTREGUE!{RESET}')
                print('\n')
                return
        print(f'{VERMELHO_CLARO}ID NÃO ENCONTRADO.')
        print('\n')
    except ValueError:
        print(f'ID INVÁLIDO.{RESET}')



def MENU():
    while True:
        print(f'{CIANO_CLARO}===== SISTEMA DE GERENCIAMENTO DE DOAÇÕES ====={RESET}')
        print(f'{AZUL_CLARO}1. REGISTRAR DOAÇÃO')
        print(f'2. VER TODAS DOAÇÕES ')
        print(f'3. CONSULTAR POR TIPO')
        print(f'4. MARCAR COMO ENTREGUE{RESET}')
        print(f'{VERMELHO_CLARO}5. SAIR{RESET}')
        ESCOLHA = str(input(f'{CIANO_CLARO} ESCOLHA UMA OPÇAO: {RESET}'))
        print('\n')
        if ESCOLHA == '1':
            REGISTRAR_DOACAO()
        elif ESCOLHA == '2':
            VER_TODAS_DOACOES()
        elif ESCOLHA == '3':
            CONSULTAR_POR_TIPO()
        elif ESCOLHA == '4':
            MARCAR_COMO_ENTREGUE()
        elif ESCOLHA == '5':

            break
        else:
            print(f'{VERMELHO_CLARO}❌OPÇÃO INVALIDA TENTA NOVAMENTE🥵😒.{RESET}')


MENU()
