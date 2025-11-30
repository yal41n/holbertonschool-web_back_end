# my comment
def list_all(mongo_collection):
    """List all documents in a collection"""
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
