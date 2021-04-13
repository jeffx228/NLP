# coding=utf-8

import spacy
nlp = spacy.load('en_core_web_sm')

from spacy.matcher import Matcher

import pandas as pd


def get_transition_matches(sample):
    explanation_transitions = ["Thus", "for example", "for instance", "namely", "to illustrate", "in other words", "in particular",
    "specifically", "such as", "for example", "for instance", "as an illustration"]

    contrast_transitions = ["On the contrary", "contrarily", "notwithstanding", "but", "however", "nevertheless", "in spite of",
                        "in contrast", "yet", "on one hand", "on the other hand", "rather", "or", "nor", "conversely", "at the same time", 
                        "while this may be true"]
    
    summary_transitions = [
    "as can be seen", "generally speaking", "in the final analysis", 
    "all things considered", "as shown above", "in the long run", "given these points", 
    "as has been noted", "in a word", "for the most part", "after all", "in fact", 
    "in summary", "in conclusion", "in short", "in brief", "in essence", 
    "to summarize", "on balance", "altogether", "overall", "ordinarily", "usually", 
    "by and large", "to sum up", "on the whole", "in any event", "in either case", "all in all", "ultimately"]


    # Explanation matches segment
    m_tool = Matcher(nlp.vocab)
    num_ematches = 0

    vocab = []

    for phrase in explanation_transitions:
        pattern = []
        phrase = phrase.split()
        for word in phrase:
            pattern.append({"LOWER" : word})
        vocab.append(pattern)

    m_tool.add("MATCH", vocab)

    explanation_matches = m_tool(sample)

    for match_id, start, end in explanation_matches:
        num_ematches += 1
        string_id = nlp.vocab.strings[match_id]  
        span = sample[start:end]                   
        # print(match_id, string_id, start, end, span.text)
        # print("Start Index:", start, "End Index:", end, "Word Matched:", span.text)

    print("Number of Explanation Transition Matches: ")
    print(num_ematches)


    # Contrast matches segment 
    vocab = []

    num_cmatches = 0

    c_tool = Matcher(nlp.vocab)

    for phrase in contrast_transitions:
        pattern = []
        phrase = phrase.split()
        for word in phrase:
            pattern.append({"LOWER" : word})
        vocab.append(pattern)

    c_tool.add("MATCH", vocab)

    contrast_matches = c_tool(sample)

    for match_id, start, end in contrast_matches:
        num_cmatches += 1
        string_id = nlp.vocab.strings[match_id]  
        span = sample[start:end]                   
        # print(match_id, string_id, start, end, span.text)
        # print("Start Index:", start, "End Index:", end, "Word Matched:", span.text)

    print("Number of Contrast Transition Matches: ")
    print(num_cmatches)


    # Summary matches segment

    vocab = []

    num_smatches = 0

    s_tool = Matcher(nlp.vocab)

    for phrase in summary_transitions:
        pattern = []
        phrase = phrase.split()
        for word in phrase:
            pattern.append({"LOWER" : word})
        vocab.append(pattern)

    s_tool.add("MATCH", vocab)

    summary_matches = s_tool(sample)

    for match_id, start, end in summary_matches:
        num_smatches += 1
        string_id = nlp.vocab.strings[match_id]  
        span = sample[start:end]                   
        # print(match_id, string_id, start, end, span.text)
        # print("Start Index:", start, "End Index:", end, "Word Matched:", span.text)

    print("Number of Summary Transition Matches: ")
    print(num_smatches)

    print("Total number of Transition Matches:")
    print(num_smatches + num_cmatches + num_ematches)


sample = pd.read_csv("clean_full_100k_rows.csv")

writing = sample["student_final_writing"]

writing = writing.tolist()

writing = sample.dropna(subset=['student_final_writing'])["student_final_writing"]

# print(sample)

# essay_doc = nlp(essay_text)

# get_transition_matches(essay_doc)

# for essay in writing:

essay = writing[2]
writing_doc = nlp(essay)
get_transition_matches(writing_doc)