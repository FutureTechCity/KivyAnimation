# Kivy sprite animation

This Kivy project demonstrates how to animate a sprite.

## Drawing your sprite

You will need to construct a sprite sheet for your animation. You can draw your sprites using the web service [Piskel](http://www.piskelapp.com/).

I made an alien invader with 2 frames of animation with each frame being 32x32 pixels. So my resulting image export was 64x32 pixels. I have saved this into my project folder and named it: `invader.png`.

![](invader.png)

## Creating an atlas

Once you have your sprite sheet you then need to tell Kivy where the frames are on the image. This requires a new `.atlas` type of file. Like a `.kv` file you can create this in any text editor program. (You can also use Spyder.) I will name my file `invader.atlas`. Because my images are 32x32 pixels and side by side, my file is as follows:

~~~
{
    "invader.png": {
        "frame1": [0, 0, 32, 32],
        "frame2": [32, 0, 32, 32]
    }
}
~~~

`frame1` specifies the frame on the left of the bitmap, and `frame2` is the one 32 pixel along.

## Create your code file

Use an editor to create a `main.py` file. You can copy the following template code into this file:

~~~
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
~~~

## Create your layout file

Use an editor to create a `animation.kv` file. You can copy the following template layout into this file:
~~~
#:kivy 1.9.0

<AnimationScreen>:
    invader: invader_1

    AnimatingImage:
        id: invader_1
        size: 32, 32
        center: root.width / 2, root.height / 2
~~~

## Test animation

You can test by running the following command from the Anaconda prompt:
~~~
python main.py
~~~

## Challenges

* Change the playback rate of the animation
* Make a longer animation (more frames)
* Make the sprite move across the screen
* Create more than one sprite
