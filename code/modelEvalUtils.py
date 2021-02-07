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
    
    
    
def makeMetricPlots(pipeline, inputX, inputY, model_name):

    # plot ROC curve
    roc = metrics.plot_roc_curve(pipeline, inputX, inputY, name=model_name)

    # plot precision and recall curves against threshold
    precision_curve, recall_curve, threshold_curve = metrics.precision_recall_curve(inputY, pipeline.predict_proba(inputX)[:,1] )

    plt.figure(dpi=80)
    plt.plot(threshold_curve, precision_curve[1:],label='precision')
    plt.plot(threshold_curve, recall_curve[1:], label='recall')
    plt.legend(loc='lower left')
    plt.xlabel('Threshold (above this probability, label as conflicting)');
    plt.title('Precision and Recall Curves');
    plt.show()
    
    
    # plot precision curve vs recall curve (I think for threshold of 0.5 but I'm not entirely sure)
#     prec_vs_rec = metrics.plot_precision_recall_curve(pipeline, inputX, inputY, name=model_name)
    

# from https://towardsdatascience.com/fine-tuning-a-classifier-in-scikit-learn-66e048c21e65
def adjusted_classes(y_probs, threshold):
    """
    This function adjusts class predictions based on the prediction threshold (t).
    Will only work for binary classification problems.
    """
    return [1 if y_prob > threshold else 0 for y_prob in y_probs]    
    

