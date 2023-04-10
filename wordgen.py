import itertools

with open("dictionary.txt") as f:
    words = set(line.strip() for line in f)

with open("pronouns.txt") as f:
    pronouns = [line.strip() for line in f]

results = set()

for L in range(1, 4):
    for subset in itertools.combinations(pronouns, L):
        joined_word = "".join(subset)
        if joined_word in words:
            syllables = "/".join(subset).rstrip('/')
            result = f"{joined_word} -> {syllables}"
            results.add(result)

results = sorted(results)

for result in results:
    print(result)

with open("output.txt", "w") as f:
    f.write("\n".join(results))
