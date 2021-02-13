	#defin list
guest_list = ['princess diana','harry styles','kevin mitnick','slick rick', 'patrick suban']
	
	#body text of invite
invite = "\nDo you want to come over for dinner?\n\nHit me up\n\n\tJosh\n"

	#write each invite
msg_0 = f"Dear {guest_list[0].title()}, \n{invite}"
msg_1 = f"Dear {guest_list[1].title()}, \n{invite}"
msg_2 = f"Dear {guest_list[2].title()}, \n{invite}"
msg_3 = f"Dear {guest_list[3].title()}, \n{invite}"
msg_4 = f"Dear {guest_list[4].title()}, \n{invite}"

	#print each invite
"""
print(msg_0)
print(msg_1)
print(msg_2)
print(msg_3)
print(msg_4)
"""

	#suban says no
popped_guest = guest_list.pop(4)
print(f"Unfortuantly {popped_guest.title()}, Said he can't make it.")

	#invite gretsky
guest_list.insert(4, 'wayne gretsky')
msg_4 = f"Dear {guest_list[4].title()}, \n{invite}"

	#re-print invatations
"""
print("\n")
print(msg_0)
print(msg_1)
print(msg_2)
print(msg_3)
print(msg_4)
"""

	#bigger table update
print(f"Dear {guest_list},\nI have found a bigger table and shall be inviting more guest.\nToodles\n\tJoshb")
print("\n")

	#guest added
guest_list.insert(0, 'steve irwin')
guest_list.insert(3, 'katherine ryan')
guest_list.append('jesus')

	#length of table
print(f"I have a whopping {len(guest_list)} people to dinner!\n")

	#updated guest list
# ['steve irwin', 'princess diana', 'harry styles', 'katherine ryan', 'kevin mitnick', 'slick rick', 'wayne gretsky', 'jesus']

	#print new invites
msg_0 = f"Dear {guest_list[0].title()}, \n{invite}"
msg_1 = f"Dear {guest_list[1].title()}, \n{invite}"
msg_2 = f"Dear {guest_list[2].title()}, \n{invite}"
msg_3 = f"Dear {guest_list[3].title()}, \n{invite}"
msg_4 = f"Dear {guest_list[4].title()}, \n{invite}"
msg_5 = f"Dear {guest_list[5].title()}, \n{invite}"
msg_6 = f"Dear {guest_list[6].title()}, \n{invite}"
msg_7 = f"Dear {guest_list[7].title()}, \n{invite}"

	#print new invites
print(msg_0)
print(msg_1)
print(msg_2)
print(msg_3)
print(msg_4)
print(msg_5)
print(msg_6)
print(msg_7)

	#removing guests
print("\nRight, my bad, but only got room for two guests.\n")

	#move harry n rick to end of lsit
guest_list.remove('harry styles')
guest_list.remove('slick rick')
guest_list.append('harry styles')
guest_list.append('slick rick')

	#write unvited body copy
unvite_body = "\n\tSorry for the news but I don't want you to come to my house.\n\n\tFuck off,\n\n\t\tDon't ever talk to me again,\n\n\t\t\tJosh :)\n"
	
	#irwin	
unvited_guest = guest_list.pop(0)
unvite = f"Oi {unvited_guest.title()}!{unvite_body}"
print(unvite)
	#di
unvited_guest = guest_list.pop(0)
unvite = f"Oi {unvited_guest.title()}!{unvite_body}"
print(unvite)
	#ryan
unvited_guest = guest_list.pop(0)
unvite = f"Oi {unvited_guest.title()}!{unvite_body}"
print(unvite)
	#mitnick
unvited_guest = guest_list.pop(0)
unvite = f"Oi {unvited_guest.title()}!{unvite_body}"
print(unvite)
	#gretsky
unvited_guest = guest_list.pop(0)
unvite = f"Oi {unvited_guest.title()}!{unvite_body}"
print(unvite)
	#jesus
unvited_guest = guest_list.pop(0)
unvite = f"Oi {unvited_guest.title()}!{unvite_body}"
print(unvite)

	#final invite
still_invite = "ayup u cunt, u still coming over?\n\n bring jonny's n lube,\n\nbig love\n\tJosh\n"

msg_0 = f"Dear {guest_list[0].title()}, \n{still_invite}"
msg_1 = f"Dear {guest_list[1].title()}, \n{still_invite}"

print(msg_0)
print(msg_1)
	
	#empty gueslist
del guest_list[0]
del guest_list[0]

print(guest_list)