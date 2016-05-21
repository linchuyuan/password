import os
import argparse
import time

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
	j = 0;
	while j != len(dict_list):
		if dict_list[j][-3:] != 'txt':
			del dict_list[j];
		else:
			j += 1;
	print dict_list;
 	time.sleep(4);
	for i in dict_list:
		print "Starting %s \n" %(i);
		os.system("aircrack-ng -w %s %s |grep -i \"KEY FOUND\" > /root/found" % (dict+i,cap));
		print "Not found in %s\n" % (i);
	
if __name__ == '__main__':
    args = parse_cmdline_args()
    result = main(args)
