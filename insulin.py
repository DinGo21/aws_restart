def seqClean(infile, outfile):
	for line in infile:
		if line.strip() == "//":
			break
		outfile.write(''.join([c for c in line.strip() if c.isalpha()]))

def	InsulinSeq():
	with open("insulin-seq/preproinsulin-seq.txt", 'r') as preproInsulinSeq:
		preproInsulinSeq.readline()
		with open("insulin-seq/preproinsulin-seq-clean.txt", 'w') as preproInsulinSeqClean:
			seqClean(preproInsulinSeq, preproInsulinSeqClean)
	with open("insulin-seq/preproinsulin-seq-clean.txt", 'r') as preproInsulinSeqClean:
		line = preproInsulinSeqClean.readline()
		with open("insulin-seq/lsinsulin-seq-clean.txt", 'w') as lsInsulinSeqClean:
			lsInsulinSeqClean.write(line[0:24])
		with open("insulin-seq/binsulin-seq-clean.txt", 'w') as binInsulinSeqClean:
			binInsulinSeqClean.write(line[24:54])
		with open("insulin-seq/cinsulin-seq-clean.txt", 'w') as cinInsulinSeqClean:
			cinInsulinSeqClean.write(line[54:89])
		with open("insulin-seq/ainsulin-seq-clean.txt", 'w') as ainInsulinSeqClean:
			ainInsulinSeqClean.write(line[89:110])

InsulinSeq()
