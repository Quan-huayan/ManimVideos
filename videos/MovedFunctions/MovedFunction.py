from manim import *

class MovedFunction(Scene):
    def construct(self):
        sinfunc = FunctionGraph(lambda t: np.sin(t-1),
                                color=RED,
                                x_range=[-7,29],
                                )
        cosfunc = FunctionGraph(lambda t: -np.cos(t-1),
                                color=BLUE,
                                x_range=[-7,29],
                                ).rotate_about_origin(PI/2)
        circ_id = Circle(1,color=WHITE)
        
        r_line = Line([0,0,0],[1,0,0])
        h_line = VMobject()
        v_line = VMobject()
        r_dot = VMobject()
        
        self.add(NumberPlane(color=ManimColor('#BBFFEA')),sinfunc,cosfunc,circ_id,r_line,h_line,v_line,r_dot)
        
        h_line.add_updater(lambda x: x.become(Line(r_line.get_end(),[r_line.get_end()[0],1,0]).set_color(ORANGE)))
        v_line.add_updater(lambda x: x.become(Line(r_line.get_end(),[1,r_line.get_end()[1],0]).set_color(ORANGE)))
        r_dot.add_updater(lambda x: x.become(Dot(r_line.get_end()).set_color(ORANGE)))
        
        self.play(
                AnimationGroup(
                    sinfunc.animate(run_time=7,rate_func=linear).shift([-7*PI,0,0]),
                    cosfunc.animate(run_time=7,rate_func=linear).shift([0,-7*PI,0]),
                    Rotate(r_line,about_point = [0,0,0], angle=7*PI, run_time=7,rate_func=linear),
                ),
        )
