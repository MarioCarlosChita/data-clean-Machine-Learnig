import pandas as pd;
data = pd.read_csv("dataset/loan_data.csv");


#limpeza e transformacao dos dados

# Categorical Values
data['Gender'].fillna(data['Gender'].mode()[0] ,inplace = True);
data['Married'].fillna(data['Married'].mode()[0],inplace = True);
data['Dependents'].fillna(data['Dependents'].mode()[0] ,inplace=True);
data['Self_Employed'].fillna(data['Self_Employed'].mode()[0] ,inplace = True);
data['Credit_History'].fillna(data['Credit_History'].mode()[0], inplace=True);

# # Numerical Values
data['LoanAmount'].fillna(data['LoanAmount'].mean() , inplace =True);
data['Loan_Amount_Term'].fillna(data['Loan_Amount_Term'].mean(), inplace=True);

# Converting categories to numbers
data['Gender']  = data['Gender'].map({'Male':0 ,'Female':1});
data['Married'] = data['Married'].map({'No':0 , 'Yes':1});
data['Education'] =data['Education'].map({'Graduate':1 ,'Not Graduate':0});
data['Dependents' ] = data['Dependents'].map({'0':0,'1':1,'3+':3});
data['Self_Employed'] =data['Self_Employed'].map({'No':0 , 'Yes':1});
data['Property_Area'] = data['Property_Area'].map({'Rural':0 ,'Semiurban':1 ,'Urban':2});
data['Loan_Status'] =  data['Loan_Status'].map({'N':0 ,'Y':1});


#Bringing all the variables in range 0  to 1  using normalize
# x =  (x - xmenor) / (xmaior - xmenor);

# data['Dependents'] = (data['Dependents']-data['Dependents'].min()) / (data['Dependents'].max()- data['Dependents'].min());

for i  in data.columns[1:] :
    data[i] =  (data[i] - data[i].min()) / (data[i].max()- data[i].min());


print(data.head().to_string());

data.to_csv('dataset/load_data_new.csv');







