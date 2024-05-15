# survey_results_public
# survey_results_schema
from pandas import DataFrame,Series,read_csv,set_option

DF=read_csv('survey_results_public.csv',index_col='Respondent')
DF_R = read_csv('survey_results_schema.csv',index_col='Column')
# display.[max_categories, max_columns, max_colwidth, max_info_columns, max_info_rows, max_rows,
# HighSalary = ((DF['ConvertedComp']>7000) & (DF['Country']=='Pakistan'))
# Countries = ['Pakistan', 'India','Germany','Canada','United States']
# Filt = (DF['Country'].isin(Countries))
# print(DF['LanguageWorkedWith'])
# Filt = DF['LanguageWorkedWith'].str.contains('Python',na=False )
# help(str.contains)
# # print(DF.loc[Filt,'LanguageWorkedWith'])
print(type(DF))