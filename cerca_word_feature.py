# coding=utf-8

import spacy
nlp = spacy.load('en_core_web_sm')

from spacy.matcher import Matcher

import pandas as pd


def get_cerca_matches(sample, cerca_words):

    # Explanation matches segment
    m_tool = Matcher(nlp.vocab)
    num_cerca_matches = 0

    vocab = []

    for phrase in cerca_words:
        pattern = []
        phrase = phrase.split()
        for word in phrase:
            pattern.append({"LOWER" : word})
        vocab.append(pattern)

    m_tool.add("MATCH", vocab)

    cerca_matches = m_tool(sample)

    for match_id, start, end in cerca_matches:
        num_cerca_matches += 1
        string_id = nlp.vocab.strings[match_id]  
        span = sample[start:end]                   
        # print(match_id, string_id, start, end, span.text)
        # print("Start Index:", start, "End Index:", end, "Word Matched:", span.text)

    print("Number of Cerca Word Matches: ")
    print(num_cerca_matches)


sample = pd.read_csv("clean_full_100k_rows.csv")

writing = sample["student_final_writing"]

words = sample["cerca_words"]

words = words.tolist()

words = sample.dropna(subset=['cerca_words'])["cerca_words"]

writing = writing.tolist()

writing = sample.dropna(subset=['student_final_writing'])["student_final_writing"]

# print("Cerca Word List: ")
# print(words[2])



essay = writing[2]
word_list = words[2].split(", ")
writing_doc = nlp(essay)
# print("Writing Sample: ")
# print(writing_doc)
get_cerca_matches(writing_doc, word_list)