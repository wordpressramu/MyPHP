import pandas as pd
#data = pd.read_csv("filename.csv")

#https://www.ibm.com/support/knowledgecenter/SS9SMM/com.ibm.commerce.commerce-workbench.admin.doc/refs/rcw_web_catalog.htm
#https://www.datacamp.com/community/tutorials/joining-dataframes-pandas
#https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
#http://www.datasciencemadesimple.com/join-merge-data-frames-pandas-python/

'''
CATALOG.csv
CATALOGDSC.csv
CATGROUP.csv
CATGRPDESC.csv
CATTOGRP.csv
CATGRPREL.csv
STORECGRP.csv
CATENTRY.csv
CATENTDESC.csv
CATGPENREL.csv
CATENTREL.csv
STORECENT.csv
CATENTRYATTR.csv
FACET.csv
ATTRVALDESC.csv
PARTNUMBERMAPPING.csv
SEOCATGROUP.csv
SEOCATENTRY.csv
OFFERPRICE.csv
'''

#Category
'''
CATGROUP.csv
CATGRPDESC.csv
CATTOGRP.csv
CATGRPREL.csv
SEOCATGROUP.csv
CATGPCALCD.csv

CATENTRY.csv
CATENTDESC.csv
CATGPENREL.csv
CATENTRYATTR.csv
SEOCATENTRY.csv
'''

CATGROUP_column_headeers = ["categoryId", "categoryName", "markForDelete"]
CATGROUP_df = pd.read_csv("input_data/CATGROUP.csv", names=CATGROUP_column_headeers)

categories_names_df = CATGROUP_df[['categoryId','categoryName']].copy()
categories_names_dict = categories_names_df.set_index('categoryId').T.to_dict('records')[0]
print(categories_names_dict)

CATGRPDESC_column_headeers = ["categoryLanague", "categoryId", "categoryDisplayName","categoryThumbnail"]
CATGRPDESC_df = pd.read_csv("input_data/CATGRPDESC.csv", names=CATGRPDESC_column_headeers)
#CATGRPDESC_df = CATGRPDESC_df[CATGRPDESC_df['categoryLanague'].isin(a)]
CATGRPDESC_df.drop( CATGRPDESC_df[ CATGRPDESC_df['categoryLanague'] != -1 ].index , inplace=True)
CATGRPDESC_df.drop(["categoryThumbnail"], axis=1, inplace=True) 

#merge two columns
categories = pd.merge(CATGROUP_df, CATGRPDESC_df, on='categoryId')
categories.to_csv('categories.csv')



#CATGRPREL
CATGRPREL_column_headeers = ["categoryIdParent", "categoryIdChild", "catalogId","childCategorySequence"]
CATGRPREL_df = pd.read_csv("input_data/CATGRPREL.csv", names=CATGRPREL_column_headeers)
CATGRPREL_df.drop(["catalogId"], axis=1, inplace=True)
CATGRPREL_df.drop_duplicates(keep='first',inplace=True) 
CATGRPREL_df = CATGRPREL_df.replace({"categoryIdParent":categories_names_dict})
print("CATGRPREL_df")
print(CATGRPREL_df.head())



#Rel
#pd.merge(df1, df2, on='Customer_id', how='left')
categories_rel_df = pd.merge(categories, CATGRPREL_df, left_on='categoryId', right_on='categoryIdChild',how='left')
categories_rel_df.drop(["categoryIdChild"], axis=1, inplace=True)
categories_rel_df.to_csv('categories_rel.csv')
print(categories_rel_df.head())
