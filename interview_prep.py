# ------------------------------------------------
# -----------------Understanding------------------
# ------------------------------------------------



# ------------------------------------------------
# --------------------Planning--------------------
# ------------------------------------------------

# Add our list as a variable
# Create a function that will sort the list
# Loop through the list and print each item

# ------------------------------------------------
# ------------------Execution---------------------
# ------------------------------------------------

listA = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']

def alphabetize(list):
  list.sort()
  for a in list:
    print(a)

alphabetize(listA)