# Import the Firebase service
from logging import exception
import firebase_admin
from firebase_admin import credentials, db

class Collection():

    def __init__(self, api_path, firebase_url, collection_name, unique_key):
        """
        To perform CRUD operations with Firebase App.
        @params api_path: Firebase AUTH API file path.
        @params firebase_url: Firebase URL for the database. 
        @params collection_name: Collection name in which CRUD operations needs to be done.
        @params unique_key: Collection must have one unique key by using that key all the operations will be done.
        """
        try:
            if api_path is not None:
                certificate = credentials.Certificate(api_path)
            else:
                raise Exception("Firebase API Key path value is missing")
            if firebase_url is None or '':
                raise Exception("URL for firebase database is must and invalid")
            self.firebaseApp = firebase_admin.initialize_app(certificate, {'databaseURL': firebase_url})
            if collection_name is None or '':
                raise Exception("collection_name should not be None or empty")
            self.collection = db.reference(collection_name)
            if unique_key is None or '':
                unique_key = 'id'
                raise Warning("UniqueKey provided is invalid. Will use 'id' as unique key")
            self.key = unique_key
        except:
            raise exception

    def __getSnapshot(self):
        """ Private method, It can access within class object 
        To get snapshot of collection """
        return self.collection.get()
    
    def __findItem(self, unique_value):
        """
        To find the item 
        @params unique_key: Key defined at init
        """
        snapshot = self.__getSnapshot()
        if snapshot == None:
            return False
        item = None
        for key, val in snapshot.items():
            if val[self.key] == unique_value:
                item = key
                break
        if(item != None):
            node = self.collection.child(item)
            return node
        else:
            return False

    def insert(self, value):
        """ 
        To insert/add new items into collection 
        @params value: Value is an JSON-serializable/dict object and it must contains unique_key and value
        @returns: boolean
        """
        if self.key in value:
            if not self.__findItem(value[self.key]):
                self.collection.push(value)
                return True
            else:
                raise Exception("Item already exists with same unique value")
        else:
            raise Exception("Key {0} not found".format(self.key))

    def getAllValues(self):
        """
        To get the entire items as list
        @returns: list of object
        """
        snapshot = self.__getSnapshot()
        if snapshot == None:
            return []
        items = []
        for key, val in snapshot.items():
            items.append(val)
        return items

    def getValue(self, unique_key):
        """
        To get the item as dict which matches the unique_key
        @returns: dict or None
        """
        items = self.getAllValues()
        return next((item for item in items if item[self.key] == unique_key), None)

    def deleteAll(self):
        """
        To delete all the items in the collection
        @returns: boolean
        """
        self.collection.delete()
        return True

    def update(self, unique_key, content):
        """ 
        To update existing item in the collection
        @returns: boolean 
        """
        itemMatchedNode = self.__findItem(unique_key)
        if(itemMatchedNode == False):
            raise Exception("Item doesn't exists")
        itemMatchedNode.set(content)
        return True

    def delete(self, unique_key):
        """
        To delete item from the list 
        @returns: boolean 
        """
        itemMatchedNode = self.__findItem(unique_key)
        if(itemMatchedNode == False):
            raise Exception("Item doesn't exists")
        itemMatchedNode.delete()
        return True

