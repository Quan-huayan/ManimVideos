from manim import *
import numpy

class RectTriangleTree(Scene):
    def step_next(self, lineLast = Line(), vTan = 0.75, tag = -1, step = 7, time = 2):#递归画分形
        if(step>0):#step为0时递归终止
            a = lineLast.get_start()
            b = lineLast.get_end()
            h = 1/(vTan*vTan + 1)*b + vTan*vTan /(vTan*vTan + 1)*a
            t = vTan/(vTan*vTan+1)*lineLast.get_vector()
            p = [tag*t[1],-tag*t[0],t[2]]
            c = h + p
        
            triangle_new = Polygon(a,b,c)
            triangle_new.set_fill(ORANGE,0.3)
        
            
            line_l = Line(Line(a,c).rotate(PI/2,about_point=a).get_end(),Line(a,c).rotate(-PI/2,about_point=c).get_start())#新三角形的一条边
            line_r = Line(Line(b,c).rotate(PI/2,about_point=c).get_start(),Line(b,c).rotate(-PI/2,about_point=b).get_end())#新正方形的一条边
            square_new_l = Polygon(a,line_l.get_start(),line_l.get_end(),c)
            square_new_l.set_fill(BLUE,0.2)
            square_new_r = Polygon(b,line_r.get_end(),line_r.get_start(),c)
            square_new_r.set_fill(BLUE,0.2)
        
            self.play(Create(triangle_new).set_run_time(time))
            self.play(Create(square_new_l).set_run_time(time))
            self.play(Create(square_new_r).set_run_time(time))
        
            #递归
            self.step_next(line_l, vTan, tag, step-1,time/2)
            self.step_next(line_r, vTan, tag, step-1,time/2)
        
        
    def construct(self):
        square_0 = Square(2).move_to([0,-3,0])
        square_0.set_fill(BLUE,0.2)
        self.play(Create(square_0).set_run_time(1))
        
        self.step_next(Line([-1,-2,0],[1,-2,0]),1,-1,9,1)
        
    
        
        