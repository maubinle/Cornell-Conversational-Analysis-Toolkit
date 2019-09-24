from convokit.transformer import Transformer
from convokit.model import Corpus
from nltk.corpus import cmudict
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize


class ComplexityTransformer(Transformer):
    """
    Extracts several metrics from utterances about 

    """
    def __init__(self):
        self.ATTR_NAME = "complexity_transformer"
        self.d = cmudict.dict()

    def __num_syllables(self, word: str):
        # adapted from post here: https://stackoverflow.com/questions/405161/detecting-syllables-in-a-word/4103234#4103234
        return [
            len(list(y for y in x if y[-1].isdigit()))
            for x in self.d[word.lower()]
        ]

    def transform(self, corpus: Corpus):
        """Adds metadata about readability of the corpus to each utterance.

        :param corpus: the corpus to compute features for.
        :type corpus: Corpus
        """
        for conv_id in corpus.conversations:
            print("doing a convo")
            conv = corpus.get_conversation(conv_id)
            for utt in conv.iter_utterances():
                cumu_sentences = 0
                cumu_words = 0
                cumu_syllables = 0
                cumu_syll_counted_words = 0
                cumu_words_over2_syllables = 0
                for sentence in sent_tokenize(utt.text):
                    cumu_sentences += 1
                    tokenized = word_tokenize(sentence)
                    cumu_words += len(tokenized)
                    for token in tokenized:
                        try:
                            syll = self.__num_syllables(token)[0]
                            cumu_syllables += syll
                            cumu_syll_counted_words += 1
                            if syll > 2:
                                cumu_words_over2_syllables += 1
                        except Exception as e:
                            pass

                # readability formulas from https://www.geeksforgeeks.org/readability-index-pythonnlp/
                if cumu_sentences > 0 and cumu_syll_counted_words > 0:
                    gunning_fog = 0.4 * ((cumu_words / cumu_sentences) + \
                      (cumu_words_over2_syllables / cumu_syll_counted_words))
                    flesch = 206.835 - (1.015 * (cumu_words / cumu_sentences)) - \
                      (84.6 * (cucumu_syllablescumu_syllablescumu_syllablesmu_syllables / cumu_syll_counted_words))
                    flesch_kincaid = (0.39 * cumu_words / cumu_sentences) + \
                      (11.8 * cumu_syllables / cumu_syll_counted_words) - 15.59
                    utt.meta['complexity'] = \
                      {"gunning_fog": gunning_fog,
                      "flesch": flesch,
                      "flesh_kincaid": flesch_kincaid,
                      "num_words": cumu_words,
                      "num_sentences": cumu_sentences}
                else:
                    utt.meta['complexity'] = \
                      {"gunning_fog": None,
                      "flesch": None,
                      "flesch_kincaid": None,
                      "num_words": None,
                      "num_sentences": None}
        return corpus