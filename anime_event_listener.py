import sublime
import sublime_plugin

import re

from Anime.utils import *

anime_completions = []
friend_completions = []
flag_completions = []
def update_animes(view):
	global anime_completions
	animes = list_all_anime(view)

	anime_completions = [[a,a+':\n\n'] for a in animes]

def update_friends(view):
	global friend_completions
	friends = list_all_friends(view)

	friend_completions = [[f,f] for f in friends]

def update_flag_completions(view):
	global flag_completions
	flag_completions = [[f,f] for f in [
		"REWATCH",
		"REWATCH?",
		"NOT-ANIME",
		"NOT-IN-MAL",
		"SCRIPT-DANGER",
		"勉強",
		"MANGA"
	]]

def is_in_friend_curly_brackets(view):
	typed_so_far = get_text_from_start_to_cursor(view)
	return None != re.match(r'^(?:(?!\})[^{\n])*\{(?:(?!\})[^{\n])*$', typed_so_far)

def is_in_flag_brackets(view):
	typed_so_far = get_text_from_start_to_cursor(view)
	return None != re.match(r'^(?:(?!\])[^[\n])*\[(?:(?!\])[^[\n])*$', typed_so_far)

def update_completions(view):
	if is_anime_list(view):
		update_animes(view)
		update_friends(view)
		update_flag_completions(view)
		
def goto_eof(view):
	size = view.size()
	r = sublime.Region(size)
	view.show(r)
	view.sel().clear()
	view.sel().add(r)


class AnimeEventListener(sublime_plugin.EventListener):
	def on_load_async(self, view):
		if is_anime_list(view):
			goto_eof(view)
			update_completions(view)

	def on_post_save_async(self, view):
		update_completions(view)
		
		
		

	def on_query_completions(self, view, prefix, locations):
		print(anime_completions)

		if not is_anime_list(view):
			return []
		selections = view.sel()
		if len(selections) != 1: 
			return []

		# Friends
		if is_in_friend_curly_brackets(view):
			return (friend_completions, sublime.INHIBIT_WORD_COMPLETIONS |
            sublime.INHIBIT_EXPLICIT_COMPLETIONS)

		if is_in_flag_brackets(view):
			return (flag_completions, sublime.INHIBIT_WORD_COMPLETIONS |
            sublime.INHIBIT_EXPLICIT_COMPLETIONS)

		# Anime titles
		return (anime_completions, sublime.INHIBIT_WORD_COMPLETIONS |
            sublime.INHIBIT_EXPLICIT_COMPLETIONS)

