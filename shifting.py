import pyodbc

conn = pyodbc.connect('''Driver={ODBC Driver 13 for SQL Server};
                      Server=tcp:hospital-resource-management.database.windows.net,1433;
                      Database=HospitalResourceManagement;Uid=kuchbhi;Pwd=Block17616;
                      Encrypt=yes;
                      TrustServerCertificate=no;
                      Connection Timeout=30;''')
                      

cursor = conn.cursor()





cursor.execute('''INSERT INTO [dbo].[{table2}] SELECT * FROM [dbo].[{table1}] WHERE {attribute} = {value}
            '''.format(table1='HospitalA', table2='HospitalB' , attribute='patient_id' , value = 16753 ))

cursor.execute('''DELETE FROM [dbo].[{table1}] WHERE patient_id = {patient_id};
            '''.format(table1='HospitalA',patient_id=16753))            
conn.commit()
