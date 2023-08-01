alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if shift > 26:
   shift = shift - 26
   print(f'shif is now {shift}')

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(text, shift):
   msg = text
   msg_list = list(msg)
   org_msg = ''
   new_msg_idx = [] 
   new_msg = ''
   for char in msg_list:
      org_msg += char
      new_msg_idx.append(alphabet.index(char)+1+shift)
   print(f"original message is {org_msg}")
   print(f"shift is {shift}")
   #print(f"new message index is {new_msg_idx}")
   for char in new_msg_idx:
      new_msg += alphabet[char-1]
   print(f"The encoded text is {new_msg}")
   
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

def decode(text, shift):
   msg = text
   msg_list = list(msg)
   ciKey = shift
   org_msg = ''
   new_msg_idx = [] 
   new_msg = ''
   for char in msg_list:
      org_msg += char
      new_msg_idx.append(alphabet.index(char)-1-shift)
   print(f"original message is {org_msg}")
   print(f"shift is {shift}")
   #print(f"new message index is {new_msg_idx}")
   for char in new_msg_idx:
      new_msg += alphabet[char+1]
   print(f"The decoded text is {new_msg}")
   

if(direction == 'encode'):
   encrypt(text,shift)
elif(direction == 'decode'):
   decode(text,shift)
else:
   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
