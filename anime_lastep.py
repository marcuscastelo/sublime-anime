import sublime
import sublime_plugin

from Anime.utils import *

def get_next_ep(ep_str):
	new_episode_str = str(1 + int(ep_str))
	if len(new_episode_str) <= 1:
		new_episode_str = '0' + new_episode_str
	return new_episode_str


class AnimeLastEpCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# Current watching anime
		current_anime_title = find_closest_anime_title(self.view)

		# Current line
		line_walker = LineFinder(self.view)
		while True:

			ep_str = find_last_episode(self.view, line_walker)
			last_ep_anime_title = find_closest_anime_title(self.view, line_walker)
			print('\n=====\n')
			print(current_anime_title)
			print(ep_str)
			print(last_ep_anime_title)

			if ep_str == None:
				self.view.insert(edit, get_cursor(self.view), 'ERROR: NOT FOUND')
				break

			if last_ep_anime_title != current_anime_title:
				line_walker.rewind()
			else:
				self.view.insert(edit, get_cursor(self.view), get_next_ep(ep_str))
				break


	

		
