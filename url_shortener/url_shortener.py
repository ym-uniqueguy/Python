import pyshorteners as ps

class Main():
    def __init__(self):
        try:
            # Create a variable to store link provided as user input
            self.url = input("Kindly input the url to be shortened: ")
            
            # Shorten the link stored in the variable above
            self.shortened_url = ps.Shortener().tinyurl.short(self.url)
            
            # Display the shortened url
            print(self.shortened_url)
            
            # Allows the user to view the shortened link
            # Program ends automatically once user presses enter key
            input("\nPress enter to exit...")

        except:
            print("""\nUnexpected error occurred! Kindly check if url is correct
and that it is not already shortened!""")
            input("\nPress enter to exit...")

if __name__ == "__main__":
    obj = Main()
