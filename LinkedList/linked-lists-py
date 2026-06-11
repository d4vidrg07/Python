class TaskList(BaseContainer):

    def __init__(self):
        super().__init__()
        self._time_spent = 0

    def add_task(self, task):
        new_node = self.Nodo(task)
        if self.first is None:
            self.first = new_node
        else:
            current = self.first
            while current.next is not None:
                current = current.next
            current.next = new_node

    def get_task(self, position):
        current = self.first
        index = 0
        while current is not None:
            if index == position:
                return current.task
            index += 1
            current = current.next
        return None

    def task_completed(self, position):
        if self.first is None:
            return None
        if position == 0:
            task = self.first.task
            self.first = self.first.next
            self._time_spent += task.duration
            return task
        current = self.first
        index = 0
        while current.next is not None:
            if index + 1 == position:
                task = current.next.task
                current.next = current.next.next
                self._time_spent += task.duration
                return task
            index += 1
            current = current.next
        return None

    @property
    def time_left(self):
        total = 0
        current = self.first
        while current is not None:
            total += current.task.duration
            current = current.next
        return total

    @property
    def time_spent(self):
        return self._time_spent
