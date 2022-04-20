class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.ipp = items_per_page
      
    def item_count(self):
        return len(self.collection)
  

    def page_count(self):
        return int(len(self.collection)/self.ipp)+1
    

    def page_item_count(self,page_index):
        if page_index+1 > self.page_count() or page_index < 0:
            return -1
        else:
            if page_index < (len(self.collection)/self.ipp)-1:
                return self.ipp
            elif page_index < 0:
                return -1
            else:
                return len(self.collection) % self.ipp
  

    def page_index(self,item_index):
        if item_index+1 > len(self.collection) or item_index < 0:
            return -1
        else:
            return int(item_index/self.ipp)