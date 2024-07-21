from random import randint 

lista_npcs = [] 


#staus do player 
player = {
    "nome": "Gabriel",
    "level": 1,
    "exp": 0,
    "exp_max": 30,
    "hp": 100,
    "hp_max" : 100,
    "dano": 25,
    
}


#Criação aleatoria de npc 
def criar_npc(level) :
    novo_npc = {
        "nome": f"monstro #{level}",
        "level": level,
        "dano": 5 * level,
        "hp": 100 * level,
        "hp_max" : 100 * level,
        "exp": 7 * level,  
    }
    
    return novo_npc 
    
def gerar_npcs(n_npcs):
    for x in range(n_npcs):
        npc = criar_npc(x+1) 
        lista_npcs.append(npc)


def exibir_npcs(): 
   for npc in lista_npcs: 
      exibir_npc(npc)

def exibir_npc(npc):
    print(
          f"nome:{npc['nome']} // level: {npc['level']}// dano: {npc['dano']} // hp: {npc['hp']}// exp:{npc['exp']}"
        )
def exibir_player():
    print(
          f"nome:{player['nome']} // level: { player ['level']}// dano: {player['dano']} // hp: {player['hp']}/hp_max: {player['hp_max']}// exp:{player['exp']}/exp_max: {player['exp_max']}"
    )

def reset_player():
    player["hp"] = player['hp_max'] 
    
def reset_npc(npc):
    npc["hp"] = npc['hp_max'] 
    
def level_up():
    if player['exp'] >= player['exp_max'] :
        player ['level'] += 1 
        player ['exp']  = 0 
        player ['exp_max']  = player ['exp_max'] * 2
        player ['dano'] = player ['dano'] *  player ['level'] 
        player ['hp_max'] = player ['hp'] * player ['level']
        reset_player()
    
def iniciar_batalha(npc):
    while player["hp"] > 0 and npc["hp"]>0:
        atacar_npc(npc)
        atacar_player(npc)
        exibir_info_batalha(npc)
        
    
    if player['hp'] > 0 : 
        print(f"Parabens {player["nome"]} Voce acaba de ganhar do mostro {npc["nome"]} !!!!!")
        player['exp'] += npc['exp']
        exibir_player()
    else:
        print(f"player{player["nome"]} acaba de morrer lutando contra mostro {npc["nome"]} >-< ")
        exibir_npc(npc)
    level_up()
    
    reset_npc(npc)
    reset_player()
    
# atacar_npc(npc) - npc:hp - player:dano 
def atacar_npc(npc): #player atacando npc 
    npc["hp"] -= player["dano"]
    
#atacar_player(npc) - playeer:hp - npc:dano
def atacar_player(npc): #npc atacando player
    player["hp"] -= npc ["dano"]


def exibir_info_batalha(npc):
    print(f"Player:{player['hp']}/{player['hp_max']}")
    print(f"Npc:{npc['nome']}/{npc['hp']}/{npc['hp_max']}")
    print("------------------------------\n")
    
    
gerar_npcs(5) 
#exibir_npcs()

npc_selecionado = lista_npcs[0] 
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)
exibir_player ()