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
    
    
    
def makeMetricPlots(pipeline, inputX, inputY, model_name, testDataBool=False):

    # plot ROC curve
#     roc = metrics.plot_roc_curve(pipeline, inputX, inputY, name=model_name)


    fpr, tpr, thresholds = metrics.roc_curve(inputY, pipeline.predict_proba(inputX)[:,1])
    
#     auc_score = metrics.roc_auc_score(inputY, pipeline.predict_proba(inputX)[:,1])
    auc_score = metrics.auc(fpr, tpr)
    
    # plot the roc curve for the model
    plt.plot([0,1], [0,1], linestyle='--', label='No Skill')
    plt.plot(fpr, tpr, label='{0} AUC : {1:.3f}'.format(model_name, auc_score))
    
    if not testDataBool:
        # calculate the g-mean for each threshold
        gmeans = np.sqrt(tpr * (1-fpr))
        # locate the index of the largest g-mean
        ix = np.argmax(gmeans)
        print('Best Threshold=%f, G-Mean=%.3f' % (thresholds[ix], gmeans[ix]))
        plt.scatter(fpr[ix], tpr[ix], marker='o', color='black', label='Best')
    
    # axis labels
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.legend()


    # plot precision and recall curves against threshold
    precision_curve, recall_curve, threshold_curve = metrics.precision_recall_curve(inputY, pipeline.predict_proba(inputX)[:,1] )

    plt.figure(dpi=80)
    plt.plot(threshold_curve, precision_curve[1:],label='precision')
    plt.plot(threshold_curve, recall_curve[1:], label='recall')
    
    if not testDataBool:
#         plt.scatter(thresholds[ix], precision_curve[ix+1], marker='o', color='black', label='Best')
        plt.axvline(x=thresholds[ix], color='k', linestyle='--', label='chosen threshold')
    
    
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
    

