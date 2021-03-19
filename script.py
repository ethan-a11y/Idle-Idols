import arcade
import math

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "IDLE IDOLS")
arcade.set_background_color(arcade.color.LIGHT_GREEN)
arcade.start_render()



#CREATE PLATFORM, PLAYER AND UPGRADE MENU
arcade.draw_rectangle_filled(650, 200, 400, 100, arcade.color.BLUE)

class enemy:
    def init(self, position_x, position_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color
    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color) 


arcade.draw_circle_filled(650, 350, 100, arcade.color.BLUE)

arcade.draw_lrtb_rectangle_filled(0, 350, 750, 0, arcade.color.LIGHT_BROWN)


arcade.finish_render()
arcade.run()

