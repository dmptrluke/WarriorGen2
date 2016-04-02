import random

def weighted_choice(choices):
    total = sum(w for c, w in choices)
    r = random.uniform(0, total)
    upto = 0
    for c, w in choices:
        if upto + w > r:
            return c
        upto += w
    assert False, "Shouldn't get here"

# basic variables
cat = {}

# pelt/marking variables
marking_types = ['{colour} spots covering {gender} whole body', '{colour} rings around {gender} eyes', 'wavy {colour} stripes on {gender} tail', 'a {colour} belly and chest', 'a long {colour} stripe running down {gender} back', '{colour} paws', '{colour} front paws', 'one {colour} back paw', '{colour} dapples on {gender} face, tail and paws', '{colour} patches covering {gender} sides', 'a {colour} muzzle', '{colour} ear-tips and tail-tips', '{colour} speckles around {gender} eyes', '{colour} spots on {gender} tail', '{colour} stripes on {gender} legs', '{colour} toes', '{colour} flecks covering {gender} pelt', 'a range of {colour} dapples varying in size covering {gender} pelt', '{colour} tips to {gender} fur']

colours = {
    "blue": ["white", "black", "silver", "grey"],
    "red": ["ginger", "cream", "white", "black", "cinnamon", "fawn"],
    "ginger": ["red", "cream"," white", "black", "cinnamon", "fawn"],
    "cream": ["red", "ginger", "fawn", "cinnamon", "brown", "golden-brown", "chocolate-brown", "white"],
    "silver": ["grey", "blue", "white", "black"],
    "white": ["blue", "grey", "silver", "black"],
    "grey": ["blue", "white", "black", "silver"],
    "brown": ["cream", "black", "chocolate-brown", "fawn", "white"],
    "black": ["white"],
    "fawn": ["cinnamon", "white", "cream", "chocolate-brown"],
    "cinnamon": ["fawn", "white", "cream", "chocolate-brown"],
    "golden-brown": ["brown", "white", "chocolate-brown", "black", "cream"],
    "chocolate-brown": ["brown", "white", "golden-brown", "black", "cream"]
}

# Name
cat["name"] = "Failtail"

# Gender
cat["gender"] = random.choice(["male", "female"])
cat["gender_objective"] = "his" if cat["gender"] == "male" else "her"
cat["gender_pronoun"] = "He" if cat["gender"] == "male" else "She"
cat["gender_warrior"] = "tom" if cat["gender"] == "male" else "she-cat"

# Warrior Cats Specific Details
if cat["gender"] == "male":
    ranks = [("warrior", 12), ("apprentice", 3), ("kit", 3), ("leader", 1), ("medicine cat", 1), ("deputy", 1), ("elder", 2)]
else:
    ranks = [("warrior", 12), ("apprentice", 3), ("kit", 3), ("leader", 1), ("medicine cat", 1), ("deputy", 1), ("elder", 2), ("queen", 2)]

cat["rank"] = weighted_choice(ranks)

# Basic Pelt
cat["pelt_colour"] = random.choice(list(colours))
cat["pelt_texture"] = random.choice(["sleek", "thick", "fluffy", "silky", "rough", "bushy", "matted"])
cat["pelt_length"] = random.choice(["short", "long", "medium-length", "very long", "very short"])
cat["pelt_shade"] = random.choice(["dark", "deep", "faded", "light", "pale", "mottled", "murky", "very dark", "dappled", "bright"])
secondary_colours = colours[cat["pelt_colour"]]

# Tabby
if random.randint(0, 1) and not cat["pelt_colour"] == "white":
    cat["tabby_type"] = random.choice(["spotted", "striped", "swirled"])
else:
    cat["tabby_type"] = None

# Pelt Markings
cat["markings"] = []

if cat["tabby_type"]:
    marking_count = random.randint(0, 1) 
else:
    marking_count = random.randint(0, 2)

for marking in range(marking_count):
    text = random.choice(marking_types)
    colour = random.choice(secondary_colours)

    marking = text.format(colour=colour, gender=cat["gender_objective"])

    # add the marking to the list
    cat["markings"].append(marking)

# Body Build
body_sizes = ["long", "tall", "small", "large"]
body_builds = ["muscular", "scrawny", "wiry", "slender", "lithe", "compact", "sleek", "sturdy", "bulky"]

cat["body_size"] = random.choice(body_sizes)
cat["body_build"] = random.choice(body_builds)

# Clans (temporary)
cat["clan"] = random.choice(["ThunderClan", "RiverClan", "WindClan", "ShadowClan"])

# Build Output


if cat["tabby_type"]:
    output = "A {pelt_shade} {pelt_colour} {tabby_type} tabby {gender_warrior} ".format(**cat)
else:
    output = "A {pelt_shade} {pelt_colour} {gender_warrior} ".format(**cat)

if cat["pelt_length"] == "normal":
    output += "with {pelt_length} fur".format(**cat)
else:
    output += "with {pelt_length} {pelt_texture} fur".format(**cat)

if marking_count == 0:
    output += ". "
elif marking_count == 1:
    output += " and {markings[0]}. ".format(**cat)
else:
    output += ". {name} has {markings[0]} and {markings[1]}. ".format(**cat)

output += "{gender_pronoun} is a {body_size}, {body_build} {rank} of {clan}. ".format(**cat)

print(output)
