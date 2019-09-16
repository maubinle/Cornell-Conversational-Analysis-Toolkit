IQ2 Debate ConvoKit Formatted Dataset
==============================================

This dataset contains a set of json files that have been formatted to fit the Convokit format. There are 108 debates in all, that were held between September 2006 and September 2015. We aim to maximize the information that is retained when converting this to a ConvoKit format.

The original dataset is taken from http://tisjune.github.io/research/iq2 and featured in the paper Zhang, Justine, et al. Conversational Flow in Oxford-Style Debates. Proceedings of the 2016 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, 2016, doi:10.18653/v1/n16-1017.

Corpus translated into ConvoKit format by Lucas Van Bramer and Marianne Aubin Le Quere.

Date: September 12, 2019

Dataset details
==============================================

User-level information

Users in this dataset are the speakers during the debate. The most prominent speakers are those that are listed in the initial dataset as being either ‘for’ a position, ‘against’ it, or a ‘moderator.’ However, there are also other speakers that do not fit into these categories, such as a ‘host’ or a ‘panelist.’ Our user corpus also includes these speaker types. 

We provide:
	- stance: whether they are ‘for’ or ‘against’ a proposition. Will be None if they are impartial such as a moderator or host.
	- bio: if available, full length bio of speaker
	- bio_short: if available, short bio of speaker
==============================================

Utterance-level information

Each utterance is a continuous speaking turn of a single speaker. 

We provide:
	- nontext: this is a dictionary of audience reaction
	- segment: which segment of the debate the utterance was spoken during
	- speakertype: the type of speaker who is saying the utterance
	- debateid: the unique id of the debate

==============================================
Conversation-level information

Our conversations are indexed by the first utterance of a conversation. This means each debate is represented as one conversation. We also provide debate-level metadata at the conversation level as they are equivalent for our dataset.

We provide:
	- summary: a summary of the debate
	- title: the title of the debate
	- date: the date of the debate
	- url: the url where the debate can be accessed
	- results: a full breakdown of the starting and ending positions of the audience in the debates. These are all represented as percentages. The 'results' json file contains 3 dicts with the following metadata:
		- breakdown: entries in this dictionary take the form position1_position2, where position1 is the position at the start of the debate and position2 is the position at the end of the debate. This breakdown is not available for the earlier debates. The entries are thus:
			- against_against
			- against_for
			- against_undecided
			- undecided_against
			- undecided_for
			- undecided_undecided
			- for_against
			- for_for
			- for_undecided
		- pre: percentage of audience that voted 'for,' 'against,' or 'undecided' at the beginning of the debate.
		- post: percentage of audience that voted 'for,' 'against,' or 'undecided' at the end of the debate.
		This results breakdown follows the same structure as the original dataset.
	- speakers: the official speakers of the debate (note our users corpus is more expansive than this definition)

==============================================
Stats:
	number of Users: 471
	number of Utterances: 26562
	number of Conversations: 108
