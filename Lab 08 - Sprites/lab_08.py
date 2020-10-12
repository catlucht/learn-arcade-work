import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.4
SPRITE_SCALING_CARROT = 0.4
CARROT_COUNT = 50
ENEMY_COUNT = 10

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5

class Player(arcade.Sprite):

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

class Carrot(arcade.Sprite):

    def reset(self):
        self.bottom = random.randrange(SCREEN_HEIGHT, SCREEN_WIDTH + 200)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        self.center_y -= 1
        if self.top < 0:
            self.reset()

class Enemy(arcade.sprite):

    def setup(self):
        # Create the enemies
        for i in range(ENEMY_COUNT):

            # Create the enemy instance
            # Enemy image from kenney.nl
            enemy = Enemy("spikeBall1.png", SPRITE_SCALING_CARROT)

            # Position the coin
            enemy.center_x = random.randrange(SCREEN_WIDTH)
            enemy.center_y = random.randrange(SCREEN_HEIGHT)

            enemy.change_x = random.randrange(-3, 4)
            enemy.change_y = random.randrange(-3, 4)

            # Add the coin to the lists
            self.enemy_list.append(enemy)


class MyGame(arcade.Window):

    def __init__(self):
        """ Initializer """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Bunny Game")

        # Load sound effects
        self.carrot_sound = arcade.load_sound("coin3.wav")
        self.enemy1_sound = arcade.load_sound("hurt4.wav")
        self.enemy2_sound = arcade.load_sound("laser1.wav")
        self.gold_carrot_sound = arcade.load_sound("secret2.wav")

        # Variables that will hold sprite lists
        self.player_list = None
        self.carrot_list = None
        self.enemy_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        arcade.set_background_color(arcade.color.GRAY_ASPARAGUS)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.carrot_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = Player("bunny1_walk1.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(CARROT_COUNT):

            # Carrot image from kenney.nl
            carrot = Carrot("carrot.png", SPRITE_SCALING_CARROT)

            # Position the carrot
            carrot.center_x = random.randrange(SCREEN_WIDTH)
            carrot.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the carrot to the list
            self.carrot_list.append(carrot)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.carrot_list.draw()
        self.player_list.draw()
        self.enemy_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_key_press(self, key, modifiers):
        """ Called when a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def update(self, delta_time):
        """ Movement and game logic """

        self.carrot_list.update()
        self.player_list.update()

        # Generate a list of all sprites that collided with the player.
        carrots_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.carrot_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for carrot in carrots_hit_list:
            carrot.reset()
            self.score += 1
            arcade.play_sound(self.carrot_sound)


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
