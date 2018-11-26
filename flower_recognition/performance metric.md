NOTE: Always check if vectors are consistently normalized (either sum of all elements or sum of all squared elements is equal 1; L1 or L2)

If not: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.normalize.html

1. Accuracy metric

   Calculate for class average (NOT over all images)

   - Approach from retrieval:

     - Using only first result
     - For each class, for each test image $I$ with label $c$, returned first result image $J_1$ with label $c_1$. 
       - If $c == c_1$, then True

   - Approach from classification

     - Methods:
       - K-nearest neighbour classifier -> only first neighbour
         - https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier
       - Random forest
         - https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier
     - Using 'score' function
       - https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier.score

2. Feature engineering

   - Feature selection: https://scikit-learn.org/stable/modules/feature_selection.html
   - PCA: https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA

3. Distances when calculating similarity for retrieval

   - https://scikit-learn.org/stable/modules/classes.html#pairwise-metrics

     - Common: cosine, euclidean,

   - Inner product (aka, dot product)

     - https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.dot.html
