# 📐 Diagrama UML - Sistema de RPG

## Diagrama de Classes (Notação UML)

```
┌────────────────────────────────────┐
│          Battle (Sistema)          │
├────────────────────────────────────┤
│ (Funções da Batalha)               │
├────────────────────────────────────┤
│ + selecionar_personagem()           │
│   : Characters                      │
│                                     │
│ + luta(p1: Characters,              │
│        p2: Characters): void        │
└────────────────────────────────────┘
           │ usa
           │ cria
           ▼
┌──────────────────────────────────────────────────────────────┐
│                     <<abstract>>                              │
│                      Characters                               │
├──────────────────────────────────────────────────────────────┤
│ - __name: str                                                │
│ - __life: int                                                │
│ - __max_life: int                                            │
│ - __attack: int                                              │
│ - __defense: int                                             │
│ + weapon_bonus: int = 0                                      │
│ + armor_bonus: int = 0                                       │
│ + pocao_uses: int = 0                                        │
│ + ability_uses: int = 1                                      │
├──────────────────────────────────────────────────────────────┤
│ + name: str {read-only}                                      │
│ + life: int {read-write}                                     │
│ + attack: int {read-only}                                    │
│ + defense: int {read-only}                                   │
│ + max_life: int {read-only}                                  │
│                                                               │
│ + atacar(alvo: Characters): int                              │
│ + receber_dano(dano: int): void                              │
│ + curar(quantidade: int): int                                │
│ + usar_pocao(quantidade: int = 30): bool                     │
│ + special_attack(alvo: Characters): int *                    │
└──────────────────────────────────────────────────────────────┘
                            △
              ┌─────────────┼─────────────┬─────────────┐
              │             │             │             │
    ┌─────────┴─────────┐ ┌─┴────────────┐ ┌──────────┴──┐ ┌───┴──────────┐
    │     Warrior       │ │   Paladin    │ │   Wizard   │ │    Archer    │
    ├───────────────────┤ ├──────────────┤ ├────────────┤ ├──────────────┤
    │ - weapon_name     │ │- weapon_name │ │- weapon_  │ │- weapon_name │
    │   = "Hemodren."   │ │  = "Ruptor   │ │  name =   │ │  = "Furacão" │
    │ - armor_name      │ │  Divino"     │ │  "Capuz"  │ │- armor_name  │
    │   = "Desespero"   │ │- armor_name  │ │- armor_   │ │  = "Arco-    │
    │ - special_name    │ │  = "Hooker"  │ │  name =   │ │  Escudo"     │
    │   = "Golpe        │ │- special_    │ │  "Zhonyas"│ │- special_    │
    │   Duplo"          │ │  name = "Golpe│ │- special_ │ │  name =      │
    │ - weapon_bonus=5  │ │  Sagrado"    │ │  name =   │ │  "Chuva de   │
    │ - armor_bonus=8   │ │- weapon_     │ │  "Bola de │ │  Flechas"    │
    │ - pocao_uses=1    │ │  bonus=5     │ │  Fogo"    │ │- weapon_     │
    │ - ability_uses=1  │ │- armor_bonus │ │- weapon_  │ │  bonus=8     │
    ├───────────────────┤ │  =6          │ │  bonus=6  │ │- armor_bonus │
    │ Stats Base:       │ │- pocao_uses= │ │- armor_   │ │  =5          │
    │ HP: 50            │ │  2           │ │  bonus=5  │ │- pocao_uses= │
    │ ATK: 13           │ │- ability_    │ │- pocao_   │ │  1           │
    │ DEF: 13           │ │  uses=1      │ │  uses=1   │ │- ability_    │
    │                   │ ├──────────────┤ │- ability_ │ │  uses=2      │
    │ + special_attack()│ │ Stats Base:  │ │  uses=2   │ ├──────────────┤
    │   dano = ATK * 2  │ │ HP: 25       │ ├────────────┤ │ Stats Base:  │
    │   - DEF           │ │ ATK: 14      │ │ Stats      │ │ HP: 20       │
    │                   │ │ DEF: 15      │ │ Base:      │ │ ATK: 10      │
    │   (Golpe Duplo)   │ │              │ │ HP: 15     │ │ DEF: 10      │
    │                   │ │ + special_   │ │ ATK: 22    │ │              │
    │                   │ │   attack()   │ │ DEF: 10    │ │ + special_   │
    │                   │ │   dano = ATK │ │            │ │   attack()   │
    │                   │ │   + 5 - DEF  │ │ + special_ │ │   dano = ATK │
    │                   │ │              │ │   attack() │ │   * 3 - DEF  │
    │                   │ │   cura =     │ │   dano =   │ │              │
    │                   │ │   DEF // 2   │ │   ATK + 10 │ │   (Chuva de  │
    │                   │ │              │ │   - DEF    │ │   Flechas)   │
    │                   │ │   (Golpe     │ │            │ │              │
    │                   │ │   Sagrado +  │ │   (Bola de │ │              │
    │                   │ │   Cura)      │ │   Fogo)    │ │              │
    └───────────────────┘ └──────────────┘ └────────────┘ └──────────────┘
```

