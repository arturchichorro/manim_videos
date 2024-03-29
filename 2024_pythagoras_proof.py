from manim import *
import numpy as np

# Configured to be a vertical video
config.pixel_height = 1920
config.pixel_width = 1080
config.background_color = LOGO_BLACK


class pyProof(MovingCameraScene):
    def construct(self):

        def place_next_to_edge(shape, edge_number, distance=0.5):
            def updater(mob, dt):
                vertices = shape.get_vertices()
                edge = vertices[edge_number-1] - vertices[edge_number]
                edge_center = vertices[edge_number] + edge/2
                edge /= np.linalg.norm(edge)
                edge_normal = np.array([edge[1], -edge[0], 0])
                mob.move_to(edge_center).shift(distance*edge_normal)
            return updater

        grid = NumberPlane(color=WHITE)

        triangleOne = Polygon([-5, -3, 0], [-5, 1, 0], [1, -3, 0],
                              color=WHITE, fill_opacity=0.5)

        triangleTwo = Polygon([-5, -3, 0], [-5, 1, 0], [1, -3, 0],
                              color=WHITE, fill_opacity=0.5)

        triangleThree = Polygon([-5, -3, 0], [-5, 1, 0], [1, -3, 0],
                                color=WHITE, fill_opacity=0.5)

        triangleFour = Polygon([-5, -3, 0], [-5, 1, 0], [1, -3, 0],
                               color=WHITE, fill_opacity=0.5)

        angleLineOne = Line([-4, -3, 0], [-4, -2, 0], color=RED)
        angleLineTwo = Line([-4, -2, 0], [-5, -2, 0], color=RED)

        bigSquare = Polygon([-5, -3, 0], [-5, 7, 0],
                            [5, 7, 0], [5, -3, 0], fill_color=RED, fill_opacity=0.75, stroke_color=RED)
        bigSquareArea = Polygon([-5, -3, 0], [-5, 7, 0],
                                [5, 7, 0], [5, -3, 0], fill_color=RED, fill_opacity=0.75, stroke_color=RED)
        smallSquareColor = Polygon([-5, 1, 0], [-1, 7, 0],
                                   [5, 3, 0], [1, -3, 0], fill_color=BLUE, fill_opacity=0.5)
        smallSquare = Polygon([-5, 1, 0], [-1, 7, 0],
                              [5, 3, 0], [1, -3, 0], fill_color=BLUE, fill_opacity=0.5)

        aOne = Tex("a")
        bOne = Tex("b")
        cOne = Tex("c")
        aTwo = Tex("a")
        bTwo = Tex("b")
        cTwo = Tex("c")
        aThree = Tex("a")
        bThree = Tex("b")
        cThree = Tex("c")
        aFour = Tex("a")
        bFour = Tex("b")
        cFour = Tex("c")

        labelsOne = VGroup(aOne, bOne, cOne)
        labelsTwo = VGroup(aTwo, bTwo, cTwo)
        labelsThree = VGroup(aThree, bThree, cThree)
        labelsFour = VGroup(aFour, bFour, cFour)

        for i, label in enumerate(labelsOne):
            label.add_updater(place_next_to_edge(
                triangleOne, i), call_updater=True)

        for i, label in enumerate(labelsTwo):
            label.add_updater(place_next_to_edge(
                triangleTwo, i), call_updater=True)

        for i, label in enumerate(labelsThree):
            label.add_updater(place_next_to_edge(
                triangleThree, i), call_updater=True)

        for i, label in enumerate(labelsFour):
            label.add_updater(place_next_to_edge(
                triangleFour, i), call_updater=True)

        # self.add(grid)
        self.add(self.camera.frame)
        self.camera.frame.save_state()

        self.play(
            AnimationGroup(
                self.camera.frame.animate.move_to(triangleOne),
                Write(triangleOne),
                lag_ratio=0.5
            )
        )

        self.play(
            AnimationGroup(
                FadeIn(angleLineOne),
                FadeIn(angleLineTwo),
                lag_ratio=0.2
            ), run_time=0.5
        )

        self.wait(0.25)

        self.play(
            AnimationGroup(
                FadeOut(angleLineOne),
                FadeOut(angleLineTwo),
                lag_ratio=0.2
            ), run_time=0.5
        )

        self.play(Write(labelsOne))

        self.play(Write(triangleTwo), run_time=0.5)

        self.play(
            triangleTwo.animate.shift(5*RIGHT+UP),
            Write(labelsTwo),
            self.camera.frame.animate.restore(),
            lag_ratio=0.5
        )

        self.play(Rotate(triangleTwo, PI/2))

        self.play(Write(triangleThree), Write(triangleFour), run_time=0.5)

        self.play(
            AnimationGroup(
                self.camera.frame.animate.shift(3*UP),
                AnimationGroup(
                    triangleThree.animate.shift(4*RIGHT+6*UP),
                    Write(labelsThree),
                    lag_ratio=0.2,
                ),
                AnimationGroup(
                    triangleFour.animate.shift(5*UP+LEFT),
                    Write(labelsFour),
                    lag_ratio=0.2,
                ),
                lag_ratio=0.4,
                run_time=1.6
            )
        )

        self.play(
            AnimationGroup(
                Rotate(triangleThree, -PI),
                Rotate(triangleFour, -PI/2),
                lag_ratio=0.4
            )
        )

        self.wait(1)

        self.play(Write(bigSquare))

        self.play(FadeOut(bigSquare))

        self.play(self.camera.frame.animate.shift(5*DOWN))

        # DECLARATIONS FOR PART WITH EQUATIONS

        areaLabel = MathTex("A_{BigSquare}").shift(6*DOWN + 5.5*LEFT)
        eqEqual = MathTex("=").next_to(areaLabel, RIGHT)

        smallTriangleOne = Polygon([-5, -3, 0], [-5, 1, 0], [1, -3, 0],
                                   color=GREEN, fill_opacity=0.5)
        smallTriangleTwo = Polygon([-5, -3, 0], [-5, 1, 0], [1, -3, 0],
                                   color=GREEN, fill_opacity=0.5).shift(5*RIGHT+UP).rotate(PI/2)
        smallTriangleThre = Polygon([-5, -3, 0], [-5, 1, 0], [1, -3, 0],
                                    color=GREEN, fill_opacity=0.5).shift(4*RIGHT+6*UP).rotate(-PI)
        smallTriangleFour = Polygon([-5, -3, 0], [-5, 1, 0], [1, -3, 0],
                                    color=GREEN, fill_opacity=0.5).shift(5*UP+LEFT).rotate(-PI/2)
        plusOne = Tex("+").shift(6*DOWN-1.5*RIGHT)
        plusTwo = Tex("+").shift(6*DOWN+0.5*RIGHT)
        plusThree = Tex("+").shift(6*DOWN+2.5*RIGHT)
        plusFour = Tex("+").shift(6*DOWN+4.5*RIGHT)

        finalSmallTriangle = Polygon([-5, -3, 0], [-5, 1, 0], [1, -3, 0],
                                     color=GREEN, fill_opacity=0.5).move_to([-1.5, -6, 0]).scale(0.2)
        fourTimes = MathTex(r"4 \times").move_to([-2.5, -6, 0])
        triangleEquationOne = VGroup(smallTriangleOne, smallTriangleTwo,
                                     smallTriangleThre, smallTriangleFour, plusOne, plusTwo, plusThree)
        triangleEquationTwo = VGroup(
            fourTimes, finalSmallTriangle).move_to([0.5, -7, 0])
        squareEquation = VGroup(plusFour, smallSquare)

        # ANIMATIONS EQUATIONS

        self.play(Write(bigSquareArea), Write(bigSquare), run_time=0.5)

        self.play(bigSquareArea.animate.move_to(
            [-5.5, -6, 0]).scale(0.1), Write(eqEqual), FadeOut(bigSquare))

        self.play(
            FadeToColor(triangleOne, GREEN),
            FadeToColor(triangleTwo, GREEN),
            FadeToColor(triangleThree, GREEN),
            FadeToColor(triangleFour, GREEN),
            run_time=0.5
        )

        self.play(
            AnimationGroup(
                AnimationGroup(
                    smallTriangleOne.animate.move_to([-2.5, -6, 0]).scale(0.2),
                    smallTriangleTwo.animate.move_to([-0.5, -6, 0]).scale(0.2),
                    smallTriangleThre.animate.move_to([1.5, -6, 0]).scale(0.2),
                    smallTriangleFour.animate.move_to([3.5, -6, 0]).scale(0.2),
                ),
                AnimationGroup(
                    FadeIn(plusOne),
                    FadeIn(plusTwo),
                    FadeIn(plusThree)
                ),
                lag_ratio=0.5
            )
        )

        self.play(FadeIn(smallSquareColor), run_time=0.5)

        self.play(
            AnimationGroup(
                smallSquare.animate.move_to(
                    [5.5, -6, 0]).scale(0.125),  # .rotate(119*PI/640),
                FadeIn(plusFour),
                lag_ratio=0.5
            )
        )

        self.play(ReplacementTransform(triangleEquationOne, triangleEquationTwo),
                  squareEquation.animate.shift(2.5*LEFT+DOWN), VGroup(bigSquareArea, eqEqual).animate.shift(3*RIGHT+DOWN))

        self.wait(2)

        underbraceOne = MathTex(r"\underbrace{}").move_to([0.5, -8, 0])
        underbraceTwo = MathTex(r"\underbrace{}").move_to([3, -8, 0])
        underbraceThree = MathTex(r"\underbrace{}").move_to([-2.5, -8, 0])

        triangleEq = MathTex(r"4 \times \frac{ab}{2}").move_to(
            [0.5, -9, 0])
        newTriangleEq = MathTex(r"2ab").move_to(
            triangleEq.get_center())
        smallSquareEq = MathTex(r"c^2").move_to([3, -9, 0])

        bSquareEq = MathTex("(a+b)^2").move_to([-2.5, -9, 0])
        newBSquareEq = MathTex(
            "a^2+2ab+b^2").move_to(bSquareEq.get_center())

        plusFive = Tex("+").move_to([2, -9, 0])
        eqEqualTwo = MathTex("=").move_to([-0.5, -9, 0])

        self.play(Write(underbraceOne), run_time=0.5)
        self.play(Write(triangleEq))
        self.play(Write(underbraceTwo), run_time=0.5)
        self.play(Write(smallSquareEq), Write(plusFive))

        self.play(ReplacementTransform(triangleEq, newTriangleEq),
                  plusFive.animate.shift(LEFT*0.5), smallSquareEq.animate.shift(LEFT*0.75), FadeOut(underbraceOne), FadeOut(underbraceTwo))

        self.wait(1)

        self.play(Write(underbraceThree), run_time=0.5)
        self.play(Write(bSquareEq), Write(eqEqualTwo))

        self.play(ReplacementTransform(bSquareEq, newBSquareEq),
                  eqEqualTwo.animate.shift(RIGHT*0.5), FadeOut(underbraceThree), VGroup(plusFive, smallSquareEq, newTriangleEq).animate.shift(RIGHT))

        self.wait(1)

        finalEq = MathTex("a^2+b^2 = c^2").move_to(VGroup(newBSquareEq, eqEqualTwo,
                                                          newTriangleEq, smallSquareEq, plusFive).get_center())

        self.wait(1)

        self.play(TransformMatchingShapes(VGroup(newBSquareEq, smallSquareEq,
                  newTriangleEq), finalEq), FadeOut(eqEqualTwo), FadeOut(plusFive))

        self.wait(2)

        self.play(
            FadeOut(
                bigSquareArea,
                triangleEquationTwo, squareEquation, eqEqual,
                triangleTwo, triangleThree, triangleFour, smallSquareColor,
                aTwo, bTwo, cTwo, aThree, bThree, cThree, aFour, bFour, cFour
            ),
            triangleOne.animate.move_to([0, -1, 0]).scale(2),
            finalEq.animate.move_to([0, -7.5, 0]).scale(2)
        )

        self.wait(3)
