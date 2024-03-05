names = ["salt",
"caerbannog",
"toast",
"brown",
"white",
"black",
"gold",
"white_splotched"]
temp = open("template.properties","r").read()
for i in names:
    open(i+".properties","w").write(temp)