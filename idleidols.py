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
        self.coins = 5
        self.enemy = enemy(650, 350, 100, arcade.color.BLUE, self.hp)
        self.hpbar = hpbar(200-self.hp*2)
        self.attack = 10
        self.enemydefense = 0
        self.bossregen = 1
        self.is_boss = False
        self.upgradeNames = [""]
        self.gameStarted = False
        self.upgradeCostList = [10, 20, 50, 100, 150, 200, 350, 600, 750, 1000, 1500, 2500, 4000, 10000, 50000, 250000]
        self.upgradeAttackBuffList = [1, 2, 4, 8, 16, 32, 64, 125, 250, 500, 1000, 2000, 2500, 3000, 3500, 5000]
        
       # self.attackText2 = attackText(1, False)
       # self.attackText3 = attackText(1, False)
        


    def setup(self):
        # Set the background color
        
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.upgradeButton1 = arcade.Sprite("upgrade.png")
        self.upgradeButton2 = arcade.Sprite("upgrade.png")
        self.upgradeButton3 = arcade.Sprite("upgrade.png")
        self.upgradeButton4 = arcade.Sprite("upgrade.png")
        self.upgradeButton5 = arcade.Sprite("upgrade.png")
        self.upgradeButton6 = arcade.Sprite("upgrade.png")
        self.upgradeButton7 = arcade.Sprite("upgrade.png")
        self.upgradeButton8 = arcade.Sprite("upgrade.png")
        self.upgradeButton9 = arcade.Sprite("upgrade.png")
        self.upgradeButton10 = arcade.Sprite("upgrade.png")
        self.upgradeButton11 = arcade.Sprite("upgrade.png")
        self.upgradeButton12 = arcade.Sprite("upgrade.png")
        self.upgradeButton13 = arcade.Sprite("upgrade.png")
        self.upgradeButton14 = arcade.Sprite("upgrade.png")
        self.upgradeButton15 = arcade.Sprite("upgrade.png")
        self.upgradeButton16 = arcade.Sprite("upgrade.png")

        
        self.upgradeButtons = []
        self.upgradeButtons.append(self.upgradeButton1)
        self.upgradeButtons.append(self.upgradeButton2)
        self.upgradeButtons.append(self.upgradeButton3)
        self.upgradeButtons.append(self.upgradeButton4)
        self.upgradeButtons.append(self.upgradeButton5)
        self.upgradeButtons.append(self.upgradeButton6)
        self.upgradeButtons.append(self.upgradeButton7)
        self.upgradeButtons.append(self.upgradeButton8)
        self.upgradeButtons.append(self.upgradeButton9)
        self.upgradeButtons.append(self.upgradeButton10)
        self.upgradeButtons.append(self.upgradeButton11)
        self.upgradeButtons.append(self.upgradeButton12)
        self.upgradeButtons.append(self.upgradeButton13)
        self.upgradeButtons.append(self.upgradeButton14)
        self.upgradeButtons.append(self.upgradeButton15)        
        self.upgradeButtons.append(self.upgradeButton16)


        for i in range(16):
            self.upgradeButtons[i].width = 85        
            self.upgradeButtons[i].height = 25
            self.upgradeButtons[i].center_x = 250
            self.upgradeButtons[i].center_y = 591 - i * 37
            
            
        print(self.upgradeButton1.width)

        self.coinText = arcade.draw_text("Coins: 5", 395, 700, arcade.color.BLACK, 20)
        self.coinText.bold = True
        
      

        
        
        
       

    def on_draw(self):
        arcade.start_render()
        self.enemy.draw()
        self.hpbar.draw()
        #print(self.coinText.text)
        self.coinText.draw()

        
        
        
        self.gameStarted = True
        #UPGRADE MENU AND PLATFORM
        arcade.draw_rectangle_filled(650, 200, 400, 100, arcade.color.BLUE)
        arcade.draw_lrtb_rectangle_filled(0, 350, 750, 0, arcade.color.LIGHT_BROWN)
    
        for i in self.upgradeButtons:
            i.draw()

        #########UPGRADE MENU#########

        #Title
        arcade.draw_text("UPGRADES", 85, 680, arcade.color.BLACK, 24)


        #UPGRADE

        for i in range(16):
            arcade.draw_text("UPGRADE " + str(i+1), 50, 580-i*37, arcade.color.BLACK, 12)
            
            
        

        


        #arcade.draw_rectangle_outline(650, 540, 200, 60, arcade.color.BLACK, 12, 0)
        
        #arcade.draw_rectangle_filled(650, 540, 150, 60, arcade.color.GREEN)

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            print("Left mouse button pressed at", x, y)
            if(x >= 550 and x <= 750 and y >= 250 and y <= 450):
                if self.attack >= self.hp:
                    self.hp = 100
                    self.hpbar = hpbar(200-self.hp*2)
                    self.coins += 2
                    self.coinText = arcade.draw_text("Coins: " + str(self.coins), 395, 700, arcade.color.BLACK, 20)
                    
                    print("coins: " + str(self.coins))
                else:
                    self.hp -= self.attack
                    self.hpbar = hpbar(200-self.hp*2)
                
                self.hpbar.draw()
                print("Hit on enemy", self.hp)
            for i in range(16):
                if x >= 210 and x <= 290 and y >= 580 - i*37 and y <= 600 - i*37:
                    if self.coins >= self.upgradeCostList[i]:
                        self.coins -= self.upgradeCostList[i]
                        self.attack += self.upgradeAttackBuffList[i]

                        print("Upgrade " + str(i+1) + " Purchased", "You have " + str(self.coins) + " left", "Your attack power is " + str(self.attack))
                    else:
                        print("You do not have the funds for this sir")
                self.coinText = arcade.draw_text("Coins: " + str(self.coins), 395, 700, arcade.color.BLACK, 20)
        
                
                
        



def main():
    window = MyGame()
    window.setup()

    arcade.run()


if __name__ == "__main__":
    main()