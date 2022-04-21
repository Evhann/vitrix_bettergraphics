import os
import ursina


class FloorCube(ursina.Entity):
    def __init__(self, position):
        super().__init__(
            position=position,
            scale=2,
            model="cube",
            texture=os.path.join("assets", "floor.png"),
            collider="box"
        )

        self.texture.filtering = None


class Floor:
    def __init__(self):
        for z in range(-20, 20, 2):

            for x in range(-20, 20, 2):
                cube = FloorCube(ursina.Vec3(x, 0, z))
