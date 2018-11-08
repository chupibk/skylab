from sklearn.neighbors import NearestNeighbors, KNeighborsClassifier
import numpy as np
import cPickle
from sklearn import metrics
from sklearn.model_selection import train_test_split


def get_data_feature():
    # open file pickle
    array = []
    with open("list_of_plant.txt", "r") as list_of_plant:
        count = 0

        # label of data
        label = []

        # adding data to training
        for plant_name in list_of_plant:
            count = count + 1
            plant_name = plant_name.rstrip()
            print("loading ./feature/" + plant_name + ".pickle")
            pickle_file = open("./feature/" + plant_name + ".pickle", "rb")
            example_dict = cPickle.load(pickle_file)
            array.append(example_dict)

            # adding label
            print("adding label for" + plant_name)
            for target_list in example_dict:
                label.append(plant_name)

    # data = np.concatenate(array)
    # cPickle.dump(data, open("./allFeature.pickle", "wb"))
    with open("allLabel.txt", "wb") as allLabel:
        for item in label:
            allLabel.write(item + "\n")
    # print("number of image ", len(data))
    print("number of label ", len(label))

    print("done concatenate data to training")


print("Load feature")
all_feature = open("./allFeature.pickle", "rb")
all_feature_data = cPickle.load(all_feature)
print("loading label")
all_label = []
with open("allLabel.txt", "r") as all_Label_file:
    for i in all_Label_file:
        all_label.append(i.rstrip())
# print all_label

print("start KNN")

test_Rose = cPickle.load(open("./test.pickle", "rb"))

# X_train, X_test, y_train, y_test = train_test_split(
#     all_feature_data, all_label, test_size=0.3)
knn = KNeighbors(n_neighbors=5)
knn.fit(all_feature_data, all_label)
y_pred = knn.predict(test_Rose)
print y_pred
# print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

# X_train, X_test, y_train, y_test = train_test_split(
#     all_feature_data, all_label, test_size=0.1)
# knn = KNeighborsClassifier(n_neighbors=5)
# knn.fit(X_train,y_train)
# y_pred = knn.predict(X_test)

# # print y_pred
# print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

