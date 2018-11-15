import cPickle

qa_list = cPickle.load(open('path_to_pickle.pickle', 'rb'))

questions, answers = zip(*qa_list)


# Numbers of QA
5.pickle: 239
3.pickle: 111
1.pickle: 441

