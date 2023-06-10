from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

model = Entity(model='scene.gltf', collider="mesh", position=(0, 0, 0), scale=1)

player = FirstPersonController()

app.run()