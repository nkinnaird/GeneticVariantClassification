from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['figure.figsize'] = (9, 6)
sns.set(context='notebook', style='whitegrid', font_scale=1.2)

def printMetricsAndConfMat(y_train, y_pred, modelAbrev):

    print(metrics.classification_report(y_train, y_pred))

    conf_mat = metrics.confusion_matrix(y_train, y_pred)
    
    plt.figure()
    
    sns.heatmap(conf_mat, cmap=plt.cm.Blues, annot=True, square=True, fmt='d',
               xticklabels=['non-conflicting', 'conflicting'],
               yticklabels=['non-conflicting', 'conflicting']);
    
    plt.xlabel('prediction')
    plt.ylabel('actual')
    plt.title(modelAbrev + " Conf Mat");
    plt.show();
