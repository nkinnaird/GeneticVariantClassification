# Genetic Variant Classification (Classification)


### Objective:
---

Predict ...


<!-- US county Covid-19 deaths scaled by population using US census data in order to identify those counties which are more at risk than others. By identifying these counties, resources can be deployed more efficiently. The figure below shows the number of Covid-19 deaths scaled per 100k persons for counties in the US.
 -->

https://www.kaggle.com/kevinarvai/clinvar-conflicting


This project was developed over two and a half weeks as part of the [Metis](https://www.thisismetis.com/) data science boot-camp in Winter 2021.



### Methodology and Results:
---




![](code/Images/ROC_Comparison.png)

![](code/Images/ConfMat_RandomForest_Train.png)
![](code/Images/ConfMat_RandomForest_Test.png)

![](code/Images/FeatureImportance_RandomForest.png)



Features: 

Categorical features:
	- SYMBOL – Gene name
	- CLNVC – Variant type
	- IMPACT – The impact modifier for the consequence type

Numeric features:
	- AF_TGP – Allele frequencies from the 1000 genomes project
	- CADD_PHRED – Phred-scaled ‘Deleteriousness’ score: http://cadd.gs.washington.edu/
	- LoFtool – Loss of Function tolerance score for loss of function variants: https://github.com/konradjk/loftee
	- Strand – Forward or backward DNA strand, defined as + (forward) or - (reverse)



### Tools and techniques:
---

- Classification: kNN, DecisionTree, RandomForest
- Feature transformation, standardization, OneHotEncoding, via ColumnTransformer
- Cross validation, GridSearchCV
- Matplotlib, Seaborn for visualization


### File details:
---

- `code/`

	- `doClassification.ipynb` - main code which fits the classification models on the train and test data, outputs plots and results
	- `modelEvalUtils.py` - file which provides various plotting and metric evaluation methods
	- `feature_importance.py` - file written by Kyle Gilde which provides feature names after data has been passed through pre-processors including OneHotEncoding, see [here](https://towardsdatascience.com/extracting-plotting-feature-names-importance-from-scikit-learn-pipelines-eb5bfa6a31f4) for an explanation and link to the code
	- `pipelineEDA.ipynb` - notebook used for exploring data processing through various pipelines and sklearn modules including ColumnTransformer and GridSearchCV 
	- `initialEDA.ipynb` - notebook used for feature and data exploration 


- `Data/`

	- `clinvar_conflicting.csv` - data file for analysis
	- `featureExplanation.txt` - explanation of various features


- `SQL_Challenges/`

	- this folder contains files relating to SQL coding work which was part of the Metis project requirements, but which does not relate to the rest of the project

