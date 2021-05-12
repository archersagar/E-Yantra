import pyodbc

conn = pyodbc.connect('''Driver={ODBC Driver 13 for SQL Server};
                      Server=tcp:hospital-resource-management.database.windows.net,1433;
                      Database=HospitalResourceManagement;Uid=kuchbhi;Pwd=Block17616;
                      Encrypt=yes;
                      TrustServerCertificate=no;
                      Connection Timeout=30;''')
                      

cursor = conn.cursor()

cmd = ("INSERT INTO [dbo].[{table}] VALUES({patient_id}, '{patient_name}','{patient_gender}' {patient_age}, '{patient_dob}', '{address}',"+
                                             "{criticalness}, {multiplier},{O2_dosage},"+
                                             "{Remdesivir_dosage});").format(table='HospitalA', patient_id = 35,patient_name = 'aaa', patient_gender="male", patient_age = 75,patient_dob = '03-jul-88',
    address = "abcd,efgh,hyd,telangana",criticalness = 5,multiplier = 1,O2_dosage = 1,Remdesivir_dosage = 0)

cursor.execute(cmd)

conn.commit()


