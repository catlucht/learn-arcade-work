import random
import arcade
import os

SPRITE_SCALING = 0.3
SPRITE_SCALING_LOCK = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Boo!"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 75

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.player_list = None
        self.coin_list = None
        self.wall_list = None

        # Set up the player
        self.player_sprite = None

        # Score
        self.score = 0

        self.physics_engine = None

        # Used in scrolling
        self.view_bottom = 0
        self.view_left = 0

        # Sound
        self.coin_sound = arcade.load_sound("secret2.wav")

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Score
        self.score = 0

        # Used in scrolling
        self.view_bottom = 0
        self.view_left = 0

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player
        # Ghost image from Emoji Island
        self.player_sprite = arcade.Sprite("Ghost Emoji.png", 0.1)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 270
        self.player_list.append(self.player_sprite)

        # --- Set up several rows of walls ---
        # Place boxes inside a loop
        for x in range(160, 801, 75):
            wall = arcade.Sprite("pattern43.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 160
            self.wall_list.append(wall)

        # Place boxes inside a loop
        for x in range(962, 2000, 75):
            wall = arcade.Sprite("pattern43.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 160
            self.wall_list.append(wall)

        # Place boxes inside a loop
        for x in range(320, 1120, 75):
            wall = arcade.Sprite("pattern32.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 320
            self.wall_list.append(wall)

        # Place boxes inside a loop
        for x in range(1280, 2100, 75):
            wall = arcade.Sprite("pattern32.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 320
            self.wall_list.append(wall)

        # Place boxes inside a loop
        for x in range(0, 481, 75):
            wall = arcade.Sprite("pattern11.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 480
            self.wall_list.append(wall)

        # Place boxes inside a loop
        for x in range(640, 1441, 75):
            wall = arcade.Sprite("pattern11.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 480
            self.wall_list.append(wall)

        # Place boxes inside a loop
        for x in range(1601, 1970, 75):
            wall = arcade.Sprite("pattern11.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 480
            self.wall_list.append(wall)

        # Place boxes inside a loop
        for x in range(160, 801, 75):
            wall = arcade.Sprite("pattern43.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 640
            self.wall_list.append(wall)

        # Place boxes inside a loop
        for x in range(962, 2000, 75):
            wall = arcade.Sprite("pattern43.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 640
            self.wall_list.append(wall)

        # Place boxes inside a loop
        for x in range(320, 1120, 75):
            wall = arcade.Sprite("pattern32.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 800
            self.wall_list.append(wall)

        # Place boxes inside a loop
        for x in range(1280, 2100, 75):
            wall = arcade.Sprite("pattern32.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 800
            self.wall_list.append(wall)

        # Place boxes inside a loop
        for x in range(0, 481, 75):
            wall = arcade.Sprite("pattern11.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 960
            self.wall_list.append(wall)

        # Place boxes inside a loop
        for x in range(640, 1441, 75):
            wall = arcade.Sprite("pattern11.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 960
            self.wall_list.append(wall)

        # Place boxes inside a loop
        for x in range(1601, 1970, 75):
            wall = arcade.Sprite("pattern11.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 960
            self.wall_list.append(wall)

        # --- Set up individual blocks ---
        wall = arcade.Sprite("lockGreen.png", SPRITE_SCALING_LOCK)
        wall.center_x = 880
        wall.center_y = 880
        self.wall_list.append(wall)

        wall = arcade.Sprite("lockGreen.png", SPRITE_SCALING_LOCK)
        wall.center_x = 1760
        wall.center_y = 1040
        self.wall_list.append(wall)

        wall = arcade.Sprite("lockGreen.png", SPRITE_SCALING_LOCK)
        wall.center_x = 1900
        wall.center_y = 560
        self.wall_list.append(wall)

        wall = arcade.Sprite("lockGreen.png", SPRITE_SCALING_LOCK)
        wall.center_x = 1080
        wall.center_y = 400
        self.wall_list.append(wall)

        wall = arcade.Sprite("lockGreen.png", SPRITE_SCALING_LOCK)
        wall.center_x = 160
        wall.center_y = 320
        self.wall_list.append(wall)

        wall = arcade.Sprite("lockGreen.png", SPRITE_SCALING_LOCK)
        wall.center_x = 80
        wall.center_y = 640
        self.wall_list.append(wall)

        # --- Set up border ---
        # Top border
        for x in range(0, 2100, 75):
            wall = arcade.Sprite("pattern04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 1120
            self.wall_list.append(wall)

        # Left border
        for y in range(-150, 2100, 75):
            wall = arcade.Sprite("pattern04.png", SPRITE_SCALING)
            wall.center_x = 0
            wall.center_y = y
            self.wall_list.append(wall)

        # Right border
        for y in range(-150, 2100, 75):
            wall = arcade.Sprite("pattern04.png", SPRITE_SCALING)
            wall.center_x = 2100
            wall.center_y = y
            self.wall_list.append(wall)

        # Bottom border
        for x in range(-150, 2100, 75):
            wall = arcade.Sprite("pattern04.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 0
            self.wall_list.append(wall)

        # -- Randomly place coins where there are no walls
        # Create the coins
        for i in range(100):

            # Create the coin instance
            # Coin image from iconfinder.com
            coin = arcade.Sprite("Skull_And_Bones_Bones_Halloween_Horror_Pirate_Skull_Dangerous_coin-512.png", 0.1)

            coin_placed_successfully = False

            while not coin_placed_successfully:
                coin.center_x = random.randrange(2000)
                coin.center_y = random.randrange(2000)

                # See if the coin is hitting anything
                wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)
                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    coin_placed_successfully = True

            self.coin_list.append(coin)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.BULGARIAN_ROSE)

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 15 + self.view_left, 20 + self.view_bottom, arcade.color.GREEN_YELLOW, 20)

    def on_key_press(self, key, modifiers):
        """ Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # --- Manage Scrolling ---

        # Keep track of if we changed the boundary. We don't want to call the
        # set_viewport command if we didn't change the view port.
        changed = False

        # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        # Make sure our boundaries are integer values. While the view port does
        # support floating point numbers, for this application we want every pixel
        # in the view port to map directly onto a pixel on the screen. We don't want
        # any rounding errors.
        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        # If we changed the boundary values, update the view port to match
        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)

        # Generate a list of all sprites that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for carrot in hit_list:
            carrot.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.coin_sound, volume=0.015)


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
