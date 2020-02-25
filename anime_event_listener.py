import sublime
import sublime_plugin

from Anime.utils import is_cursor_at_first_word, list_all_anime, is_anime

completions = []
def update_animes(view):
	global completions
	animes = list_all_anime(view)

	completions = [[a,a+':'] for a in animes]

class AnimeEventListener(sublime_plugin.EventListener):

	def on_load_async(self, view):
		if is_anime(view):
			update_animes(view)

	def on_post_save_async(self, view):
		if is_anime(view):
			update_animes(view)

	def on_query_completions(self, view, prefix, locations):
		if not is_anime(view):
			return []

		selections = view.sel()
		if len(selections) != 1: 
			return []

		return (completions, sublime.INHIBIT_WORD_COMPLETIONS |
            sublime.INHIBIT_EXPLICIT_COMPLETIONS)
