import pandas as pd        # English: pandas is used to handle CSV/Excel files and tables
                          # Arabic: البانداس تُستخدم للتعامل مع ملفات CSV/Excel والجداول

import numpy as np         # English: numpy is used for numeric operations and handling NaN (empty values)
                          # Arabic: النمباي تُستخدم للعمليات الحسابية ومعالجة القيم الفارغة NaN

#import matplotlib.pyplot as plt  # English: matplotlib is used to make simple charts for checking data
                                # Arabic: ماتبلوتليب تُستخدم لرسم مخططات بسيطة لمراجعة البيانات

#import seaborn as sns      # English: seaborn makes nicer charts, optional but helpful
                          # Arabic: سيبورن يجعل المخططات أجمل، اختياري لكنه مفيد

#sns.set(style="whitegrid") # English: set a clean grid style for charts
                          # Arabic: تعيين نمط شبكة نظيف للمخططات
                          
df = pd.read_csv('messy_HR_data.csv')  
# English: load the CSV file into a pandas DataFrame
# Arabic: تحميل ملف CSV داخل DataFrame باستخدام البانداس

print(f"Review rows: {df.head()}")        
# English: show the first 5 rows
# Arabic: عرض أول 5 صفوف

print(f"Information: {df.info()}")        
# English: show info about columns, types, and missing values
# Arabic: عرض معلومات عن الأعمدة، نوع البيانات، والقيم المفقودة

print(f"Description: df.describe()")   
# English: show statistics of numeric columns (mean, min, max, etc.)
# Arabic: عرض إحصاءات للأعمدة الرقمية (المتوسط، الحد الأدنى، الحد الأقصى، إلخ)


df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]  
# English: remove spaces, lowercase all names, replace spaces with underscores
# Arabic: إزالة المسافات، تحويل جميع الحروف إلى صغيرة، واستبدال المسافات بشرطات سفلية

df['name'] = df['name'].str.strip().str.title()  
# English: remove extra spaces and capitalize first letters of names
# Arabic: إزالة المسافات الزائدة وتكبير الحرف الأول من كل اسم

# Convert 'age' to numeric, invalid parsing will become NaN
df['age'] = pd.to_numeric(df['age'], errors='coerce')

# Fill missing values (NaN) with median
df['age'] = df['age'].fillna(df['age'].median())  
# English: fill empty age values with the median
# Arabic: ملء القيم الفارغة في عمود العمر بالوسيط (Median)

df['email'] = df['email'].fillna('no_email@example.com')  
# English: fill empty email cells with a default email
# Arabic: ملء الخانات الفارغة في عمود البريد الإلكتروني بقيمة افتراضية



df = df.drop_duplicates()  
# English: remove duplicate rows
# Arabic: إزالة الصفوف المكررة



df.to_csv('samples/cleaned_sample.csv', index=False)  
# English: save cleaned DataFrame as CSV
# Arabic: حفظ DataFrame المنظف كملف CSV

df.to_excel('samples/cleaned_sample.xlsx', index=False)  
# English: save cleaned DataFrame as Excel
# Arabic: حفظ DataFrame المنظف كملف Excel