
def open_file_return_list_splitted(file):
	"""
	Open a file and split it at ","
	:param file: where the file is
	:return: a list with each items separated by ","
	"""
	initial_list = []
	initial_list = open(file,"r") # mise en forme de la liste de travail initiale
	initial_list = initial_list.read() # mise en forme de la liste de travail initiale
	list_split = initial_list.split(",") # mise en forme de la liste de travail initiale
	return list_split