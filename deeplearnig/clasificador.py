# Import the modules
from sklearn.externals import joblib
from sklearn import datasets
from skimage.feature import hog
from sklearn.svm import LinearSVC
import numpy as np
from collections import Counter

print "cargando los datos"
dataset = datasets.fetch_mldata("MNIST Original")
print "extrayendo los datos"
features = np.array(dataset.data, 'int16') 
labels = np.array(dataset.target, 'int')

print "extrayendo el hog"
list_hog_fd = []
for feature in features:
    fd = hog(feature.reshape((28, 28)), orientations=9, pixels_per_cell=(14, 14), cells_per_block=(1, 1), visualise=False)
    list_hog_fd.append(fd)
hog_features = np.array(list_hog_fd, 'float64')

print "Count of digits in dataset", Counter(labels)

print "creando el modelo smv lineal"
clf = LinearSVC()

print "asignando las etiquetas"
clf.fit(hog_features, labels)

print "escribiendo el archivo"
joblib.dump(clf, "digits_cls.pkl", compress=3)