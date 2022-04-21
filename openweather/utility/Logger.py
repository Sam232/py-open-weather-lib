
class Logger:
    def report(self, action, datetime, message):
        print("{} - {}: {}\n", datetime, action, message)
