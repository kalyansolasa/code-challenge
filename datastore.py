from gcloud import datastore
import os
import time


class Datastore(object):
    def __init__(self):
        self.client = self.create_client(os.environ['PROJECTID'])

    def create_client(self, project_id):
        return datastore.Client(project_id)

    def add_user(self, user_data):
        key = self.client.key(self.dataset)

        user = datastore.Entity(key)

        user.update(user_data)

        client.put(user)
        return user.key

    def list_users(self, dataset, filters=[]):
        print(filters)
        qry = self.client.query(kind=dataset, filters=filters)
        return list(qry.fetch())

