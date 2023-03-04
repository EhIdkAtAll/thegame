import pygame, json, os

def blit_alpha(target, source, location, opacity):
        x = location[0]
        y = location[1]
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)        
        target.blit(temp, location)

class TileMap():

    def __init__(self, tile_size, tiles_file, image_file):

        self.running = True

        self.tile_size = tile_size
        self.nbr_x_tiles = 380/self.tile_size
        self.nbr_y_tiles = 220/self.tile_size

        self.tiles = {".".join(f.split(".")[:-1]):pygame.image.load(tiles_file+f) for f in os.listdir(tiles_file)}
        self.images = {".".join(f.split(".")[:-1]):pygame.image.load(image_file+f) for f in os.listdir(image_file) if f != "Mini"}

        [print("Loaded TILE:", tile) for tile in self.tiles]
        [print("Loaded IMAGE:", img) for img in self.images]
        self.tile_map = {}
        self.all_layers = {}
        self.collidables = []
        self.current_layer = None

        self.camerapos = [0,0]
        self.basecamerapos = None

        self.loaded_map = None

        self.pixelfont = pygame.font.Font("PixelFont.ttf", 15)

    def load_map(self, path):
        with open(path, 'r') as f:
            json_data = json.load(f)
        
        self.tile_map = json_data['map']
        self.all_layers = json_data['all_layers']
        self.camerapos = json_data["camera_pos"]
        self.loaded_map = path

        print("Loaded MAP:",path[6:-5])
        print()
    
    def draw_map(self, display, playerpos):
        self.collidables = []
        for layer in sorted([int(layr) for layr in self.all_layers]):
            #print(f"            LAYER {layer}")
            for tile in self.tile_map[str(layer)].values():

                if self.all_layers[str(layer)]["layerspeed"] < 1:
                    addedlayerspeedx = + (tile["pos"][0] / 2 * self.tile_size)
                    addedlayerspeedy = + (tile["pos"][1] / 2 * self.tile_size)
                elif self.all_layers[str(layer)]["layerspeed"] == 1:
                    addedlayerspeedx = 0
                    addedlayerspeedy = 0
                else:
                    addedlayerspeedx = - (tile["pos"][0] / 2 * self.tile_size)
                    addedlayerspeedy = - (tile["pos"][1] / 2 * self.tile_size)

                if self.all_layers[str(layer)]["layerspeed"] == 0:
                    x = tile["pos"][0] * self.tile_size
                    y = tile["pos"][1] * self.tile_size
                else:
                    x = (tile["pos"][0] - playerpos[0]) * self.tile_size * self.all_layers[str(layer)]["layerspeed"] + addedlayerspeedx
                    y = (tile["pos"][1] - playerpos[1]) * self.tile_size * self.all_layers[str(layer)]["layerspeed"] + addedlayerspeedy
                    
                if tile["type"] in self.tiles:
                    toblit = self.tiles[tile["type"]]
                if tile["type"] in self.images:
                    toblit = self.images[tile["type"]]

                if (-380 <= x <= 380 and -220 <= y <= 220 and tile["type"] in self.images) or (-10 <= x <= 380 and -10 <= y <= 220 and tile["type"] in self.tiles):
                    if self.current_layer == None or layer == int(self.current_layer):
                        display.blit(toblit, (x, y))
                    else:
                        if self.opacity:
                            blit_alpha(display, toblit, (x,y), 100)
                        else:
                            display.blit(toblit, (x, y))

                    if tile["layer"] == 0:
                        rect = toblit.get_rect()
                        rect.topleft = (x, y)
                        self.collidables.append(rect)                                                                       

                    #print("Layer: ",layer," | Current pos: ",[x/10,y/10], " | Tile pos: ", tile["pos"], "| Type: ", tile["type"])  
            #print("-------------------------------")
        #print('===============================')
                
    def movecamera(self, mov):
        self.camerapos[0] += mov["right"]
        self.camerapos[0] -= mov["left"]
        self.camerapos[1] -= mov["up"]
        self.camerapos[1] += mov["down"]

    def collides(self, rect):
        collisionindex = pygame.Rect.collidelist(rect, self.collidables)
        if collisionindex == -1:
            return False
        return True