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
print("kill @e[type=!player]")
print("kill @e[type=!player]")
print("kill @e[type=!player]")
for x,v in enumerate(names):
    for y in range(16):
        print(f"summon minecraft:cat ~{x} ~ ~{y} {{variant:{v},CollarColor:{y},NoAI:1}}")
for x in range(16):
    print(f"summon minecraft:wolf ~{x+12} ~ ~15 {{CollarColor:{x},NoAI:1}}")
