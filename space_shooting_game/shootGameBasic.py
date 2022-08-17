from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from animation_examples.scrolling_bakcground import Bak

class ShootApp(App):

    def build(self):
        self.lay = FloatLayout()
        self.back = Bak()
        self.lay.add_widget(self.back)
        self.spaceShip = Image(source='../imgs/spacship.png', on_touch_move=self.move_ship, size_hint=(0.1,0.1))
        self.lay.add_widget(self.spaceShip)
        self.rock = Image(source='../imgs/rock.png', pos=(300,0), size_hint=(0.2,0.2))
        self.lay.add_widget(self.rock)
        Clock.schedule_interval(self.move_rock, 0.009)
        return self.lay

    def is_obj_touch_point(self, obj_p, point):
        w = obj_p.size[0]
        h = obj_p.size[1]
        if point[0]>=obj_p.center[0]-(w/2) and point[0]<=obj_p.center[0]+(w/2) and point[1] >= obj_p.center[1]-(h/2) and point[1]<=obj_p.center[1]+(h/2):
            return True

    def move_ship(self, instance, touch):
        if self.is_obj_touch_point(self.spaceShip, touch.pos):
            self.spaceShip.center=touch.pos

    def move_rock(self, time_passed):
        self.rock.pos[0] = self.rock.pos[0]-1
        if self.spaceShip.collide_widget(self.rock):
            print("boom")

ShootApp().run()