# Romano Žic
# Ovo je bilo za projekt iz fizike,
# Kod je užasan, napisan je što je brže bilo moguće,
# Ukratko nije dobar primjer

from manim import *

BallImg = ImageMobject("beach_ball.png").scale(0.15)
RockImg = ImageMobject("rock.png").scale(0.15)
grav_u = 9.8  # (m/s2)
tlak_boja = GREEN
tlak_boja_b = GREEN_B
Fg_boja = RED
Fel_boja = RED_B
masa_boja = GRAY
pov_boja = YELLOW
vol_boja = BLUE
gustoća_boja = ORANGE
dubina_boja = PURPLE
Dl_boja = PURPLE_B
fu_boja = WHITE


class Fizika(Scene):
    def construct(self):

        uzgon = Tex("Uzgon").scale(3.5)  # tekst uzgon na početku
        self.play(Write(uzgon), run_time=1.5)
        self.wait(0.5)
        self.play(Unwrite(uzgon))
        self.remove(uzgon)

        self.play(FadeIn(BallImg.move_to(LEFT * 3 + DOWN)))  # slika lopte
        self.play(FadeIn(RockImg.move_to(RIGHT * 3 + DOWN)))  # slika kamena

        voda = Rectangle(color=vol_boja, height=8, width=20, fill_opacity=0.3).move_to(
            DOWN * 2.5
        )
        self.play(FadeIn(voda))  # voda se stvara

        self.play(BallImg.animate.shift(UP * 2.5))  # Lopta pluta
        self.play(RockImg.animate.shift(DOWN * 7))  # Kamen tone
        self.wait(0.2)
        self.play(FadeOut(BallImg, RockImg, voda))  # Završili smo s kamenom i loptom
        self.wait(0.2)

        why = Tex("Zašto?").scale(3.5)
        self.play(Write(why))
        self.wait(0.5)
        self.play(Unwrite(why))
        self.remove(why)


