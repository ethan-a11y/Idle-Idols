import arcade
import random

# --- Constants ---


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750

#650, 350, 100, arcade.color.BLUE

class hpbar:
    def __init__(self, hpbardecline):
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

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprites With Walls Example")
        self.hp = 100
        self.enemy = enemy(650, 350, 100, arcade.color.BLUE, self.hp)
        self.hpbar = hpbar(200-self.hp*2)
        self.attack = 1
        self.enemydefense = 0
        self.bossregen = 1
        self.is_boss = False
        self.upgradeNames = [""]
        self.gameStarted = False
        
       # self.attackText2 = attackText(1, False)
       # self.attackText3 = attackText(1, False)
        


    def setup(self):
        # Set the background color
        
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.upgradeButton1 = None
        self.upgradeButton2 = None
        self.upgradeButton3 = None
        self.upgradeButton4 = None
        self.upgradeButton5 = None
        self.upgradeButton6 = None
        self.upgradeButton7 = None
        self.upgradeButton8 = None
        self.upgradeButton9 = None
        self.upgradeButton10 = None
        self.upgradeButton11 = None
        
      
        self.upgradeButtons = [self.upgradeButton1, self.upgradeButton2, self.upgradeButton3, self.upgradeButton4, self.upgradeButton5, self.upgradeButton6, self.upgradeButton7, self.upgradeButton8, self.upgradeButton9, self.upgradeButton10, self.upgradeButton11]
        x = 0
        for i in self.upgradeButtons:
            x += 1
            i = arcade.Sprite("upgrade.png")
            i.width = 85
            i.height = 25 + x *24
            i.center_x = 250
            i.center_y = 590
            
        
        
        
       

    def on_draw(self):
        arcade.start_render()
        self.enemy.draw()
        self.hpbar.draw()
        
        
        
        self.gameStarted = True
        #UPGRADE MENU AND PLATFORM
        arcade.draw_rectangle_filled(650, 200, 400, 100, arcade.color.BLUE)
        arcade.draw_lrtb_rectangle_filled(0, 350, 750, 0, arcade.color.LIGHT_BROWN)
    
        for i in self.upgradeButtons:
            print(i)

        #########UPGRADE MENU#########

        #Title
        arcade.draw_text("UPGRADES", 85, 680, arcade.color.BLACK, 24)


        #UPGRADE

        for i in range(16):
            arcade.draw_text("UPGRADE " + str(i), 50, 580-i*34, arcade.color.BLACK, 12)
            
        

        


        #arcade.draw_rectangle_outline(650, 540, 200, 60, arcade.color.BLACK, 12, 0)
        
        #arcade.draw_rectangle_filled(650, 540, 150, 60, arcade.color.GREEN)

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            print("Left mouse button pressed at", x, y)
            if(x >= 550 and x <= 750 and y >= 250 and y <= 450):
                self.hp -= self.attack
                self.hpbar = hpbar(200-self.hp*2)
                self.hpbar.draw()
                print("Hit on enemy", self.hp)
                
                
        



def main():
    window = MyGame()
    window.setup()

    arcade.run()


if __name__ == "__main__":
    main()