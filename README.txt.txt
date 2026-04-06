Binary Classification - Wisconsin Diagnostic Breast Cancer (WDBC)

Project Overview:
This project focuses on building and evaluating binary classification models to predict breast cancer diagnosis (malignant or benign) using the Wisconsin Diagnostic Breast Cancer (WDBC) dataset. The primary goal is to practice building and evaluating a classification model using one of the provided datasets.

Dataset:
The dataset used is the Wisconsin Diagnostic Breast Cancer (WDBC) dataset, which contains 32 datapoints with 30 being features captured by the WDBC studies. The target variable is the 'diagnosis', indicating whether the mass is malignant (M) or benign (B) in one of the datapoints.

Key Dataset Attributes
 -   ID number
 -   Diagnosis (M = malignant, B = benign): Mapped to 1 and 0 respectively.
 -   30 Features: Features including radius, texture, perimeter, area, smoothness, compactness, concavity, concave points, symmetry, and fractal dimension. For each of these ten features, the mean, SE, and "worst" are captured.

Summary:
1. Data Mounting and Initial Inspection:
 -   The 'data.csv' file was loaded into a pandas DataFrame.
 -   Initial data cleaning checks confirmed no missing values (except for an Unnamed, column 32) and no duplicate id values.
 -   The 'id' and 'Unnamed': 32 columns were removed to clean the dataset.
 -   The 'diagnosis' column was mapped to numerical (1/0) for model training.

2. Exploratory Data Analysis (EDA:
 -   Histograms: Overlapping grouped bar charts were used to visualize the distribution of each feature against the diagnosis. This revealed strong correlations between larger mean values (radius, perimeter, area, compactness, concavity, concave points) and malignant diagnoses.
 -   Correlation Heatmaps: Heatmaps were generated for three groups of features: 'mean', 'se', and 'worst'. These visualizations reinforced the findings from the histograms, showing high inter-correlation among certain feature groups and their relationship with the target variable(diagnosis).

3. Model Training - Baseline Logistic Regression:
 -   Data Split: The dataset was split into an 80:20 training and testing set (random_state=42).
 -   Feature Selection: Initial features for the model were selected based on EDA insights: ['radius_mean','perimeter_mean','area_mean','compactness_mean','concave points_mean'].
 -   Model: A Logistic Regression model was chosen as the initial model used for the classification task, suitable for interpretable linear relationships.
 -   Performance:
    -   Precision: 0.974
    -   Accuracy: 0.939
    -   Recall: 0.860
    -   F1-Score: 0.914
    -   AUC: 0.923
    -   Confusion Matrix: [[70, 1], [6, 37]] (6 false negatives)
 -   Interpretation: The Logistic Regression model showed an overall good performance, but the recall (86%) indicated a notable number of false negatives, which is a critical concern in a medical context.

4. Model Improvement - Hyperparameter Tuning:

A. Hyper tuned Logistic Regression:
 -    - -Technique: - - GridSearchCV was used to tune hyperparameters for the Logistic Regression model.
 -    - -Best Parameters: - - The optimized model used C=1438.45.
 -    - -Performance: - -
     -   Precision: 0.905
     -   Accuracy: 0.921
     -   Recall: 0.884
     -   F1-Score: 0.894
     -   AUC: 0.914
     -   Confusion Matrix: [[67, 4], [5, 38]] (5 false negatives)
 -   Interpretation: Tuning improved recall (reducing false negatives from 6 to 5) but slightly decreased in precision and accuracy. This indicated a trade-off with improved recall being beneficial for reducing total false negatives.

B. Random Forest Classification (Alternative Model)
 -   Model: A Random Forest Classifier was introduced to handle non-linear relationships and provide feature importance.
 -   Best Parameters: max_depth=None, max_features='sqrt', min_samples_leaf=4, min_samples_split=2, n_estimators=1000.
 -   Performance:
     -   Precision: 0.860
     -   Accuracy: 0.894
     -   Recall: 0.860
     -   F1-Score: 0.860
     -   AUC: 0.888
     -   Confusion Matrix: [[65, 6], [63, 37]] (6 false negatives)
 -    Interpretation: The Random Forest model achieved the similar recall and the below performance with the logistic Regression models, making it the underwhelming choice for a medical classification task in comparison.

Conclusion

The comprehensive comparison of the models highlights that the hyper tuned Logistic Regression offered high precision and accuracy. This the most effective for this breast cancer diagnosis task. Its superior recall (0.884) and lowest number of false negatives (5) are critical in a medical context, where missing a malignant diagnosis can have severe consequences for accessing treatment. This outcome demonstrates the importance of considering specific performance metrics based on the real-world implications of the classification.
