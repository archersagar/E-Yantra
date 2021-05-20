import pyodbc

conn = pyodbc.connect('''Driver={ODBC Driver 13 for SQL Server};
                      Server=tcp:hospital-resource-management.database.windows.net,1433;
                      Database=HospitalResourceManagement;Uid=kuchbhi;Pwd=Block17616;
                      Encrypt=yes;
                      TrustServerCertificate=no;
                      Connection Timeout=30;''')
                      

cursor = conn.cursor()

cmd = ("INSERT INTO [dbo].[{table}] VALUES({patient_id}, '{patient_name}', {patient_age}, '{patient_dob}','{patient_gender}', '{address}',"+
                                             "{criticalness},{O2_dosage},"+
                                             "{Remdesivir_dosage});").format(table='HospitalG',patient_id = 123,patient_name = 'Ramesh',patient_age = 31,patient_dob = '15-aug-90',
    patient_gender='Male',address = "#123, Second Cross, Hyd",criticalness = 2,O2_dosage = 440,Remdesivir_dosage = 2)

cursor.execute(cmd)

conn.commit()