---

## 🎮 Classe Battle - Sistema de Combate

A classe `Battle` (ou módulo `battle.py`) não é uma classe tradicional no seu código, mas uma **classe utilitária com métodos estáticos**. Aqui está a representação correta em UML:

```
┌────────────────────────────────────────────────────────────┐
│                      <<utility>>                            │
│                       Battle                                │
├────────────────────────────────────────────────────────────┤
│ (Sem atributos - apenas funções)                           │
├────────────────────────────────────────────────────────────┤
│ + {static} selecionar_personagem(): Characters             │
│   - Exibe menu com as 4 classes disponíveis               │
│   - Obtém entrada do usuário (escolha 1-4)                │
│   - Obtém nome do personagem                               │
│   - Retorna: instância da classe escolhida                │
│                                                             │
│ + {static} luta(p1: Characters,                            │
│              p2: Characters): void                         │
│   - Executa combate por turnos                            │
│   - p1 vs p2 alternando turnos                            │
│   - Cada turno: menu de ações (ataque/especial/poção)     │
│   - Termina quando um personagem atinge HP ≤ 0            │
│   - Anuncia vencedor                                       │
└────────────────────────────────────────────────────────────┘
           │ cria (instancia)
           │ utiliza
           ▼
┌──────────────────────────────────────────────────────────────┐
│                     <<abstract>>                              │
│                      Characters                               │
```

---

## 📋 Relacionamento: Battle ↔ Characters

| Aspecto | Detalhes |
|---------|----------|
| **Tipo de Relação** | Dependência / Utilização |
| **O que faz** | `Battle` cria e manipula instâncias de `Characters` |
| **Métodos que usam** | `selecionar_personagem()` instancia as 4 subclasses |
| **Em `luta()`** | Chama `atacar()`, `special_attack()`, `usar_pocao()`, `receber_dano()` |

---

## ✅ O que você adicionou (com melhorias):

### Seu formato:
```
batalha
+selecionar_personagem():personagem
---------------------------------------------
+luta(p1,p2)
```

### Formato UML correto:
```
┌─────────────────────────────────────┐
│        <<utility>> Battle           │
├─────────────────────────────────────┤
│ + selecionar_personagem()            │
│   : Characters                       │
│                                      │
│ + luta(p1: Characters,               │
│        p2: Characters): void         │
└─────────────────────────────────────┘
```

---

## 🔧 Complementações Necessárias:

### 1️⃣ **Tipos de Retorno e Parâmetros**
✅ `selecionar_personagem(): Characters` - retorna um personagem
✅ `luta(p1: Characters, p2: Characters): void` - não retorna nada

### 2️⃣ **Estereótipo `<<utility>>`**
- Indica que é uma classe com métodos estáticos (não instancia)
- Não tem atributos de instância
- Apenas agrupa funções relacionadas

