# Genetic Variant Classification (Classification)


### Objective:
---


### Methodology and Results:
---




![](code/Images/ROC_Comparison.png)

![](code/Images/FeatureImportance_RandomForest.png)



Features: 

Categorical features
	- SYMBOL – Gene name
	- CLNVC – Variant type
	- IMPACT – The impact modifier for the consequence type
Numeric features 
	- AF_TGP – Allele frequencies from the 1000 genomes project
	- CADD_PHRED – Phred-scaled ‘Deleteriousness’ score: http://cadd.gs.washington.edu/
	- LoFtool – Loss of Function tolerance score for loss of function variants: https://github.com/konradjk/loftee
	- Strand – Forward or backward DNA strand, defined as + (forward) or - (reverse)




### Data:
---

https://www.kaggle.com/kevinarvai/clinvar-conflicting



### Tools and techniques:
---




### File details:
---

- `code/`

	- `doClassification.ipynb` - main code which 
	- `modelEvalUtils.py` - 
	- `feature_importance.py` - https://towardsdatascience.com/extracting-plotting-feature-names-importance-from-scikit-learn-pipelines-eb5bfa6a31f4
	- `pipelineEDA.ipynb` - 
	- `initialEDA.ipynb` - 


- `Data/`

	- `clinvar_conflicting.csv` - 
	- `featureExplanation.txt` - 


- `SQL_Challenges/`

