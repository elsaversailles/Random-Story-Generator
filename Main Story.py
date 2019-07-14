#Simple randomstory generator, the randomplace variable was wrongly added
#Elsa Versailles

import random

print ('Hello Reader!')
print ('|')
readername = input("What is your name? ")


print ('|')
print ("Hello " + readername + "!")

names = [" Zara", " Aisha", " Taktus", " Satchi", " Emheareane", " Stephanie", " Fhranzyne", " Jhaylen", " Mia", " Olivia", " Amelia"," Anna",  " Emily", " Ava", " Lily", " Sophia", " Isabel"," Grace", " Poppy", " Vera" ]

names2 = [" Oliver", " Harry",  " Jack ", "Noah", " Charlie", " Jacob", " Alfie", " Freddie", " Oscar", " Leo", " Logan", " Archie", " Theo", " Thomas", "James", "Joshua", " Henry", " William", " Max" ]

places = ["Castle", "House", "Tunnel", "Train Station", "Store"]

quest = ["seek the holy grail", "return the ring", "slay the dragon"]

roles = ["knight", "amazon warrior", "driver", "cashier", "biker", "programmer" ]

planet = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Uranus", "Neptune", "Pluto"]

randomname2 = random.choice(names2)
randomname = random.choice(names)
randomplace = random.choice(places)
randomrole = random.choice(roles)
randomquest = random.choice(quest)
randomplanet = random.choice(planet)

#Story section
#Original disabled
stoy = "Once upon a time there was a " + randomrole + " called " + randomname + " and then " + randomname2 + " foodie " +    randomquest + "."


#test story 3

#story1 to story10 was renamed

s1 = "The story:  " + randomname + " looked at the crumpled hawk in her hands and felt stable."
s2 = "She walked over to the window and reflected on her industrial surroundings. She had always loved dirty " + randomplace + " with its icy, important igloos. It was a place that encouraged her tendency to feel stable."
s3 = "Then she saw something in the distance, or rather someone. It was the figure of " + randomname2 + ". " + randomname2 + " was a down to earth wally with handsome eyes and tall warts." + randomname +  " gulped. She glanced at her own reflection. She was a spiteful, violent, whiskey drinker with greasy eyes and beautiful warts. Her friends saw her as a lively, low lawyer. Once, she had even helped a crooked baby cross the road."

s4 = "But not even a spiteful person who had once helped a crooked baby cross the road, was prepared for what" +randomname2 + " had in store today. The drizzle rained like gyrating humming birds,making Helen worried"

s5 = "As " + randomname + "  stepped outside and " + randomname2 + "  came closer, she could see the crooked glint in his eye."

s6 = ' "I am here because I want a phone number," ' + randomname2 + " bellowed, in a grateful tone. He slammed his fist against " + randomname + "'s chest, with the force of 8234 goldfish. I frigging hate you," + randomname + " looked back, even more worried and still fingering the crumpled hawk." + randomname2 + " get out of my house,  she replied."

s7 = "They looked at each other with sleepy feelings, like two gloopy, gigantic giraffes eating at a very remarkable Halloween party, which had indie music playing in the background and two brave uncles swimming to the beat."

s8 = "Suddenly," + randomname2 + " lunged forward and tried to punch" + randomname + " in the face. Quickly," + randomname + " grabbed the crumpled hawk and brought it down on" + randomname2 + " skull."  + randomname2 +  " handsome eyes trembled and his tall warts wobbled. He looked stable, his body raw like a roasted, rare rock."

s9 = "Then he let out an agonising groan and collapsed onto the ground. Moments later " + randomname2 + " was dead." + randomname +  " went back inside and made herself a nice glass of whiskey."

s10 = "THE END " + randomplace + "!"

#Listing

nightstory = [ s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]

#end of story 1

#start of story2 Sloppy wars

f1 = "A long, long time ago in a sloppy, sloppy galaxy..."

f2 = "After leaving the hilly planet " + randomplanet + " , a group of men fly toward a distant speck. The speck gradually resolves into an old-fashioned, space hut."

f3 = "Civil war strikes the galaxy, which is ruled by " + randomname + " a dull imp capable of gluttony and even cruelty."

f4 = "Terrified, a peculiar sprite known as " + randomname + " flees the Empire, with her protector, " + randomname2 + "."

f5 = "They head for Falmouth on the planet " + randomplanet + "." "When they finally arrive, a fight breaks out. " + randomname2 + " uses his sloppy sword to defend" + randomname + "." + randomname2 + " and" + randomname + " decide it's time to leave " + randomplanet + " and steal a scooter to shoot their way out."

f6 = "They encounter a tribe of elves. " + randomname2 + " is attacked and the sprite is captured by the elves and taken back to Falmouth. " + randomname2 + " must fight to save " + randomname + " but when he accidentally unearths a frantic sausage, the entire future of the sloppy, hilly galaxy is at stake."


nightstory2 = [f1, f2, f3, f4, f5, f6]



# test only part 
m1 = ("taktus")
m2 = ("tktus")
m3 = ("son son")
m4 = ("sats")
nightstory3 = [m1, m2, m3, m4]

#nightstory4 picks a one story from the random list in the variable
nightstory4 = [nightstory, nightstory2, nightstory3]
#end of story2

#randomchoice

n1 = random.choice(nightstory)
n2 = random.choice(nightstory2)
n3 = random.choice(nightstory3)
n4 = random.choice(nightstory4)
#Character section

character = "Characters:"

print('|')
print (character)
print('|....Female......|')
print (randomname)
print ('|....Male....|')
print (randomname2)
print('|....Setting....|')
print(randomplanet)

#Story section
print ('|')
#print (n1)
print("|")
#print (n2)
print("|")
#prints the resultant random value
print(n4)
