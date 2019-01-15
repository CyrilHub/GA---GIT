class Dog:

    def __init__(self, name="", age=0):
    # Note the defaults.

      self.name = name # All dogs have a name.
      self.age = age # All dogs have an age.

    # All dogs have a bark function.
    """Prints a message stating name and age to stdout"""
    def bark_hello(self):
      print("Woof! I am called", self.name, "; I am", self.age, "human-years old.")

# Declare the objects.
gracie = Dog("Gracie", 8)
spitz = Dog("Spitz", 5)
buck = Dog("Buck", 3)

# Test them out!
gracie.bark_hello()
print("This dog's name is", gracie.name)
print("This dog's age is", gracie.age)

gracie.name = "NOT GRACIE"
print(gracie.name)
spitz.bark_hello()
buck.bark_hello()

random.name
