import os
import argparse

def parse_cmdline_args():

	parser = argparse.ArgumentParser(description='Run tests')
	parser.add_argument('--dictionary', dest='dict',default=None,help='dictionary file')
	parser.add_argument('--capture', dest='cap',default=None,help='capture file')
	args = parser.parse_args()

	return args

def main (args):
	dict = args.dict;
	cap = args.cap;
	dict_list = os.listdir(dict);
	for i in dict_list:
		os.system("aircrack-ng -w %s %s" % (dict+i,cap));
	
if __name__ == '__main__':
    args = parse_cmdline_args()
    result = main(args)
