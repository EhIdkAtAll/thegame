import pygame, json

class Button():
	def __init__(self, x, y, image, scale = 1):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.clicked = False

	def draw(self, surface):
		self.action = False

		pos = pygame.mouse.get_pos()

		if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] and not self.clicked:
				self.clicked = True
				self.action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		surface.blit(self.image, (self.rect.x, self.rect.y))

		return self.action
	
	def act(self):
		return self.action


class Slider():
	def __init__(self, x, y, bar_image, button_image, valuetochange = None, scale = 1):
		self.x = x
		self.y = y

		self.bar_width = int(bar_image.get_width() * scale)
		self.bar_height = int(bar_image.get_height() * scale)
		self.button_width = int(button_image.get_width() * scale)
		self.button_height = int(button_image.get_height() * scale)

		self.value = 50
		self.valuetochange = valuetochange
		self.selected = False

		self.bar_image = pygame.transform.scale(bar_image, (self.bar_width, self.bar_height))
		self.button_image = pygame.transform.scale(button_image, (self.button_width, self.button_height))

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
			
			if self.valuetochange != None:
				with open("config.json", "r") as f:
					data = json.load(f)
				
				data[self.valuetochange] = self.value
				
				with open("config.json", "w") as f:
					json.dump(data, f)

		if self.selected and self.initial_center[0] - self.bar_image.get_width() / 2 + self.button_image.get_width() / 2 < pygame.mouse.get_pos()[0] < self.initial_center[0] + self.bar_image.get_width() / 2 - self.button_image.get_width() / 2:
			self.button_rect.center = (pygame.mouse.get_pos()[0], self.button_rect.center[1])
			self.value = self.button_rect.center[0] - self.initial_center[0] + 50
	
	def value(self):
		return self.value
	
		
class CheckBox():
	def __init__(self, x, y, unchecked_image, checked_image, scale = 1, valuetochange = None):
		self.x = x
		self.y = y

		self.checked = False
		self.valuetochange = valuetochange
		self.clicked = False
	
		self.unchecked_width = int(unchecked_image.get_width() * scale)
		self.unchecked_height = int(unchecked_image.get_height() * scale)
		self.checked_width = int(checked_image.get_width() * scale)
		self.checked_height = int(checked_image.get_height() * scale)

		self.unchecked_image = pygame.transform.scale(unchecked_image, (self.unchecked_width, self.unchecked_height))
		self.checked_image = pygame.transform.scale(checked_image, (self.checked_width, self.checked_height))

		self.unchecked_rect = self.unchecked_image.get_rect()
		self.checked_rect = self.checked_image.get_rect()

		self.unchecked_rect.center = (x,y)
		self.checked_rect.center = (x,y)

		self.initial_center = (x,y)

	def draw(self, surface):
		if self.checked:
			surface.blit(self.unchecked_image, (self.unchecked_rect.x, self.unchecked_rect.y))
		else:
			surface.blit(self.checked_image, (self.checked_rect.x, self.checked_rect.y))
		
		if self.unchecked_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and not self.clicked:
			self.checked = not self.checked
			self.clicked = True

			if self.valuetochange != None:
				with open("config.json", "r") as f:
					data = json.load(f)
			
				data[self.valuetochange] = self.checked
			
				with open("config.json", "w") as f:
					json.dump(data, f)

		if self.clicked and not pygame.mouse.get_pressed()[0]:
			self.clicked = False

	def ischecked(self):
		return self.checked