class BrowserHistory(ContainerBase):

    def __init__(self):
        super().__init__()

    def visit(self, url):
        new_node = self.Node(url)
        if self.first is None:
            self.first = new_node
            self.current = new_node
            return
        if self.current.next is not None:
            self.current.next = None
        new_node.prev = self.current
        self.current.next = new_node
        self.current = new_node

    def back(self):
        if self.current is None or self.current.prev is None:
            return False
        self.current = self.current.prev
        return True

    def forward(self):
        if self.current is None or self.current.next is None:
            return False
        self.current = self.current.next
        return True

    def contains(self, url):
        temp = self.first
        while temp is not None:
            if temp.url == url:
                return True
            temp = temp.next
        return False

    @property
    def current_url(self):
        if self.current is None:
            return None
        return self.current.url

    @property
    def size(self):
        count = 0
        temp = self.first
        while temp is not None:
            count += 1
            temp = temp.next
        return count
