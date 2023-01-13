from godot import exposed, export
from godot import *


@exposed
class Icon(Sprite):

	# member variables here, example:
	a = export(int)
	b = export(str, default='foo')

	def _ready(self):
		print(help(export))
		
		pass
	
