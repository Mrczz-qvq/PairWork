
import pygame

class TextBox:
    def __init__(self, w, h, x, y, font=None):
        self.width = w
        self.height = h
        self.x = x
        self.y = y
        self.text = ""  # 文本框内容

        if font is None:
            self.font = pygame.font.Font(None, 32)  # 使用pygame自带字体
        else:
            self.font = font

    def draw(self, dest_surf):
        text_surf = self.font.render(self.text, True, (0, 0, 0))
        dest_surf.blit(text_surf, (self.x, self.y + (self.height - text_surf.get_height())),
                       (0, 0, self.width, self.height))

    def key_down(self, event):

        unicode = event.unicode
        key = event.key

        if key == 8:
            self.text = self.text[:-1]

            return

        if key == 301:

            return

        if key == 13:
            print("回车测试")
            print(self.text)

            return
        if unicode != "":
            char = unicode
        else:
            char = chr(key)
        self.text += char

    def get_text(self):
        return self.text

    def clear(self):
        self.text = ''

