
class OwnLogger():

    def __init__(self):
        self.new_message = {'massage':[], 'lavel':[]}

    def log(self, message, level):
        self.new_message['massage'].append(message)
        self.new_message['lavel'].append(level)

    def show_last(self, level = "all"):
        if level == "all":
            return self.new_message['massage'][-1]    
        else:    
            i = self.new_message['level'].reverse().index(level)
            return self.new_message['massage'].reverse()[i]