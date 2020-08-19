# from attributes_and_methods.document_management_3.project.category import Category
# from attributes_and_methods.document_management_3.project.document import Document
# from attributes_and_methods.document_management_3.project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = [c for c in self.categories if c.id == category_id]
        if category:
            category[0].name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = [t for t in self.topics if t.id == topic_id]
        if topic:
            topic[0].topic = new_topic
            topic[0].storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = [d for d in self.documents if d.id == document_id]
        if document:
            document[0].file_name = new_file_name

    def delete_category(self, category_id):
        category = [c for c in self.categories if c.id == category_id]
        if category:
            self.categories.remove(category[0])

    def delete_topic(self, topic_id):
        topic = [t for t in self.topics if t.id == topic_id]
        if topic:
            self.topics.remove(topic[0])

    def delete_document(self, document_id):
        document = [d for d in self.documents if d.id == document_id]
        if document:
            self.documents.remove(document[0])

    def get_document(self, document_id):
        document = [d for d in self.documents if d.id == document_id]
        if document:
            return document[0]

    def __repr__(self):
        result = f"\n".join([d.__repr__() for d in self.documents])
        return result


# c1 = Category(1, "work")
# t1 = Topic(1, "daily tasks", "C:\\work_documents")
# Topic.edit(t1, "night tasksm", "C-tashaci")
# d1 = Document(1, 1, 1, "finilize project")
# d2 = Document.from_instance(2, c1, t1, "tashaci")
# Document.add_tag(d2, "novi tashaci")
# Document.add_tag(d2, "po novi tashaci")
# Document.remove_tag(d2, "novi tashaci")
# Document.edit(d2, "Nov")
#
# d1.add_tag("urgent")
# d1.add_tag("work")
#
# storage = Storage()
# # storage.add_category(c1)
# storage.add_topic(t1)
# storage.add_document(d1)
# storage.add_document(d2)
#
# storage.edit_category(1, "work_updated")
# # storage.edit_topic(1,  "daily tasks updated", "C:\\work_documents updated")
# storage.edit_document(1, "finilize project updated")
#



# # print(c1)
# print(t1)
# print(storage.get_document(1))
# print(storage)
