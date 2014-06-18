import random

class Pokemon():
	def __init__(self,name,level,kind,is_wild,attack,defense,speed,evasiveness,special,accuracy,hp,status):
		self.name = name
		self.level = level
		self.kind = kind
		self.is_wild = is_wild
		self.exp = 0
		self.amt_to_lvl_up = 12
		self.moves = {}
		
		#stats
		self.attack = attack
		self.defense = defense
		self.speed = speed
		self.evasiveness = evasiveness
		self.special = special
		self.accuracy = accuracy
		self.hp = hp
		self.status = status
	
		#stats battle
		self.battle_attack = self.attack
		self.battle_defense = self.defense
		self.battle_speed = self.speed
		self.battle_evasiveness = self.evasiveness
		self.battle_special = self.special
		self.battle_accuracy = self.accuracy
		self.battle_hp = self.hp
	def lvl_up_check(self):
		if self.exp > self.amt_to_lvl_up:
			self.level+= 1
			self.exp = self.exp - self.amt_to_lvl_up
			self.amt_to_lvl_up = int((8/5*self.amt_to_lvl_up) + 12)
			print "Your " + self.name + " is now level " + str(self.level) + "! Congratulations!"
	
	def dead_check(self):
		if self.battle_hp <= 0:
			return 1
		else:
			print "{0} has {1} HP left".format(self.name, self.battle_hp)
			return 0
	
	def attack_pokemon(self,second_pokemon,battle_choice):
		attack_power = int(((((2 * self.level / 5 + 2) * self.attack * self.moves[battle_choice].strength / second_pokemon.defense) / 50) + 2) * 1.5 * random.randint(80,100) / 100)
		print "{0} uses {1} and does {2} damage!".format(self.name,self.moves[battle_choice].name,attack_power)
		return attack_power

class move():
	def __init__(self,name,strength,kind,description,pp):
		self.name = name
		self.strength = strength
		self.kind = kind
		self.description = description
		self.pp = pp

class trainer():
	def __init__(self,name,money,bag, pokemon):
		self.name = name
		self.money = money
		self.bag = bag
		self.pokemon = pokemon
		
	def switch_pokemon(self):
		print "Who would you like to switch to?"
		for x in self.pokemon:
			print "{0}. {1}\n	Health: {2}/{3}".format(x,self.pokemon[x].name,self.pokemon[x].battle_hp,self.pokemon[x].hp)
		selection = int(input("Selection: "))
		
		while selection > len(self.pokemon):
			print "Please make a valid selection."
			selection = int(input("Selection: "))
			
		return self.pokemon[selection]

class item():
	def __init__(self,name,description,effect):
		self.name = name
		self.description = description
		self.effect = effect

def which_is_highest(*kargs):
	list = []
	
	for x in kargs:
		list.append(x)
	temp = list[0]
	
	for x in list:
		if x > temp:
			temp = x
	return temp

def enemy_logic(trainer_pokemon,enemy_pokemon):
	
	attack_change_weight = .15
	defense_change_weight = .25
	accuracy_change_weight = .3
	special_change_weight = .15
	attack_weight = .6
	
	if trainer_pokemon.attack > enemy_pokemon.attack:
		attack_change_weight = .3
	if trainer_pokemon.defense > enemy_pokemon.defense:
		defense_change_weight = .35
	if trainer_pokemon.accuracy > enemy_pokemon.accuracy:
		accuracy_change_weight = .4
	if trainer_pokemon.special > enemy_pokemon.special:
		special_change_weight = .3
	
	if enemy_pokemon.is_wild == True:
		descriptions = []
		for x in enemy_pokemon.moves:
			descriptions.append(enemy_pokemon.moves[x].description)
	
		if  "status_change_attack" not in descriptions:
			attack_change_weight = 0
		if "status_change_defense" not in descriptions:
			defense_change_weight = 0
		if "status_change_accuracy" not in descriptions:
			accuracy_change_weight = 0
		if "status_change_special" not in descriptions:
			special_change_weight = 0
		if "attack" not in descriptions:
			attack_weight = 0


	
	attack_change_weight *= random.randint(1,10)			
	defense_change_weight *= random.randint(1,10)
	accuracy_change_weight *= random.randint(1,10)
	special_change_weight *= random.randint(1,10)
	attack_weight *= random.randint(1,10)
	
	attack_change_weight = round(attack_change_weight,3)
	defense_change_weight = round(defense_change_weight,3)
	accuracy_change_weight = round(accuracy_change_weight,3)
	special_change_weight = round(special_change_weight,3)
	attack_weight = round(attack_weight,3)
	
	
	find_value = which_is_highest(attack_change_weight,defense_change_weight, accuracy_change_weight, special_change_weight,attack_weight)
	
	change_weight = {attack_change_weight: "status_change_attack", \
					 defense_change_weight: "status_change_defense", \
					 accuracy_change_weight: "status_change_accuracy", \
					 special_change_weight: "status_change_special", \
					 attack_weight: "attack"}
	"""
	print change_weight
	
	print "attack_change_weight: " + str(attack_change_weight)
	print "defense change weight: " + str(defense_change_weight)
	print "accuracy change weight: " + str(accuracy_change_weight)			Error catching for weights
	print "special change weight: " + str(special_change_weight)
	print "attack weight: " + str(attack_weight)
	
	print find_value
	print change_weight[find_value]
	"""
	for x in enemy_pokemon.moves:
		if enemy_pokemon.moves[x].description == change_weight[find_value]:
			enemy_move = enemy_pokemon.moves[x]
		
	[k for k, v in enemy_pokemon.moves.iteritems() if v == enemy_pokemon.moves[x]]
	
	return k		
												
