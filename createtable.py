import pyodbc

conn = pyodbc.connect('''Driver={ODBC Driver 13 for SQL Server};
                      Server=tcp:hospital-resource-management.database.windows.net,1433;
                      Database=HospitalResourceManagement;Uid=kuchbhi;Pwd=Block17616;
                      Encrypt=yes;
                      TrustServerCertificate=no;
                      Connection Timeout=30;''')
                      

cursor = conn.cursor()

cursor.execute('''CREATE TABLE {tablename}(
                    Patient_id INT,
                    Patient_name VARCHAR(20),
                    Patient_gender VARCHAR(10),
                    Patient_age INT,
                    Patient_dob DATE,
                    address VARCHAR(50),
                    critical_level INT,
                    multiplier INT,
                    O2_dosage INT,
                    Remdesivir_dosage INT);
            '''.format(tablename='HospitalB'))
conn.commit()
