class Restaurant(object):
    bankrupt=False
    def open_branch(self):
        if not self.bankrupt:
            print("branch opened")

    x=Restaurant()
    x.bankrupt
    False

    y=Restaurant()
    y.bankrupt=True
    y.bankrupt
    True

    x.bankrupt
    False

    class Restaurant(object):
        bankrupt = False
        def open_branch(this):
            if not this.bankrupt:
                print("branch opened")
