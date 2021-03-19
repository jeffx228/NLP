# coding=utf-8
from lexical_diversity import lex_div as ld

# with a precreated vocab list, this code can comb through text,
# count the number of matches with vocab words (without repeats),
# and return the result.
text = "The state was named for the Colorado River, which Spanish travelers named the Río Colorado for the ruddy silt the river carried from the mountains. The Territory of Colorado was organized on February 28, 1861, and on August 1, 1876, U.S. President Ulysses S. Grant signed Proclamation 230 admitting Colorado to the Union as the 38th state. Colorado is nicknamed the Centennial State because it became a state a century after the signing of the United States Declaration of Independence. Colorado is bordered by Wyoming to the north, Nebraska to the northeast, Kansas to the east, Oklahoma to the southeast, New Mexico to the south, Utah to the west, and touches Arizona to the southwest at the Four Corners. Colorado is noted for its vivid landscape of mountains, forests, high plains, mesas, canyons, plateaus, rivers, and desert lands. Colorado is part of the western or southwestern United States, and one of the Mountain States. Denver is the capital and most populous city of Colorado. Residents of the state are known as Coloradans, although the antiquated term Coloradoan is occasionally used."

print("Writing sample: ")
print(text)


tok = ld.tokenize(text)

res = [] 
for i in tok:
    i.lower() 
    if i not in res: 
        res.append(i) 

vocab = ["state", "ruddy", "silt", "aggregate"]

print("Vocab words: ")
print(vocab)


vocab_counter = 0

words_used = []

for i in res:
    for word in vocab:
        if (word == i):
            vocab_counter += 1
            words_used.append(word)


print("Number of vocab words used: ")
print(vocab_counter)

print("Words used: ")
print(words_used)