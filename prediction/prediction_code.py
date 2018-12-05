import pandas as pd
pd.options.mode.chained_assignment = None
import plotly
import plotly.graph_objs as go
from django.contrib.staticfiles.templatetags.staticfiles import static

data1 = pd.read_excel(r'/Users/apurva/Google Drive/Visual Analytics/Project/Prediction/mysite/prediction/static/prediction/numeric_cleaned.xls')

def plot1(form_data):
    data2 = data1[(data1['PropertyCity'] == int(form_data['city']))
    & (data1['Veteran'] == int(form_data['veteran']))
    &( data1['EstimatedCreditScore'] == int(form_data['credit_score']))
    &( data1['BankruptcyForeClosureCheck'] == int(form_data['bankfore']))
    &( data1['PropertyUse'] == int(form_data['property']))]
    data2 = data2[(data2['EstimatedPropertyValue'].between(int(form_data['prop_value'])-5000, int(form_data['prop_value'])+5000, inclusive=True))
    & (data2['LoanAmountRequested'].between(int(form_data['loan_amt'])-5000, int(form_data['loan_amt'])+5000, inclusive=True))
    & (data2['AdditionalCashRequired'].between(int(form_data['cash'])-5000, int(form_data['cash'])+5000, inclusive=True))]
    labels = data2['LenderId'].unique()
    sizes = [ data2['LenderId'][(data2['LenderId'] == i)].count() for i in data2['LenderId'].unique()]
    trace = go.Pie(labels=labels, values=sizes)
    return plotly.offline.plot([trace], validate=False, output_type='div')

def plot2(form_data):
    data2 = data1[(data1['PropertyCity'] == int(form_data['city']))
    & (data1['Veteran'] == int(form_data['veteran']))
    &( data1['EstimatedCreditScore'] == int(form_data['credit_score']))
    &( data1['BankruptcyForeClosureCheck'] == int(form_data['bankfore']))
    &( data1['PropertyUse'] == int(form_data['property']))]
    data2 = data2[(data2['EstimatedPropertyValue'].between(int(form_data['prop_value'])-5000, int(form_data['prop_value'])+5000, inclusive=True))
    & (data2['LoanAmountRequested'].between(int(form_data['loan_amt'])-5000, int(form_data['loan_amt'])+5000, inclusive=True))
    & (data2['AdditionalCashRequired'].between(int(form_data['cash'])-5000, int(form_data['cash'])+5000, inclusive=True))]
    pd.to_numeric(data2['APRPercentage'])
    data2['APRPercentage'] = data2['APRPercentage'].mask(data2['APRPercentage'].between(3.5,4), 1)
    data2['APRPercentage'] = data2['APRPercentage'].mask(data2['APRPercentage'].between(4,4.5), 2)
    data2['APRPercentage'] = data2['APRPercentage'].mask(data2['APRPercentage'].between(4.5,5), 3)
    data2['APRPercentage'] = data2['APRPercentage'].mask(data2['APRPercentage'].between(5,5.5), 4)
    data2['APRPercentage'] = data2['APRPercentage'].mask(data2['APRPercentage'].between(5.5,6), 5)
    data2['APRPercentage'] = data2['APRPercentage'].mask(data2['APRPercentage'].between(6,6.5), 6)
    data2['APRPercentage'] = data2['APRPercentage'].mask(data2['APRPercentage'].between(6.5,7), 7)
    a = {i:data2['APRPercentage'][(data2['APRPercentage'] == i)].count() for i in data2['APRPercentage'].unique()}
    a = dict(sorted(a.items()))
    x1 = a.keys()
    y1 = a.values()
    trace = go.Bar(x=list(x1), y=list(y1))
    return plotly.offline.plot([trace], validate=False, output_type='div')

def plot3(form_data):
    data2 = data1[(data1['PropertyCity'] == int(form_data['city']))
    & (data1['Veteran'] == int(form_data['veteran']))
    &( data1['EstimatedCreditScore'] == int(form_data['credit_score']))
    &( data1['BankruptcyForeClosureCheck'] == int(form_data['bankfore']))
    &( data1['PropertyUse'] == int(form_data['property']))]
    data2 = data2[(data2['EstimatedPropertyValue'].between(int(form_data['prop_value'])-5000, int(form_data['prop_value'])+5000, inclusive=True))
    & (data2['LoanAmountRequested'].between(int(form_data['loan_amt'])-5000, int(form_data['loan_amt'])+5000, inclusive=True))
    & (data2['AdditionalCashRequired'].between(int(form_data['cash'])-5000, int(form_data['cash'])+5000, inclusive=True))]
    labels = data2['AmortizationType'].unique()
    sizes = [ data2['AmortizationType'][(data2['AmortizationType'] == i)].count() for i in data2['AmortizationType'].unique()]
    trace = go.Pie(labels=labels, values=sizes)
    return plotly.offline.plot([trace], validate=False, output_type='div')

def plot4(form_data):
    data2 = data1[(data1['PropertyCity'] == int(form_data['city']))
    & (data1['Veteran'] == int(form_data['veteran']))
    &( data1['EstimatedCreditScore'] == int(form_data['credit_score']))
    &( data1['BankruptcyForeClosureCheck'] == int(form_data['bankfore']))
    &( data1['PropertyUse'] == int(form_data['property']))]
    data2 = data2[(data2['EstimatedPropertyValue'].between(int(form_data['prop_value'])-5000, int(form_data['prop_value'])+5000, inclusive=True))
    & (data2['LoanAmountRequested'].between(int(form_data['loan_amt'])-5000, int(form_data['loan_amt'])+5000, inclusive=True))
    & (data2['AdditionalCashRequired'].between(int(form_data['cash'])-5000, int(form_data['cash'])+5000, inclusive=True))]
    labels = ['IsFHALoan','IsJumboLoan','IsVALoan']
    sizes = [ data2['IsFHALoan'][(data2[i] == True)].count() for i in labels]
    trace = go.Pie(labels=labels, values=sizes)
    return plotly.offline.plot([trace], validate=False, output_type='div')

def plot5(form_data):
    data2 = data1[(data1['PropertyCity'] == int(form_data['city']))
    & (data1['Veteran'] == int(form_data['veteran']))
    &( data1['EstimatedCreditScore'] == int(form_data['credit_score']))
    &( data1['BankruptcyForeClosureCheck'] == int(form_data['bankfore']))
    &( data1['PropertyUse'] == int(form_data['property']))]
    data2 = data2[(data2['EstimatedPropertyValue'].between(int(form_data['prop_value'])-5000, int(form_data['prop_value'])+5000, inclusive=True))
    & (data2['LoanAmountRequested'].between(int(form_data['loan_amt'])-5000, int(form_data['loan_amt'])+5000, inclusive=True))
    & (data2['AdditionalCashRequired'].between(int(form_data['cash'])-5000, int(form_data['cash'])+5000, inclusive=True))]
    labels = ['IsBestOffer','NotBestOffer']
    sizes = [ data2['IsBestOffer'][(data2['IsBestOffer'] == True)].count(), data2['IsBestOffer'][(data2['IsBestOffer'] == False)].count()]
    trace = go.Pie(labels=labels, values=sizes)
    return plotly.offline.plot([trace], validate=False, output_type='div')
