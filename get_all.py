import os
import argparse
import time

def parse_cmdline_args():

	parser = argparse.ArgumentParser(description='Run tests')
	parser.add_argument('--dicti', dest='dict',default=None,help='dictionary file')
	args = parser.parse_args()

	return args

def main (args):
	dict = args.dict;
	dict_list = os.listdir(dict);
	j = 0;
	while j != len(dict_list):
		if dict_list[j][-3:] != 'txt':
			del dict_list[j];
		else:
			j += 1;
	print dict_list;
 	time.sleep(4);
	f = open("this_all.txt","a+");
	for i in dict_list:
		t = open(dict + i,"r");
		read = t.read();
		read = str_replace(read," ","");
		t.close();
		t.open(dict +i, "w+");
		t.write(read);
		t.close();
		f.write(read);

def str_replace(string,target,replace,reset=None,reset_count=1):
        string = string + target;
        temp = '';
        temp_count = 0;
        count = 0;
        for i in range(len(string)):
                if string[i:i+len(target)] == target and count < reset_count:
                        temp = temp + string[temp_count:i] + replace;
                        temp_count = i+len(target);
                        if not reset:
                                pass;
                        else:
                                count = count + 1;
                elif string[i:i+len(target)] == target:
			count = 0 ;
	string = temp[:len(temp) - len(replace)];
	return string

	
if __name__ == '__main__':
    args = parse_cmdline_args()
    result = main(args)
