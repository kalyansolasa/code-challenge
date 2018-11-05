import requests

k = reuests.get('http://127.0.0.1:5000/listusers')
print(k.json())
''' 
it will return all records as json response
[{'company': 'PwC',
  'line_of_service': 'consulting',
  'last_name': 'majji',
  'id': 'emp1',
  'first_name': 'ram',
  'territory': 'australia'},
 {'first_name': 'kalyan',
  'territory': 'india',
  'company': 'PwC',
  'line_of_service': 'assurance',
  'last_name': 'solasa',
  'id': 'emp2'},
 {'id': 'emp3',
  'first_name': 'manoj',
  'territory': 'australia',
  'company': 'PwC',
  'line_of_service': 'tax',
  'last_name': 'nimala'}]
'''

k = reuests.get('http://127.0.0.1:5000/listusers?territory=india')
print(k.json())
'''
response:
    [{'company': 'PwC',
  'line_of_service': 'assurance',
  'last_name': 'solasa',
  'id': 'emp2',
  'first_name': 'kalyan',
  'territory': 'india'}]
'''

k = reuests.get('http://127.0.0.1:5000/listusers?line_of_service=assurance')
print(k.json())
'''
response:
[{'id': 'emp2',
  'first_name': 'kalyan',
  'territory': 'india',
  'company': 'PwC',
  'line_of_service': 'assurance',
  'last_name': 'solasa'}]

'''

k = requests.get('http://127.0.0.1:5000/listusers?id=emp2,emp3')
'''
reponse:
    [{'territory': 'india',
  'company': 'PwC',
  'line_of_service': 'assurance',
  'last_name': 'solasa',
  'id': 'emp2',
  'first_name': 'kalyan'},
 {'id': 'emp3',
  'first_name': 'manoj',
  'territory': 'australia',
  'company': 'PwC',
  'line_of_service': 'tax',
  'last_name': 'nimala'}]
  '''


