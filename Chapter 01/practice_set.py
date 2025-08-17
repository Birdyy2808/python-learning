import pyttsx3
import os

# Question 1 -> Print twinkle twinle poem

print(''' 
      Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the trav'ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

'Tis your bright and tiny spark,
Lights the trav'ller in the dark:
Tho' I know not what you are,
Twinkle, twinkle, little star. ''')

# Question 2 -> Use repel to print 5 table
# Done

# Question 3 -> Use external module
# pip install pyttsx3
voice = pyttsx3.speak("Hello Vaibhav")

# Question 4 -> use os module to show the content of the file
dir = "C:\\Users\\Vaibhav Singh\\Documents\\python-zero-to-hero\\Chapter 1"

for file in os.listdir(dir):
    print(file)
    
