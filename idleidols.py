import arcade
import random
import time
import threading

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
        self.baseHp = 400
        self.hp = self.baseHp
        self.coins = 500000000
        self.enemy = enemy(650, 350, 100, arcade.color.BLUE, self.hp)
        self.hpbar = hpbar(200-self.hp/self.baseHp*200)
        self.coinsAdded = arcade.draw_text("+ 0", 600, 700, arcade.color.YELLOW, 20)
        self.attack = 50        
        self.wave = 1
        self.level = 8
        self.levelWave = arcade.draw_text("Level " + str(self.level) + ", Wave (" + str(self.wave) + "/5)", 545, 604, arcade.color.BLACK, 20)
        self.enemydefense = 0
        self.bossregen = 1
        self.is_boss = False
        self.bossHp = 2500
        self.upgradeNames = [""]
        self.gameStarted = False
        
        self.upgradeCostList = [10, 20, 50, 100, 150, 200, 350, 600, 750, 1000, 1500, 2500, 4000, 10000, 50000, 250000]
        self.upgradeAttackBuffList = [1, 2, 4, 8, 16, 32, 64, 125, 250, 500, 1000, 2000, 2500, 3000, 3500, 5000]
        

        #DPS Timer
        


       # self.attackText2 = attackText(1, False)
       # self.attackText3 = attackText(1, False)
        

    
    

    def setup(self):
        # Set the background color
        
        arcade.set_background_color(arcade.color.DARK_BLUE)
        #### CONFIGURING ALL UPGRADE BUTTONS, MAY NOT NEED SPECIFIC VARIABLES IN THE FUTURE --> SEE IN NOTES BELOW ####
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
            self.upgradeButtons[i].center_x = 200
            self.upgradeButtons[i].center_y = 591 - i * 37
            
            
        print(self.upgradeButton1.width)

        self.coinText = arcade.draw_text("Coins: " + str(self.coins), 395, 700, arcade.color.BLACK, 20)
        self.coinText.bold = True

    
  


      

        
        
        
    
    

    def on_draw(self):
        arcade.start_render()
        self.enemy.draw()
        self.hpbar.draw()
        #print(self.coinText.text)
        self.coinText.draw()
        self.coinsAdded.draw()
        self.levelWave.draw()

        

        
        
        
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
            arcade.draw_text("COST " + str(round(self.upgradeCostList[i])), 280, 585-i*37, arcade.color.BLACK, 12)
            
            
        

    
        

        #arcade.draw_rectangle_outline(650, 540, 200, 60, arcade.color.BLACK, 12, 0)
        
        #arcade.draw_rectangle_filled(650, 540, 150, 60, arcade.color.GREEN)

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            print("Left mouse button pressed at", x, y)
            ####Checks to see if player has clicked on enemy####
            if(x >= 550 and x <= 750 and y >= 250 and y <= 450):
                #Will respawn a new enemy if the attack is more than the remaining health of the enemy; this stops errors with the HP bar because the width can't go below zero
                if self.attack >= self.hp:
                    self.hp = self.baseHp
                    if self.level % 10 == 0:
                        self.hpbar = hpbar(200-self.hp/self.bossHp*200)
                    else:
                        self.hpbar = hpbar(200-self.hp/self.baseHp*200)
                    self.coins += 2
                    self.coinsAdded = arcade.draw_text("+ " + str(2), 600, 700, arcade.color.YELLOW, 20)
                    self.coinText = arcade.draw_text("Coins: " + str(self.coins), 395, 700, arcade.color.BLACK, 20)
                    
                    print("coins: " + str(self.coins))
                    self.hpbar.draw()
                    #### Wave goes up by one every time you kill an enemy, new level every 5 waves ####
                    if self.wave < 5:
                        self.wave += 1
                        #### !IMPORTANT NOTEE! I CHANGE THE TEXT IN THIS FUNCTION INSTEAD OF THE ON_DRAW FUNCTION BECAUSE I THINK IT IS LESS CPU DEMANDING AS YOU ARE NOT RUNNING IT 80 TIMES A SECOND ####
                        self.levelWave = arcade.draw_text("Level " + str(self.level) + ", Wave (" + str(self.wave) + "/5)", 545, 604, arcade.color.BLACK, 20)
                    else:
                        self.level += 1
                        if self.level % 10 == 0:
                            self.is_boss = True
                            self.bossHp = self.level/10 * 2500 * self.level/10
                            self.hp = self.bossHp
                            self.hpbar = hpbar(200-self.hp/self.bossHp*200)
                            
                        else:

                            self.wave = 1
                            
                            self.baseHp *= (1.1 + round(self.level % 5) /10 * 0.2)
                            self.hp = round(self.baseHp)
                            self.hpbar = hpbar(200-self.hp/self.baseHp*200)
                            self.levelWave = arcade.draw_text("Level " + str(self.level) + ", Wave (" + str(self.wave) + "/5)", 545, 604, arcade.color.BLACK, 20)
                            #### Error must be fixed ####
                            """def gfg():
                                print("Worked")
  
                            timer = threading.Timer(2.0, gfg)
                            timer.start()"""
                    
                #### TAKES A WAY HEALTH ON HP VARIABLE AND THE HP BAR USING A SPECIAL ALGORITHM    
                else:
                    self.hp -= self.attack
                    #### Width of HP bar is 200 pixels, therfore to workout how much of the bar is remaining, you need to convert the remaining hp as a percentage of the base hp (which will create 100 pixels of data) then multiply by 2 to get the doubled percentage and therfore the amount of pixels to fill the hp bar by
                    if self.level % 10 == 0:
                        self.hpbar = hpbar(200-self.hp/self.bossHp*200)
                    else:
                        self.hpbar = hpbar(200-self.hp/self.baseHp*200)
                    self.hpbar.draw()
                
                
                print("Hit on enemy", self.hp)

            #### This loop checks to see if the user has hit one of the upgrade buttons and if so which one, using the i operator to decipher the y co-ordinate and therfore which button
            for i in range(16):
                if x >= 160 and x <= 240 and y >= 580 - i*37 and y <= 600 - i*37:
                    #### Uses lists as an easy way to set costs and buffs ####
                    if self.coins >= self.upgradeCostList[i]:
                        self.coins -= self.upgradeCostList[i]
                        #### Fixing can't divide by zero error ####
                        if i != 0:
                            #### Algorithm creates exponential growth for the upgrades to ensure a more challenging game, exponent increases as the upgrades get higher ####
                            self.upgradeCostList[i] *= 1 + i * (0.15/i)
                        else:
                            self.upgradeCostList[i] *= 1.1
                        self.attack += self.upgradeAttackBuffList[i]

                        print("Upgrade " + str(i+1) + " Purchased", "You have " + str(self.coins) + " left", "Your attack power is " + str(self.attack))
                    else:
                        print("You do not have the funds for this sir")
                self.coinText = arcade.draw_text("Coins: " + str(round(self.coins)), 395, 700, arcade.color.BLACK, 20)
        
                
                
        



def main():
    window = MyGame()
    window.setup()

    arcade.run()


if __name__ == "__main__":
    main()