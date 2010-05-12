import GameLogic
import Morse_Object
import MorseMath

class Gyroscope_Class(Morse_Object.Morse_Object_Class):
	""" Class definition for the gyroscope sensor.
		Sub class of Morse_Object. """
	yaw = 0.0
	pitch = 0.0
	roll = 0.0

	def __init__(self, obj, parent=None):
		""" Constructor method.
			Receives the reference to the Blender object.
			The second parameter should be the name of the object's parent. """
		print ("######## GYROSCOPE '%s' INITIALIZING ########" % obj.name)
		# Call the constructor of the parent class
		super(self.__class__,self).__init__(obj, parent)

		print ('######## GYROSCOPE INITIALIZED ########')


	def default_action(self):
		""" Main function of this component. """

		self.yaw, self.pitch, self.roll = MorseMath.euler_angle(self.blender_obj)

		# Store the values in the robot's object
		self.robot_parent.yaw = self.yaw
		self.robot_parent.pitch = self.pitch
		self.robot_parent.roll = self.roll

		#print ("[Y %.4f, P %.4f, R %.4f" % (self.yaw, self.pitch, self.roll))
