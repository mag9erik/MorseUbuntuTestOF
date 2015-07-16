from morse.builder import *
#from mysim.builder.sensors import Opticflow
from math import pi

bpymorse.set_speed(1000, 5, 5)

""" Cat (Quadrotor) """
#cat = Quadrotor()
#cat.translate(x=0.0, z=1.0)
#cat.rotate(z=pi/2)

# Waypoint controller (x,y,z, yaw and tolerance (default is 0.2))
#waypoint = RotorcraftWaypoint()
#cat.append(waypoint)
#waypoint.add_stream('socket')


""" rotor (atrv)"""
rotor = Quadrotor()#ATRV()
rotor.translate (x=2,y=0, z=0.5)
rotor.rotate(z=0)
rotor.properties(NoGravity=True, GroundRobot=False)
 
#keyb = Keyboard()
#keyb.properties(Speed=4.0)
#rotor.append(keyb)

rotorPose = Pose()
rotor.append(rotorPose)


#motionvw = MotionVW()
#motionvw.properties(ControlType='Position')
#motionvw.set_speed(1, 0)
#waypoint.ControlType('Position')
#rotor.append(motionvw)


#rotorPose.add_stream('socket')

#waypoint = RotorcraftWaypoint()
#rotor.append(waypoint)
#waypoint.add_stream('socket')

motionvw = MotionVW()
rotor.append(motionvw)
motionvw.add_stream('socket')
motionvw.add_service('socket')

#semanticC = SemanticCamera()
#semanticC.translate(x=0.3, z=-0.05)
#semanticC.rotate(x=+0.2)
#cat.append(semanticC)
#semanticC.properties(Vertical_Flip=False)

#cam = Opticflow()

#camV = VideoCamera()
#camV.translate(x=-1, z=1)
#camV.rotate(x=pi/2, y=-pi/2, z=0)
#rotor.append(camV)
#camV.properties(Vertical_Flip=False, capturing = True, cam_width = 352, cam_height = 100, #cam_focal = 64)
#camV.frequency(100)
#acam.add_service('socket')

camG = VideoCamera()
camG.translate(x=0, z=0.2)
camG.rotate(x=pi/2, y=0.0, z=0.0)
rotor.append(camG)
#camG.properties(Vertical_Flip=False, capturing = True, cam_width = 176, cam_height = 50, cam_focal = 64)
camG.properties(Vertical_Flip=False, capturing = True, cam_width = 352, cam_height = 100, cam_focal = 64)
camG.frequency(1000)
camG.add_service('socket')
camG.add_stream('socket')


#camD = VideoCamera()
#camD.translate(x=0.0, z=0.2)
#camD.rotate(x=-pi/2, y=0.0, z=0.0)
#rotor.append(camD)
#camD.properties(Vertical_Flip=False, capturing = True, cam_width = 176, #cam_height = 50, cam_focal = 64)
#camD.frequency(500)
#camD.add_service('socket')
#camD.add_stream('socket')

#catPose = Pose()
#cat.append(catPose)
#catPose.add_stream('socket')




""" The playground """
env = Environment('couloir1')
env.set_camera_location([-10.0, -2.0, 10.0])
env.set_camera_rotation([1.0470, 0, -1.3])
#env.set_camera_clip(1,2)
env.set_physics_step_sub(5)
#env.set_viewport('TEXTURED')
#viewport_shade – enum in [‘BOUNDBOX’, ‘WIREFRAME’, ‘SOLID’, ‘TEXTURED’], default ‘WIREFRAME’
#env.set_material_mode('MULTITEXTURE')
#material_mode – enum in [‘SINGLETEXTURE’, ‘MULTITEXTURE’, ‘GLSL’]
#env.select_display_camera(semanticC)
#env.show_debug_properties()
env.show_framerate()
env.set_time_strategy(TimeStrategies.FixedSimulationStep)



