names = ["all_black",
"british_shorthair",
"calico",
"jellie",
"persian",
"ragdoll",
"red",
"siamese",
"tabby",
"black",
"white"]
temp = open("template.properties","r").read()
for i in names:
    open(i+".properties","w").write(temp)