import json
import random
import enum
from pathlib import Path
from typing import Iterable

from .words import default_articles, default_adjectives, default_nouns, default_verbs, default_adverbs


root_path = Path(__file__).parent


class PhrasePart(enum.Flag):
    """
    An enum to specify the mode of the identifier.
    """
    ARTICLE = enum.auto()
    ADJECTIVE = enum.auto()
    NOUN = enum.auto()
    VERB = enum.auto()
    ADVERB = enum.auto()


default_phrase_structures = [
    PhrasePart.ARTICLE | PhrasePart.ADJECTIVE | PhrasePart.NOUN | PhrasePart.VERB | PhrasePart.ADVERB,
    PhrasePart.ARTICLE | PhrasePart.ADJECTIVE | PhrasePart.NOUN | PhrasePart.VERB,
    PhrasePart.ARTICLE | PhrasePart.ADJECTIVE | PhrasePart.NOUN,
    PhrasePart.ARTICLE | PhrasePart.NOUN | PhrasePart.VERB | PhrasePart.ADVERB,
    PhrasePart.ARTICLE | PhrasePart.NOUN | PhrasePart.VERB,
    PhrasePart.ARTICLE | PhrasePart.NOUN,
    PhrasePart.ADJECTIVE | PhrasePart.NOUN,
]


class PhraseGenerator:
    """
    A class to generate random phrases based on the words in dictionary.

    :param structures: The structures to use when generating the phrases.
    :param max_word_length: The maximum length of the words to use.
    :param separator: The separator between the words.
    :param articles: A list of articles to use.
    :param adjectives: A list of adjectives to use.
    :param nouns: A list of nouns to use.
    :param verbs: A list of verbs to use.
    :param adverbs: A list of adverbs to use.
    """

    def __init__(self, structures: PhrasePart | list[PhrasePart] | None = None, 
                       max_word_length: int | None = None, 
                       separator: str = "_",
                       articles: Iterable[str] | None = None,
                       adjectives: Iterable[str] | None = None,
                       nouns: Iterable[str] | None = None,
                       verbs: Iterable[str] | None = None,
                       adverbs: Iterable[str] | None = None,
                       ):
        max_word_length = max_word_length or 100
        articles = articles or default_articles
        adjectives = adjectives or default_adjectives
        nouns = nouns or default_nouns
        verbs = verbs or default_verbs
        adverbs = adverbs or default_adverbs

        if "an" in articles:
            articles = list(articles)
            articles.remove("an")
            if "a" not in articles:
                articles.append("a")

        self.articles = list(filter(lambda word: len(word) <= max_word_length, articles))
        self.adjectives = list(filter(lambda word: len(word) <= max_word_length, adjectives))
        self.nouns = list(filter(lambda word: len(word) <= max_word_length, nouns))
        self.verbs = list(filter(lambda word: len(word) <= max_word_length, verbs))
        self.adverbs = list(filter(lambda word: len(word) <= max_word_length, adverbs))

        self.structures = structures or default_phrase_structures
        self.separator = separator

    def generate_phrase(self) -> str:
        """
        Generates a random phrase.
        
        :return: The generated phrase.
        """

        if isinstance(self.structures, list):
            struct = random.choice(self.structures)
        else:
            struct = self.structures

        phrase = []

        if PhrasePart.ADJECTIVE in struct:
            phrase.append(random.choice(self.adjectives))

        if PhrasePart.NOUN in struct:
            phrase.append(random.choice(self.nouns))

        if PhrasePart.VERB in struct:
            phrase.append(random.choice(self.verbs))

        if PhrasePart.ADVERB in struct:
            phrase.append(random.choice(self.adverbs))

        if PhrasePart.ARTICLE in struct:
            article = random.choice(self.articles)
            if article == "a" and (phrase[0][0] in "aeiou"):
                article = "an"
            phrase.insert(0, article)

        return self.separator.join(phrase).replace("_", self.separator)
    
    def n_combinations(self):
        """
        Returns the number of possible combinations for each structure.

        :return: A dictionary with the number of combinations for each structure.
        """
        if isinstance(self.structures, list):
            structures = self.structures
        else:
            structures = [self.structures]
        
        results = {}
        for structure in structures:
            counts = []
            if PhrasePart.ADJECTIVE in structure:
                counts.append(len(self.adjectives))

            if PhrasePart.NOUN in structure:
                counts.append(len(self.nouns))

            if PhrasePart.VERB in structure:
                counts.append(len(self.verbs))
            
            if PhrasePart.ADVERB in structure:
                counts.append(len(self.adverbs))

            if PhrasePart.ARTICLE in structure:
                counts.append(len(self.articles))

            combinations = 1
            for count in counts:
                combinations *= count

            results[structure] = combinations

        return results


if __name__ == "__main__":
    test_structures = [
        *default_phrase_structures,
        PhrasePart.ARTICLE,
        PhrasePart.ADJECTIVE,
        PhrasePart.NOUN,
        PhrasePart.VERB,
        PhrasePart.ADVERB,
    ]

    def print_test_phrases(word_size_limit: int | None):
        """
        Docstring
        """
        print(f"word_size_limit: {word_size_limit}")
        
        for structure in test_structures:
            phrase_generator = PhraseGenerator(structure, max_word_length=word_size_limit)
            n_combinations = phrase_generator.n_combinations()[structure]
            phrase = phrase_generator.generate_phrase()
            print("  ", f"{structure.name}({n_combinations}): {phrase}")

        print("")
    
    print_test_phrases(None)
    print_test_phrases(6)
    print_test_phrases(5)
    print_test_phrases(4)
    

    



