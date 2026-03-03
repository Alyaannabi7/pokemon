import pygame
from urllib.request import urlopen, Request
import json
import io

class Pokemon:
    def __init__(self, name):
        self.name = name
        # api url
        self.url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        
        # json data
        self.data = self._get_data()
        
        self.hp = self.data['stats'][0]['base_stat']
        
        # face et dos 
        self.url_front = self.data['sprites']['front_default']
        self.url_back = self.data['sprites']['back_default']
        
        #On transforme ces URLs en images Pygame
        self.image_front = self._load_image(self.url_front)
        self.image_back = self._load_image(self.url_back)
        
        #rect colision 
        self.image = self.image_front
        self.rect = self.image.get_rect()

    def _get_data(self):
        #connect api 
        req = Request(self.url, headers=self.headers)
        with urlopen(req) as response:
            return json.loads(response.read())

    def _load_image(self, url):
        # taille
        req = Request(url, headers=self.headers)
        with urlopen(req) as response:
            image_str = response.read()
        image_file = io.BytesIO(image_str)
        image = pygame.image.load(image_file)
        # On redimensionne à 400x400 pixels
        return pygame.transform.scale(image, (400, 400))

    def draw(self, screen, x, y):
        self.rect.topleft = (x, y)
        screen.blit(self.image, self.rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False