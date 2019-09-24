
from convokit.transformer import Transformer
from convokit.model import Corpus

class LengthTracker(Transformer):
    """
    Extracts how far along a conversation a particular utterance is.

    """

    def __init__(self):
        self.ATTR_NAME = "length_tracker"

    def transform(self, corpus: Corpus):
        """Extract politeness strategies from each utterances in the corpus and annotate
        the utterances with the extracted strategies. Requires that the corpus has previously
        been transformed by a Parser, such that each utterance has dependency parse info in
        its metadata table.
        
        :param corpus: the corpus to compute features for.
        :type corpus: Corpus
        """
        for conv_id in corpus.conversations:
            conv = corpus.get_conversation(conv_id)
            num_utts = len(conv.get_utterance_ids())
            for i, utt in enumerate(conv.iter_utterances()):
                length_through_conv = i/num_utts
                utt.meta['length_tracker'] = [i,length_through_conv]

        return corpus

