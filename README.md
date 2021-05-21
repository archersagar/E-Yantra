# Hospital Resource Management

We have created a database management system at the hospital level for keeping track of SOS resources and rate of consumption. 
If the consumption is high the hospital admin is notified, so that there is enough time to source extra supplies.
In case of severe issues, the influx of patients can be shifted to a partner vacant hospital. 

## Code snippet to enter patient details into the database through HTMl website

```python
cmd = ("INSERT INTO [dbo].[{table}] VALUES({patient_id}, '{patient_name}', {patient_age}, '{patient_dob}','{patient_gender}', '{address}',"+ "{criticalness},{O2_dosage},"+"{Remdesivir_dosage});").format(table='HospitalG',patient_id = 123,patient_name = 'Ramesh',patient_age = 31,patient_dob = '15-aug-90', patient_gender='Male',address = "#123, Second Cross, Hyd",criticalness = 2,O2_dosage = 440,Remdesivir_dosage = 2)
```




