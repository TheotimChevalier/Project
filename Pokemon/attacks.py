from mainTypes2 import EnumTypes

class CategoryAttack:
    Physical = 0
    Speciale = 1
    Status = 2

class SetAttack:
  def __init__(self, name, typeAttack, category, puissance, precision, pp):
    self.name = name
    self.type = typeAttack
    self.category = category
    self.puissance = puissance
    self.precision = precision
    self.pp = pp

attacks = {
  1: SetAttack("Riposte", EnumTypes.Combat, CategoryAttack.Physical, 0, 100, 20),
2: SetAttack("Frappe Atlas", EnumTypes.Combat, CategoryAttack.Physical, 40, 100, 20),
3: SetAttack("Double Pied", EnumTypes.Combat, CategoryAttack.Physical, 30, 100, 30),
4: SetAttack("Balayage", EnumTypes.Combat, CategoryAttack.Physical, 50, 100, 20),
5: SetAttack("Mawashi Geri", EnumTypes.Combat, CategoryAttack.Physical, 60, 80, 15),
6: SetAttack("Pied Sauté", EnumTypes.Combat, CategoryAttack.Physical, 70, 95, 25),
7: SetAttack("Sacrifice", EnumTypes.Combat, CategoryAttack.Physical, 85, 80, 25),
8: SetAttack("Pied Voltige", EnumTypes.Combat, CategoryAttack.Physical, 85, 90, 20),
9: SetAttack("Draco-Rage", EnumTypes.Dragon, CategoryAttack.Speciale, 0, 100, 10),
10: SetAttack("Repli", EnumTypes.Eau, CategoryAttack.Speciale, 0, 100, 40),
11: SetAttack("Écume", EnumTypes.Eau, CategoryAttack.Speciale, 20, 100, 30),
12: SetAttack("Claquoir", EnumTypes.Eau, CategoryAttack.Speciale, 35, 75, 10),
13: SetAttack("Pistolet à O", EnumTypes.Eau, CategoryAttack.Speciale, 40, 100, 25),
14: SetAttack("Bulles d'O", EnumTypes.Eau, CategoryAttack.Speciale, 65, 100, 20),
15: SetAttack("Cascade", EnumTypes.Eau, CategoryAttack.Speciale, 80, 100, 15),
16: SetAttack("Pince-Masse", EnumTypes.Eau, CategoryAttack.Speciale, 90, 85, 10),
17: SetAttack("Surf", EnumTypes.Eau, CategoryAttack.Speciale, 95, 100, 15),
18: SetAttack("Hydrocanon", EnumTypes.Eau, CategoryAttack.Speciale, 120, 80, 5),
19: SetAttack("Cage-Éclair", EnumTypes.Electrique, CategoryAttack.Speciale, 0, 100, 20),
20: SetAttack("Éclair", EnumTypes.Electrique, CategoryAttack.Speciale, 40, 100, 30),
21: SetAttack("Poing-Éclair", EnumTypes.Electrique, CategoryAttack.Speciale, 75, 100, 15),
22: SetAttack("Tonnerre", EnumTypes.Electrique, CategoryAttack.Speciale, 95, 100, 15),
23: SetAttack("Fatal-Foudre", EnumTypes.Electrique, CategoryAttack.Speciale, 120, 70, 5),
24: SetAttack("DanseFlamme", EnumTypes.Feu, CategoryAttack.Speciale, 15, 70, 15),
25: SetAttack("Flammèche", EnumTypes.Feu, CategoryAttack.Speciale, 40, 100, 25),
26: SetAttack("Poing de Feu", EnumTypes.Feu, CategoryAttack.Speciale, 75, 100, 15),
27: SetAttack("Lance-Flamme", EnumTypes.Feu, CategoryAttack.Speciale, 95, 100, 15),
28: SetAttack("Déflagration", EnumTypes.Feu, CategoryAttack.Speciale, 120, 85, 5),
29: SetAttack("Brume", EnumTypes.Glace, CategoryAttack.Speciale, 0, 0, 30),
30: SetAttack("Buée Noire", EnumTypes.Glace, CategoryAttack.Speciale, 0, 0, 30),
31: SetAttack("Onde Boréale", EnumTypes.Glace, CategoryAttack.Speciale, 65, 100, 20),
32: SetAttack("Poing-Glace", EnumTypes.Glace, CategoryAttack.Speciale, 75, 100, 15),
33: SetAttack("Laser Glace", EnumTypes.Glace, CategoryAttack.Speciale, 95, 100, 10),
34: SetAttack("Blizzard", EnumTypes.Glace, CategoryAttack.Speciale, 120, 90, 5),
35: SetAttack("Sécrétion", EnumTypes.Insecte, CategoryAttack.Speciale, 0, 95, 40),
36: SetAttack("Dard Nuée", EnumTypes.Insecte, CategoryAttack.Physical, 14, 85, 20),
37: SetAttack("Vampirisme", EnumTypes.Insecte, CategoryAttack.Physical, 20, 100, 15),
38: SetAttack("Double-Dard", EnumTypes.Insecte, CategoryAttack.Physical, 25, 100, 20),
39: SetAttack("Adaptation", EnumTypes.Normal, CategoryAttack.Speciale, 0, 0, 30),
40: SetAttack("Affûtage", EnumTypes.Normal, CategoryAttack.Speciale, 0, 0, 30),
41: SetAttack("Armure", EnumTypes.Normal, CategoryAttack.Speciale, 0, 0, 30),
42: SetAttack("Berceuse", EnumTypes.Normal, CategoryAttack.Speciale, 0, 55, 15),
43: SetAttack("Boul'Armure", EnumTypes.Normal, CategoryAttack.Speciale, 0, 0, 40),
44: SetAttack("Brouillard", EnumTypes.Normal, CategoryAttack.Speciale, 0, 100, 20),
45: SetAttack("Clonage", EnumTypes.Normal, CategoryAttack.Speciale, 0, 0, 10),
46: SetAttack("Copie", EnumTypes.Normal, CategoryAttack.Speciale, 0, 0, 10),
47: SetAttack("Croissance", EnumTypes.Normal, CategoryAttack.Speciale, 0, 0, 40),
48: SetAttack("Cyclone", EnumTypes.Normal, CategoryAttack.Speciale, 0, 100, 20),
49: SetAttack("Danse-Lames", EnumTypes.Normal, CategoryAttack.Speciale, 0, 0, 30),
50: SetAttack("E-Coque", EnumTypes.Normal, CategoryAttack.Speciale, 0, 0, 10),
51: SetAttack("Entrave", EnumTypes.Normal, CategoryAttack.Speciale, 0, 55, 20),
52: SetAttack("Flash", EnumTypes.Normal, CategoryAttack.Speciale, 0, 70, 20),
53: SetAttack("Grincement", EnumTypes.Normal, CategoryAttack.Speciale, 0, 85, 40),
54: SetAttack("Grobisou", EnumTypes.Normal, CategoryAttack.Speciale, 0, 75, 10),
55: SetAttack("Groz'Yeux", EnumTypes.Normal, CategoryAttack.Speciale, 0, 100, 30),
56: SetAttack("Hurlement", EnumTypes.Normal, CategoryAttack.Speciale, 0, 100, 20),
57: SetAttack("Intimidation", EnumTypes.Normal, CategoryAttack.Speciale, 0, 75, 30),
58: SetAttack("Jet de Sable", EnumTypes.Normal, CategoryAttack.Speciale, 0, 100, 15),
59: SetAttack("Lilliput", EnumTypes.Normal, CategoryAttack.Speciale, 0, 0, 20),
60: SetAttack("Métronome", EnumTypes.Normal, CategoryAttack.Speciale, 0, 0, 10),
61: SetAttack("Mimi-Queue", EnumTypes.Normal, CategoryAttack.Speciale, 0, 100, 30),
62: SetAttack("Morphing", EnumTypes.Normal, CategoryAttack.Speciale, 0, 0, 10),
63: SetAttack("Puissance", EnumTypes.Normal, CategoryAttack.Speciale, 0, 0, 30),
64: SetAttack("Reflet", EnumTypes.Normal, CategoryAttack.Speciale, 0, 0, 15),
65: SetAttack("Rugissement", EnumTypes.Normal, CategoryAttack.Speciale, 0, 0, 40),
66: SetAttack("Soin", EnumTypes.Normal, CategoryAttack.Speciale, 0, 0, 20),
67: SetAttack("Trempette", EnumTypes.Normal, CategoryAttack.Speciale, 0, 0, 40),
68: SetAttack("Ultrason", EnumTypes.Normal, CategoryAttack.Speciale, 0, 55, 20),
69: SetAttack("Croc Fatal", EnumTypes.Normal, CategoryAttack.Speciale, 0, 90, 10),
70: SetAttack("Patience", EnumTypes.Normal, CategoryAttack.Speciale, 0, 0, 10),
71: SetAttack("Sonicboom", EnumTypes.Normal, CategoryAttack.Physical, 0, 90, 20),
72: SetAttack("Empal'Korne", EnumTypes.Normal, CategoryAttack.Physical, 0, 30, 5),
73: SetAttack("Guillotine", EnumTypes.Normal, CategoryAttack.Physical, 0, 30, 5),
74: SetAttack("Constriction", EnumTypes.Normal, CategoryAttack.Physical, 10, 100, 35),
75: SetAttack("Étreinte", EnumTypes.Normal, CategoryAttack.Physical, 15, 85, 20),
76: SetAttack("Furie", EnumTypes.Normal, CategoryAttack.Physical, 15, 85, 20),
77: SetAttack("Ligotage", EnumTypes.Normal, CategoryAttack.Physical, 15, 90, 20),
78: SetAttack("Pilonnage", EnumTypes.Normal, CategoryAttack.Physical, 15, 85, 20),
79: SetAttack("Torgnoles", EnumTypes.Normal, CategoryAttack.Physical, 15, 85, 10),
80: SetAttack("Combo-Griffe", EnumTypes.Normal, CategoryAttack.Physical, 18, 80, 15),
81: SetAttack("Poing Comète", EnumTypes.Normal, CategoryAttack.Physical, 18, 85, 15),
82: SetAttack("Frénésie", EnumTypes.Normal, CategoryAttack.Physical, 20, 100, 20),
83: SetAttack("Picanon", EnumTypes.Normal, CategoryAttack.Physical, 20, 100, 15),
84: SetAttack("Charge", EnumTypes.Normal, CategoryAttack.Physical, 35, 95, 35),
85: SetAttack("Tornade", EnumTypes.Normal, CategoryAttack.Physical, 35, 100, 40),
86: SetAttack("Écras'Face", EnumTypes.Normal, CategoryAttack.Physical, 40, 100, 35),
87: SetAttack("Griffe", EnumTypes.Normal, CategoryAttack.Physical, 40, 100, 35),
88: SetAttack("Jackpot", EnumTypes.Normal, CategoryAttack.Physical, 40, 100, 20),
89: SetAttack("Vive-Attaque", EnumTypes.Normal, CategoryAttack.Physical, 40, 100, 30),
90: SetAttack("Coupe", EnumTypes.Normal, CategoryAttack.Physical, 50, 95, 30),
91: SetAttack("Poing Karaté", EnumTypes.Normal, CategoryAttack.Physical, 50, 100, 25),
92: SetAttack("Lutte", EnumTypes.Normal, CategoryAttack.Physical, 50, 100, 0),
93: SetAttack("Force Poigne", EnumTypes.Normal, CategoryAttack.Physical, 55, 100, 30),
94: SetAttack("Météores", EnumTypes.Normal, CategoryAttack.Physical, 60, 0, 20),
95: SetAttack("Morsure", EnumTypes.Normal, CategoryAttack.Physical, 60, 100, 25),
96: SetAttack("Écrasement", EnumTypes.Normal, CategoryAttack.Physical, 65, 100, 20),
97: SetAttack("Koud'Korne", EnumTypes.Normal, CategoryAttack.Physical, 65, 100, 25),
98: SetAttack("Coud'Boule", EnumTypes.Normal, CategoryAttack.Physical, 70, 100, 15),
99: SetAttack("Tranche", EnumTypes.Normal, CategoryAttack.Physical, 70, 100, 20),
100: SetAttack("Uppercut", EnumTypes.Normal, CategoryAttack.Physical, 70, 100, 10),
101: SetAttack("Coupe-Vent", EnumTypes.Normal, CategoryAttack.Physical, 80, 100, 10),
102: SetAttack("Croc de Mort", EnumTypes.Normal, CategoryAttack.Physical, 80, 90, 15),
103: SetAttack("Force", EnumTypes.Normal, CategoryAttack.Physical, 80, 100, 15),
104: SetAttack("Souplesse", EnumTypes.Normal, CategoryAttack.Physical, 80, 75, 20),
105: SetAttack("Triplattaque", EnumTypes.Normal, CategoryAttack.Physical, 80, 100, 10),
106: SetAttack("Ultimapoing", EnumTypes.Normal, CategoryAttack.Physical, 80, 85, 20),
107: SetAttack("Plaquage", EnumTypes.Normal, CategoryAttack.Physical, 85, 100, 15),
108: SetAttack("Bélier", EnumTypes.Normal, CategoryAttack.Physical, 90, 85, 20),
109: SetAttack("Mania", EnumTypes.Normal, CategoryAttack.Physical, 90, 100, 20),
110: SetAttack("Bomb'Œuf", EnumTypes.Normal, CategoryAttack.Physical, 100, 75, 16),
111: SetAttack("Coud'Krâne", EnumTypes.Normal, CategoryAttack.Physical, 100, 100, 15),
112: SetAttack("Damoclès", EnumTypes.Normal, CategoryAttack.Physical, 100, 100, 15),
113: SetAttack("Ultimawashi", EnumTypes.Normal, CategoryAttack.Physical, 120, 75, 5),
114: SetAttack("Destruction", EnumTypes.Normal, CategoryAttack.Physical, 130, 100, 5),
115: SetAttack("DUltralaser", EnumTypes.Normal, CategoryAttack.Physical, 150, 90, 5),
116: SetAttack("Explosion", EnumTypes.Normal, CategoryAttack.Physical, 170, 100, 5),
117: SetAttack("Para-Spore", EnumTypes.Plante, CategoryAttack.Speciale, 0, 75, 30),
118: SetAttack("Poudre Dodo", EnumTypes.Plante, CategoryAttack.Speciale, 0, 75, 15),
119: SetAttack("Spore", EnumTypes.Plante, CategoryAttack.Speciale, 0, 100, 15),
120: SetAttack("Vampigraine", EnumTypes.Plante, CategoryAttack.Speciale, 0, 90, 10),
121: SetAttack("Vol-Vie", EnumTypes.Plante, CategoryAttack.Speciale, 20, 100, 20),
122: SetAttack("Fouet Lianes", EnumTypes.Plante, CategoryAttack.Speciale, 35, 100, 10),
123: SetAttack("Méga-Sangsue", EnumTypes.Plante, CategoryAttack.Speciale, 40, 100, 10),
124: SetAttack("Tranch'Herbe", EnumTypes.Plante, CategoryAttack.Speciale, 55, 95, 25),
125: SetAttack("Danse-Fleur", EnumTypes.Plante, CategoryAttack.Speciale, 70, 100, 25),
126: SetAttack("Lance-Soleil", EnumTypes.Plante, CategoryAttack.Speciale, 120, 100, 10),
127: SetAttack("Acidarmure", EnumTypes.Poison, CategoryAttack.Speciale, 0, 0, 40),
128: SetAttack("Gaz Toxik", EnumTypes.Poison, CategoryAttack.Speciale, 0, 55, 40),
129: SetAttack("Poudre Toxik", EnumTypes.Poison, CategoryAttack.Speciale, 0,75, 35),
130: SetAttack("Toxik", EnumTypes.Poison, CategoryAttack.Speciale, 0, 85, 10),
131: SetAttack("Dard-Venin", EnumTypes.Poison, CategoryAttack.Physical,15, 100, 35),
132: SetAttack("Purédpois", EnumTypes.Poison, CategoryAttack.Physical, 20, 70, 20),
133: SetAttack("Acide", EnumTypes.Poison, CategoryAttack.Physical, 40, 100, 30),
134: SetAttack("Détritus", EnumTypes.Poison, CategoryAttack.Physical, 65, 100, 20),
135: SetAttack("Amnésie", EnumTypes.Psy, CategoryAttack.Speciale, 0, 0, 20),
136: SetAttack("Bouclier", EnumTypes.Psy, CategoryAttack.Speciale, 0, 0, 30),
137: SetAttack("Hâte", EnumTypes.Psy, CategoryAttack.Speciale, 0, 0, 30),
138: SetAttack("Hypnose", EnumTypes.Psy, CategoryAttack.Speciale, 0, 60, 20),
139: SetAttack("Mur Lumière", EnumTypes.Psy, CategoryAttack.Speciale, 0, 0, 30),
140: SetAttack("Protection", EnumTypes.Psy, CategoryAttack.Speciale, 0, 0, 20),
141: SetAttack("Repos", EnumTypes.Psy, CategoryAttack.Speciale, 0, 0, 10),
142: SetAttack("Télékinésie", EnumTypes.Psy, CategoryAttack.Speciale, 0, 80, 15),
143: SetAttack("Téléport", EnumTypes.Psy, CategoryAttack.Speciale, 0, 0, 20),
144: SetAttack("Yoga", EnumTypes.Psy, CategoryAttack.Speciale, 0, 0, 40),
145: SetAttack("Vague Psy", EnumTypes.Psy, CategoryAttack.Speciale, 0, 80, 15),
146: SetAttack("Choc Mental", EnumTypes.Psy, CategoryAttack.Speciale, 50, 100, 25),
147: SetAttack("Rafale Psy", EnumTypes.Psy, CategoryAttack.Speciale, 65, 100, 20),
148: SetAttack("Psyko", EnumTypes.Psy, CategoryAttack.Speciale, 90, 100, 10),
149: SetAttack("Dévorêve", EnumTypes.Psy, CategoryAttack.Speciale, 100, 100, 15),
150: SetAttack("Hypnose", EnumTypes.Psy, CategoryAttack.Speciale, 0, 60, 20),
151: SetAttack("Choc Mental", EnumTypes.Psy, CategoryAttack.Speciale, 50, 100, 25),
152: SetAttack("Rafale Psy", EnumTypes.Psy, CategoryAttack.Speciale, 65, 100, 20),
153: SetAttack("Psyko", EnumTypes.Psy, CategoryAttack.Speciale, 90, 100, 10),
154: SetAttack("Dévorêve", EnumTypes.Psy, CategoryAttack.Speciale, 100, 100, 15),
155: SetAttack("Barrage", EnumTypes.Roche, CategoryAttack.Speciale, 0, 100, 5),
156: SetAttack("Jet-Pierres", EnumTypes.Roche, CategoryAttack.Speciale, 50, 90, 15),
157: SetAttack("Roulade", EnumTypes.Roche, CategoryAttack.Speciale, 30, 90, 20),
158: SetAttack("Balayage", EnumTypes.Roche, CategoryAttack.Physical, 50, 100, 20),
159: SetAttack("Jet de Sable", EnumTypes.Roche, CategoryAttack.Speciale, 0, 100, 15),
160: SetAttack("Pistolet à O", EnumTypes.Roche, CategoryAttack.Speciale, 0, 100, 25),
161: SetAttack("Mawashi Geri", EnumTypes.Roche, CategoryAttack.Physical, 60, 80, 15),
162: SetAttack("Chute de Pierres", EnumTypes.Roche, CategoryAttack.Physical, 100, 80, 5),
163: SetAttack("Seisme", EnumTypes.Sol, CategoryAttack.Physical, 100, 100, 10),
164: SetAttack("Ampleur", EnumTypes.Sol, CategoryAttack.Physical, 20, 100, 30),
165: SetAttack("Séisme", EnumTypes.Sol, CategoryAttack.Physical, 100, 100, 10),
166: SetAttack("Surf", EnumTypes.Sol, CategoryAttack.Physical, 95, 100, 15),
167: SetAttack("Telluriforce", EnumTypes.Sol, CategoryAttack.Physical, 75, 100, 10),
168: SetAttack("Séisme", EnumTypes.Sol, CategoryAttack.Physical, 100, 100, 10),
169: SetAttack("Laser Glace", EnumTypes.Sol, CategoryAttack.Physical, 100, 100, 15),
170: SetAttack("Météores", EnumTypes.Sol, CategoryAttack.Speciale, 60, 0, 20),
171: SetAttack("Rafale Feu", EnumTypes.Sol, CategoryAttack.Speciale, 70, 100, 15),
172: SetAttack("Tonnerre", EnumTypes.Sol, CategoryAttack.Speciale, 110, 70, 5),
173: SetAttack("Surf", EnumTypes.Sol, CategoryAttack.Speciale, 95, 100, 15),
174: SetAttack("Dracogriffe", EnumTypes.Sol, CategoryAttack.Physical, 80, 100, 15),
175: SetAttack("Coup de Main", EnumTypes.Tenèbres, CategoryAttack.Physical, 0, 100, 20),
176: SetAttack("Morsure", EnumTypes.Tenèbres, CategoryAttack.Physical, 60, 100, 25),
177: SetAttack("Croc Fatal", EnumTypes.Tenèbres, CategoryAttack.Physical, 80, 90, 10),
178: SetAttack("Éclat Ténébreux", EnumTypes.Tenèbres, CategoryAttack.Speciale, 80, 100, 15),
179: SetAttack("Hurlement", EnumTypes.Tenèbres, CategoryAttack.Speciale, 0, 100, 20),
180: SetAttack("Attraction", EnumTypes.Fée, CategoryAttack.Speciale, 0, 100, 15),
181: SetAttack("Brume Capiteuse", EnumTypes.Fée, CategoryAttack.Speciale, 0, 100, 20),
182: SetAttack("Poudre Dodo", EnumTypes.Fée, CategoryAttack.Speciale, 0, 75, 15),
183: SetAttack("Poudre Fureur", EnumTypes.Fée, CategoryAttack.Speciale, 0, 100, 20),
184: SetAttack("Bouclier", EnumTypes.Fée, CategoryAttack.Speciale, 0, 0, 30),
185: SetAttack("Ondes Étranges", EnumTypes.Fée, CategoryAttack.Speciale, 90, 100, 10),
186: SetAttack("Choc Venin", EnumTypes.Fée, CategoryAttack.Physical, 10, 100, 35),
187: SetAttack("Damoclès", EnumTypes.Fée, CategoryAttack.Physical, 100, 100, 15),
188: SetAttack("Empal'Korne", EnumTypes.Fée, CategoryAttack.Physical, 100, 100, 5),
189: SetAttack("Géomancie", EnumTypes.Fée, CategoryAttack.Speciale, 120, 100, 5),
190: SetAttack("Météores", EnumTypes.Fée, CategoryAttack.Speciale, 90, 0, 20),
191: SetAttack("Poudre Dodo", EnumTypes.Fée, CategoryAttack.Speciale, 0, 75, 15),
192: SetAttack("Tourmagik", EnumTypes.Fée, CategoryAttack.Speciale, 60, 100, 20),
193: SetAttack("Luminocanon", EnumTypes.Fée, CategoryAttack.Speciale, 80, 100, 10),
194: SetAttack("Berceuse", EnumTypes.Fée, CategoryAttack.Speciale, 0, 55, 15),
195: SetAttack("Écosphere", EnumTypes.Fée, CategoryAttack.Speciale, 80, 100, 10),
196: SetAttack("Toile Élek", EnumTypes.Insecte, CategoryAttack.Speciale, 55, 95, 15),
197: SetAttack("Exploforce", EnumTypes.Insecte, CategoryAttack.Speciale, 90, 100, 10),
198: SetAttack("Méga-Sangsue", EnumTypes.Insecte, CategoryAttack.Speciale, 40, 100, 10),
199: SetAttack("Acide", EnumTypes.Insecte, CategoryAttack.Physical, 40, 100, 30),
200: SetAttack("Amnésie", EnumTypes.Insecte, CategoryAttack.Physical, 0, 0, 20)
  
  
  
}