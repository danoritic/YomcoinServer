from main import db
# import google.cloud.firestore_v1.base_document.DocumentSnapshot
from google.cloud.firestore_v1.base_document import DocumentSnapshot

doc_list:list[DocumentSnapshot] =db.collection('users').stream()






for i in doc_list:
    
    print(i)
    print(i.to_dict())
    
    print(len(i.reference.collection('my_transactions').stream()))
    

print(list(doc_list))
print(type(doc_list))

