import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


def draw_face():
    """ Draw the face """
    arcade.draw_circle_filled(300, 300, 200, arcade.csscolor.PERU)


def draw_eye(x, y):
    """ Draw an eye """

    # Iris
    arcade.draw_circle_filled(x, y, 40, arcade.csscolor.FOREST_GREEN)

    # Pupil
    arcade.draw_ellipse_filled(x, y, 25, 75, arcade.csscolor.BLACK)

    # Outline
    arcade.draw_circle_outline(x, y, 40, arcade.csscolor.BLACK)


def draw_cheek(x, y):
    """ Draw a cheek """
    arcade.draw_circle_filled(x, y, 73, (194, 125, 58))


def draw_nose():
    """ Draw the nose """

    # Inside
    arcade.draw_triangle_filled(305, 300, 330, 250, 280, 250, arcade.csscolor.INDIANRED)

    # Outline
    arcade.draw_triangle_outline(305, 300, 330, 250, 280, 250, arcade.csscolor.BLACK)


def draw_whiskers(x, y):
    """ Draw whiskers """
    arcade.draw_line(355 + x - 305, 220 + y - 220, 455 + x - 305, 220 + y - 220, arcade.csscolor.BLACK, 3)
    arcade.draw_line(255 + x - 305, 220 + y - 220, 150 + x - 305, 220 + y - 220, arcade.csscolor.BLACK, 3)
    arcade.draw_line(355 + x - 305, 230 + y - 220, 455 + x - 305, 250 + y - 220, arcade.csscolor.BLACK, 3)
    arcade.draw_line(355 + x - 305, 210 + y - 220, 455 + x - 305, 190 + y - 220, arcade.csscolor.BLACK, 3)
    arcade.draw_line(255 + x - 305, 230 + y - 220, 150 + x - 305, 250 + y - 220, arcade.csscolor.BLACK, 3)
    arcade.draw_line(255 + x - 305, 210 + y - 220, 150 + x - 305, 190 + y - 220, arcade.csscolor.BLACK, 3)


def draw_ears(x, y):
    """ Draw the ears """

    # Outside
    arcade.draw_triangle_filled(480 + x - 302.5,
                                370 + y - 370,
                                370 + x - 302.5,
                                460 + y - 370,
                                540 + x - 302.5,
                                540 + y - 370,
                                arcade.csscolor.PERU)
    arcade.draw_triangle_filled(125 + x - 302.5,
                                370 + y - 370,
                                215 + x - 302.5,
                                480 + y - 370,
                                70 + x - 302.5,
                                540 + y - 370,
                                arcade.csscolor.PERU)

    # Inside
    arcade.draw_triangle_filled(460 + x - 302.5,
                                410 + y - 370,
                                420 + x - 302.5,
                                455 + y - 370,
                                495 + x - 302.5,
                                490 + y - 370,
                                arcade.csscolor.LIGHT_CORAL)
    arcade.draw_triangle_filled(145 + x - 302.5,
                                410 + y - 370,
                                190 + x - 302.5,
                                450 + y - 370,
                                115 + x - 302.5,
                                490 + y - 370,
                                arcade.csscolor.LIGHT_CORAL)

    # Outline
    arcade.draw_triangle_outline(460 + x - 302.5,
                                 410 + y - 370,
                                 420 + x - 302.5,
                                 455 + y - 370,
                                 495 + x - 302.5,
                                 490 + y - 370,
                                 arcade.csscolor.BLACK)
    arcade.draw_triangle_outline(145 + x - 302.5,
                                 410 + y - 370,
                                 190 + x - 302.5,
                                 450 + y - 370,
                                 115 + x - 302.5,
                                 490 + y - 370,
                                 arcade.csscolor.BLACK)


def draw_tongue():
    """ Draw the tongue """
    arcade.draw_arc_filled(305, 210, 40, 70, arcade.csscolor.LIGHT_CORAL, -180, 0)
    arcade.draw_arc_outline(305, 210, 40, 70, arcade.csscolor.BLACK, -180, 0)


def add_text(x, y):
    """ Add the text """
    arcade.draw_text("MEOW!", x, y, arcade.color.BLACK_BEAN, 27)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Kool Kat")

    # --- Set the background color ---
    arcade.set_background_color(arcade.color.MISTY_ROSE)

    arcade.start_render()

    # --- Draw the cat ---
    draw_face()
    draw_eye(380, 350)
    draw_eye(230, 350)
    draw_cheek(355, 220)
    draw_cheek(255, 220)
    draw_nose()
    draw_whiskers(305, 220)
    draw_ears(302.5, 370)
    draw_tongue()
    add_text(254, 40)

    arcade.finish_render()

    arcade.run()


main()
