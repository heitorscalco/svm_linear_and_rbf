"""
=============
PREPROCESSOR AND TRAINING SCRIPT TO SVM WITH LINEAR AND RBF KERNELS, USING LIBSVM
- THE DATA TO TRAIN RBF KERNEL ARE IN SPARSE FORMAT

-ONLY FOR PREPROCESSED FILES...
"""
import auxiliar_functions
import datetime
import sys
import commands #Command executer
# import preprocessor_functions  # IF YOU NEED PREPROCESS THE DATASET -> NOT TESTED


def main():
	
	ts_inicial = datetime.datetime.now()
	if(len(sys.argv) <= 1):
		print "***WRONG!*** Usage: python preprocessing_svm.py dataset ['rbf' or 'linear'] [num_threads]"
		return
	
	training_type = str(sys.argv[2]).upper()

	############################################################################
	# Define No. of threads
	############################################################################	
	try:
		threads = int(sys.argv[3])
	except Exception, e:
		try:
			# Read how many threads the processor have.
			comando = "cat /proc/cpuinfo | grep -m1 'cpu cores' | cut -c 13"
			threads = int(commands.getoutput(comando))
		except Exception, e:
			threads = 1		
	finally:
		print "Using %s threads..." % threads

	############################################################################
	# Preprocessing
	############################################################################
	dataset = auxiliar_functions.Dataset()
	if(training_type == 'LINEAR'):
		x, y = dataset.addSample(filename = str(sys.argv[1]), sparse = False)
	else:
		x, y = dataset.addSample(filename = str(sys.argv[1]), sparse = True)

	xtrain, ytrain, xtest, ytest = dataset.splitWithProportion(x, y, proportion = 0.8)	
	
	del dataset, x, y

	print "Lenght of Training Set: " + str(len(xtrain))
	print "Lenght of Testing Set: " + str(len(xtest))


	############################################################################
	# Save x, y into a file
	############################################################################
	# manipulation = Manipulation()
	# manipulation.writeInFile("arquivo_saida_svm", x, y)
	# del manipulation	

	trainer = auxiliar_functions.Trainer()
	trainer.info(xtrain, ytrain)
	tester = auxiliar_functions.Tester()

	if(training_type == 'LINEAR'):
		###################################
		# start the Linear training process	
		###################################
		print "\nLinear: "
		trainer.linearTrainer(	x = xtrain, 
								y = ytrain, 
								threads = threads, 
								parms = "-c 4 -q")
				
		tester.predict_linear(model_filename = str(sys.argv[0])+'_linear.model', x = xtest, y = ytest)		

	else:		
		###################################
		#start the RBF training process
		###################################
		print "\nRBF:"
		trainer.rbfTrainer(	x = xtrain, 
							y = ytrain, 
							parms = "")		
		tester.predict_rbf(model_filename = str(sys.argv[0])+'_rbf.model', x = xtest, y = ytest)		

	del trainer, tester	
	print "Duration: " + str(datetime.datetime.now()-ts_inicial)
main()



