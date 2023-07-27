image dummy f_idle = "sprites/dummy_front_idle.png"

init python:

    class MinigameDisplayable(renpy.Displayable):

        def __init__(self, **kwargs):

            super(MinigameDisplayable, self).__init__(**kwargs)
        
        def render(self, width, height, st, at):

            r = renpy.Render(width, height)

            return render

        def event(self, ev, x, y, st):

            return
        
        def visit(self):

            return