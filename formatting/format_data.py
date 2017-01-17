import tokenize
import os

data_path = "../data/"

def dedup():
    texts = set()
    for filename in os.listdir(data_path):
	text = open(data_path + filename).read()
	if text not in texts:
	    texts.add(text)
        else:
	    os.delete(data_path + filename)

def format_data_file_titles():
    pass

if __name__ == "__main__":
    dedup()
    format_data_file_titles()
