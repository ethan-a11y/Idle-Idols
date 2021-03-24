import arcade

# --- Constants ---


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750

#650, 350, 100, arcade.color.BLUE

class hpbar:
    def __init__(self, hpbardecline):
        print("init")
        self.hpbardecline = hpbardecline

    def draw(self):
        #HP Bar
        arcade.draw_lrtb_rectangle_outline(546, 754, 574, 506, arcade.color.BLACK, 5)
        arcade.draw_lrtb_rectangle_filled(550, 750, 570, 510, arcade.color.RED)
        arcade.draw_lrtb_rectangle_filled(550, 750-self.hpbardecline, 570, 510, arcade.color.GREEN)
        



class enemy:
    def __init__(self, position_x, position_y, radius, color, hp):
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)
        


class MyGame(arcade.Window):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprites With Walls Example")
        self.hp = 100
        self.enemy = enemy(650, 350, 100, arcade.color.BLUE, self.hp)
        self.hpbar = hpbar(200-self.hp*2)


    def setup(self):
        # Set the background color
        
        arcade.set_background_color(arcade.color.DARK_BLUE)
        
       

    def on_draw(self):
        arcade.start_render()
        self.enemy.draw()
        self.hpbar.draw()
        #UPGRADE MENU AND PLATFORM
        arcade.draw_rectangle_filled(650, 200, 400, 100, arcade.color.BLUE)
        arcade.draw_lrtb_rectangle_filled(0, 350, 750, 0, arcade.color.LIGHT_BROWN)
        

        


        #arcade.draw_rectangle_outline(650, 540, 200, 60, arcade.color.BLACK, 12, 0)
        
        #arcade.draw_rectangle_filled(650, 540, 150, 60, arcade.color.GREEN)

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            print("Left mouse button pressed at", x, y)
            if(x >= 550 and x <= 750 and y >= 250 and y <= 450):
                self.hp -= 5
                self.hpbar = hpbar(200-self.hp*2)
                self.hpbar.draw()
                print("Hit on enemy", self.hp)
        



def main():
    window = MyGame()
    window.setup()

    arcade.run()


if __name__ == "__main__":
    main()