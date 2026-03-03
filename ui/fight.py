import pygame
from button import Button

class Fight:
    def __init__(self, player_pokemon, enemy_pokemon, font):
        self.player = player_pokemon
        self.enemy = enemy_pokemon
        self.font = font

        # pv
        self.player_current_hp = self.player.hp
        self.enemy_current_hp = self.enemy.hp

        # button
        self.button_fight = Button(400, 600, "FIGHT", font, bg_color=(255, 255, 255))
        self.button_potion = Button(700, 600, "USE POTION", font, bg_color=(255, 255, 255))

        # health bar
        self.bar_width = 300
        self.bar_height = 25

    def draw_health_bar(self, screen, x, y, current_hp, max_hp, color=(0, 255, 0)):
        # Fond gris
        pygame.draw.rect(screen, (128, 128, 128), (x, y, self.bar_width, self.bar_height))
        # pv proportionnels
        hp_width = int((current_hp / max_hp) * self.bar_width)
        pygame.draw.rect(screen, color, (x, y, hp_width, self.bar_height))
        #text pv
        hp_text = self.font.render(f"{current_hp}/{max_hp} HP", True, (255, 255, 255))
        screen.blit(hp_text, (x + 5, y - 30))

    def handle_event(self, event):
        #buton fight ans potion
        if self.button_fight.is_clicked(event):
            self.attack()
        if self.button_potion.is_clicked(event):
            self.use_potion()

    def attack(self):
        # Dégâts aléatoires entre 10 et 30
        import random
        damage = random.randint(10, 30)
        self.enemy_current_hp -= damage
        if self.enemy_current_hp < 0:
            self.enemy_current_hp = 0

    def use_potion(self):
        #20pv potion
        heal = 20
        self.player_current_hp += heal
        if self.player_current_hp > self.player.hp:
            self.player_current_hp = self.player.hp

    def draw(self, screen):

        if self.player:
            self.player.draw(screen, 50, 350)

        if self.enemy:
            self.enemy.draw(screen, 650, 50)

        if self.player:
            self.draw_health_bar(screen, 50, 320, self.player_current_hp, self.player.hp)
        if self.enemy:
            self.draw_health_bar(screen, 650, 20, self.enemy_current_hp, self.enemy.hp, color=(255, 0, 0))
        
        #button fight et potion
        self.button_fight.draw(screen)
        self.button_potion.draw(screen)