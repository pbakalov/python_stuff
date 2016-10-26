#here a nice way to add and subtract elements from a vector

rather than using randint(0,len(deck)-1) you could just do 
card = random.choice(deck) 
HAND.append(card) 
deck.remove(card) 

although it would be more efficient to do remove card by index which then 
gets us back to using randint, like this 

i = random.randint(0, len(deck)-1) 
HAND.append(deck[i]) 
del deck[i] 

but i guess speed probably isn't a big factor here 

also you could have done 
i=random.randint(0, len(deck)-1) 
HAND.append(deck.pop(i)) 
