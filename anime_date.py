import sublime
import sublime_plugin

from Anime.utils import get_cursor, get_date

class AnimeDateCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		text = get_date() + '\n\n'
		self.view.insert(edit, get_cursor(self.view), text)
