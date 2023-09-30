# phrase_generator

Generates random phrases from a dictionary of words. Words are always lower case
and by separated by underscores by default.


## Examples


```python
from phrase_generator import PhraseGenerator, PhrasePart


# Generate phrase with default settings
phrase_generator = PhraseGenerator()
phrase = phrase_generator.generate_phrase()
print(phrase)


# Generate phrase with custom list of phrase structures
phrase_structures = [
    PhrasePart.ARTICLE | PhrasePart.ADJECTIVE | PhrasePart.NOUN,
    PhrasePart.ARTICLE | PhrasePart.NOUN | PhrasePart.VERB,
    PhrasePart.ARTICLE | PhrasePart.NOUN,
    PhrasePart.ADJECTIVE | PhrasePart.NOUN,
]
phrase_generator = PhraseGenerator(phrase_structures)
phrase = phrase_generator.generate_phrase()
print(phrase)


# Generate phrase with one custom phrase structure
phrase_generator = PhraseGenerator(PhrasePart.ARTICLE | PhrasePart.NOUN)
phrase = phrase_generator.generate_phrase()
print(phrase)


# Generate phrase with word length limit and custom separator
phrase_generator = PhraseGenerator(max_word_length=5, separator=" ")
phrase = phrase_generator.generate_phrase()
print(phrase)

# Generate phrase with custom list of words
phrase_generator = PhraseGenerator(
    articles=["the", "a", "an"],
    nouns=["cat", "dog", "bird"],
    verbs=["runs", "jumps", "flies"],
    adjectives=["big", "small", "fast"],
    adverbs=["quickly", "slowly", "quietly"],
)
phrase = phrase_generator.generate_phrase()
print(phrase)

# Print number of phrase combinations for each phrase structure
phrase_generator = PhraseGenerator()
print("\nNumber of phrase combinations:")
for structure, n_combinations in phrase_generator.n_combinations().items():
    print(f"{structure.name}: {n_combinations}")



```

```plain
a_mint_fences
my_ceiling_empties
the_ceramic
fine june
the_big_cat_flies_quietly

Number of phrase combinations:
ARTICLE|ADJECTIVE|NOUN|VERB|ADVERB: 9452833004736
ARTICLE|ADJECTIVE|NOUN|VERB: 29632705344
ARTICLE|ADJECTIVE|NOUN: 46887192
ARTICLE|NOUN|VERB|ADVERB: 8462697408
ARTICLE|NOUN|VERB: 26528832
ARTICLE|NOUN: 41976
ADJECTIVE|NOUN: 2604844
```
