# -*- coding: utf-8 -*-
"""
השתמשו בחיצים כדי להזיז את האובייקט ולסובב אותו
עם או בלי המקשים Ctrl ו Shift לחוצים
*בכל מצב זה יזוז באופן שונה*
"""

import kivy3
from kivy.app import App
from kivy3 import Scene, Renderer, PerspectiveCamera
from kivy3.loaders import OBJMTLLoader
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.clock import Clock
import serial
shader_file = "./simple.glsl"
obj_file = "./test6.obj"
mtl_file = "./test9.mtl"


class MainApp(App):

    def build(self):
        root = FloatLayout()
        self.renderer = Renderer(shader_file=shader_file)
        scene = Scene()
        camera = PerspectiveCamera(15, 1, 1, 1000)
        loader = OBJMTLLoader()
        obj = loader.load(obj_file, mtl_file)

        scene.add(*obj.children)
        for obj in scene.children:
            obj.pos.z = -40.

        self.renderer.render(scene, camera)
        self.orion = scene.children[0]

        root.add_widget(self.renderer)
        self.renderer.bind(size=self._adjust_aspect)
        Window.bind(on_key_down=self.on_key_press)
        self.microbit = serial.Serial('COM6', 9600)
        Clock.schedule_interval(self.micro_read, 0.02)
        return root

    def _adjust_aspect(self, inst, val):
        rsize = self.renderer.size
        aspect = rsize[0] / float(rsize[1])
        self.renderer.camera.aspect = aspect

    def micro_read(self, dt):
        dct = str(self.microbit.readline()).replace("b'(","")
        dct = dct.replace(")\\r\\n'", "")
        axes = dct.split(", ")
        xyz = []
        for ax in axes:
            xyz.append(int(ax))
        if xyz[0] < 100 and xyz[1] < 100 and xyz[2] > 300:
            xyz[2] = 0
        else:
            xyz[0] /= 1000
            xyz[1] /= 1000
            xyz[2] /= 1000
        self.orion.rot.x += xyz[0]
        self.orion.rot.y += xyz[1]
        self.orion.rot.z += xyz[2]
        print(xyz)

    def on_key_press(self, *args):
        if 'shift' in args[4]:
            if args[1] == 275:
                self.orion.rot.z += 0.1
            elif args[1] == 276:
                self.orion.rot.z -= 0.1
        elif 'ctrl' in args[4]:
            if args[1] == 275:
                self.orion.pos.x += 1
            elif args[1] == 276:
                self.orion.pos.x -= 1
            elif args[1] == 273:
                self.orion.pos.y += 1
            elif args[1] == 274:
                self.orion.pos.y -= 1
        elif args[1] == 273:
            self.orion.rot.x += 1
        elif args[1] == 274:
            self.orion.rot.x -= 1
        elif args[1] == 275:
            self.orion.rot.y += 1
        elif args[1] == 276:
            self.orion.rot.y -= 1


if __name__ == '__main__':
    MainApp().run()