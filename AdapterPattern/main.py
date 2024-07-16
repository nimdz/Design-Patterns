# main.py

# Target interface
class Target:
    def request(self) -> str:
        pass

# Adaptee class with a different interface
class Adaptee:
    def specific_request(self) -> str:
        return "Adaptee's specific request"

# Adapter class that makes Adaptee compatible with Target
class Adapter(Target):
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee

    def request(self) -> str:
        # Translating the request to the Adaptee's specific request
        return self.adaptee.specific_request()

# Client code
def client_code(target: Target):
    print(target.request())

# Using the Adapter pattern
if __name__ == "__main__":
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    client_code(adapter)
