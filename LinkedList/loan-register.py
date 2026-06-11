class LoanRegister(ContainerBase):

    def __init__(self):
        super().__init__()
        self._penalties_collected = 0

    def append_loan(self, loan):
        new_node = self.Node(loan)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

    def attend_return(self):
        if self.first is None:
            return None
        loan = self.first.loan
        self._penalties_collected += loan.days_overdue * 2
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return loan

    @property
    def penalties_collected(self):
        return self._penalties_collected

    def separate_overdue(self):
        overdue_register = LoanRegister()
        current = self.first
        self.first = None
        self.last = None
        while current is not None:
            next_node = current.next
            current.next = None
            if current.loan.days_overdue > 0:
                overdue_register.append_loan(current.loan)
            else:
                if self.first is None:
                    self.first = current
                    self.last = current
                else:
                    self.last.next = current
                    self.last = current
            current = next_node
        return overdue_register
