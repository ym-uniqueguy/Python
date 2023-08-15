import pyttsx3

class Main():
    # Define the init constructor
    def __init__(self):
        try:
        
            # Open file to read text from
            f = open("text.txt", "r")

            # Store read text from file in a variable
            text_to_read = f.read()

            # This line is for testing purpose
            print(text_to_read)

            # Create object
            speech = pyttsx3.init()

            # Get current voice
            voices = speech.getProperty("voices")

            # Set voice, index 0 is for male, 1 for female
            speech.setProperty("voice", voices[1].id)

            # Read the text
            speech.say(text_to_read)

            # Save the read to audio file
            speech.save_to_file(text_to_read, 'demo.mp3')

            # Run and wait for the speech to text to finish
            speech.runAndWait()

            # Close the file
            f.close()

        except:
            print("""\nUnexpected error occurred! Please check
selected file(s) exist!""")
            input("\nPress enter to exit...")
                
if __name__ == "__main__":
    obj = Main()
