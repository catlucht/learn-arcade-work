import arcade

arcade.open_window(600, 600, "Kool Kat")

# --- Set the background color ---
arcade.set_background_color(arcade.color.MISTY_ROSE)

arcade.start_render()

# --- Draw the face ---
arcade.draw_circle_filled(300, 300, 200, arcade.csscolor.PERU)

# --- Draw the eyes ---

# Draw the iris
arcade.draw_circle_filled(380, 350, 40, arcade.csscolor.FOREST_GREEN)
arcade.draw_circle_filled(230, 350, 40, arcade.csscolor.FOREST_GREEN)

# Draw the pupil
arcade.draw_ellipse_filled(380, 350, 25, 75, arcade.csscolor.BLACK)
arcade.draw_ellipse_filled(230, 350, 25, 75, arcade.csscolor.BLACK)

# Draw the outline
arcade.draw_circle_outline(380, 350, 40, arcade.csscolor.BLACK)
arcade.draw_circle_outline(230, 350, 40, arcade.csscolor.BLACK)

# --- Draw the cheeks ---
arcade.draw_circle_filled(355, 220, 73, (194, 125, 58))
arcade.draw_circle_filled(255, 220, 73, (194, 125, 58))

# --- Draw the nose ---

# Draw the inside
arcade.draw_triangle_filled(305, 300, 330, 250, 280, 250, arcade.csscolor.INDIANRED)

# Draw the outline
arcade.draw_triangle_outline(305, 300, 330, 250, 280, 250, arcade.csscolor.BLACK)

# --- Draw the whiskers ---
arcade.draw_line(355, 220, 455, 220, arcade.csscolor.BLACK, 3)
arcade.draw_line(255, 220, 150, 220, arcade.csscolor.BLACK, 3)
arcade.draw_line(355, 230, 455, 250, arcade.csscolor.BLACK, 3)
arcade.draw_line(355, 210, 455, 190, arcade.csscolor.BLACK, 3)
arcade.draw_line(255, 230, 150, 250, arcade.csscolor.BLACK, 3)
arcade.draw_line(255, 210, 150, 190, arcade.csscolor.BLACK, 3)

# --- Draw the ears ---

# Outside
arcade.draw_triangle_filled(480, 370, 370, 460, 540, 540, arcade.csscolor.PERU)
arcade.draw_triangle_filled(125, 370, 215, 480, 70, 540, arcade.csscolor.PERU)

# Inside
arcade.draw_triangle_filled(460, 410, 420, 455, 495, 490, arcade.csscolor.LIGHT_CORAL)
arcade.draw_triangle_filled(145, 410, 190, 450, 115, 490, arcade.csscolor.LIGHT_CORAL)

# Outline
arcade.draw_triangle_outline(460, 410, 420, 455, 495, 490, arcade.csscolor.BLACK)
arcade.draw_triangle_outline(145, 410, 190, 450, 115, 490, arcade.csscolor.BLACK)

# --- Draw the tongue ---
arcade.draw_arc_filled(305, 210, 40, 70, arcade.csscolor.LIGHT_CORAL, -180, 0)
arcade.draw_arc_outline(305, 210, 40, 70, arcade.csscolor.BLACK, -180, 0)

# --- Add Text ---
arcade.draw_text("MEOW!", 254, 40, arcade.color.BLACK_BEAN, 27)

# --- Finish drawing ---
arcade.finish_render()

arcade.run()