def opening(trainer_pokemon, enemy_pokemon):
	print "Enemy {0} appears!".format(enemy_pokemon.name)
	print "\nGo {0}!\n".format(trainer_pokemon.name) 
	
def menu(trainer_pokemon, enemy_pokemon, trainer):
	while enemy_pokemon.hp > 0 and trainer_pokemon.hp > 0:
		print trainer_pokemon.name + " has " + str(trainer_pokemon.battle_hp) + " health left."
		print "1: Attack	2: Bag \n3: Pokemon	4: Run"
		
		selection = int(raw_input("What would you like to do?"))
		print ""
		
		
		while selection > 4 or selection < 1:
			selection = int(raw_input("What would you like to do?"))
			print ""
			
		#attack selection
		if selection == 1:
			for x in trainer_pokemon.moves:
				print str(x) + ". " + trainer_pokemon.moves[x].name
		
			battle_choice = int(raw_input("have " + trainer_pokemon.name + " do what?"))
		
			while battle_choice > len(trainer_pokemon.moves) or battle_choice < 1:
				battle_choice = int(raw_input("have " + trainer_pokemon.name + " do what?"))
			
			if trainer_pokemon.battle_speed > enemy_pokemon.battle_speed:
				enemy_pokemon.battle_hp -= trainer_pokemon.attack_pokemon(enemy_pokemon,battle_choice)
				if enemy_pokemon.dead_check() == 1:
					print "{0} has fainted.".format(enemy_pokemon.name)
					exit()
				trainer_pokemon.battle_hp -= enemy_pokemon.attack_pokemon(trainer_pokemon,enemy_logic(trainer_pokemon,enemy_pokemon))
				if trainer_pokemon.dead_check() == 1:
					print "{0} has fainted.".format(trainer_pokemon.name)
					exit()
				menu(trainer_pokemon,enemy_pokemon,trainer)
			else:
				trainer_pokemon.battle_hp -= enemy_pokemon.attack_pokemon(trainer_pokemon,enemy_logic(trainer_pokemon,enemy_pokemon))
				if trainer_pokemon.dead_check() == 1:
					print "{0} has fainted.".format(trainer_pokemon.name)
					exit()
				enemy_pokemon.battle_hp -= enemy_pokemon.attack_pokemon(enemy_pokemon,battle_choice)
				if enemy_pokemon.dead_check() == 1:
					print "{0} has fainted.".format(enemy_pokemon.name)
					exit()
				menu(trainer_pokemon,enemy_pokemon,trainer)
				
				
			
		"""
		#Open bag
		if selection == 2:
			do.nothing
		"""
	
		#pokemon selection
		if selection == 3:
			new_pokemon = trainer.switch_pokemon()
			new_pokemon.battle_hp -= enemy_pokemon.attack_pokemon(new_pokemon,enemy_logic(new_pokemon,enemy_pokemon))
			if new_pokemon.dead_check() == 1:
				print "{0} has fainted.".format(new_pokemon.name)
				exit()
			menu(new_pokemon,enemy_pokemon,trainer)
			
		#run
		if selection == 4:
			run_away(trainer_pokemon, enemy_pokemon)

def run_away(trainer_pokemon, enemy_pokemon):
	weight = trainer_pokemon.speed / enemy_pokemon.speed
	
	weight *= random.random()
	
	if weight >= 1:
		print "{0} runs away!".format(trainer_pokemon.name)
		exit()
	else:
		trainer_pokemon.battle_hp -= enemy_pokemon.attack_pokemon(trainer_pokemon,enemy_logic(trainer_pokemon,enemy_pokemon))
		if trainer_pokemon.dead_check() == 1:
			print "{0} has fainted.".format(trainer_pokemon.name)
		else:
			menu(trainer_pokemon,enemy_pokemon)
			

pikachu = Pokemon("Pikachu", 4, "Electric", False, 6, 3, 8, 10, 12, 10, 10, None)

caterpie = Pokemon("Caterpie", 2, "Bug", True, 1, 2, 4, 2, 5, 100, 100, None)
big = Pokemon("Big Ass Pokemon", 2, "Bug", False, 9, 100, 13, 14, 100, 19, 12, None)

thundershock = move("Thundershock", 45, "Electric", "attack", 20)
tackle = move("Tackle", 25, "Normal", "attack", 35)

growl = move("Growl", 0, "Normal", "status_change_attack", 35)



pikachu.moves[1] = thundershock
pikachu.moves[2] = tackle

caterpie.moves[1] = tackle
caterpie.moves[2] = growl

player_pokemon = {1: pikachu, 2: big}
player = trainer("Karl", 7000, None, player_pokemon)

opening(pikachu,caterpie)
menu(pikachu,caterpie,player)
