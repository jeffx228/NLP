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
        print("Start Index:", start, "End Index:", end, "Word Matched:", span.text)

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
        print("Start Index:", start, "End Index:", end, "Word Matched:", span.text)

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
        print("Start Index:", start, "End Index:", end, "Word Matched:", span.text)

    print("Number of Summary Transition Matches: ")
    print(num_smatches)

def clean_vector(vector_string):
  if pd.isnull(vector_string):
    return None
  remove_parentheses = re.sub(r"c\(", "", vector_string)
  remove_parentheses = re.sub(r"\)", "", remove_parentheses)
  array = remove_parentheses.split("\", ")
  remove_quotes = [re.sub(r'^"|"$', "", stem) for stem in array]
  # add_back_quotes = [re.sub(r"\\", '\\"', stem) for stem in array]

  return remove_quotes

essay_text = "In George Orwell’s 1984, thus, the Party is an infallible totalitarian regime centered on surveillance, lies, and psychological manipulation. Nobody escapes the grasp of the telescreens. Inner and Outer Party members alike are constantly monitored and watched, facing threat of execution or psychological torture upon any hint of nonconformity. Everybody in Oceania is watched except for the proles, the working-class people who know little about the Party and mostly live under false pretenses of prosperity, lies that are spread by the government. It would seem that with such a societal structure, the Party is omnipotent. In fact, at many points in the book, including the ending, we are led to believe that there is no hope of ever ending the Party. The protagonist Winston, however, who is a member of the Outer Party, has an inexplicable fascination with the proles and believes they have the potential to overthrow the Party. But before he can further explore his curiosity in them, he is caught for his crimes and sent to the Ministry of Love, where he is tortured. A plausible interpretation of this ending is that there is ultimately no hope of ever defeating the Party. To what extent is this true? Can the proles still bring hope of an overthrow of the Party despite an ending where Winston’s own rebellious thoughts and actions are shut down and tamed? 	Winston ultimately gets caught and his loyalty to his partner Julia is subsequently usurped by an undying love for Big Brother. We’re reminded by Winston, however, that the end of the Party cannot be brought about by any one person but rather the collective dissatisfaction of a generation of working-class people who demand better living conditions. Even while Winston is doomed, the real hope is in the future of the proles, through their numbers, through their virility, and through their eventual consciousness. If they can hold onto their humanity, the proles will eventually realize the terrible conditions they are living in because they will be able to feel it in their bodies. They will become conscious of their situation, unite, and rebel against the party. With their numbers and humanity, we are actually to believe that even despite such a pessimistic ending to the book, there is still hope of a prole rebellion eventually defeating the Party. In the beginning, the proles are shown to be a subjugated majority of the population with very little agency in their own lives, let alone the ability to influence Party politics. Yet, Winston still has a gut feeling about the potential of the proles, which we can see when he writes in his diary, “‘If there is hope, it lies in the proles.’” (Orwell 82). His epiphany is described as a “...statement of a mystical truth and a palpable absurdity” (Orwell 82). It is a “mystical truth” because only the proles, who collectively make up 85 percent of Oceania’s population, have the actual manpower and numbers to overthrow the Party; yet, it is also a “palpable absurdity” since the proles have no ambition or conscious thought to do such a thing. The prime example of an absence of motivation to rebel is the proles’ obsession with the Lottery, a Party-propagated scam advertising large weekly pay-outs, much of which are nonexistent. The proles dedicate much of their attention to the Lottery. In fact, it’s described that “...[i]t was probable that there were some millions of proles for whom the Lottery was the principal if not the only reason for remaining alive. It was their delight, their folly, their anodyne, their intellectual stimulant” (Orwell 83). It’s this very “anodyne” that causes the proles to become numb towards everything else around them: their terrible living conditions, the corruption of the government, the propaganda, and most importantly, their true strength. They clearly lack ambition and conscious thought. If the proles could become aware of their situation, they would be unstoppable. We see that “...[w]here the Lottery was concerned, even people who could barely read and write seemed capable of intricate calculations and staggering feats of memory” (Orwell 83). While the proles have these intellectual capabilities, they are wasting their aptitude on the wrong things. Winston has faith in their potential, but it’s apparent how an overthrow of the Party in the short-term can be deemed a “palpable absurdity.” In the present, the proles are much like a sleeping beast; once they are awakened, they have the capacity to affect real change and destroy the Party. Winston’s view of the hope for a future prole rebellion alters in Part 2. Some time has passed since Winston’s initial venture into the prole district, and he has settled into his relationship with Julia, most of which takes place in Mr. Charrington’s upstairs apartment with a window overlooking other prole residences. One morning, Winston hears a singing red-armed prole woman. Specifically, he notices how “her body, roughened by work till it was coarse in the grain like an overripe turnip, could be beautiful” (219). In comparing her body to a turnip, Winston emphasizes her fertility and posits that she was the bearer of several children in the past. His perspective grows. Thinking about this woman, her life, her children, and the purpose of her existence, Winston also begins to think about “...the hundreds or thousands of millions of people just like this, people ignorant of one another’s existence, held apart by walls of hatred and lies, and yet almost exactly the same—people who had never learned to think but were storing up in their hearts and bellies and muscles the power that would one day overturn the world” (Orwell 220). But power alone wouldn’t be enough. In order to truly have a chance at overcoming the Party, the proles also must develop conscious thought and the will to fight. While it may seem difficult for an entire population of subjugated people to suddenly become aware of their circumstances, the sheer amount of living people guarantees that there are at least a few outliers who can become a threat to the Party. In Winston’s discussion of the proles, the reader learns that “[a] few agents of the Thought Police moved always among them, spreading false rumors and marking down and eliminating the few individuals who were judged capable of becoming dangerous…” (Orwell 71). The proles, despite being left in the dark about political ideas, have the potential to create individuals who can rise above the others and become conscious about their situation. These individuals could harness the power to influence and spread sentiments of dissent to those around them, planting the seeds for a full-scale proletariat revolution. So unlike him and Julia, who were forbidden to have children and who he believes are already doomed, the red-armed woman has the capacity to create “a race of conscious beings,” which through numbers and outliers alone, “must one day come” (262). Winston’s thoughts are cut short when he predicts his own future, and the Thought Police come to take him and Julia away. Even in his eerily accurate foresight of his own eventual destruction, we can see how Winston’s damnation is also lined with hope and the underpinnings for a future created by the proles and for the proles. Some may argue that the Party’s regime is too overbearing and careful to allow for insurrection to occur. Even Winston and Julia, two intelligent rebels, were eventually caught in their secretive actions. For instance, the Party had the ability and resources to shut down covert rule-breaking by internal Party members; how could a full-scale rebellion by the masses ever slip through the cracks? In the third act, while Winston is being reeducated, O’Brien elucidates the truth about the proles before breaking Winston’s mind. He says, “The program it [The Book] sets forth is nonsense. The secret accumulation of knowledge—a gradual spread of enlightenment—ultimately a proletarian rebellion—the overthrow of the Party. You foresaw yourself that that was what it would say. It is all nonsense” (Orwell 261). O’Brien continues by saying, “The proletarians will never revolt, not in a thousand years or a million. They cannot. If you have ever cherished any dreams of violent insurrection, you must abandon them” (261-262). At first glance, this appears to be damning evidence for the loss of hope of rebellion. However, one point to note is that O’Brien could be telling Winston this just to quash his resolve for a rebellion and assimilate back into society as a normal Party member again. He doesn’t give Winston any concrete reasoning for why it’s necessary to abandon hope. O’Brien simply phrases his thoughts as a command when he tells Winston to abandon his “dreams of violent insurrection” (262). This is reminiscent of the conditioning and retraining that Winston receives in Room 101, where Winston is forced to learn lies as truth. O’Brien’s reasoning fails the most in the fact that through all of the subversion that is employed on the proles, they have held onto the most important thing: their humanity. As Winston describes them in his thoughts, “They [the proles] were not loyal to a party or a country or an idea, they were loyal to one another. The proles had stayed human. They had held on to the primitive emotions which he himself had to relearn by conscious effort” (165). In the current state, O’Brien is correct to say that the proles are in no position to revolt. However, if the proles cling onto their humanity and continue to produce generations of living humans who prioritize loyalty to people over loyalty to a party, we cannot discard the possibility of a future rebellion. Even though O’Brien was able to quash Winston’s humanity through psychological torture in Room 101, he cannot destroy humanity in every single prole because of their sheer numbers. It’s even indicated that the proles have a higher level of humanity than party members, given that they were able to hold on to the “primitive emotions” that Winston had to relearn. These primitive emotions could lead to “...mute protest in your own bones, the instinctive feeling that the conditions you lived in were intolerable and that at some other time they must have been different” (73). Once the proles realize this, they will fight for each other and not for the Party. And because this is a result of the primitive emotions ingrained in each and every prole, it is only a matter of time before they rise up. These are the foundations for the race of conscious beings that must one day come and defeat the Party. Although hope can be hard to hold onto, especially in a totalitarian regime like the Party in 1984, it can never be truly lost as long as the proles retain their humanity and continue their bloodline. Ultimately, it makes sense that Orwell’s message during a time of totalitarian regimes globally is that there is some hope in fighting against them. Logically, it follows that the best chance of triumph over the tyranny of a few elite must be the disillusionment of the masses. Stomping out a rebellion of the proletariat class requires crushing each person’s humanity individually. A regime where power lies in the hands of a few can never do this, because the proles completely outnumber the elites and can always persist and fight. This is why Orwell’s optimism lies with the masses and why a generation of conscious individuals with numbers and beliefs is more powerful than any corrupt establishment. In short, if there is hope, it lies with the proles."


sample = pd.read_csv("clean_full_100k_rows.csv")

writing = sample["student_final_writing"]

writing = writing.tolist()

writing = sample.dropna(subset=['student_final_writing'])["student_final_writing"]

print(sample)

essay_doc = nlp(essay_text)



get_transition_matches(essay_doc)

for essay in writing:
    writing_doc = nlp(essay)
    get_transition_matches(writing_doc)