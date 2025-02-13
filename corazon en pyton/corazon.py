from manim import *
import numpy as np

class Corazon(Scene):
    def construct(self):
        # 1) Crear ejes
        ejes = Axes(
            x_range=[-2, 2, 0.5],
            y_range=[-2, 2, 0.5],
            x_length=6,
            y_length=6,
            tips=False,
            axis_config={"color": WHITE},
        )
        ejes.to_edge(UP)

        titulo = Text(
            "Jenny, ¿quieres ser mi San Valentín?", 
            font_size=40, 
            color=RED
        )
        titulo.next_to(ejes, DOWN, buff=0.5)

       
        escala = 0.06
        def heart_parametric(t):
            x = 16 * np.sin(t)**3
            y = 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)
            return ejes.coords_to_point(escala*x, escala*y)

        # 4) Crear el objeto ParametricFunction (el corazón)
        corazon = ParametricFunction(
            heart_parametric, 
            t_range=[0, TAU],  # de 0 a 2*pi
            color=RED,
            stroke_width=6
        )

        # 5) Animaciones en escena
        #    - Primero aparecen los ejes y el texto
        #    - Luego se traza la curva del corazón lentamente
        self.play(Create(ejes), Write(titulo), run_time=2)
        
        # Animate la "línea" del corazón de principio a fin
        self.play(Create(corazon), run_time=4, rate_func=linear)

        # Pausa al final para que puedas ver el resultado
        self.wait(2)
