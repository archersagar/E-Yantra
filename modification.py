import pyodbc

conn = pyodbc.connect('''Driver={ODBC Driver 13 for SQL Server};
                      Server=tcp:hospital-resource-management.database.windows.net,1433;
                      Database=HospitalResourceManagement;Uid=kuchbhi;Pwd=Block17616;
                      Encrypt=yes;
                      TrustServerCertificate=no;
                      Connection Timeout=30;''')
                      

cursor = conn.cursor()



cursor.execute('''UPDATE [dbo].[{table}] SET {attribute} = {value} WHERE patient_id = {patient_id};
            '''.format(table='HospitalA',attribute = 'patient_age', value=25, patient_id = 16753 ))
conn.commit()
