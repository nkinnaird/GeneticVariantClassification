from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

plt.rcParams['figure.figsize'] = (9, 6)
sns.set(context='notebook', style='whitegrid', font_scale=1.2)

def printMetricsAndConfMat(y_train, y_pred, modelAbrev):

    print(metrics.classification_report(y_train, y_pred))

    conf_mat = metrics.confusion_matrix(y_train, y_pred)
    
    plt.figure()
    
    sns.heatmap(conf_mat, cmap=plt.cm.Blues, annot=True, square=True, fmt='d',
               xticklabels=['non-conflicting', 'conflicting']);
    
    plt.yticks(np.array([0.25, 1.35]),('non-conflicting','conflicting'))

    plt.xlabel('Predicted Target')
    plt.ylabel('Actual Target')
    plt.title(modelAbrev + " Confusion Matrix");
    plt.show();
    
    
    
def makeMetricPlots(pipeline, inputX, inputY, model_name, inputThreshold, testData=False):
    
    # plot ROC curve
    # roc = metrics.plot_roc_curve(pipeline, inputX, inputY, name=model_name)
    # replaced with the code below

    fpr, tpr, thresholds = metrics.roc_curve(inputY, pipeline.predict_proba(inputX)[:,1])
    
    auc_score = metrics.auc(fpr, tpr)
    
    plt.figure(dpi=80)

    # plot the roc curve for the model
    plt.plot([0,1], [0,1], linestyle='--', label='No Skill')
    plt.plot(fpr, tpr, label='{0} AUC : {1:.2f}'.format(model_name, auc_score))
    
    best_roc_threshold = 0.5 # set this value so it doesn't complain when I run on the test data, for which the best threshold will have already been set
    if not testData:
        # calculate the g-mean for each threshold
        gmeans = np.sqrt(tpr * (1-fpr))
        # locate the index of the largest g-mean
        ix = np.argmax(gmeans)
        best_roc_threshold = thresholds[ix]
        print('Best ROC Threshold=%f' % (best_roc_threshold))
        plt.scatter(fpr[ix], tpr[ix], marker='o', color='black', label='Best ROC Threshold: {0:.2f}'.format(best_roc_threshold))
        
        iClosest = (np.abs(thresholds - inputThreshold)).argmin()
        plt.scatter(fpr[iClosest], tpr[iClosest], marker='o', color='blue', label='Chosen Threshold: {0:.2f}'.format(inputThreshold))
    
    # axis labels
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve for Train Data');
    if testData: plt.title('ROC Curve for Test Data');
    plt.legend()
    plt.show()


    # plot precision and recall curves against threshold (but only for non-test data)
    if not testData:

        precision_curve, recall_curve, threshold_curve = metrics.precision_recall_curve(inputY, pipeline.predict_proba(inputX)[:,1] )

        plt.figure(dpi=80)
        plt.plot(threshold_curve, precision_curve[1:],label='precision')
        plt.plot(threshold_curve, recall_curve[1:], label='recall')

        plt.axvline(x=inputThreshold, color='k', linestyle='--', label='chosen threshold')

        plt.legend(loc='lower left')
        plt.xlabel('Threshold (above this probability, label as conflicting)');
        plt.title('Precision and Recall Curves for Train Data');
        plt.show()
    
    
    # plot precision curve vs recall curve (I think for threshold of 0.5 but I'm not entirely sure) 
    # replaced with the above code 
    # prec_vs_rec = metrics.plot_precision_recall_curve(pipeline, inputX, inputY, name=model_name)
    
    return best_roc_threshold, (fpr, tpr)
    
# from https://towardsdatascience.com/fine-tuning-a-classifier-in-scikit-learn-66e048c21e65
def adjusted_classes(y_probs, threshold):
    """
    This function adjusts class predictions based on the prediction threshold (t).
    Will only work for binary classification problems.
    """
    return [1 if y_prob > threshold else 0 for y_prob in y_probs]    



def makeCombinedROC(tuples, model_names):
    
    plt.figure(dpi=80)
    plt.plot([0,1], [0,1], linestyle='--', label='No Skill')

    
    for i, data in enumerate(tuples):
        
        auc_score = metrics.auc(data[0], data[1])
        plt.plot(data[0], data[1], label='{0} AUC : {1:.2f}'.format(model_names[i], auc_score))
    
    
    # axis labels
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curves for Test Data');
    plt.legend()
    plt.show()