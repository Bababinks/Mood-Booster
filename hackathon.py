
import random

fun_facts = [ "Just like humans, young goats pick up accents from other goats." , "According to physics, every element on our planet was previously formed at the heart of a star: we are made of stardust." ,  "Hunting unicorns is legal in Michigan." ,  "Sea otters hold hands while sleeping to not drift apart." ,  "Bats sing love songs" , "The voice actors for Minnie and Mickey were married in real life." , "Fart Battles were popular art scrolls created in Japan during the Edo period." ,  "If you have a pizza with radius Z and thickness A, its volume is = Pi*Z*Z*A" , "Eating chocolate is good for your emotional and physical help." ,  "You can change your language on Facebook to 'Pirate'", "Manatees are also known as ‘floaty potatoes’" ,  "Shakira was rejected from the school choir because the teacher thought she sounded like a goat. And now look where she is now…" , "Benjamin Franklin wrote 'Fart Proudly', a scientific essay about farts" , "The most overdue library book was returned 288 years late" , "Cows moo in accents specific to their region, just like humans." ]

emotion = input( "How are you feeling today? (Happy, Stressed, Sad, Frustrated, Tired, Scared, Confused, Proud, Heartbroken, Anxious): ")

if emotion == "Happy":
	print()

elif emotion == "Stressed":
	print( "I’m so sorry you are feeling stressed right now :(, maybe take a 30 min break by watching Netflix or hanging out with your friends/ pets. After this break is over, take a couple deep breaths to allow your mind to refocus and get in a proper mind space to tackle your tasks for the day!" )
	response = input("Do you feel better now (Yes/No)?: ")
	while response == "No":
		print( "Here's a fun fact that will hopefully cheer you up!: " , end = '' )
		print(random.choice(fun_facts))
		response = input("Do you feel better now (Yes/No)?: " )

elif emotion == "Sad":
	print( "Oh no :( take a couple minutes to yourself and try to regroup. Being sad is okay as long as it is not for an extreme amount of time. If you need help or someone to talk to try to reach out to your friends, family, and/or school for help. I hope your sadness goes away soon!" )
	question1 = input("Have you been sad for an extreme amount of time, lost interest in hanging with friends, and/or artipcating in previously fun acitivities?: (Yes/No) ")
	if question1 == "Yes":
		print("I'm sorry you have been feeling this way, if you feel suicidal at any point please call this number 800-273-8255 ")
	response = input("Do you feel better now (Yes/No)?: ")
	while response == "No":
		print( "Here's a fun fact that will hopefully cheer you up!: " , end = '' )
		print(random.choice(fun_facts))
		response = input("Do you feel better now (Yes/No)?: " )

elif emotion == "Frustrated":
	print( "I’m sorry! 2020 has been a frustrating year for me as well. I find that giving myself some time for self-care through exercise and nutrition helps me to feel better. Some techniques such as going for a walk or making a delicious snack might help channel some of that anger (if none of these help, try screaming in a pillow)." )
	question1 = input("Did you try screaming into your pillow?: (Yes/No) ")
	while question1 == "No":
		print("Dude i'm telling you it helps sooo much, pleaseee try it! ")
		question1 = input("Well did you try it yet? (Yes/No) ")
	response = input("Do you feel better now (Yes/No)?: ")
	while response == "No":
		print( "Here's a fun fact that will hopefully cheer you up!: " , end = '' )
		print(random.choice(fun_facts))
		response = input("Do you feel better now (Yes/No)?: " )

elif emotion == "Proud":
	print( "Wow, pop off. It’s the best feeling when you know your self worth, and are proud of all that you have done. Keep the hard work up, it’s paying off already!" )
	question1 = input("Did you do something to reward yourself?: (Yes/No) ")
	if question1 == "No":
		print("In the words of the infamous Donna from the TV show “Parks and Rec”, treat yo’ self! Go out and get ice cream or something ")
	print( "Here's a fun fact to reward you!: " , end = '' )
	print(random.choice(fun_facts))

elif emotion == "Heartbroken":
	print("Even though it is okay to feel this way, don’t look at this as being a bad thing because everything happens for a reason! I know you will grow from this and find someone that truly cares about you in the future.For right now focus on self-love by reminding yourself how amazing and worthy you are. Also a pint of icecream never hurt anyone!")
	question = input("Are you heartbroken from a boyfriend/girlfriend? ")
	if question == "Yes":
		print("Here is a website to help get you back on track ;) - https://tinder.com/?lang=en")
	response = input("Do you feel better now (Yes/No)?: ")
	while response == "No":
		print("Here's a fun fact that will hopefully cheer you up!: ", end='')
		print(random.choice(fun_facts))
		response = input("Do you feel better now (Yes/No)?: ")

elif emotion == "Anxious":
	print("I’m sorry you feel that way. The conditions surrounding us, especially now in the heat of a pandemic and presidential race, are extremely anxiety provoking. My recommendation is to remind yourself that everything will be okay, and to confide in your loved ones if you feel you need assistance. Keep your head up, you got this!")
	question2 = input("Have you gone outside today yet (Yes/No)? ")
	if question2 == "No":
		print("Studies show that spending time in nature can help relieve stress and anxiety, improve your mood, and boost feelings of happiness and wellbeing. Try taking a walk outside for at least 10 minutes today!")
		response = input("Do you feel better now (Yes/No)?: ")
	while response == "No":
		print("Here's a fun fact that will hopefully cheer you up!: ", end='')
		print(random.choice(fun_facts))
		response = input("Do you feel better now (Yes/No)?: ")

elif emotion == "Confused":
	print("Thats rough! Being confused is the worse, especailly if you can not receive help. Don't stress, take a step back and evaluate all your resources such as google or even school databases. If you still are confused, talk to a friend or trusted adult to help you surpass your obstacle! ")
	question2 = input("Have you gone outside today yet or taken a break from your problem (Yes/No)? ")
	if question2 == "No":
		print("Studies show that spending time in nature can help relieve stress and anxiety, improve your mood, and boost feelings of happiness and wellbeing. Try taking a walk outside for at least 10 minutes today!")
		response = input("Do you feel better now (Yes/No)?: ")
	while response == "No":
		print("Here's a fun fact that will hopefully cheer you up!: ", end='')
		print(random.choice(fun_facts))
		response = input("Do you feel better now (Yes/No)?: ")

elif emotion == "Scared":
	question2 = input("Why are you scared?: ")
	print("Many times, situations seem intimidating but are in reality much more navigable than they appear to be. Remember to stay cool, calm and collected, and you will be able to push through any situation you may face, no matter how daunting")
	response = input("Do you feel better now (Yes/No)?: ")
	while response == "No":
		print("Here's a fun fact that will hopefully cheer you up!: ", end='')
		print(random.choice(fun_facts))
		response = input("Do you feel better now (Yes/No)?: ")

elif emotion == "Tired":
	print("I’m exhausted too, life can be draining. Remember that naps, every now and again, are very healthy and you need proper sleep and down time to function! Go take care of yourself today, catch up on that beauty rest. Go take a nap or get some caffeine in ya! " )
	question2 = input("Did you take a nap (Yes/No)? ")
	if question2 == "No":
		print("Sleep is very important! You are gonna need your energy to beat any obstacles you encounter. Remember you are powerful when you are energized! ")
	response = input("Do you feel better now (Yes/No)?: ")
	while response == "No":
		print("Here's a fun fact that will hopefully cheer you up!: ", end='')
		print(random.choice(fun_facts))
		response = input("Do you feel better now (Yes/No)?: ")



print("Yayy, I'm glad you are feeling good, pass the good vibez to everyone <3 ")