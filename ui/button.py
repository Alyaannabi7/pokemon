import pygame


class Button:
    # Taille fixe pour tous tes boutons
    WIDTH = 300
    HEIGHT = 80

    def __init__(self, x: int, y: int, text: str, font, bg_color=(255, 255, 255)):
        # On utilise WIDTH et HEIGHT ici
        self.rect = pygame.Rect(x, y, self.WIDTH, self.HEIGHT)
        self.text = text
        self.font = font
        self.bg_color = bg_color # On stocke la couleur choisie

    def draw(self, surface):
        # On dessine avec la couleur stockée et les bords arrondis
        pygame.draw.rect(surface, self.bg_color, self.rect, border_radius=15)

        if self.text:
            # Texte noir (0,0,0) pour contraster avec le fond
            text_surface = self.font.render(self.text, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=self.rect.center)
            surface.blit(text_surface, text_rect)

    def is_clicked(self, event) -> bool:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False