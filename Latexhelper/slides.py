from time import localtime

class Slide:
	"""
	Class to representate a document tex. 
	"""
	
	def __init__(self, title, author, date='{}/{}/{}'.format(tuple(localtime)[2],tuple(localtime)[1],tuple(localtime)[2]), theme="Warsaw",color_theme="dolphin":
				 self.title=title
				 self.author=author
				 self.date=date
				 self.theme=theme
				 self.color_theme=color_theme
