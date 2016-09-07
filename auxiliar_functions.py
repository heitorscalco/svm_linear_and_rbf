# encoding:utf-8
from liblinearutil import * #Linear
from svmutil import * # RBF
from numpy import random


class Manipulation(object):		
	'''File Manipulation'''
	def writeInFile(self, filename, vector_x, vector_y):
		f = open(filename, 'w+')
		for i in xrange(0,len(vector_x)):
			dado_str = vector_y[i] + " "
			j = 0
			for x in vector_x[i]:
				dado_str += str((j+1))+":"
				dado_str += str(x)+" "
				j += 1					
			dado_str += "\n"
			f.writelines(dado_str)		
		f.close

class Trainer(object):
	'''Training algorithms'''
	def linearTrainer(self, x, y, threads = 1, parms = ""):
		
		parameters = parms + " -n " + str(threads)
		model = train(y, x, parameters)
		p_label, p_acc, p_val = predict(y, x, model)
		ACC, MSE, SCC = evaluations(y, p_label)
		print "ACC: %s" % str(ACC)
		print "MSE: %s" % str(MSE)
		print "SCC: %s" % str(SCC)
		save_model(str(sys.argv[0])+'_linear.model', model)	
		return 

	def rbfTrainer(self, x, y, parms = ""):				
		model = svm_train(y, x, parms)
		p_label, p_acc, p_val = svm_predict(y, x, model)
		svm_save_model(str(sys.argv[0])+'_rbf.model', model)
		return 

	def info(self, x, y):
		print "Lenght of X: " + str(len(x))
		print "Lenght of Y: " + str(len(y))

class Tester(object):
	"""docstring for Tester"""
	def predict_linear(self, model_filename, x, y):
		try:
			print "\n\n\n\nTESTING WITH TESTER DATASET IN LINEAR..."
			model = load_model(model_filename)
			p_label, p_acc, p_val = predict(y, x, model)
			# print  p_acc, p_val
		except Exception, e:
			print "ERROR IN PREDICTION: " + str(e)
		return

	def predict_rbf(self, model_filename, x, y):
		try:
			print "\n\n\n\nTESTING WITH TESTER DATASET IN RBF..."
			model = svm_load_model(model_filename)
			p_label, p_acc, p_val = svm_predict(y, x, model)
		except Exception, e:
			print "ERROR IN PREDICTION: " + str(e)
		return
		
		
		


class Dataset(object):	

	def addSample(self, filename, sparse = False):
		'''
		If you are preprocessing the data for LINEAR Kernel, so use SPARSE = FALSE
		Otherwise, if you are preprocessing the data for RBF KERNEL, use SPARSE = TRUE

		'''
		dataset = []
		answers = []
		flag = 0
		f = open(filename,'r');
		for line in f.xreadlines():
			number_of_columns = line.count(',') + 1
			break

		for line in f.xreadlines():			
			new_data = {} if sparse == True else []
			data =  line.split(",", number_of_columns);
			counter = 0;
			for iterator in data:				
				if ((counter == number_of_columns-1)):
					if (iterator == "0.1;\n"):
						dataset.append(new_data)
						answers.append(1.0)
					else:
						dataset.append(new_data)
						answers.append(-1.0)
					break
				else:
					if(sparse == True):
						if int(float(iterator)) != 0:
							new_data[counter] = float(iterator)
						else: 
							pass
					else:
						new_data.append(float(iterator))
				counter = counter + 1
			del new_data
		f.close()
		return dataset, answers

	def splitWithProportion(self, dataset, answer_dataset, proportion = 0.8):
	  """Produce two new datasets, the first one containing the fraction given
	  by `proportion` of the samples."""
	  indicies = random.permutation(len(dataset))
	  separator = int(len(dataset) * proportion)

	  leftIndicies = indicies[:separator]
	  rightIndicies = indicies[separator:]

	  train_ds = []
	  train_ds_as = []
	  test_ds = []
	  test_ds_as = []

	  for x in leftIndicies:
	    train_ds.append(dataset[x])
	    train_ds_as.append(answer_dataset[x])
	  for x in rightIndicies:
	    test_ds.append(dataset[x])
	    test_ds_as.append(answer_dataset[x])
	  
	  return train_ds, train_ds_as, test_ds, test_ds_as