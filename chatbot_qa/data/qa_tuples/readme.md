import cPickle

qa_list = cPickle.load(open('path_to_pickle.pickle', 'rb'))

questions, answers = zip(*qa_list)
