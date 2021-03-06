

#=========================== SIMULATION OBJECTS ==============================#
class Jet:	#Base jet class
	def __init__(self):	
		self.fuel;			#In gallons?		
		self.weight;		#In pounds
		self.emg_status;	#Emergency Status
		self.apt_status;	#Process Status
		self.atc_status;	#ATC Status
		self.location;		#Tuple (x,y)
		self.heading;		#In degrees (0 - 360)
		self.speed;			#Ground speed (MPH) ?
		self.altitude;		#In Feet
		self.burn_rate;		#Gallons per hour?
		self.history = []	#Stores each of the preceding variables for each time step of simulation


class P_Jet(Jet): #Passenger jet
	def __init__(self):
		self.passengers;	#Number of passengers. Avg weight will be 150 Lb per passenger
		self.ploy = TIME_TO_BOARD


class C_Jet(Jet): #Cargo jet 
	def __init__(self):
		self.cargo;			#In pounds


class ATC:					#Air Traffic Control: Serves as main logic controller of simulation
	def __init__(self):
		self.jets = []		#List of all jets in simulation
		
		#We don't NEED a seperate list for each Airport process status but I'm leaving them here for now:
		#It might make it easier later to do it this way.
		self.jets_air  = []
		self.jets_hold = []		#This should be treated as a queue: FIFO
		self.jets_land = []		
		self.jets_taxi = []		
		self.jets_term = []
		self.jets_take = []
		self.terminals = []	#List of all terminals at the airport

	def update(jet):
		pass


class Terminal: #Base Terminal class
	def __init__(self, x,y):
		self.loc = (x,y)	#Location of terminal
		self.jet;			#Each terminal can hold a single jet		
		self.has_jet;		#Bool for if terminal is occupied or not

	def refuel(jet):
		pass


class P_Terminal(Terminal): #Passenger Terminal
	def __init__(self):
		pass

	def deboard_passengers(self, jet): 
		pass

	def service(self, jet):		#After deboarding, the jet must be made ready for the next trip
		pass				#This process takes TIME_TO_SERVICE amount of time

	def board_passengers(self, jet):	#After being serviced, board passengers
		pass					#This takes TIME_TO_BOARD amount of time
	
	
class C_Terminal(Terminal): #Cargo Terminal
	def __init__(self):
		pass

	def unload_cargo(self, jet):
		pass

	def service(self, jet):
		pass

	def load_cargo(self, jet):
		pass



class Path:
	def __init__(self):
		self.path = []		#List of points which make up the path

#=========================== SIMULATION OBJECTS ==============================#

#============================== JET STATUSES =================================#
from enum import Enum
class ap_stat(Enum):	#Airport Process Status
	A = 0		#In the air
	H = 1		#In holding pattern
	L = 2		#Landing
	TX = 3		#Taxiing			
	TE = 4		#At a terminal
	TA = 5		#Taking off
	

class atc_stat(Enum):	#Jet ATC Status
	AW = 0		#Awaiting instructions from ATC
	EX = 1		#Executing instructions from ATC
	IN = 2		#Inactive - not requesting clearance, not executing anything


class e_stat(Enum):	#Emergency Status
	n = 0		#Normal, no emergency
	e = 1		#Emergency 
#============================ END JET STATUSES ================================#