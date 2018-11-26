# Flower classification performance

Dataset: Oxford 102 classes, 8189 images



Original paper: http://www.robots.ox.ac.uk/~vgg/publications/papers/nilsback08.pdf

> >The dataset is divided into a training set, a validation set
> >and a test set. The training set and validation set each consist
> >of 10 images per class (totalling 1030 images each). The
> >test set consist of the remaining 6129 images (minimum 20
> >per class). The validation set is used to optimize the number
> >of visual words for each of the features, and the radius and
> >spacing of the SIFT features.
> >For both the validation and test sets, performance is measured
> >per class (in the same manner as for Caltech101/256),
> >i.e. the final performance is the classification averaged over
> >all classes (not over all images).

## State-of-the-art (SOTA) performance

1. Performance metrics

   - Class average classification for the overall recognition performance (M1)
   - OR over all images (M2)



   Metrics:

   - [1] first nearest neighbor classifier using $\chi^2$ as the distance function (M1)
   - [2] weighted rank, aimed at retrieval (M2)

   - 

2. Performance

| Publication                        | mean accuracy (=M1) |
| ---------------------------------- | ------------------- |
| HSV + SIFT int + SIFT bd + HOG [1] | 72.8 %              |
| CNN-SVM w/o seg [3]                | 74.7 %              |
| CNNaug-SVM w/o seg [3]             | 86.8%               |
| ONE + SVM [4]                      | 86.82%              |
|                                    |                     |





References:

[1] Nilsback, M-E. and Zisserman, A., Automated flower classification over a large number of classes
Proceedings of the Indian Conference on Computer Vision, Graphics and Image Processing (2008);  http://www.robots.ox.ac.uk/~vgg/publications/papers/nilsback08.pdf

[2] M.-E. Nilsback and A. Zisserman. A visual vocabulary for flower classification. In Proc. CVPR, volume 2, pages 1447–1454, 2006; https://www.ics.uci.edu/~welling/teaching/273ASpring09/nilsback06.pdf

[3] harif Razavian, A., Azizpour, H., Sullivan, J. and Carlsson, S., 2014. CNN features off-the-shelf: an astounding baseline for recognition. In *Proceedings of the IEEE conference on computer vision and pattern recognition workshops* (pp. 806-813).; https://www.cv-foundation.org/openaccess/content_cvpr_workshops_2014/W15/papers/Razavian_CNN_Features_Off-the-Shelf_2014_CVPR_paper.pdf

[4] Xie, L., Hong, R., Zhang, B. and Tian, Q., 2015, June. Image classification and retrieval are one. In *Proceedings of the 5th ACM on International Conference on Multimedia Retrieval* (pp. 3-10). Acm.;  http://or.nsfc.gov.cn/bitstream/00001903-5/156708/1/1000014261125.pdf