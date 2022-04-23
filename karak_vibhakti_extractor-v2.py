import glob
import sys
import subprocess
from pathlib import Path
import re

given_file = sys.argv[1]

fp1 = open(given_file,'r')
morph_lines = fp1.read().split("\n") # Create a list containing all lines
fp1.close() # Close file

sentence = []
drel = []
vib = []
sentence_id = 1
drel_flag = 0
vib_flag = 0
karak = []
i = 0
kar = ''
out_hash = {}
brac_flag = 0
for morph_line in morph_lines:
	brac_flag = 0
	if(re.search('<Sentence id', morph_line)):
		sen_id = re.sub(r'<Sentence id=\'(.*)\'>', r'\1', morph_line)
		#print(sen_id)
	if(not re.search('\(\(', morph_line) and not re.search(r'\)\)', morph_line) and re.search(r'\t', morph_line)):
		sentence.append(morph_line.split("\t")[1])
	#	if(not re.search(r'PUNC', morph_line)):
	#		morph_line = re.sub(r'^.*<fs af=\'(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*)\' .*', r'\1(\7)', morph_line)
	#		vib.append(morph_line)
	if(re.search(r'drel', morph_line)):
		brac_flag = 0
		k_flag = 0
		kar = ''
		drel_flag = 1
		vib_flag = 0
		morph_line1 = morph_line
		morph_line = re.sub(r'^.*drel', 'drel', morph_line)
		morph_line = re.sub(r'>', '', morph_line)
		drel.append(morph_line)
		if(re.search(r'(PSP|NST|N_NST)', morph_lines[i+1]) and not re.search(r'drel', morph_lines[i+1]) and not re.search(r'\)\)', morph_lines[i+1]) and vib_flag == 0):
			if(re.search(r'\(\(', morph_lines[i+1]) or re.search(r'\)\)', morph_lines[i+1])):
				#k_flag = 1
				#kar += " "
				continue
			k_flag = 1
			k = morph_lines[i+1].split("\t")
			kar = k[1]
			#karak.append(k[1])
			vib_flag = 1
		if(re.search(r'\(\(', morph_lines[i+2]) or re.search(r'\)\)', morph_lines[i+2])):
			brac_flag = 1	
		elif(re.search(r'(PSP|NST|N_NST)', morph_lines[i+2]) and not re.search(r'drel', morph_lines[i+2]) and not re.search(r'\)\)', morph_lines[i+2]) and vib_flag == 0  and brac_flag == 0):
			
			k_flag = 1
			k = morph_lines[i+2].split("\t")
			kar += " " + k[1]
			#karak.append(k[1])
			#print(k[1])
		if(re.search(r'\(\(', morph_lines[i+3]) or re.search(r'\)\)', morph_lines[i+3])):
			brac_flag = 1
		elif(re.search(r'(PSP|NST|N_NST)', morph_lines[i+3]) and not re.search(r'drel', morph_lines[i+3]) and not re.search(r'\)\)', morph_lines[i+3]) and vib_flag==0  and brac_flag == 0):
			
			k_flag = 1
			k = morph_lines[i+3].split("\t")
			kar += " " + k[1]
			#karak.append(k[1])
		try:
			s = morph_lines[i+4]
			if(re.search(r'\(\(', morph_lines[i+4]) or re.search(r'\)\)', morph_lines[i+4])):
				brac_flag = 1
			elif(re.search(r'(PSP|NST|N_NST)', morph_lines[i+4]) and not re.search(r'drel', morph_lines[i+4]) and not re.search(r'\)\)', morph_lines[i+4]) and vib_flag==0  and brac_flag == 0 ):
				
				k_flag = 1
				k = morph_lines[i+4].split("\t")
				kar += " " + k[1]
			#karak.append(k[1])
		except:
			s = ''
		try:
			s = morph_lines[i+5]
			if(re.search(r'\(\(', morph_lines[i+5]) or re.search(r'\)\)', morph_lines[i+5])):	
				brac_flag = 1
			elif(re.search(r'(PSP|NST|N_NST)', morph_lines[i+5]) and not re.search(r'drel', morph_lines[i+5]) and not re.search(r'\)\)', morph_lines[i+5]) and vib_flag==0 and brac_flag == 0):
				
				k_flag = 1
				k = morph_lines[i+5].split("\t")
				kar += " " + k[1]
			#karak.append(k[1])
		except:
			s = ''
		if(k_flag == 0):
			kar += ""
			#karak.append("")
		karak.append(kar)
	if(re.search('</Sentence', morph_line)):
		final_sentence = ' '.join(sentence)
		#final_drel = ', '.join(drel)
		#final_vib = ', '.join(vib)
		for d,k in zip(drel, karak):
			d = re.sub(r"drel='(.*):.*'", r"\1" , d)
			#print(sen_id, d, k, final_sentence, sep="\t")
			if(d + "\t" + k in out_hash):
				occur = out_hash[d + "\t" + k].split("\t")[0]
				occur = int(occur) + 1
				sentid = out_hash[d + "\t" + k].split("\t")[1]
				out_hash[d + "\t" + k] = str(occur)  + "\t" + sen_id+", " + sentid + "\t" + final_sentence
			else:
				out_hash[d + "\t" + k] = str(1) + "\t" + sen_id + "\t" + final_sentence
		#print(final_drel)
		#print(final_vib)
		sentence = []
		drel = []
		vib = []
		karak = []
		sentence_id = sentence_id + 1
	i = i + 1
	brac_flag = 0

for o in out_hash:
	#print(o, out_hash[o])
	val = out_hash[o]
	vals = val.split("\t")
	print(vals[1] + "\t" + o + "\t" + vals[0] + "\t" + vals[2])
