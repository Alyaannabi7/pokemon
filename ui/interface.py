import pygame
from pokemonchoice import Pokemon
from enemy_random import Random_Pokemon
from button import Button
from fight import Fight  # <-- import de la classe Fight

pygame.init()

#config
window_width, window_height = 1100, 700
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pokémon Battle")
font = pygame.font.Font("./ui/LuckyRookies400.ttf", 40) 


# ASSETS
bg_menu = pygame.transform.scale(pygame.image.load("./Asset/bgmenu.png"), (1100, 700))
bg_choice = pygame.transform.scale(pygame.image.load("./Asset/background.pokemon-choice.png"), (1100, 700))
bg_fight = pygame.transform.scale(pygame.image.load("./Asset/fight_image.jpg"), (1100, 700))

# buttons
button_play = Button(395, 290, "PLAY", font, bg_color=(255, 203, 5))
button_exit = Button(395, 590, "EXIT", font, bg_color=(255, 203, 5))
button_addPokemon = Button(395, 390, "ADD POKEMON", font, bg_color=(255, 203, 5))
button_pokedex = Button(395, 490, "POKEDEX", font, bg_color=(255, 203, 5))


game_state = "MENU"
selected_pokemon = None
enemy_pokemon = None
fight_manager = None
running = True

pika = Pokemon("pikachu")
evoli = Pokemon("eevee")
salameche = Pokemon("charmander")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # menu
        if game_state == "MENU":
            if button_play.is_clicked(event):
                game_state = "CHOICE"
            if button_exit.is_clicked(event):
                running = False

        # choice pokemon
        elif game_state == "CHOICE":
            for p in [pika, evoli, salameche]:
                if p.is_clicked(event):
                    selected_pokemon = p
                    selected_pokemon.image = selected_pokemon.image_back  # dos du Pokémon

                    #Pokemon random enemi
                    enemy_pokemon = Random_Pokemon()

                    # fight manager
                    fight_manager = Fight(selected_pokemon, enemy_pokemon, font)

                    game_state = "FIGHT"

        # fight event
        elif game_state == "FIGHT":
            if fight_manager:
                fight_manager.handle_event(event)

    # drawing
    if game_state == "MENU":
        screen.blit(bg_menu, (0, 0))
        button_play.draw(screen)
        button_addPokemon.draw(screen)
        button_pokedex.draw(screen)
        button_exit.draw(screen)

    elif game_state == "CHOICE":
        screen.blit(bg_choice, (0, 0))
        pika.draw(screen, 50, 200)
        evoli.draw(screen, 350, 200)
        salameche.draw(screen, 650, 200)

    elif game_state == "FIGHT":
        screen.blit(bg_fight, (0, 0))
        if fight_manager:
            fight_manager.draw(screen)

    pygame.display.update()

pygame.quit()