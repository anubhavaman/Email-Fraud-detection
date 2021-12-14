# Email-Fraud-detection
Email fraud detection Using Classification
Fraudsters obtain sensitive information from people by pretending to be from recognized sources. In a fraud email, the sender can convince you to provide personal information under false pretenses .


It considers the detection of a fraud email as a classification problem and describes the use of machine learning algorithms to classify emails as phished or ham. 
some features were extracted from all emails in a dataset which consists of n number of phished emails and  m number of  ham emails. These features are fed into the classifiers and results are noted. Our Aim is to develop  a system  which provides higher accuracy and study the variation of features.
The dataset is collected by the Publically available sources. We will use Naïve bayes classifier to solve this problem. Naïve Bayes is a very good  machine learning algorithm applied in email filtering.


Why use Naive Bayes?

•	NB is very simple, easy to implement and fast because essentially you’re just doing a bunch of counts.
•	If the NB conditional independence assumption holds, then it will converge quicker than discriminative models like logistic regression.
•	NB needs works well even with less sample data.
•	NB is highly scalable. It scales linearly with the number of predictors and data points.
•	NB can be used for both binary and multi-class classification problems and handles continuous and discrete data 
•	NB is not sensitive to irrelevant features



Steps we are going to follow:

1.	Download spam and ham emails
2.	Unpacked each email and concatenated their subject and body (because it ia great indicator whether an email is a spam or ham.)
3.	Converted the lists to dataframes, joined the spam and ham dataframes and shuffled the resultant dataframe
4.	Split the dataframe into train and test dataframes in 80:20 ratio
5.	Train the training data using Naïve Bayes
6.	Using the trained models, predicted the email label for test dataset