### 3️⃣ **Documentação dos Métodos**
```
+ selecionar_personagem(): Characters
  - Propósito: Exibe menu e cria personagem
  - Entrada: Escolha (1-4) + Nome
  - Saída: Instância de Characters (Warrior, Paladin, Wizard ou Archer)
  - Efeitos: Imprime menu, pede entrada do usuário

+ luta(p1: Characters, p2: Characters): void
  - Propósito: Executa combate por turnos
  - Entrada: Dois personagens
  - Saída: Nenhuma (apenas imprime resultado)
  - Efeitos: Altera vida dos personagens, alterna turnos
```

---

## 📊 Diagrama Completo com Battle

```
                    ┌─────────────────────────┐
                    │   <<utility>>           │
                    │      Battle             │
                    ├─────────────────────────┤
                    │+ selecionar_personagem()│
                    │  : Characters           │
                    │                         │
                    │+ luta(p1,p2): void     │
                    └────────────┬────────────┘
                                 │ utiliza
                                 │ cria
                                 ▼
                    ┌────────────────────────────────────┐
                    │    <<abstract>>                    │
                    │      Characters                    │
                    ├────────────────────────────────────┤
                    │ - __name, __life, __max_life       │
                    │ - __attack, __defense              │
                    │ + weapon_bonus, armor_bonus        │
                    ├────────────────────────────────────┤
                    │ + name, life, attack, defense      │
                    │ + atacar(alvo): int                │
                    │ + special_attack(alvo): int *      │
                    │ + receber_dano(dano): void         │
                    │ + curar(qtd): int                  │
                    │ + usar_pocao(): bool               │
                    └────────────────────────────────────┘
                                 △
              ┌──────────────────┼──────────────────┬──────────────────┐
              │                  │                  │                  │
        ┌─────┴────┐      ┌──────┴────┐      ┌──────┴────┐      ┌─────┴────┐
        │ Warrior  │      │ Paladin   │      │  Wizard   │      │ Archer   │
        └──────────┘      └───────────┘      └───────────┘      └──────────┘
```

---

## 📝 Versão

### Modificadores de Acesso
| Símbolo | Significado | Exemplo |
|---------|------------|---------|
| `-` | **Privado** | `-__name: str` (não pode ser acessado fora da classe) |
| `+` | **Público** | `+weapon_bonus: int` (pode ser acessado de qualquer lugar) |
| `#` | **Protegido** | (não usado neste projeto) |

### Atributos
- `attribute: type` - Declaração normal
- `attribute: type = valor_padrao` - Com valor padrão
- `{read-only}` - Propriedade que só lê (getter)
- `{read-write}` - Propriedade que lê e escreve (getter + setter)

### Métodos
- `+ method(param: type): return_type` - Método público que retorna um tipo
- `*` - Método abstrato (deve ser implementado nas subclasses)

### Herança
- Seta `△` aponta de filha para mãe
- `Warrior` herda de `Characters`

---

# 🔍 Função `getattr()` - Explicação Completa

## O que é `getattr()`?

`getattr()` é uma função built-in do Python que **obtém o valor de um atributo de um objeto de forma segura**. Permite que você acesse atributos dinamicamente, com a possibilidade de definir um valor padrão caso o atributo não exista.

### Sintaxe
```python
getattr(objeto, 'nome_atributo', valor_padrao)
```

### Parâmetros
1. **objeto**: O objeto de onde você quer obter o atributo
2. **'nome_atributo'**: O nome do atributo como string
3. **valor_padrao** (opcional): O valor retornado se o atributo não existir

---

## Por Que Usamos `getattr()` Neste Projeto?

### ❌ Problema Sem `getattr()`

Imagine que queremos acessar `weapon_bonus` de um personagem:

```python
# Forma direta (perigosa)
dano = self.attack + self.weapon_bonus - alvo.defense
#                     ↑
#            O que acontece se weapon_bonus não existir?
#            ❌ AttributeError: 'Wizard' object has no attribute 'weapon_bonus'
```

**Problema:** Se a classe não tiver o atributo `weapon_bonus` definido, o programa **quebra com erro**.

---

### ✅ Solução Com `getattr()`

