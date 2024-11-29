nested_json = {
   "user": {
       "id": 1,
       "details": {
           "name": "Alice",
           "contact": {
               "email": "alice@example.com",
               "phone": "123-456-7890"
           }
       }
   }
}

# { 
# 'userId':1,
# 'user.details.name':'Alice',
# 'user.details.contact.email':'alice@example.com',
# user.details.contact.phone':'123-456-7890'
# }

# print(nested_json["user"])
# print(len(nested_json["user"]))

# output_dict = {}
# for i in range(0,len(nested_json["user"])):
#     if len(nested_json["user"][i]) > 1:

# output_dict = {}
# output_dict['userId'] = nested_json["user"]["id"]
# output_dict['user.details.name'] = nested_json["user"]["details"]["name"]
# output_dict['user.details.contact.email'] = nested_json["user"]["details"]["contact"]["email"]
# output_dict['user.details.contact.phone'] = nested_json["user"]["details"]["contact"]["phone"]
# print(output_dict)

data = {
   "company": {
       "departments": [
           {
               "name": "Engineering",
               "employees": [
                   {"name": "Alice", "id": 101, "skills": ["Python", "Databricks"]},
                   {"name": "Bob", "id": 102, "skills": ["Java", "Spark"]}
               ]
           },
           {

               "name": "HR",
               "employees": [
                   {"name": "Charlie", "id": 201, "skills": ["Recruiting", "Excel"]},
                   {"name": "Dana", "id": 202, "skills": ["Communication", "Compliance"]}
               ]
           }
       ]
   }
}


# [['python','Databricks'],['java','spark']]

# output_dict = {}
for key,value in data.items():
    # print(key,value)
    # if key == "departments":
    #     print(value)
    for key,value in data["company"]:
        print(value)

