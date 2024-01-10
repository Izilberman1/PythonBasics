#!/usr/bin/env python
# coding: utf-8

# In[15]:


#program that calculates your age according to birth year#
birth_year = input("what year were you born? ")
age = 2024-int(birth_year)
print("\n")
print(f'your age is: {age}')


# In[20]:


#Ask for username and password and output password length in number and as asteric symbols#
username = input("please create a username: ")
password = input("please create a password: ")

pass_len = len(password)
hidden_pass = '*' * pass_len
print(f'{username}, password {hidden_pass}, is {pass_len} letters long.')


# In[25]:


#Lists#
cart = ['Hummus',
        'Olive Oil', 
        "Za'tar", 
        'Pitas', 
        'Tahini', 
        'Paprika', 
        'Tomatoes', 
        'Lamb', 
        'Rice', 
        'Parsley', 
        'Lemon', 
        'Salt']
print(cart[0::2])


# In[26]:


#Lists are Immutable#
cart[0] = 'Guacamole'
print(cart)


# In[29]:


#copying the list#
cart[0] = 'Guacamole'
new_cart = cart[:] #this [:] allows for copying
new_cart[0] = 'chestnut'
print(cart)
print(new_cart)


# In[30]:


#modifying the list#
cart[0] = 'Guacamole'
new_cart = cart #this gets modified with the change of the first index 0
new_cart[0] = 'chestnut'
print(cart)
print(new_cart)


# In[31]:


#list adding methods
basket = [1,2,3,4,5]

basket.append(100)
new_list = basket
print(basket)
print(new_list)


# In[32]:


#list adding methods
basket = [1,2,3,4,5]

basket.insert(4, 100) #adds 100 to the index of 4 in place
new_list = basket
print(basket)
print(new_list)


# In[33]:


#list adding methods
basket = [1,2,3,4,5]

basket.extend([100, 101]) #extends our list in place by adding 100, 101
new_list = basket
print(basket)
print(new_list)


# In[34]:


#list removing methods
basket = [1,2,3,4,5]

basket.pop(0) #removes the index 0
print(basket)


# In[35]:


#list removing methods
basket = [1,2,3,4,5]

basket.remove(4) #removes the number 4 from the list
print(basket)


# In[37]:


#list removing methods
basket = [1,2,3,4,5]

basket = basket.pop(4) #returns the the number value at index 4
print(basket)


# In[38]:


#list removing methods
basket = [1,2,3,4,5]

basket = basket.clear() #removes the values from all of the indexes in the basket
print(basket)


# In[42]:


#list removing methods
basket = ['a','b','c','d','e']

print(basket.index('d')) #outputs which index the value 'd' is at


# In[44]:


#list removing methods
basket = ['a','b','c','d','e']

print(basket.index('e',0,5)) #(value,start index,end at index) outputs which index the value 'e' is at


# In[45]:


basket = ['a','b','c','d','e']
print('e' in basket) #is the value 'e' in basket?


# In[49]:


basket = ['a','b','c','d','e']
print(basket.count('d'))#how many times the value 'd' occurs in basket list


# In[50]:


basket = ['a','f','b','c','d','e']
basket.sort()#sorts the basket list in alphabetical order
print(basket)


# In[51]:


basket = ['a','f','b','c','d','e']
print(sorted(basket))#sorts basket alphabetically in a new list
print(basket)#original basket list


# In[52]:


basket = ['a','f','b','c','d','e']
basket.reverse()#reverses the indexes values in places without sorting
print(basket)


# In[53]:


basket = ['a','f','b','c','d','e']
basket.sort()#sorts the values of basket list in alphabetical order
basket.reverse()#reverses the indexes values in places without sorting
print(basket)


# In[54]:


basket = ['a','f','b','c','d','e']
basket.sort()#sorts the values of basket list in alphabetical order
basket.reverse()#reverses the indexes values in places without sorting
print(basket[::-1])#Slices the list by creating a new basket list in alphabetical order
print(basket)#prints the last modification of the original basket


# In[56]:


print(list(range(101)))


# In[58]:


sentence = ' '
new_sentence = sentence.join(['hi','my','name','is','ITAMAR'])
print(new_sentence)


# In[59]:


new_sentence = ' '.join(['hi','my','name','is','ITAMAR'])
print(new_sentence)


# In[60]:


#list unpacking
a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]

print(a)
print(b)
print(c)
print(other)
print(d)


# In[ ]:




