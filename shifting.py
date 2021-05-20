import pyodbc

conn = pyodbc.connect('''Driver={ODBC Driver 13 for SQL Server};
                      Server=tcp:hospital-resource-management.database.windows.net,1433;
                      Database=HospitalResourceManagement;Uid=kuchbhi;Pwd=Block17616;
                      Encrypt=yes;
                      TrustServerCertificate=no;
                      Connection Timeout=30;''')
                      

cursor = conn.cursor()





cursor.execute('''INSERT INTO [dbo].[{table2}] SELECT * FROM [dbo].[{table1}] WHERE {attribute} = {value}
            '''.format(table1='HospitalG', table2='HospitalH' , attribute='patient_id' , value = 123 ))

cursor.execute('''DELETE FROM [dbo].[{table1}] WHERE {attribute} = {value};
            '''.format(table1='HospitalG',attribute='patient_id',value=123))            
conn.commit()
