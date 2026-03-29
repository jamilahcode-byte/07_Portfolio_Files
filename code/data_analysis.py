import pandas as pd        # English: for handling dataframes
                          # Arabic: للتعامل مع الجداول (DataFrame)

import matplotlib.pyplot as plt  # English: for plotting basic charts
                                # Arabic: لرسم المخططات الأساسية

import seaborn as sns      # English: for nicer and advanced charts
                          # Arabic: لرسم مخططات أجمل وأكثر تقدماً

sns.set(style="whitegrid") # English: clean grid style for charts
                          # Arabic: تعيين نمط شبكة نظيف للمخططات
                          
df = pd.read_csv('cleaned_HR.csv')  
# English: load cleaned CSV into pandas DataFrame
# Arabic: تحميل ملف CSV المنظف داخل DataFrame

df.head()        
# English: show first 5 rows
# Arabic: عرض أول 5 صفوف

df.info()        
# English: show columns, types, missing values
# Arabic: عرض الأعمدة، نوع البيانات، والقيم المفقودة

df.describe()    
# English: summary statistics for numeric columns
# Arabic: عرض الإحصاءات للأعمدة الرقمية (المتوسط، الحد الأدنى، الحد الأقصى، إلخ)

# English: count number of employees per department
# Arabic: عد عدد الموظفين في كل قسم

plt.figure(figsize=(8,5))
sns.countplot(data=df, x='department', palette='coolwarm')
plt.title("Number of Employees per Department")  # English: chart title
plt.xlabel("Department")                          # English: x-axis label
plt.ylabel("Count")                               # English: y-axis label
plt.xticks(rotation=45)                           # English: rotate labels for readability
plt.show()


