import pygame, json

class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False

		pos = pygame.mouse.get_pos()

		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] and not self.clicked:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action


class Slider():
	def __init__(self, x, y, bar_image="assets/bar_image.png", button_image="assets/button_image.png", scale=1):
		self.x = x
		self.y = y

		self.scale = scale
		self.value = 50
		self.selected = False

		self.bar_image = pygame.transform.scale(bar_image, (int(113 * scale), int(19 * scale)))
		self.button_image = pygame.transform.scale(button_image, (int(18 * scale), int(16 * scale)))

		self.bar_rect = self.bar_image.get_rect()
		self.button_rect = self.button_image.get_rect()
		self.bar_rect.center = (x,y)
		self.button_rect.center = (x,y)
		self.initial_center = (x,y)

	
	def draw(self, surface):
		surface.blit(self.bar_image, (self.bar_rect.x, self.bar_rect.y))
		surface.blit(self.button_image, (self.button_rect.x, self.button_rect.y))

		if self.button_rect.collidepoint(pygame.mouse.get_pos()) and not self.selected and pygame.mouse.get_pressed()[0]:
			self.selected = True
		
		if self.selected and (not self.bar_rect.collidepoint(pygame.mouse.get_pos()) or not pygame.mouse.get_pressed()[0]):
			self.selected = False
			
			with open("config.json", "r") as f:
				data = json.load(f)
			
			data["soundlevel"] = self.value
			
			with open("config.json", "w") as f:
				json.dump(data, f)

		if self.selected and self.initial_center[0] - self.bar_image.get_width() / 2 + self.button_image.get_width() / 2 < pygame.mouse.get_pos()[0] < self.initial_center[0] + self.bar_image.get_width() / 2 - self.button_image.get_width() / 2:
			self.button_rect.center = (pygame.mouse.get_pos()[0], self.button_rect.center[1])
			self.value = self.button_rect.center[0] - self.initial_center[0] + 50
	
		



