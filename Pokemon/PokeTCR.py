'''
Created on 9 nov. 2023

@author: Chevalier Théotim
'''


import random
from mainTypes2 import EnumTypes
from attacks import attacks, SetAttack

class SetPokemon:
  def __init__(self, name:str, hp:int, attack:int, defense:int, specAttack:int, specDefense:int, speed:int, types:list[EnumTypes], xp:int, ptsXp:int, maxXP:int, attacksPokemon:list[SetAttack]):
    self.name = name #nom
    self.hp = hp #iv pv
    self.attack = attack #iv attack
    self.defense = defense #iv defense
    self.specAttack = specAttack #iv spé attaque
    self.specDefense = specDefense #iv spé defense
    self.speed = speed  #iv speed
    self.types = types #type list[EnumTypes]
    self.xp = xp  #xp actuell du pokemon
    self.life = 10 #cacluler les pv en fonction des iv / lvl, pv du actuel pokemon
    #self.capXp = capXp #cap xp pour cacluler les niveau //1029.495
    self.ptsXp = ptsXp #xp donner 
    self.maxXp = maxXP  #xp lvl 100
    self.attacks = attacksPokemon #attaque list[setAttack]

    """
    calculer xp pour le lvl suivant : N = (N^3) * 5
    calculer le lvl : Niveau (N) = Racine carrée (XP / 5)
    """