```python
# Forma segura com getattr()
bonus_arma = getattr(self, 'weapon_bonus', 0)
#             ↑          ↑                    ↑
#           função    objeto             valor padrão (se não existir)

dano = self.attack + bonus_arma - alvo.defense
#      Se weapon_bonus não existir, usa 0!
```

**Vantagem:** Se o atributo não existir, usa o valor padrão `0` em vez de quebrar o programa.

---

## Exemplos Práticos do Seu Código

### 1️⃣ Em `Personagem.py` - Método `atacar()`

```python
def atacar(self, alvo):
    # Obtém weapon_bonus, se não existir usa 0
    bonus_arma = getattr(self, 'weapon_bonus', 0)
    #                    ↑       ↑               ↑
    #                personagem atributo    padrão
    
    ataque_total = self.attack + bonus_arma
    dano = ataque_total - alvo.defense
    
    if dano < 0:
        dano = 0
    
    alvo.receber_dano(dano)
    return dano
```

**Por que usar aqui?**
- Nem todas as subclasses definem `weapon_bonus` logo de entrada
- Se usássemos `self.weapon_bonus` diretamente, daria erro se não existisse
- Com `getattr()`, se não houver bônus de arma, usa 0 e tudo funciona

---

### 2️⃣ Em `Personagem.py` - Property `defense`

```python
@property
def defense(self):
    # Obtém armor_bonus (bônus de armadura)
    return self.__defense + getattr(self, 'armor_bonus', 0)
    #                                  ↑               ↑
    #                        proteção contra     valor padrão
    #                       atributo inexistente
```

**Por que usar aqui?**
- Cada classe filha pode ou não ter `armor_bonus`
- A defesa base sempre existe (`self.__defense`)
- O bônus é opcional: se não existir, soma 0
- Permite flexibilidade: classes podem ter ou não armadura

---

### 3️⃣ Em `Personagem.py` - Método `special_attack()` (classes filhas)

```python
def special_attack(self, alvo):
    # Verifica se ability_uses existe, se não usa 0
    if getattr(self, 'ability_uses', 0) <= 0:
        print(f'{self.name} não tem usos restantes da habilidade!')
        return 0
    #      ↑
    # Se ability_uses não existir, a condição <= 0 será verdadeira
    # porque getattr retorna 0 (valor padrão)
    
    self.ability_uses -= 1
    # ... resto da lógica
```

**Por que usar aqui?**
- Verifica se ainda existem usos da habilidade
- Se não houver o atributo, considera como 0 usos (sem habilidade)
- Previne erros ao tentar decrementar um atributo inexistente

---

### 4️⃣ Em `battle.py` - Menu de Seleção

```python
def selecionar_personagem():
    classes = [
        ("1", "Guerreiro", Warrior),
        ("2", "Paladino", Paladin),
        ("3", "Mago", Wizard),
        ("4", "Arqueiro", Archer),
    ]

    print("\n=== ESCOLHA SUA CLASSE ===")
    for esc, label, cls in classes:
        temp = cls("__stats__")  # Cria instância temporária para exibir
        
        # Obtém os nomes de equipamento, se não existirem usa "—"
        weapon = getattr(temp, 'weapon_name', '—')
        #                 ↑      ↑              ↑
        #            objeto   atributo      símbolo padrão
        
        armor = getattr(temp, 'armor_name', '—')
        ability = getattr(temp, 'special_name', '—')
        
        print(f"{esc} - {label}  |  HP:{temp.life} ATK:{temp.attack} DEF:{temp.defense}  |  Arma:{weapon}  Armadura:{armor}  Habilidade:{ability}")
```

**Por que usar aqui?**
- Personagens podem ter diferentes tipos de equipamento
- Se um não tiver `weapon_name` definido, mostra `—` em vez de dar erro
- Torna o código robusto: funciona mesmo se atributos estiverem faltando

---

### 5️⃣ Em `battle.py` - Anúncio de Habilidade

```python
elif acao == "2":
    dano = atacante.special_attack(defensor)
    # Obtém o nome da habilidade especial
    special = getattr(atacante, 'special_name', 'ataque especial')
    #                 ↑            ↑                ↑
    #            personagem   nome da         nome padrão
    #                         habilidade      se não existir
    
    print(f"{atacante.name} usou {special} causando {dano} de dano!")
```

**Por que usar aqui?**
- Se o personagem não tiver `special_name` definido, mostra "ataque especial"
- Evita erro ao tentar imprimir um atributo inexistente

---

## 📊 Comparação: Com vs Sem `getattr()`

### ❌ SEM `getattr()` - Código Frágil

```python
def atacar(self, alvo):
    # Acesso direto - PERIGOSO!
    ataque_total = self.attack + self.weapon_bonus  # ← Pode quebrar!
    dano = ataque_total - alvo.defense
    return dano

# Se criar uma classe sem weapon_bonus:
class MinhaClasse(Characters):
    pass

guerreiro = MinhaClasse("Test")
guerreiro.atacar(outro)  # ❌ AttributeError!
```

### ✅ COM `getattr()` - Código Robusto

```python
def atacar(self, alvo):
    # Acesso seguro com valor padrão
    bonus = getattr(self, 'weapon_bonus', 0)  # ← Seguro!
    ataque_total = self.attack + bonus
    dano = ataque_total - alvo.defense
    return dano

# Mesmo sem weapon_bonus:
class MinhaClasse(Characters):
    pass

guerreiro = MinhaClasse("Test")
guerreiro.atacar(outro)  # ✅ Funciona! Usa bonus = 0
```

---

## 🎯 Benefícios do `getattr()` Neste Projeto

| Benefício | Descrição |
|-----------|-----------|
| **Segurança** | Evita `AttributeError` se um atributo não existir |
| **Flexibilidade** | Permite subclasses com atributos diferentes |
| **Compatibilidade** | Código funciona com classes que podem ou não ter certos atributos |
| **Manutenibilidade** | Fácil adicionar novos atributos opcionais |
| **Defaultização** | Define valores padrão automaticamente |

---

## 📚 Casos de Uso em Python

```python
# Exemplo 1: Acesso simples
class Pessoa:
    def __init__(self):
        self.nome = "João"

p = Pessoa()
print(getattr(p, 'nome'))           # Output: "João"
print(getattr(p, 'idade', 25))      # Output: 25 (não existe, usa padrão)

# Exemplo 2: Verificar atributo existe
class Carro:
    def __init__(self):
        self.rodas = 4

c = Carro()
if hasattr(c, 'motor'):  # hasattr usa getattr internamente
    print("Tem motor")
else:
    print("Sem motor")

# Exemplo 3: Dinâmico (como no seu código)
def exibir_atributo(obj, attr_name):
    valor = getattr(obj, attr_name, "Não disponível")
    print(f"{attr_name}: {valor}")

exibir_atributo(guerreiro, 'weapon_name')      # OK
exibir_atributo(guerreiro, 'poder_teleportação')  # "Não disponível"
```

---

## 🔗 Relação com Encapsulamento

`getattr()` é especialmente útil quando combinado com **encapsulamento**:

```python
class Characters:
    def __init__(self):
        self.__life = 100  # Privado
        self.weapon_bonus = 0  # Público
    
    @property
    def life(self):  # Getter
        return self.__life

# Com getattr(), podemos acessar de forma segura:
print(getattr(personagem, 'life'))         # ✅ OK (é uma property)
print(getattr(personagem, '__life'))       # ❌ Não funciona (privado)
print(getattr(personagem, 'vida', 0))      # ✅ OK (usa padrão)
```

---

## Resumo

| Conceito | O que faz |
|----------|-----------|
| `getattr(obj, 'attr', default)` | Obtém o valor de um atributo, retornando `default` se não existir |
| **Neste projeto** | Torna o código robusto contra atributos ausentes |
| **Vantagem** | Evita erros, permite flexibilidade, código mais limpo |
| **Usado em** | `Personagem.py`, `battle.py`, todas as classes |

**Em uma frase:** `getattr()` é o "jeito seguro" de acessar atributos que podem ou não existir! 🎯
