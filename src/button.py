import src.print_text as prt

class Button:
    def __init__(self, width, height, inactive_color=(13, 162, 50), active_color=(23, 204, 58)):
        self.width = width
        self.height = height
        self.active_color = active_color
        self.inactive_color = inactive_color

    def draw(self, x, y, message, action=None, font_size=10, sub=None):
        mouse = prt.cfg.pygame.mouse.get_pos()
        click = prt.cfg.pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                prt.cfg.pygame.draw.rect(prt.cfg.display, (self.active_color), (x, y, self.width, self.height))

                if click[0] == 1:
                    if action is not None and sub is None:
                        action()
                    elif action is not None and sub is not None:
                        action(sub)

        else:
            prt.cfg.pygame.draw.rect(prt.cfg.display, (self.inactive_color), (x, y, self.width, self.height))
        prt.print_text(message, x + 10, y + 10, font_size=font_size)

