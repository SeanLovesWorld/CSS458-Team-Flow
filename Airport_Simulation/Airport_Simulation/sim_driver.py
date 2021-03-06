#I have set the global contants at placeholder times untill we figure out
#average times for them. 
#We could also play with them to see how they affect throughput of the airport

#Feel free to add constants, just don't remove any without consulting the team.
#Basically, don't break it.
#============================ GLOBAL CONSTANTS ===============================#
TIME_TO_BOARD	= 60	#In minutes
TIME_TO_DEBOARD = 60	#In minutes
TIME_TO_REFUEL	= 60	#In minutes
TIME_TO_SERVICE = 60	#In minutes
MAX_PASSENGERS  = 150	
TIME_TICKS		= 1440  #In minutes 
NUM_JETS_TO_INITILIZE = 40	#We need to find out how many jets there are at time X. 
							#Time X being the time we start our simulation: 13:00 ? I think we should start at 00:00. 
							#Regardless, we need to know on average how many jets are at the airport at that time

#========================== END GLOBAL CONSTANTS =============================#


#================================ IMPORTS ====================================#
from classes import *
#============================== END IMPORTS ==================================#


#============================== SIMULATION ===================================#

# Misc Notes:
# We'll need some way of fast-forwarding through the sim.  Worry about that later.

def airport_sim():
	
	#Step 1: Initilize ATC
	tower = ATC()
	
	#Step 2: Initilize Terminals
	init_terminals(tower)

	#Step 3: Initilize Jets - Passenger and Cargo	
	init_jets(tower)

	#Step 4: Initilize paths
	init_paths(tower)

	#Step 5: Start Time
	for i in range(TIME_TICKS):
		# For each plane in the sim:
			# For planes in the air:
				# Location will be updated based on heading and speed
				# Fuel will be updated based on weight, speed and altitude, and burn rate 
				# Heading will be updated based on path needed to align with runway or holding pattern or avoid other jets -- NOT ANYMORE? Since we arne't simulating this
				# Weight will be updated based on remaining fuel, cargo on board or num passengers, 
			# If a plane in the air is in range to request landing, it will send a landing request ATC
			# If the plane is at a terminal and is ready to taxi it will send a taxi request to ATC
			# If a plane is on the taxiway and is ready to takeoff it will send a takeoff request to ATC
			# If a plane is on the taxiway and is ready to go to terminal it will send a go-to terminal request to ATC
		# The ATC will:
			# Take in requests from planes in the sim
			# Issue the appropriate instructions for planes based on known factors 
			# Instruct the plane or planes with the highest landing priority to land
			# Instruct planes requesting to land to enter holding pattern or land
			# Instruct planes requesting to taxi to runway to hold or begin taxiing
			# Instruct planes requesting to taxi to terminal to hold or begin taxiing
			# Update landing priorities for each plane in sim
		# The terminals will:
			# For planes that are at a terminal:
			# Refuel the plane: Planes fuel will be updated
			# Board passengers or cargo 
		pass

#============================ END SIMULATION =================================#

#========================== SIMULATION METHODS ===============================#
def init_terminals(atc_object):
	"""Create 80 Terminals:
		- 14 A Terminals: Numbered 1 - 14 
		- 11 B Terminals: Numbered 3 - 14
		- 12 C Terminals: Numbered 2 - 3, 9 - 12, 14 - 18, 20
		- 11 D Terminals: Numbered 1 - 11
		- 23 Cargo "terminals" Not numbered 		

		All terminals will be initilized with CUSTOM COORDINATES to match their
		real life location. 

		Each Terminal is added to the atc_objects' list of terminals
		"""

	# Passenger Terminals are initilized as P_Terminal
	# Cargo Terminals are initilized as C_Terminal
	# Each terminal will be added to the ATC objects list of terminals by appending it to the list
	#
	# Example: atc_object.terminals.append(terminal) 
	
	pass

def init_jets(atc_object):
	"""	Create NUM_JETS_TO_INITILIZE and place them at terminals.
		A few jets will be placed on taxiways, and a few will be 
		initilized in the air. 
		
		Of the jets in the air there will be three places they can 
		be initilized: 
			1. Landing
			2. In a holding pattern waiting to land
			3. Incoming to the airport

		These are not shown on screen and are only simulated in name 
		only. Depending on where they get initilized, they'll get 
		placed in different ATC lists. The ATC object has a list for
		each place a jet can get created. 

		Most will be passenger jets, some will be cargo jets.
	"""

	# Passenger jets are initilized as P_Jet, cargo jets as C_Jet.
	# Each jet will be added to the appropriate 
	# Just like with terminals
	pass

def init_paths(atc_object):
	pass
#======================== END SIMULATION METHODS =============================#
