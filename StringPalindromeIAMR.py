'''st = input("Enter the string..")
rev = st[::-1]
if st == rev:
    print("string is palindrome..")
else:
    print("string is not palindrome..")'''

'''st = "my aaaaa name is Ram"
st = st.replace("a","p")
print(st)'''

'''st = "skill,risers.and,brain,mentors."

st = st.replace(".","*")
st = st.replace(",",".")
st = st.replace("*",",")
print(st)'''

st = input("Enter the string..")

#this is a python language
st = st.split()

st = st[::-1]

st = " ".join(st)
print(st)