pokemons = {
  1: SetPokemon("Bulbizarre", 45, 49, 49, 65, 65, 45, 0, 0, 64, [EnumTypes.Plante, EnumTypes.Poison], [attacks[1], attacks[1]]),
  2: SetPokemon("Herbizarre", 60, 62, 63, 80, 80, 60, 0, 0, 64, [EnumTypes.Plante, EnumTypes.Poison], [attacks[3], attacks[1]]),
  3: SetPokemon("Florizarre", 80, 82, 83, 100, 100, 80, 0, 0, 64, [EnumTypes.Plante, EnumTypes.Poison], [attacks[4], attacks[1]]),
  4: SetPokemon("Salamèche", 39, 52, 43, 60, 50, 65, 0, 0, 64, [EnumTypes.Feu], [attacks[4], attacks[1]]),
  5: SetPokemon("Reptincel", 58, 64, 58, 80, 65, 80, 0, 0, 64, [EnumTypes.Feu], [attacks[5], attacks[1]]),
  6: SetPokemon("Dracaufeu", 78, 84, 78, 109, 85, 100, 0, 0, 64, [EnumTypes.Feu], [attacks[8], attacks[1]]),
  7: SetPokemon("Carapuce", 44, 48, 65, 50, 64, 43, 0, 0, 64, [EnumTypes.Eau], [attacks[6], attacks[1]]),
  8: SetPokemon("Carabaffe", 59, 63, 80, 65, 80, 58, 0, 0, 64, [EnumTypes.Eau], [attacks[6], attacks[1]]),
  9: SetPokemon("Tortank", 79, 83, 100, 85, 105, 78, 0, 0, 64, [EnumTypes.Eau], [attacks[7], attacks[1]]),
  10: SetPokemon("Chenipan", 45, 30, 35, 20, 20, 45, 0, 0, 64, [EnumTypes.Insecte], [attacks[2], attacks[3]]),
  11: SetPokemon("Chrysacier", 50, 20, 55, 25, 25, 30, 0, 0, 64, [EnumTypes.Insecte], [attacks[4], attacks[5]]),
  12: SetPokemon("Papilusion", 60, 45, 50, 90, 80, 70, 0, 0, 64, [EnumTypes.Insecte, EnumTypes.Vol], [attacks[6], attacks[7]]),
  13: SetPokemon("Aspicot", 40, 35, 30, 20, 20, 50, 0, 0, 64, [EnumTypes.Insecte, EnumTypes.Poison], [attacks[8], attacks[9]]),
  14: SetPokemon("Coconfort", 45, 25, 50, 25, 25, 35, 0, 0, 64, [EnumTypes.Insecte, EnumTypes.Poison], [attacks[10], attacks[11]]),
  15: SetPokemon("Dardargnan", 65, 90, 40, 45, 80, 75, 0, 0, 64, [EnumTypes.Insecte, EnumTypes.Poison], [attacks[12], attacks[13]]),
  16: SetPokemon("Roucool", 40, 45, 40, 35, 35, 56, 0, 0, 64, [EnumTypes.Normal, EnumTypes.Vol], [attacks[14], attacks[15]]),
  17: SetPokemon("Roucoups", 63, 60, 55, 50, 50, 71, 0, 0, 64, [EnumTypes.Normal, EnumTypes.Vol], [attacks[16], attacks[17]]),
  18: SetPokemon("Roucarnage", 83, 80, 75, 70, 70, 101, 0, 0, 64, [EnumTypes.Normal, EnumTypes.Vol], [attacks[18], attacks[19]]),
  19: SetPokemon("Rattata", 30, 56, 35, 25, 35, 72, 0, 0, 64, [EnumTypes.Normal], [attacks[20], attacks[21]]),
  20: SetPokemon("Rattatac", 55, 81, 60, 50, 70, 97, 0, 0, 64, [EnumTypes.Normal], [attacks[22], attacks[23]]),
  21: SetPokemon("Piafabec", 40, 60, 30, 31, 31, 70, 0, 0, 64, [EnumTypes.Normal, EnumTypes.Vol], [attacks[24], attacks[25]]),
  22: SetPokemon("Rapasdepic", 65, 90, 65, 61, 61, 100, 0, 0, 64, [EnumTypes.Normal, EnumTypes.Vol], [attacks[26], attacks[27]]),
  23: SetPokemon("Abo", 35, 60, 44, 40, 54, 55, 0, 0, 64, [EnumTypes.Poison], [attacks[28], attacks[29]]),
  24: SetPokemon("Arbok", 60, 85, 69, 65, 79, 80, 0, 0, 64, [EnumTypes.Poison], [attacks[30], attacks[31]]),
  25: SetPokemon("Pikachu", 35, 55, 40, 50, 50, 90, 0, 0, 64, [EnumTypes.Electrique], [attacks[32], attacks[33]]),
  26: SetPokemon("Raichu", 60, 90, 55, 90, 80, 110, 0, 0, 64, [EnumTypes.Electrique], [attacks[34], attacks[35]]),
  27: SetPokemon("Sabelette", 50, 75, 85, 20, 30, 40, 0, 0, 64, [EnumTypes.Sol], [attacks[36], attacks[37]]),
  28: SetPokemon("Sablaireau", 75, 100, 110, 45, 55, 65, 0, 0, 64, [EnumTypes.Sol], [attacks[38], attacks[39]]),
  29: SetPokemon("Nidoran♀", 55, 47, 52, 40, 40, 41, 0, 0, 64, [EnumTypes.Poison], [attacks[40], attacks[41]]),
  30: SetPokemon("Nidorina", 70, 62, 67, 55, 55, 56, 0, 0, 64, [EnumTypes.Poison], [attacks[42], attacks[43]]),
  31: SetPokemon("Nidoqueen", 90, 82, 87, 75, 85, 76, 0, 0, 64, [EnumTypes.Poison, EnumTypes.Sol], [attacks[44], attacks[45]]),
  32: SetPokemon("Nidoran♂", 46, 57, 40, 40, 40, 50, 0, 0, 64, [EnumTypes.Poison], [attacks[46], attacks[47]]),
  33: SetPokemon("Nidorino", 61, 72, 57, 55, 55, 65, 0, 0, 64, [EnumTypes.Poison], [attacks[48], attacks[49]]),
  34: SetPokemon("Nidoking", 81, 102, 77, 85, 75, 85, 0, 0, 64, [EnumTypes.Poison, EnumTypes.Sol], [attacks[50], attacks[51]]),
  35: SetPokemon("Mélofée", 70, 45, 48, 60, 65, 35, 0, 0, 64, [EnumTypes.Fée], [attacks[52], attacks[53]]),
  36: SetPokemon("Mélodelfe", 95, 70, 73, 85, 90, 60, 0, 0, 64, [EnumTypes.Fée], [attacks[54], attacks[55]]),
  37: SetPokemon("Goupix", 38, 41, 40, 50, 65, 65, 0, 0, 64, [EnumTypes.Feu], [attacks[56], attacks[57]]),
  38: SetPokemon("Feunard", 73, 76, 75, 81, 100, 100, 0, 0, 64, [EnumTypes.Feu], [attacks[58], attacks[59]]),
  39: SetPokemon("Rondoudou", 115, 70, 45, 60, 75, 20, 0, 0, 64, [EnumTypes.Normal, EnumTypes.Fée], [attacks[60], attacks[61]]),
  40: SetPokemon("Grodoudou", 140, 140, 70, 85, 90, 45, 0, 0, 64, [EnumTypes.Normal, EnumTypes.Fée], [attacks[62], attacks[63]]),
  41: SetPokemon("Nosferapti", 40, 45, 35, 30, 40, 55, 0, 0, 64, [EnumTypes.Poison, EnumTypes.Vol], [attacks[64], attacks[65]]),
  42: SetPokemon("Nosferalto", 75, 80, 70, 65, 85, 90, 0, 0, 64, [EnumTypes.Poison, EnumTypes.Vol], [attacks[66], attacks[67]]),
  43: SetPokemon("Mystherbe", 45, 60, 62, 40, 40, 60, 0, 0, 64, [EnumTypes.Plante, EnumTypes.Poison], [attacks[68], attacks[69]]),
  44: SetPokemon("Ortide", 60, 75, 65, 55, 55, 90, 0, 0, 64, [EnumTypes.Plante, EnumTypes.Poison], [attacks[70], attacks[71]]),
  45: SetPokemon("Rafflesia", 75, 90, 80, 70, 85, 100, 0, 0, 64, [EnumTypes.Plante, EnumTypes.Poison], [attacks[72], attacks[73]]),
  46: SetPokemon("Paras", 35, 70, 55, 45, 55, 25, 0, 0, 64, [EnumTypes.Insecte, EnumTypes.Plante], [attacks[74], attacks[75]]),
  47: SetPokemon("Parasect", 60, 95, 80, 60, 80, 30, 0, 0, 64, [EnumTypes.Insecte, EnumTypes.Plante], [attacks[76], attacks[77]]),
  48: SetPokemon("Mimitoss", 60, 55, 50, 40, 55, 45, 0, 0, 64, [EnumTypes.Insecte, EnumTypes.Poison], [attacks[78], attacks[79]]),
  49: SetPokemon("Aéromite", 70, 80, 75, 70, 85, 90, 0, 0, 64, [EnumTypes.Insecte, EnumTypes.Poison], [attacks[80], attacks[81]]),
  50: SetPokemon("Taupiqueur", 10, 55, 25, 35, 45, 95, 0, 0, 64, [EnumTypes.Sol], [attacks[82], attacks[83]]),
  51: SetPokemon("Triopikeur", 35, 80, 50, 50, 70, 120, 0, 0, 64, [EnumTypes.Sol], [attacks[84], attacks[85]]),
  52: SetPokemon("Miaouss", 40, 45, 35, 40, 40, 90, 0, 0, 64, [EnumTypes.Normal], [attacks[86], attacks[87]]),
  53: SetPokemon("Persian", 65, 70, 60, 65, 65, 115, 0, 0, 64, [EnumTypes.Normal], [attacks[88], attacks[89]]),
  54: SetPokemon("Psykokwak", 50, 52, 48, 65, 50, 55, 0, 0, 64, [EnumTypes.Eau], [attacks[90], attacks[91]]),
  55: SetPokemon("Akwakwak", 80, 82, 78, 95, 80, 85, 0, 0, 64, [EnumTypes.Eau], [attacks[92], attacks[93]]),
  56: SetPokemon("Férosinge", 40, 80, 35, 35, 45, 70, 0, 0, 64, [EnumTypes.Combat], [attacks[94], attacks[95]]),
  57: SetPokemon("Colossinge", 65, 105, 60, 60, 70, 95, 0, 0, 64, [EnumTypes.Combat], [attacks[96], attacks[97]]),
  58: SetPokemon("Caninos", 55, 70, 45, 70, 50, 60, 0, 0, 64, [EnumTypes.Feu], [attacks[98], attacks[99]]),
  59: SetPokemon("Arcanin", 90, 110, 80, 100, 80, 95, 0, 0, 64, [EnumTypes.Feu], [attacks[100], attacks[101]]),
  60: SetPokemon("Ptitard", 40, 50, 40, 40, 54, 55, 0, 0, 64, [EnumTypes.Eau], [attacks[102], attacks[103]]),
  61: SetPokemon("Têtarte", 65, 65, 65, 50, 64, 70, 0, 0, 64, [EnumTypes.Eau], [attacks[104], attacks[105]]),
  62: SetPokemon("Tartard", 90, 85, 85, 70, 85, 70, 0, 0, 64, [EnumTypes.Eau, EnumTypes.Combat], [attacks[106], attacks[107]]),
  63: SetPokemon("Abra", 25, 20, 15, 105, 55, 90, 0, 0, 64, [EnumTypes.Psy], [attacks[108], attacks[109]]),
  64: SetPokemon("Kadabra", 40, 35, 30, 120, 70, 105, 0, 0, 64, [EnumTypes.Psy], [attacks[110], attacks[111]]),
  65: SetPokemon("Alakazam", 55, 50, 45, 135, 85, 120, 0, 0, 64, [EnumTypes.Psy], [attacks[112], attacks[113]]),
  66: SetPokemon("Machoc", 70, 80, 50, 35, 35, 35, 0, 0, 64, [EnumTypes.Combat], [attacks[114], attacks[115]]),
  67: SetPokemon("Machopeur", 80, 100, 70, 50, 60, 45, 0, 0, 64, [EnumTypes.Combat], [attacks[116], attacks[117]]),
  68: SetPokemon("Mackogneur", 90, 130, 80, 65, 85, 55, 0, 0, 64, [EnumTypes.Combat], [attacks[118], attacks[119]]),
  69: SetPokemon("Chétiflor", 50, 75, 35, 70, 30, 40, 0, 0, 64, [EnumTypes.Plante, EnumTypes.Poison], [attacks[120], attacks[121]]),
  70: SetPokemon("Boustiflor", 65, 90, 50, 85, 45, 55, 0, 0, 64, [EnumTypes.Plante, EnumTypes.Poison], [attacks[122], attacks[123]]),
  71: SetPokemon("Empiflor", 80, 105, 65, 100, 70, 70, 0, 0, 64, [EnumTypes.Plante, EnumTypes.Poison], [attacks[124], attacks[125]]),
  72: SetPokemon("Tentacool", 40, 40, 35, 50, 100, 70, 0, 0, 64, [EnumTypes.Eau, EnumTypes.Poison], [attacks[126], attacks[127]]),
  73: SetPokemon("Tentacruel", 80, 70, 65, 80, 120, 100, 0, 0, 64, [EnumTypes.Eau, EnumTypes.Poison], [attacks[128], attacks[129]]),
  74: SetPokemon("Racaillou", 40, 80, 100, 30, 30, 20, 0, 0, 64, [EnumTypes.Roche, EnumTypes.Sol], [attacks[130], attacks[131]]),
  75: SetPokemon("Gravalanch", 55, 95, 115, 45, 45, 35, 0, 0, 64, [EnumTypes.Roche, EnumTypes.Sol], [attacks[132], attacks[133]]),
  76: SetPokemon("Grolem", 80, 120, 130, 55, 65, 45, 0, 0, 64, [EnumTypes.Roche, EnumTypes.Sol], [attacks[134], attacks[135]]),
  77: SetPokemon("Ponyta", 50, 85, 55, 65, 65, 90, 0, 0, 64, [EnumTypes.Feu], [attacks[136], attacks[137]]),
  78: SetPokemon("Galopa", 65, 100, 70, 80, 80, 105, 0, 0, 64, [EnumTypes.Feu], [attacks[138], attacks[139]]),
  79: SetPokemon("Ramoloss", 90, 65, 65, 40, 40, 15, 0, 0, 64, [EnumTypes.Eau, EnumTypes.Psy], [attacks[140], attacks[141]]),
  80: SetPokemon("Flagadoss", 95, 75, 110, 100, 80, 30, 0, 0, 64, [EnumTypes.Eau, EnumTypes.Psy], [attacks[142], attacks[143]]),
  81: SetPokemon("Magnéti", 25, 35, 70, 95, 55, 45, 0, 0, 64, [EnumTypes.Electrique, EnumTypes.Acier], [attacks[144], attacks[145]]),
  82: SetPokemon("Magnéton", 50, 60, 95, 120, 70, 70, 0, 0, 64, [EnumTypes.Electrique, EnumTypes.Acier], [attacks[146], attacks[147]]),
  83: SetPokemon("Canarticho", 60, 65, 55, 50, 50, 115, 0, 0, 64, [EnumTypes.Normal, EnumTypes.Vol], [attacks[148], attacks[149]]),
  84: SetPokemon("Doduo", 35, 85, 45, 35, 35, 75, 0, 0, 64, [EnumTypes.Normal, EnumTypes.Vol], [attacks[150], attacks[151]]),
  85: SetPokemon("Dodrio", 60, 110, 70, 60, 60, 110, 0, 0, 64, [EnumTypes.Normal, EnumTypes.Vol], [attacks[152], attacks[153]]),
  86: SetPokemon("Otaria", 65, 45, 55, 45, 70, 45, 0, 0, 64, [EnumTypes.Eau], [attacks[154], attacks[155]]),
  87: SetPokemon("Lamantine", 90, 70, 80, 70, 95, 70, 0, 0, 64, [EnumTypes.Eau, EnumTypes.Glace], [attacks[156], attacks[157]]),
  88: SetPokemon("Tadmorv", 80, 80, 50, 40, 50, 25, 0, 0, 64, [EnumTypes.Poison], [attacks[158], attacks[159]]),
  89: SetPokemon("Grotadmorv", 105, 105, 75, 65, 100, 50, 0, 0, 64, [EnumTypes.Poison], [attacks[160], attacks[161]]),
  90: SetPokemon("Kokiyas", 30, 42, 80, 42, 50, 25, 0, 0, 64, [EnumTypes.Eau], [attacks[162], attacks[163]]),
  91: SetPokemon("Crustabri", 50, 70, 100, 50, 100, 35, 0, 0, 64, [EnumTypes.Eau], [attacks[164], attacks[165]]),
  92: SetPokemon("Fantominus", 30, 35, 30, 100, 35, 80, 0, 0, 64, [EnumTypes.Spectre, EnumTypes.Poison], [attacks[166], attacks[167]]),
  93: SetPokemon("Spectrum", 45, 50, 45, 115, 55, 90, 0, 0, 64, [EnumTypes.Spectre, EnumTypes.Poison], [attacks[168], attacks[169]]),
  94: SetPokemon("Ectoplasma", 60, 65, 60, 130, 75, 110, 0, 0, 64, [EnumTypes.Spectre, EnumTypes.Poison], [attacks[170], attacks[171]]),
  95: SetPokemon("Onix", 35, 45, 160, 30, 45, 70, 0, 0, 64, [EnumTypes.Roche, EnumTypes.Sol], [attacks[172], attacks[173]]),
  96: SetPokemon("Soporifik", 60, 48, 45, 43, 90, 42, 0, 0, 64, [EnumTypes.Psy], [attacks[174], attacks[175]]),
  97: SetPokemon("Hypnomade", 85, 73, 70, 73, 115, 67, 0, 0, 64, [EnumTypes.Psy], [attacks[176], attacks[177]]),
  98: SetPokemon("Krabby", 30, 105, 90, 25, 25, 50, 0, 0, 64, [EnumTypes.Eau], [attacks[178], attacks[179]]),
  99: SetPokemon("Krabboss", 50, 130, 115, 50, 50, 75, 0, 0, 64, [EnumTypes.Eau], [attacks[180], attacks[181]]),
  100: SetPokemon("Voltorbe", 40, 30, 50, 55, 55, 100, 0, 0, 64, [EnumTypes.Electrique], [attacks[182], attacks[183]]),
  101: SetPokemon("Électrode", 60, 50, 70, 80, 80, 140, 0, 0, 64, [EnumTypes.Electrique], [attacks[184], attacks[185]]),
  102: SetPokemon("Noeunoeuf", 60, 40, 80, 60, 45, 40, 0, 0, 64, [EnumTypes.Plante, EnumTypes.Psy], [attacks[186], attacks[187]]),
  103: SetPokemon("Noadkoko", 95, 95, 85, 125, 75, 85, 0, 0, 64, [EnumTypes.Plante, EnumTypes.Psy], [attacks[188], attacks[189]]),
  104: SetPokemon("Osselait", 50, 50, 95, 40, 50, 35, 0, 0, 64, [EnumTypes.Sol], [attacks[190], attacks[191]]),
  105: SetPokemon("Ossatueur", 60, 80, 110, 50, 80, 45, 0, 0, 64, [EnumTypes.Sol], [attacks[192], attacks[193]]),
  106: SetPokemon("Kicklee", 50, 120, 53, 35, 110, 87, 0, 0, 64, [EnumTypes.Combat], [attacks[194], attacks[195]]),
  107: SetPokemon("Tygnon", 50, 105, 79, 35, 110, 76, 0, 0, 64, [EnumTypes.Combat], [attacks[196], attacks[197]]),
  108: SetPokemon("Excelangue", 90, 55, 75, 60, 75, 30, 0, 0, 64, [EnumTypes.Normal], [attacks[198], attacks[199]]),
  109: SetPokemon("Smogo", 40, 65, 95, 60, 45, 35, 0, 0, 64, [EnumTypes.Poison], [attacks[200], attacks[200]]),
110: SetPokemon("Smogogo", 65, 90, 120, 85, 70, 60, 0, 0, 64, [EnumTypes.Poison], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
111: SetPokemon("Rhinocorne", 80, 85, 95, 30, 30, 25, 0, 0, 64, [EnumTypes.Sol, EnumTypes.Roche], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
112: SetPokemon("Rhinoféros", 80, 85, 95, 30, 30, 25, 0, 0, 64, [EnumTypes.Sol, EnumTypes.Roche], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
113: SetPokemon("Leveinard", random.randint(1, 200), 5, 5, 35, 105, 50, 0, 0, 64, [EnumTypes.Normal], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
114: SetPokemon("Saquedeneu", 45, 49, 49, 65, 65, 45, 0, 0, 64, [EnumTypes.Plante], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
115: SetPokemon("Kangourex", 105, 95, 80, 40, 80, 90, 0, 0, 64, [EnumTypes.Normal], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
116: SetPokemon("Hypotrempe", 30, 40, 70, 70, 25, 60, 0, 0, 64, [EnumTypes.Eau, EnumTypes.Dragon], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
117: SetPokemon("Hypocean", 55, 65, 95, 95, 45, 85, 0, 0, 64, [EnumTypes.Eau, EnumTypes.Dragon], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
118: SetPokemon("Poissirène", 45, 67, 60, 35, 50, 63, 0, 0, 64, [EnumTypes.Eau], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
119: SetPokemon("Poissoroy", 80, 92, 65, 65, 80, 68, 0, 0, 64, [EnumTypes.Eau], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
120: SetPokemon("Stari", 30, 45, 55, 70, 55, 85, 0, 0, 64, [EnumTypes.Eau], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
121: SetPokemon("Staross", 60, 75, 85, 100, 85, 115, 0, 0, 64, [EnumTypes.Eau, EnumTypes.Psy], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
122: SetPokemon("M. Mime", 40, 45, 65, 100, 120, 90, 0, 0, 64, [EnumTypes.Psy, EnumTypes.Fée], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
123: SetPokemon("Insécateur", 70, 110, 80, 55, 80, 105, 0, 0, 64, [EnumTypes.Insecte, EnumTypes.Vol], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
124: SetPokemon("Lippoutou", 65, 50, 35, 115, 95, 95, 0, 0, 64, [EnumTypes.Glace, EnumTypes.Psy], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
125: SetPokemon("Élektek", 65, 83, 57, 95, 85, 105, 0, 0, 64, [EnumTypes.Electrique], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
126: SetPokemon("Magmar", 65, 95, 57, 100, 85, 93, 0, 0, 64, [EnumTypes.Feu], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
127: SetPokemon("Scarabrute", 55, 125, 100, 55, 70, 85, 0, 0, 64, [EnumTypes.Combat], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
128: SetPokemon("Tauros", 75, 100, 95, 40, 70, 110, 0, 0, 64, [EnumTypes.Normal], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
129: SetPokemon("Magicarpe", 20, 10, 55, 15, 20, 80, 0, 0, 64, [EnumTypes.Eau], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
130: SetPokemon("Léviator", 95, 125, 79, 60, 100, 81, 0, 0, 64, [EnumTypes.Eau, EnumTypes.Vol], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
131: SetPokemon("Lokhlass", 130, 85, 80, 85, 95, 60, 0, 0, 64, [EnumTypes.Eau, EnumTypes.Glace], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
132: SetPokemon("Métamorph", 48, 48, 48, 48, 48, 48, 0, 0, 64, [EnumTypes.Normal], [attacks[random.randint(1, 200)]]),
133: SetPokemon("Évoli", 55, 55, 50, 45, 65, 55, 0, 0, 64, [EnumTypes.Normal], [attacks[random.randint(1, 200)]]),
134: SetPokemon("Aquali", 130, 65, 60, 110, 95, 65, 0, 0, 64, [EnumTypes.Eau], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
135: SetPokemon("Voltali", 65, 65, 60, 110, 95, 130, 0, 0, 64, [EnumTypes.Electrique], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
136: SetPokemon("Pyroli", 65, 130, 60, 110, 95, 65, 0, 0, 64, [EnumTypes.Feu], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
137: SetPokemon("Porygon", 65, 60, 70, 75, 85, 40, 0, 0, 64, [EnumTypes.Normal], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
138: SetPokemon("Amonita", 35, 40, 100, 90, 55, 35, 0, 0, 64, [EnumTypes.Roche, EnumTypes.Eau], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
139: SetPokemon("Amonistar", 70, 60, 125, 115, 70, 55, 0, 0, 64, [EnumTypes.Roche, EnumTypes.Eau], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
140: SetPokemon("Kabuto", 30, 80, 90, 45, 55, 55, 0, 0, 64, [EnumTypes.Roche, EnumTypes.Eau], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
141: SetPokemon("Kabutops", 60, 115, 105, 65, 70, 80, 0, 0, 64, [EnumTypes.Roche, EnumTypes.Eau], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
142: SetPokemon("Ptéra", 80, 105, 65, 60, 75, 130, 0, 0, 64, [EnumTypes.Roche, EnumTypes.Vol], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
143: SetPokemon("Ronflex", 160, 110, 65, 65, 110, 30, 0, 0, 64, [EnumTypes.Normal], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
144: SetPokemon("Artikodin", 90, 85, 100, 95, 125, 85, 0, 0, 64, [EnumTypes.Glace, EnumTypes.Vol], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
145: SetPokemon("Électhor", 90, 90, 85, 125, 90, 100, 0, 0, 64, [EnumTypes.Electrique, EnumTypes.Vol], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
146: SetPokemon("Sulfura", 90, 100, 90, 125, 85, 90, 0, 0, 64, [EnumTypes.Feu, EnumTypes.Vol], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
147: SetPokemon("Minidraco", 41, 64, 45, 50, 50, 50, 0, 0, 64, [EnumTypes.Dragon], [attacks[random.randint(1, 200)]]),
148: SetPokemon("Draco", 61, 84, 65, 70, 70, 70, 0, 0, 64, [EnumTypes.Dragon], [attacks[random.randint(1, 200)]]),
149: SetPokemon("Dracolosse", 91, 134, 95, 100, 100, 80, 0, 0, 64, [EnumTypes.Dragon, EnumTypes.Vol], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
150: SetPokemon("Mewtwo", 106, 110, 90, 154, 90, 130, 0, 0, 64, [EnumTypes.Psy], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
151: SetPokemon("Mew", 100, 100, 100, 100, 100, 100, 0, 0, 64, [EnumTypes.Psy], [attacks[random.randint(1, 200)], attacks[random.randint(1, 200)]]),
}

def choose_player_pokemon():
    print("Choose your Pokemon:")
    for pokemon_id, pokemon in pokemons.items():
        print(f"{pokemon_id}: {pokemon.name}")

    while True:
        try:
            player_choice = int(input("Enter the ID of your Pokemon: "))
            return pokemons[player_choice]
        except KeyError:
            print("Invalid Pokemon ID. Try again.")

def main():
    player_pokemon = choose_player_pokemon()
    computer_pokemon = random.choice(list(pokemons.values()))

    print(f"You chose {player_pokemon.name}. Computer chose {computer_pokemon.name}.")

    while player_pokemon.hp > 0 and computer_pokemon.hp > 0:


        def afficher_details_combat(pokemon1, pokemon2):
            print(f"{pokemon1.name} VS {pokemon2.name}")
            print(f"{pokemon1.name} - HP: {pokemon1.hp}")
            print(f"{pokemon2.name} - HP: {pokemon2.hp}")
            print("\nDébut du combat!\n")

        pokemon1 = player_pokemon
        pokemon2 = computer_pokemon
        afficher_details_combat(player_pokemon, computer_pokemon)


        if player_pokemon.hp > 0:
            print("You win!")
            break
        else:
            print("Computer wins!")
            break

if __name__ == "__main__":
    main()