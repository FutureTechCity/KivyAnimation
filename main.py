from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from kivy.clock import Clock

class AnimatingImage(Image):
    time = 0.0
    rate = 0.2
    frame = 1
    def update(self, dt):
        self.time += dt
        if (self.time > self.rate):
            self.time -= self.rate
            self.source = "atlas://invader/frame" + str(self.frame)
            self.frame = self.frame + 1
            if (self.frame > 2):
                self.frame = 1
    
class AnimationScreen(Widget):
    invader = ObjectProperty(None)
    def update(self, dt):
        self.invader.update(dt)

class AnimationApp(App):
    def build(self):
        animation = AnimationScreen()
        Clock.schedule_interval(animation.update, 1.0/60.0)
        return animation

if __name__ == '__main__':
    AnimationApp().run()