class Fizika_tlak(ThreeDScene):
    def construct(self):

        masa = ValueTracker(0.5)
        duljina_kocke = ValueTracker(1)

        naslov = Tex("Tlak").scale(2.5).to_corner(UL, buff=0.4)
        self.add_fixed_in_frame_mobjects(naslov)  # ne pomiče sa kamerom
        self.play(Write(naslov))
        self.set_camera_orientation(
            phi=60 * DEGREES, theta=-70 * DEGREES
        )  # postavljanje kamere

        kocka = always_redraw(
            lambda: Cube(
                side_length=duljina_kocke.get_value() * 2,
                stroke_width=1,
                fill_opacity=0.5,
            )
        )

        kocka2 = always_redraw(
            lambda: Cube(
                side_length=duljina_kocke.get_value() * 2,
                stroke_width=1,
                fill_opacity=0.5,
                fill_color=masa_boja,
            )
        )

        kocka3 = always_redraw(
            lambda: Cube(
                side_length=duljina_kocke.get_value() * 2,
                stroke_width=1,
                fill_opacity=0.5,
                fill_color=masa_boja,
            )
        )

        masa_oznaka = always_redraw(
            lambda: MathTex(
                r"{m=}", {round(masa.get_value(), 2)}, r"{kg}", color=masa_boja
            )
            .move_to(
                kocka.get_center()
                + IN * duljina_kocke.get_value()
                + RIGHT * duljina_kocke.get_value()
                + RIGHT * 2.2
                + UP
            )
            .scale(1.5)
        )

        volumen_oznaka = always_redraw(
            lambda: MathTex(
                r"{V=}",
                {round(duljina_kocke.get_value() ** 3, 2)},
                r"{m^3}",
                color=vol_boja,
            )
            .scale(1.5)
            .move_to(masa_oznaka.get_center() + DOWN)
            .align_to(masa_oznaka, LEFT)
        )

        pov_oznaka = always_redraw(  # oznaka za površinu kocke
            lambda: MathTex(
                r"{A}",
                r"=",
                {round(duljina_kocke.get_value() ** 2, 2)},
                r"{m^2}",
                color=pov_boja,
            )
            .scale(1.5)
            .move_to(masa_oznaka.get_center() + DOWN * 2)
            .align_to(masa_oznaka, LEFT)
        )

        pov_kvadrat = always_redraw(
            lambda: Square(
                side_length=duljina_kocke.get_value() * 2,
                color=pov_boja,
                fill_opacity=0.3,
            )
            .move_to(kocka.get_center() + IN * duljina_kocke.get_value())
            .set_z_index(kocka.z_index - 1)
        )

        sila_grav = always_redraw(
            lambda: Arrow3D(
                start=kocka.get_center(),
                end=kocka.get_center() + IN * (2 + masa.get_value()),
                color=Fg_boja,
            )
        )

        grav_oznaka = (
            MathTex(r"\vec{F_g}", color=Fg_boja)
            .scale(1.2)
            .rotate(60 * DEGREES, axis=RIGHT)
            .rotate(-13.3333 * DEGREES, axis=UP)
            .move_to(sila_grav.get_end() + DOWN + LEFT * 0.5)
        )

        grav_formula = (
            MathTex(r"\vec{F_g}", r"=", r"{m}", r"{g}", color=Fg_boja)
            .scale(1.2)
            .rotate(60 * DEGREES, axis=RIGHT)
            .rotate(-13.3333 * DEGREES, axis=UP)
            .move_to(sila_grav.get_end() + DOWN + LEFT * 1.5)
        )
        grav_formula[2].set_color(masa_boja)

        grav_rješenje = (
            MathTex(
                r"\vec{F_g}",
                r"=",
                {round(masa.get_value(), 2)},
                r"*",
                {grav_u},
                r"=",
                {round(masa.get_value() * grav_u, 2)},
                r"N",
                color=Fg_boja,
            )
            .scale(1.2)
            .rotate(60 * DEGREES, axis=RIGHT)
            .rotate(-13.3333 * DEGREES, axis=UP)
            .move_to(sila_grav.get_end() + DOWN * 1.2 + LEFT * 3)
        )
        grav_rješenje[2].set_color(masa_boja)

        grav_updating = always_redraw(
            lambda: MathTex(
                r"\vec{F_g}",
                r"=",
                {round(masa.get_value() * grav_u, 2)},
                r"N",
                color=Fg_boja,
            )
            .scale(1.2)
            .rotate(60 * DEGREES, axis=RIGHT)
            .rotate(-13.333333 * DEGREES, axis=UP)
            .move_to(
                kocka.get_center() + IN * (2 + masa.get_value()) + DOWN + LEFT * 1.5
            )
        )

        tlak_formula = (
            MathTex(
                r"{P}",
                r"=",
                r"{F",
                r"\over",
                r"A}",
                color=tlak_boja,
            )
            .scale(1.5)
            .rotate(60 * DEGREES, axis=RIGHT)
            .rotate(-10 * DEGREES, axis=UP)
            .move_to(naslov.get_center() + DOWN * 3 + LEFT * 1.6)
        )
        tlak_formula[2].set_color(Fg_boja)
        tlak_formula[4].set_color(pov_boja)

        tlak_rješenje = (
            MathTex(
                r"{P}",
                r"=",
                r"{" + f"{round(masa.get_value(), 2) * grav_u}",
                r"\over",
                f"{round(duljina_kocke.get_value() ** 2, 2)}" + r"}",
                r"=",
                {
                    round(
                        (masa.get_value() * grav_u) / (duljina_kocke.get_value() ** 2),
                        2,
                    )
                },
                r"{Pa}",
                color=tlak_boja,
            )
            .scale(1.5)
            .rotate(60 * DEGREES, axis=RIGHT)
            .rotate(-10 * DEGREES, axis=UP)
            .move_to(naslov.get_center() + DOWN * 3 + LEFT)
            .align_to(tlak_formula, LEFT)
        )
        tlak_rješenje[2].set_color(Fg_boja)
        tlak_rješenje[4].set_color(pov_boja)

        tlak_updating = always_redraw(
            lambda: MathTex(
                r"{P}",
                r"=",
                {
                    round(
                        (masa.get_value() * grav_u) / (duljina_kocke.get_value() ** 2),
                        2,
                    )
                },
                r"{Pa}",
                color=tlak_boja,
            )
            .scale(1.5)
            .rotate(60 * DEGREES, axis=RIGHT)
            .rotate(-10 * DEGREES, axis=UP)
            .move_to(
                naslov.get_center() + DOWN * 3 + LEFT * 2.5,
                aligned_edge=tlak_rješenje.get_bottom(),
            )
        )

        self.play(DrawBorderThenFill(kocka))
        self.play((Write(VGroup(masa_oznaka, volumen_oznaka), run_time=2)))
        self.wait(2)

        self.play(DrawBorderThenFill(pov_kvadrat))
        self.play(Write(pov_oznaka))
        self.wait(4)

        self.play(Create(sila_grav))
        self.play(Write(grav_oznaka))
        self.wait()

        self.play(TransformMatchingTex(grav_oznaka, grav_formula))
        self.wait()

        self.play(TransformMatchingTex(grav_formula, grav_rješenje))
        self.wait()

        self.play(TransformMatchingTex(grav_rješenje, grav_updating))
        self.wait(6)

        self.play(Write(tlak_formula))
        self.wait()

        self.play(TransformMatchingTex(tlak_formula, tlak_rješenje))
        self.wait()

        self.play(TransformMatchingTex(tlak_rješenje, tlak_updating))
        self.wait()

        self.play(duljina_kocke.animate.set_value(0.5))
        self.wait()

        self.play(FadeIn(kocka2.shift(OUT * 7)), run_time=0.01)
        self.play(
            kocka2.shift(OUT * 7).animate.shift(
                IN * 7 + OUT * duljina_kocke.get_value() * 2
            )
        )
        kocka2.add_updater(
            lambda poz: poz.move_to(
                kocka.get_center() + OUT * duljina_kocke.get_value() * 2
            )
        )
        masa.set_value(1)
        self.play(FadeIn(kocka3.shift(OUT * 9)), run_time=0.01)
        self.play(
            kocka3.shift(OUT * 9).animate.shift(
                IN * 9 + OUT * duljina_kocke.get_value() * 4
            )
        )
        kocka3.add_updater(
            lambda poz: poz.move_to(
                kocka.get_center() + OUT * duljina_kocke.get_value() * 4
            )
        )
        masa.set_value(1.5)
        self.wait()

        self.play(duljina_kocke.animate.set_value(1.2))
        self.wait()

        kocka3.clear_updaters()
        masa.set_value(1)
        self.play(
            kocka3.move_to(
                kocka.get_center() + OUT * duljina_kocke.get_value() * 4
            ).animate.shift(OUT * 4),
        )
        self.remove(kocka3)
        kocka2.clear_updaters()
        masa.set_value(0.5)
        self.play(
            kocka2.move_to(
                kocka.get_center() + OUT * duljina_kocke.get_value() * 2
            ).animate.shift(OUT * 4),
        )
        self.remove(kocka2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


class Raspisivanje_tlaka(Scene):
    def construct(self):
        veličina_svega = 3
        tlak = MathTex(r"{P}", r"=", r"{F", r"\over", r"A}", color=tlak_boja).scale(
            veličina_svega
        )
        tlak[4].set_color(pov_boja)
        tlak[2].set_color(Fg_boja)

        tlak2 = MathTex(
            r"{P}", r"=", r"{m", r"g", r"\over", r"A}", color=tlak_boja
        ).scale(veličina_svega)
        tlak2[2].set_color(masa_boja)
        tlak2[3].set_color(Fg_boja)
        tlak2[5].set_color(pov_boja)

        tlak3 = (
            MathTex(
                r"{P}", r"=", r"{\rho", r"V", r"g", r"\over", r"A}", color=tlak_boja
            )
            .scale(veličina_svega)
            .shift(LEFT * 3.5)
        )
        tlak3[2].set_color(gustoća_boja)
        tlak3[3].set_color(vol_boja)
        tlak3[4].set_color(Fg_boja)
        tlak3[6].set_color(pov_boja)

        tlak4 = MathTex(
            r"{P}",
            r"=",
            r"{\rho",
            r"h",
            r"A",
            r"g",
            r"\over",
            r"A}",
            color=tlak_boja,
        ).scale(veličina_svega)
        tlak4[2].set_color(gustoća_boja)
        tlak4[3].set_color(dubina_boja)
        tlak4[4].set_color(pov_boja)
        tlak4[5].set_color(Fg_boja)
        tlak4[7].set_color(pov_boja)

        tlak5 = MathTex(
            r"{P}",
            r"=",
            r"{\rho",
            r"h",
            r"g",
            r"}",
            color=tlak_boja,
        ).scale(veličina_svega)
        tlak5[2].set_color(gustoća_boja)
        tlak5[3].set_color(dubina_boja)
        tlak5[4].set_color(Fg_boja)

        gustoća = (
            MathTex(r"{\rho}", r"=", r"{m", r"\over", r"V}", color=gustoća_boja)
            .scale(veličina_svega)
            .shift(RIGHT * 3.5)
        )
        gustoća[2].set_color(masa_boja)
        gustoća[4].set_color(vol_boja)

        gustoća2 = (
            MathTex(r"{m}", r"=", r"{\rho}", r"V}", color=gustoća_boja)
            .scale(veličina_svega)
            .shift(RIGHT * 3.5)
        )
        gustoća2[0].set_color(masa_boja)
        gustoća2[3].set_color(vol_boja)

        self.play(Write(tlak))
        self.wait(5.5)

        self.play(TransformMatchingTex(tlak, tlak2))
        self.wait()

        self.play(tlak2.animate.shift(LEFT * 3.5))
        self.play(Write(gustoća))
        self.wait()

        self.play(TransformMatchingTex(gustoća, gustoća2))
        self.wait(2.5)

        self.play(TransformMatchingShapes(VGroup(tlak2, gustoća2), tlak3))
        self.play(tlak3.animate.move_to(ORIGIN))
        self.wait()

        self.play(TransformMatchingTex(tlak3, tlak4))
        self.wait()

        c1 = Cross(tlak4[4])
        c2 = Cross(tlak4[7])
        self.play(Create(c1), Create(c2))
        self.wait()

        self.play(TransformMatchingTex(tlak4, tlak5), FadeOut(VGroup(c1, c2)))
        self.wait(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


dulj_h_kocke = 1.2


class ThreeD_Kocka_u_2D(ThreeDScene):
    def construct(self):
        fill_op = ValueTracker(0.5)
        duljina_kocke = ValueTracker(2)

        kocka = always_redraw(
            lambda: Cube(
                side_length=duljina_kocke.get_value(),
                stroke_width=1,
                fill_opacity=fill_op.get_value(),
                fill_color=vol_boja,
            )
        )
        self.set_camera_orientation(phi=60 * DEGREES, theta=-70 * DEGREES)
        self.play(FadeIn(kocka))
        self.wait(0.5)
        self.play(duljina_kocke.animate.set_value(dulj_h_kocke))
        self.move_camera(phi=0, theta=-90 * DEGREES)
        self.play(fill_op.animate.set_value(1))


class hidrostatski_tlak(Scene):
    def construct(self):

        veličina_oznaka = 1.1
        veličina_raspisivanja = 2.5

        kocka = Square(
            side_length=dulj_h_kocke,
            stroke_width=1,
            fill_opacity=1,
            fill_color=vol_boja,
        )

        kord_sustav = Axes(
            x_range=[0, 5, 1],
            x_length=5 * dulj_h_kocke,
            y_range=[-5, 1, 1],
            y_length=6 * dulj_h_kocke,
            tips=False,
            axis_config={"include_numbers": True},
        ).to_edge(RIGHT)

        duljina_mora = 8
        more = Square(
            side_length=duljina_mora, fill_opacity=0.5, color=DARK_BLUE, stroke_width=0
        ).move_to(
            kord_sustav.coords_to_point(0, 0)
            + DOWN * (duljina_mora / 2)
            + RIGHT * (duljina_mora / 2)
        )

        more_text = (
            Tex("More", color=DARK_BLUE, stroke_color=WHITE, stroke_width=0.5)
            .scale(2)
            .move_to(kord_sustav.coords_to_point(4.3, -4.8))
        )

        gustoća = (
            MathTex(r"\rho = 1000 kg/{m^3}", color=gustoća_boja)
            .scale(veličina_oznaka)
            .to_edge(LEFT, buff=0.3)
            .shift(UP * 2)
        )

        tlak_formula = (
            MathTex(
                r"{P}",
                r"=",
                r"{\rho}",
                r"{h}",
                r"{g}",
                color=tlak_boja,
            )
            .scale(veličina_oznaka)
            .to_edge(LEFT, buff=0.3)
        )
        tlak_formula[2].set_color(gustoća_boja)
        tlak_formula[3].set_color(dubina_boja)
        tlak_formula[4].set_color(Fg_boja)

        tlak1 = (
            MathTex(
                r"{P}",
                r"=",
                r"1000",
                r"*",
                r"3",
                r"*",
                grav_u,
                r"=",
                round(1000 * 3 * grav_u),
                color=tlak_boja,
            )
            .scale(veličina_oznaka)
            .to_edge(LEFT, buff=0.3)
        )
        tlak1[2].set_color(gustoća_boja)
        tlak1[4].set_color(dubina_boja)
        tlak1[6].set_color(Fg_boja)

        tlak1_r = (
            MathTex(
                r"{P}",
                r"=",
                round(1000 * 3 * grav_u),
                r"Pa",
                color=tlak_boja,
            )
            .scale(veličina_oznaka)
            .to_edge(LEFT, buff=0.3)
        )

        tlak1_ras = (
            MathTex(
                r"{P_1}",
                r"=",
                r"1000",
                r"*",
                r"3",
                r"*",
                grav_u,
                color=tlak_boja,
            )
            .scale(veličina_raspisivanja)
            .shift(UP)
        )
        tlak1_ras[2].set_color(gustoća_boja)
        tlak1_ras[4].set_color(dubina_boja)
        tlak1_ras[6].set_color(Fg_boja)

        tlak1_ras2 = (
            MathTex(
                r"{P_1}",
                r"=",
                r"{\rho}",
                r"{h_1}",
                r"{g}",
                color=tlak_boja,
            )
            .scale(veličina_raspisivanja)
            .shift(UP)
        )
        tlak1_ras2[2].set_color(gustoća_boja)
        tlak1_ras2[3].set_color(dubina_boja)
        tlak1_ras2[4].set_color(Fg_boja)

        tlak2 = (
            MathTex(
                r"{P}",
                r"=",
                r"1000",
                r"*",
                r"4",
                r"*",
                grav_u,
                r"=",
                round(1000 * 4 * grav_u),
                color=tlak_boja_b,
            )
            .scale(veličina_oznaka)
            .to_edge(LEFT, buff=0.3)
            .shift(DOWN * 2)
        )
        tlak2[2].set_color(gustoća_boja)
        tlak2[4].set_color(dubina_boja)
        tlak2[6].set_color(Fg_boja)

        tlak2_r = (
            MathTex(
                r"{P}",
                r"=",
                round(1000 * 4 * grav_u),
                r"Pa",
                color=tlak_boja_b,
            )
            .scale(veličina_oznaka)
            .to_edge(LEFT, buff=0.3)
            .shift(DOWN * 2)
        )

        tlak2_ras = (
            MathTex(
                r"{P_2}",
                r"=",
                r"1000",
                r"*",
                r"4",
                r"*",
                grav_u,
                color=tlak_boja_b,
            )
            .scale(veličina_raspisivanja)
            .shift(DOWN)
        )
        tlak2_ras[2].set_color(gustoća_boja)
        tlak2_ras[4].set_color(dubina_boja)
        tlak2_ras[6].set_color(Fg_boja)

        tlak2_ras2 = (
            MathTex(
                r"{P_2}",
                r"=",
                r"{\rho}",
                r"{h_2}",
                r"{g}",
                color=tlak_boja_b,
            )
            .scale(veličina_raspisivanja)
            .shift(DOWN)
        )
        tlak2_ras2[2].set_color(gustoća_boja)
        tlak2_ras2[3].set_color(dubina_boja)
        tlak2_ras2[4].set_color(Fg_boja)

        l1 = DashedLine(
            start=kord_sustav.coords_to_point(0, -3),
            end=kord_sustav.coords_to_point(2, -3),
        )

        l2 = DashedLine(
            start=kord_sustav.coords_to_point(0, -4),
            end=kord_sustav.coords_to_point(2, -4),
        )

        fu_ras = MathTex(
            r"{P_2}",
            r"-",
            r"{P_1}",
            r"=",
            r"{\rho}",
            r"{g}",
            r"\left(",
            r"{h_2}",
            r"{-}",
            r"{h_1}",
            r"\right)",
            color=fu_boja,
        ).scale(veličina_raspisivanja)
        fu_ras[0].set_color(tlak_boja_b)
        fu_ras[2].set_color(tlak_boja)
        fu_ras[4].set_color(gustoća_boja)
        fu_ras[5].set_color(Fg_boja)
        fu_ras[7].set_color(dubina_boja)
        fu_ras[9].set_color(dubina_boja)

        fu_ras2 = MathTex(
            r"{\Delta P}",
            r"=",
            r"{\rho}",
            r"{g}",
            r"\left(",
            r"{h_2}",
            r"{-}",
            r"{h_1}",
            r"\right)",
            color=fu_boja,
        ).scale(veličina_raspisivanja)
        fu_ras2[0].set_color(tlak_boja)
        fu_ras2[2].set_color(gustoća_boja)
        fu_ras2[3].set_color(Fg_boja)
        fu_ras2[5].set_color(dubina_boja)
        fu_ras2[7].set_color(dubina_boja)

        fu_ras3 = MathTex(
            r"{\Delta P}",
            r"=",
            r"{\rho}",
            r"{g}",
            r"{\Delta h}",
            color=fu_boja,
        ).scale(veličina_raspisivanja)
        fu_ras3[0].set_color(tlak_boja)
        fu_ras3[2].set_color(gustoća_boja)
        fu_ras3[3].set_color(Fg_boja)
        fu_ras3[4].set_color(dubina_boja)

        fu_ras4 = MathTex(
            r"{",
            r"{F}",
            r"\over",
            r"A}",
            r"=",
            r"{\rho}",
            r"{g}",
            r"{\Delta h}",
            color=fu_boja,
        ).scale(veličina_raspisivanja)
        fu_ras4[1].set_color(tlak_boja)
        fu_ras4[3].set_color(pov_boja)
        fu_ras4[5].set_color(gustoća_boja)
        fu_ras4[6].set_color(Fg_boja)
        fu_ras4[7].set_color(dubina_boja)

        fu_ras5 = MathTex(
            r"{",
            r"{F}",
            r"\over",
            r"A}",
            r"=",
            r"{\rho}",
            r"{g}",
            r"{\Delta h}",
            r"{\Big /}",
            r"*",
            r"{A}",
            color=fu_boja,
        ).scale(veličina_raspisivanja)
        fu_ras5[1].set_color(tlak_boja)
        fu_ras5[3].set_color(pov_boja)
        fu_ras5[5].set_color(gustoća_boja)
        fu_ras5[6].set_color(Fg_boja)
        fu_ras5[7].set_color(dubina_boja)
        fu_ras5[10].set_color(pov_boja)

        fu_ras6 = MathTex(
            r"{F}",
            r"=",
            r"{\rho}",
            r"{g}",
            r"{\Delta h}",
            r"*",
            r"{A}",
            color=fu_boja,
        ).scale(veličina_raspisivanja)
        fu_ras6[2].set_color(gustoća_boja)
        fu_ras6[3].set_color(Fg_boja)
        fu_ras6[4].set_color(dubina_boja)
        fu_ras6[6].set_color(pov_boja)

        fu_ras7 = MathTex(
            r"{F}",
            r"=",
            r"{\rho}",
            r"{g}",
            r"{V}",
            color=fu_boja,
        ).scale(veličina_raspisivanja)
        fu_ras7[2].set_color(gustoća_boja)
        fu_ras7[3].set_color(Fg_boja)
        fu_ras7[4].set_color(vol_boja)

        fu_formula = MathTex(
            r"{F}",
            r"_{u}",
            r"=",
            r"{\rho}",
            r"_{flu}",
            r"{g}",
            r"{V}",
            r"_{uron}",
            color=fu_boja,
        ).scale(veličina_raspisivanja)
        fu_formula[3:5].set_color(gustoća_boja)
        fu_formula[5:7].set_color(Fg_boja)
        fu_formula[6:8].set_color(vol_boja)

        self.add(kocka)
        self.wait()

        self.play(Write(gustoća))
        self.play(
            kocka.animate.move_to(
                kord_sustav.coords_to_point(1, -3)
                + DOWN * (dulj_h_kocke / 2)
                + RIGHT * (dulj_h_kocke / 2)
            )
        )
        self.play(AnimationGroup(Create(more), Write(more_text)))
        self.play(Create(kord_sustav))
        self.play(Write(l1), run_time=0.6)
        self.wait()

        self.play(Write(tlak_formula))
        self.wait()

        self.play(TransformMatchingTex(tlak_formula, tlak1))
        self.wait()

        self.play(TransformMatchingTex(tlak1, tlak1_r))
        self.wait()

        b = Brace(l2, DOWN)
        temp = VGroup(b, Tex("???").next_to(b, DOWN))
        self.play(Write(l2), Write(temp))
        self.wait()

        self.play(Write(tlak_formula.shift(DOWN * 2)))
        self.play(TransformMatchingTex(tlak_formula, tlak2))
        self.play(TransformMatchingTex(tlak2, tlak2_r))
        self.wait()

        self.play(Unwrite(temp))
        self.wait()

        strelice = VGroup()
        for num in range(-2, 1):
            strelice.add(
                Arrow(
                    start=kocka.get_bottom() + LEFT * (num / 2),
                    end=kocka.get_top() + LEFT * (num / 2),
                    buff=0,
                )
            ).add_updater(
                lambda poz: poz.move_to(kocka.get_center() + LEFT * (num / 2))
            )
        self.play(Create(strelice))
        self.wait()

        self.play(
            kocka.animate.move_to(
                kord_sustav.coords_to_point(1, 0.5)
                + DOWN * (dulj_h_kocke / 2)
                + RIGHT * (dulj_h_kocke / 2)
            )
        )
        self.wait()

        self.play(Uncreate(strelice))
        self.wait()

        self.play(
            kocka.animate.move_to(
                kord_sustav.coords_to_point(1, -3)
                + DOWN * (dulj_h_kocke / 2)
                + RIGHT * (dulj_h_kocke / 2)
            )
        )
        self.play(Unwrite(gustoća))
        self.wait()

        desna_strana = VGroup(kocka, more, more_text, kord_sustav, l1, l2)
        self.play(
            desna_strana.animate.shift(RIGHT * 8),
            tlak1_r.animate.move_to(ORIGIN + UP).scale(veličina_raspisivanja),
            tlak2_r.animate.move_to(ORIGIN + DOWN).scale(veličina_raspisivanja),
        )
        self.remove(desna_strana)
        self.wait()

        self.play(TransformMatchingTex(tlak1_r, tlak1_ras))
        self.play(TransformMatchingTex(tlak2_r, tlak2_ras))
        self.wait(2)

        self.play(TransformMatchingTex(tlak1_ras, tlak1_ras2))
        self.play(TransformMatchingTex(tlak2_ras, tlak2_ras2))
        self.wait()

        self.play(TransformMatchingShapes(VGroup(tlak1_ras2, tlak2_ras2), fu_ras))
        self.wait()

        self.play(TransformMatchingTex(fu_ras, fu_ras2))
        self.wait()

        self.play(TransformMatchingTex(fu_ras2, fu_ras3))
        self.wait()

        self.play(TransformMatchingTex(fu_ras3, fu_ras4))
        self.wait()

        self.play(TransformMatchingTex(fu_ras4, fu_ras5))
        self.wait()

        c1 = Cross(fu_ras5[3])
        c2 = Cross(fu_ras5[10])
        self.play(Create(c1), Create(c2))
        self.wait()

        self.play(TransformMatchingTex(fu_ras5, fu_ras6), FadeOut(c1), FadeOut(c2))
        self.wait()

        self.play(TransformMatchingTex(fu_ras6, fu_ras7))
        self.wait()

        self.play(TransformMatchingTex(fu_ras7, fu_formula))
        self.wait(2)

        self.play(FadeOut(fu_formula))
        self.wait()


class final_pokus(Scene):
    def construct(self):

        veličina_oznaka = 1.5
        volumen = 0.02
        fu = 1000 * grav_u * volumen

        masa_k = 40
        masa_l = 4
        fg_k = masa_k * grav_u
        fg_l = masa_l * grav_u

        kord_sustav = Axes(
            x_range=[0, 5, 1],
            x_length=5 * dulj_h_kocke,
            y_range=[-5, 1, 1],
            y_length=6 * dulj_h_kocke,
            tips=False,
            axis_config={"include_numbers": True},
        ).to_edge(RIGHT)

        duljina_mora = 8
        more = Square(
            side_length=duljina_mora, fill_opacity=0.5, color=DARK_BLUE, stroke_width=0
        ).move_to(
            kord_sustav.coords_to_point(0, 0)
            + DOWN * (duljina_mora / 2)
            + RIGHT * (duljina_mora / 2)
        )

        more_text = (
            Tex("More", color=DARK_BLUE, stroke_color=WHITE, stroke_width=0.5)
            .scale(2)
            .move_to(kord_sustav.coords_to_point(4.3, -4.8))
        )

        l1 = DashedLine(
            start=kord_sustav.coords_to_point(0, -3),
            end=kord_sustav.coords_to_point(5, -3),
        )

        self.play(
            AnimationGroup(
                FadeIn(BallImg.move_to(ORIGIN).scale(0.7).shift(LEFT * 5)),
                FadeIn(RockImg.move_to(ORIGIN).scale(0.7).shift(LEFT * 2)),
            )
        )
        self.wait()

        volumen_oznaka = (
            MathTex(
                r"{V} = ",
                volumen,
                r"{m^3}",
                color=vol_boja,
            )
            .scale(veličina_oznaka)
            .to_edge(LEFT, buff=0.3)
            .shift(UP * 3)
        )

        masa_k_oznaka = (
            MathTex(
                r"{m}_k = ",
                masa_k,
                r"{kg}",
                color=masa_boja,
            )
            .scale(veličina_oznaka)
            .to_edge(LEFT, buff=0.3)
            .shift(UP * 1.5)
        )

        masa_l_oznaka = (
            MathTex(
                r"{m}_l = ",
                masa_l,
                r"{kg}",
                color=masa_boja,
            )
            .scale(veličina_oznaka)
            .to_edge(LEFT, buff=0.3)
        )

        desna_strana = VGroup(more, more_text, kord_sustav)
        self.add(desna_strana.shift(RIGHT * 8))
        self.play(desna_strana.animate.shift(LEFT * 8))
        self.play(
            BallImg.animate.move_to(
                kord_sustav.coords_to_point(0.5, -3)
                + DOWN * (BallImg.width / 2)
                + RIGHT * (BallImg.width / 2)
            ),
            RockImg.animate.move_to(
                kord_sustav.coords_to_point(3, -3)
                + DOWN * (RockImg.width / 2)
                + RIGHT * (RockImg.width / 2)
            ),
        )
        self.wait()

        self.play(Write(l1))
        self.wait()

        self.play(Write(volumen_oznaka))
        self.wait()

        self.play(AnimationGroup(Write(masa_k_oznaka), Write(masa_l_oznaka)))
        self.wait()

        vel_vek_oznake = 0.6

        vek_k_fg = Arrow(
            start=RockImg.get_center(),
            end=RockImg.get_center() + DOWN * (fg_k / 100),
            color=Fg_boja,
            buff=0,
        )

        vek_l_fg = Arrow(
            start=BallImg.get_center(),
            end=BallImg.get_center() + DOWN * (fg_l / 100),
            color=Fg_boja,
            buff=0,
        )

        vek_k_fu = Arrow(
            start=RockImg.get_center(),
            end=RockImg.get_center() + UP * (fu / 100),
            color=fu_boja,
            buff=0,
        )

        vek_l_fu = Arrow(
            start=BallImg.get_center(),
            end=BallImg.get_center() + UP * (fu / 100),
            color=fu_boja,
            buff=0,
        )

        k_fg_oznaka = (
            MathTex(r"{Fg} = ", fg_k, r"N", color=Fg_boja)
            .scale(vel_vek_oznake)
            .move_to(RockImg.get_center() + RIGHT + DOWN * 0.4)
        )

        l_fg_oznaka = (
            MathTex(r"{Fg} = ", fg_l, r"N", color=Fg_boja)
            .scale(vel_vek_oznake)
            .move_to(BallImg.get_center() + RIGHT + DOWN * 0.4)
        )

        k_fu_oznaka = (
            MathTex(r"{Fu} = ", fu, r"N", color=fu_boja)
            .scale(vel_vek_oznake)
            .move_to(RockImg.get_center() + RIGHT + UP * 0.4)
        )

        l_fu_oznaka = (
            MathTex(r"{Fu} = ", fu, r"N", color=fu_boja)
            .scale(vel_vek_oznake)
            .move_to(BallImg.get_center() + RIGHT + UP * 0.4)
        )

        self.play(
            AnimationGroup(
                Create(vek_k_fg),
                Write(k_fg_oznaka),
                Create(vek_l_fg),
                Write(l_fg_oznaka),
            )
        )
        self.wait(2.5)

        self.play(
            AnimationGroup(
                Create(vek_k_fu),
                Write(k_fu_oznaka),
                Create(vek_l_fu),
                Write(l_fu_oznaka),
            )
        )
        self.wait(7)

        self.play(
            FadeOut(vek_k_fg, vek_k_fu, k_fg_oznaka, k_fu_oznaka),
            RockImg.animate.shift(DOWN * 3),
        )
        self.wait()

        self.play(
            FadeOut(vek_l_fg, vek_l_fu, l_fg_oznaka, l_fu_oznaka),
            BallImg.animate.shift(UP * 5.5),
        )
        self.wait()

        vek_l_fg2 = Arrow(
            start=BallImg.get_center(),
            end=BallImg.get_center() + DOWN * (fg_l / 100),
            color=Fg_boja,
            buff=0,
        )

        vek_l_fu2 = Arrow(
            start=BallImg.get_center(),
            end=BallImg.get_center() + UP * (1000 * grav_u * 0.004 / 100),
            color=fu_boja,
            buff=0,
        )

        l_fg_oznaka2 = (
            MathTex(r"{Fg} = ", fg_l, r"N", color=Fg_boja)
            .scale(vel_vek_oznake)
            .move_to(BallImg.get_center() + RIGHT + DOWN * 0.4)
        )

        l_fu_oznaka2 = (
            MathTex(
                r"{Fu} = ",
                1000 * grav_u * 0.004,
                r"N",
                color=fu_boja,
                stroke_color=BLACK,
                stroke_width=0.4,
            )
            .scale(vel_vek_oznake)
            .move_to(BallImg.get_center() + RIGHT + UP * 0.4)
        )

        self.play(
            AnimationGroup(
                Create(vek_l_fg2),
                Write(l_fg_oznaka2),
                Create(vek_l_fu2),
                Write(l_fu_oznaka2),
            )
        )
        self.wait(13)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


grav_u = 10  # m/s2
m_lopte = 408  # g
vol_lopte = 0.00019  # m3
fg_l = 4.08  # N
orig_produlj = 0.115  # m
zrak_produlj = 0.138  # m
voda_produlj = 0.127  # m
delta_produlj_zrak = round(zrak_produlj - orig_produlj, 3)  # m
delta_produlj_voda = round(voda_produlj - orig_produlj, 3)  # m


class insert_density(Scene):
    def construct(self):

        gustoća = MathTex(
            r"{\rho}", r"=", r"{m", r"\over", r"V}", color=gustoća_boja
        ).scale(3)
        gustoća[2].set_color(masa_boja)
        gustoća[4].set_color(vol_boja)

        self.play(Write(gustoća))
        self.wait()
        self.play(Unwrite(gustoća))


class insert_masa(Scene):
    def construct(self):

        m_glass = 84  # g
        m_uk = 801  # g
        m_vode = m_uk - m_glass  # g
        vol_vode = 25  # oz
        vol_vode_m3 = 0.0007  # m3

        masa_vode = (
            MathTex(r"{m_{vode}}", r"=", m_vode, r"g", color=masa_boja)
            .scale(2)
            .to_edge(LEFT, buff=0.3)
            .shift(UP)
        )

        masa_vode_kg = (
            MathTex(r"{m_{vode}}", r"=", m_vode / 1000, r"kg", color=masa_boja)
            .scale(2)
            .to_edge(LEFT, buff=0.3)
            .shift(UP)
        )

        volumen_vode = (
            MathTex(r"{V_{vode}}", r"=", vol_vode, r"oz", color=vol_boja)
            .scale(2)
            .to_edge(LEFT, buff=0.3)
            .shift(DOWN)
        )

        volumen_vode_m3 = (
            MathTex(r"{V_{vode}}", r"=", vol_vode_m3, r"{m^3}", color=vol_boja)
            .scale(2)
            .to_edge(LEFT, buff=0.3)
            .shift(DOWN)
        )

        gustoća = (
            MathTex(r"{\rho}", r"=", r"{{m}", r"\over", r"V}", color=gustoća_boja)
            .scale(2)
            .to_edge(RIGHT, buff=0.3)
        )
        gustoća[2].set_color(masa_boja)
        gustoća[4].set_color(vol_boja)

        gustoća_ras = (
            MathTex(
                r"{\rho}",
                r"=",
                r"{",
                m_vode / 1000,
                r"kg",
                r"\over",
                vol_vode_m3,
                r"{m^3}",
                r"}",
                color=gustoća_boja,
            )
            .scale(2)
            .to_edge(RIGHT, buff=0.3)
        )
        gustoća_ras[3:5].set_color(masa_boja)
        gustoća_ras[6:8].set_color(vol_boja)

        gustoća_rješenje = MathTex(
            r"{\rho}",
            r"=",
            round((m_vode / 1000) / vol_vode_m3, 2),
            r"kg",
            r"/",
            r"{m^3}",
            color=gustoća_boja,
        ).scale(2)

        self.wait()
        self.play(Write(masa_vode))
        self.play(Write(volumen_vode))
        self.wait()

        self.play(TransformMatchingTex(masa_vode, masa_vode_kg))
        self.play(TransformMatchingTex(volumen_vode, volumen_vode_m3))
        self.wait(2)

        self.play(Write(gustoća))
        self.wait(2)

        self.play(
            TransformMatchingShapes(
                VGroup(masa_vode_kg, volumen_vode_m3, gustoća), gustoća_ras
            )
        )
        self.play(gustoća_ras.animate.move_to(ORIGIN))
        self.wait(2)

        self.play(TransformMatchingTex(gustoća_ras, gustoća_rješenje))
        self.wait(2)
        self.play(Unwrite(gustoća_rješenje))
        self.wait(0.5)


class insert_uzgon(Scene):
    def construct(self):

        fu_ras7 = MathTex(
            r"{F}",
            r"=",
            r"{\rho}",
            r"{g}",
            r"{V}",
            color=fu_boja,
        ).scale(3)
        fu_ras7[2].set_color(gustoća_boja)
        fu_ras7[3].set_color(Fg_boja)
        fu_ras7[4].set_color(vol_boja)

        fu_formula = MathTex(
            r"{F}",
            r"_{u}",
            r"=",
            r"{\rho}",
            r"_{flu}",
            r"{g}",
            r"{V}",
            r"_{uron}",
            color=fu_boja,
        ).scale(3)
        fu_formula[3:5].set_color(gustoća_boja)
        fu_formula[5:7].set_color(Fg_boja)
        fu_formula[6:8].set_color(vol_boja)

        self.play(Write(fu_ras7))
        self.wait()

        self.play(TransformMatchingTex(fu_ras7, fu_formula))
        self.wait(2.5)

        self.play(Unwrite(fu_formula))
        self.wait(0.5)


class insert_fg(Scene):
    def construct(self):

        masa_lopte = (
            MathTex(r"{m_l}", r"=", m_lopte, r"g", color=masa_boja).scale(2).shift(UP)
        )
        masa_lopte_kg = (
            MathTex(r"{m_l}", r"=", m_lopte / 1000, r"kg", color=masa_boja)
            .scale(2)
            .shift(UP)
        )

        fg_formula = (
            MathTex(r"{F_g}", r"=", r"{m}", r"{g}", color=Fg_boja).scale(2).shift(DOWN)
        )
        fg_formula[2].set_color(masa_boja)

        fg_formula_rje = (
            MathTex(r"{F_g}", r"=", m_lopte / 1000, r"*", grav_u, color=Fg_boja)
            .scale(2)
            .shift(DOWN)
        )
        fg_formula_rje[2].set_color(masa_boja)

        fg_formula_final = MathTex(
            r"{F_g}", r"=", (m_lopte / 1000) * grav_u, r"N", color=Fg_boja
        ).scale(3)

        self.wait(0.5)
        self.play(Write(masa_lopte))
        self.play(TransformMatchingTex(masa_lopte, masa_lopte_kg))
        self.wait()

        self.play(Write(fg_formula))
        self.wait()

        self.play(
            TransformMatchingShapes(VGroup(fg_formula, masa_lopte_kg), fg_formula_rje)
        )
        self.play(TransformMatchingTex(fg_formula_rje, fg_formula_final))
        self.wait()

        self.play(Unwrite(fg_formula_final))
        self.wait(0.5)


class insert_el_sila(Scene):
    def construct(self):

        Fg_je_Fel = MathTex(r"{F_g}", r"=", r"{F_{el}}", color=Fg_boja).scale(3)
        Fg_je_Fel[2].set_color(Fel_boja)

        Fg_je_Fel_ras = MathTex(
            r"{F_g}", r"=", r"{\Delta l}", r"{K}", color=Fg_boja
        ).scale(3)
        Fg_je_Fel_ras[2].set_color(Dl_boja)
        Fg_je_Fel_ras[3].set_color(Fel_boja)

        Fg_je_Fel_ras2 = MathTex(
            r"{m}", r"{g}", r"=", r"{\Delta l}", r"{K}", color=Fg_boja
        ).scale(3)
        Fg_je_Fel_ras2[0].set_color(masa_boja)
        Fg_je_Fel_ras2[3].set_color(Dl_boja)
        Fg_je_Fel_ras2[4].set_color(Fel_boja)

        Fg_je_Fel_ras2 = MathTex(
            r"{m}", r"{g}", r"=", r"{\Delta l}", r"{K}", color=Fg_boja
        ).scale(3)
        Fg_je_Fel_ras2[0].set_color(masa_boja)
        Fg_je_Fel_ras2[3].set_color(Dl_boja)
        Fg_je_Fel_ras2[4].set_color(Fel_boja)

        Fg_je_Fel_ras3 = MathTex(
            m_lopte / 1000,
            r"*",
            grav_u,
            r"=",
            delta_produlj_zrak,
            r"{K}",
            color=Fg_boja,
        ).scale(3)
        Fg_je_Fel_ras3[0].set_color(masa_boja)
        Fg_je_Fel_ras3[4].set_color(Dl_boja)
        Fg_je_Fel_ras3[5].set_color(Fel_boja)

        Fg_je_Fel_ras4 = MathTex(
            fg_l,
            r"=",
            delta_produlj_zrak,
            r"{K}",
            color=Fg_boja,
        ).scale(3)
        Fg_je_Fel_ras4[2].set_color(Dl_boja)
        Fg_je_Fel_ras4[3].set_color(Fel_boja)

        Fg_je_Fel_ras5 = MathTex(
            fg_l,
            r"=",
            delta_produlj_zrak,
            r"{K}",
            r"\big /",
            delta_produlj_zrak,
            color=Fg_boja,
        ).scale(3)
        Fg_je_Fel_ras5[2].set_color(Dl_boja)
        Fg_je_Fel_ras5[3].set_color(Fel_boja)
        Fg_je_Fel_ras5[5].set_color(Dl_boja)

        Fg_je_Fel_ras6 = MathTex(
            round(fg_l / delta_produlj_zrak, 3),
            r"=",
            r"{K}",
            color=Fel_boja,
        ).scale(3)

        Fg_je_Fel_final = MathTex(
            r"{K}",
            r"=",
            round(fg_l / delta_produlj_zrak, 3),
            r"N/m",
            color=Fel_boja,
        ).scale(3)

        Dl_formula = MathTex(
            r"{\Delta l}", r"=", r"{l2}", r"-", r"{l1}", color=Dl_boja
        ).scale(3)

        Dl_formula_rje = MathTex(
            r"{\Delta l}", r"=", zrak_produlj, r"-", orig_produlj, color=Dl_boja
        ).scale(3)

        Dl_formula_final = MathTex(
            r"{\Delta l}", r"=", delta_produlj_zrak, r"{m}", color=Dl_boja
        ).scale(3)

        self.play(Write(Dl_formula))
        self.wait()

        self.play(TransformMatchingTex(Dl_formula, Dl_formula_rje))
        self.wait()

        self.play(TransformMatchingTex(Dl_formula_rje, Dl_formula_final))
        self.wait()

        self.play(
            Dl_formula_final.animate.scale(0.6666).to_edge(LEFT, buff=0.3).shift(UP * 3)
        )
        self.play(Write(Fg_je_Fel))
        self.wait()

        self.play(TransformMatchingTex(Fg_je_Fel, Fg_je_Fel_ras))
        self.wait()

        self.play(TransformMatchingTex(Fg_je_Fel_ras, Fg_je_Fel_ras2))
        self.wait()

        self.play(
            TransformMatchingShapes(
                VGroup(Fg_je_Fel_ras2, Dl_formula_final), Fg_je_Fel_ras3
            )
        )
        self.wait()

        self.play(TransformMatchingTex(Fg_je_Fel_ras3, Fg_je_Fel_ras4))
        self.wait()

        self.play(TransformMatchingTex(Fg_je_Fel_ras4, Fg_je_Fel_ras5))
        self.wait()

        self.play(TransformMatchingTex(Fg_je_Fel_ras5, Fg_je_Fel_ras6))
        self.wait()

        self.play(TransformMatchingTex(Fg_je_Fel_ras6, Fg_je_Fel_final))
        self.wait()

        self.play(Unwrite(Fg_je_Fel_final))
        self.wait(0.5)


class insert_prividna_te(Scene):
    def construct(self):

        Dl_formula = MathTex(
            r"{\Delta l}", r"=", r"{l2}", r"-", r"{l1}", color=Dl_boja
        ).scale(3)

        Dl_formula_rje = MathTex(
            r"{\Delta l}", r"=", voda_produlj, r"-", orig_produlj, color=Dl_boja
        ).scale(3)

        Dl_formula_final = MathTex(
            r"{\Delta l}", r"=", delta_produlj_voda, r"{m}", color=Dl_boja
        ).scale(3)

        Fel_formula = (
            MathTex(r"{F_{el}}", r"=", r"{\Delta l}", r"{K}", color=Fel_boja)
            .scale(3)
            .shift(DOWN * 2)
        )
        Fel_formula[2].set_color(Dl_boja)

        Fel_račun = MathTex(
            r"{F_{el}}",
            r"=",
            delta_produlj_voda,
            r"*",
            round(fg_l / delta_produlj_zrak, 3),
            color=Fel_boja,
        ).scale(3)
        Fel_račun[2].set_color(Dl_boja)

        Fel_final = MathTex(
            r"{F_{el}}",
            r"=",
            round(delta_produlj_voda * (fg_l / delta_produlj_zrak), 3),
            r"N",
            color=Fel_boja,
        ).scale(3)

        fg_formula_final = MathTex(
            r"{F_g}", r"=", (m_lopte / 1000) * grav_u, r"N", color=Fg_boja
        ).scale(2.4)

        Fu_formula2 = MathTex(
            r"{F_u}", r"=", r"{F_g}", r"-", r"{F_{el}}", color=fu_boja
        ).scale(3)
        Fu_formula2[2].set_color(Fg_boja)
        Fu_formula2[4].set_color(Fel_boja)

        Fu_rješenje = MathTex(
            r"{F_u}",
            r"=",
            (m_lopte / 1000) * grav_u,
            r"-",
            round(delta_produlj_voda * (fg_l / delta_produlj_zrak), 3),
            color=fu_boja,
        ).scale(3)
        Fu_rješenje[2].set_color(Fg_boja)
        Fu_rješenje[4].set_color(Fel_boja)

        Fu_rješenje = MathTex(
            r"{F_u}",
            r"=",
            (m_lopte / 1000) * grav_u,
            r"-",
            round(delta_produlj_voda * (fg_l / delta_produlj_zrak), 3),
            color=fu_boja,
        ).scale(3)
        Fu_rješenje[2].set_color(Fg_boja)
        Fu_rješenje[4].set_color(Fel_boja)

        Fu_final = MathTex(
            r"{F_u}",
            r"=",
            (m_lopte / 1000) * grav_u
            - round(delta_produlj_voda * (fg_l / delta_produlj_zrak), 3),
            r"N",
            color=fu_boja,
        ).scale(3)

        self.play(Write(Dl_formula))
        self.play(TransformMatchingTex(Dl_formula, Dl_formula_rje))
        self.wait(0.5)

        self.play(TransformMatchingTex(Dl_formula_rje, Dl_formula_final))
        self.play(Dl_formula_final.animate.shift(UP * 2))
        self.play(Write(Fel_formula))
        self.play(
            TransformMatchingShapes(VGroup(Fel_formula, Dl_formula_final), Fel_račun)
        )
        self.wait(0.5)

        self.play(TransformMatchingTex(Fel_račun, Fel_final))
        self.wait()

        self.play(Fel_final.animate.scale(0.8).shift(UP * 2.5))
        self.play(Write(fg_formula_final.shift(DOWN * 2.5)))
        self.wait()

        self.play(Write(Fu_formula2))
        self.wait()

        self.play(
            TransformMatchingShapes(
                VGroup(Fu_formula2, fg_formula_final, Fel_final), Fu_rješenje
            )
        )
        self.wait()

        self.play(TransformMatchingTex(Fu_rješenje, Fu_final))
        self.wait()

        self.play(Unwrite(Fu_final))
        self.wait()


class insert_volumen(Scene):
    def construct(self):

        volumen_cl = MathTex(
            r"{V}", r"=", vol_lopte * 100000, r"{cl}", color=vol_boja
        ).scale(3)

        volumen_m3 = MathTex(r"{V}", r"{=}", vol_lopte, r"{m^3}", color=vol_boja).scale(
            3
        )

        fu_formula = (
            MathTex(
                r"{F_{u}}",
                r"=",
                r"{\rho}",
                r"_{flu}",
                r"{g}",
                r"{V_{uron}}",
                color=fu_boja,
            )
            .scale(3)
            .shift(DOWN * 2)
        )
        fu_formula[2:4].set_color(gustoća_boja)
        fu_formula[4].set_color(Fg_boja)
        fu_formula[5].set_color(vol_boja)

        fu_formula_ras = (
            MathTex(
                r"{\rho}",
                r"_{flu}",
                r"=",
                r"{",
                r"{F_{u}}",
                r"\over",
                r"{g}",
                r"{V_{uron}}",
                r"}",
                color=gustoća_boja,
            )
            .scale(3)
            .shift(DOWN * 1.8)
        )
        fu_formula_ras[4].set_color(fu_boja)
        fu_formula_ras[6].set_color(Fg_boja)
        fu_formula_ras[7].set_color(vol_boja)

        fu_formula_ras2 = (
            MathTex(
                r"{\rho}",
                r"_{flu}",
                r"=",
                r"{",
                r"{F_{u}}",
                r"\over",
                grav_u,
                r"*",
                vol_lopte,
                r"}",
                color=gustoća_boja,
            )
            .scale(3)
            .shift(DOWN * 1.8)
        )
        fu_formula_ras2[4].set_color(fu_boja)
        fu_formula_ras2[6].set_color(Fg_boja)
        fu_formula_ras2[8].set_color(vol_boja)

        fu_oznaka = (
            MathTex(
                r"{F_g}",
                r"{=}",
                (m_lopte / 1000) * grav_u
                - round(delta_produlj_voda * (fg_l / delta_produlj_zrak), 3),
                r"N",
                color=fu_boja,
            )
            .scale(3)
            .shift(UP * 2)
        )

        fu_formula_ras3 = (
            MathTex(
                r"{\rho}",
                r"_{flu}",
                r"=",
                r"{",
                (m_lopte / 1000) * grav_u
                - round(delta_produlj_voda * (fg_l / delta_produlj_zrak), 3),
                r"\over",
                grav_u,
                r"*",
                vol_lopte,
                r"}",
                color=gustoća_boja,
            )
            .scale(3)
            .shift(DOWN * 1.8)
        )
        fu_formula_ras3[4].set_color(fu_boja)
        fu_formula_ras3[6].set_color(Fg_boja)
        fu_formula_ras3[8].set_color(vol_boja)

        fu_formula_ras4 = MathTex(
            r"{\rho}",
            r"_{mora}",
            r"=",
            round(
                (
                    (m_lopte / 1000) * grav_u
                    - (delta_produlj_voda * (fg_l / delta_produlj_zrak))
                )
                / (grav_u * vol_lopte)
            ),
            r"kg/{m^3}",
            color=gustoća_boja,
        ).scale(3)

        self.play(Write(volumen_cl))
        self.wait()

        self.play(TransformMatchingShapes(volumen_cl, volumen_m3))
        self.wait()

        self.play(volumen_m3.animate.shift(UP * 2))
        self.play(Write(fu_formula))
        self.wait(5)

        self.play(TransformMatchingTex(fu_formula, fu_formula_ras))
        self.wait()

        self.play(
            AnimationGroup(
                TransformMatchingTex(fu_formula_ras, fu_formula_ras2),
                TransformMatchingTex(volumen_m3, fu_formula_ras2),
            )
        )
        self.wait()

        self.play(Write(fu_oznaka))
        self.wait()

        self.play(
            AnimationGroup(
                TransformMatchingTex(fu_formula_ras2, fu_formula_ras3),
                TransformMatchingTex(fu_oznaka, fu_formula_ras3),
            )
        )
        self.play(fu_formula_ras3.animate.move_to(ORIGIN))
        self.wait()

        self.play(TransformMatchingTex(fu_formula_ras3, fu_formula_ras4))
        rainbow_square = Rectangle(
            height=fu_formula_ras4[3:5].height + 0.5,
            width=fu_formula_ras4[3:5].width + 0.5,
        ).move_to(fu_formula_ras4[3:5])
        for c in [RED, ORANGE, YELLOW, GREEN, BLUE, "#4B0082", PURPLE]:
            self.play(
                ShowPassingFlash(
                    rainbow_square.set_color(c),
                    run_time=0.8,
                    rate_func=rate_functions.linear,
                )
            )
        self.play(Unwrite(fu_formula_ras4))
        self.wait()


class credits(Scene):
    def construct(self):
        skala = 1.5

        video_editor = (
            Tex(r"Video editing/\\Glas1:", color=GREEN)
            .scale(skala)
            .shift(UP * 2 + LEFT * 3)
        )

        rančunalo = (
            Tex(r"Računanje/\\Glas2:", color=BLUE)
            .scale(skala)
            .shift(UP * 2 + RIGHT * 3)
        )

        glumci = (
            Tex(r"Mjerenja/\\Glumci:", color=ORANGE).scale(skala).shift(DOWN + LEFT * 3)
        )

        snimatelj = (
            Tex(r"Mjerenja/\\Snimatelj:", color=YELLOW)
            .scale(skala)
            .shift(DOWN + RIGHT * 3)
        )

        ja = (
            Tex("Romano Žic", color=GREEN)
            .scale(skala)
            .next_to(video_editor.get_bottom(), DOWN)
        )

        ivomije = (
            Tex("Ivo Urem", color=BLUE)
            .scale(skala)
            .next_to(rančunalo.get_bottom(), DOWN)
        )

        drotovi = (
            Tex(r"Ian Galešić\\Daniel Dabo", color=ORANGE)
            .scale(skala)
            .next_to(glumci.get_bottom(), DOWN)
        )

        kamera = (
            Tex("Marul Lerga", color=YELLOW)
            .scale(skala)
            .next_to(snimatelj.get_bottom(), DOWN)
        )

        oznake = VGroup(video_editor, rančunalo, glumci, snimatelj)
        osobe = VGroup(ja, ivomije, drotovi, kamera)

        self.play(Write(oznake))
        self.play(Write(osobe))
        self.wait(3)
