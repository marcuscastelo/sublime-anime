def _get_raw_time():
	now_time = datetime.datetime.now().time()
	text = str(now_time)[0:5]
	return text

def get_time(isFirst):
	raw_time = _get_raw_time()
	return raw_time + (' - ' if isFirst else ' ')

def get_date(): 
	now = datetime.datetime.now()
	text = str(now.strftime("%d/%m/%Y"))
	return text