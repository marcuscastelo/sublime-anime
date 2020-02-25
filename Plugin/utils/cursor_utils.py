def get_cursor(view):
	return view.sel()[0].begin()

def is_cursor_at_first_word(view):
	selected_lines = view.lines(view.sel()[0])
	if len(selected_lines) != 1:
		return False #Multiple or 0 lines selected 

	line = selected_lines[0]

	typed_text = view.substr(line)
	if ' ' in typed_text: 
		return False

	return True