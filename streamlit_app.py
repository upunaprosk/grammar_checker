from viz import *

spacy_model = "en_grammar_checker"
default_text = """Nowadays modern society demands not only father, but mother to work. It is undoubtedly, that such situation affects the relationships between parents and their children. As adults spend a lot of time working, children have not enough time to communicate with them. 
Firstly, we should highlight the reasons why does it happen. Taking into consideration Russia, that we now living in the period of economical crisis. It is getting harder and harder for families to pay for everything: starting from rent, medicine, food and ending with children's education and leisure time. Trying to cope with economical family problems women often had to work. Trying to give children more, they take from them the most important thing - communication with their parents. For example, parents dream to give their children a present - a journey to Disneyland. To make this dream happen they should work hard and a lot. But their plans may be ruined, because they had not enough time to ask their children whether they wanted this journey or not. 
Moreover, we should not forget to point out situations, when mother decides to go to work not because of the lack of money, but because she needs to show the society her professional skills, needs self realisation. 
These reasons may lead to some serious problems. Firstly, such situation may damage the system of communication between children and parents. For example, when children gets from their parents only money, but no care and support, they may start to consider them to be just "money-givers". They would not listen to them, would not do anything their parents want without receiving money. More than that, children may be just hurt by the lack of parenting. And it may cause the situation when children simply get angry with their parents and do not want to communicate with them no longer, because they think that their parent do not care about them. 
But it is not the worth that can happen when parents spend too much time on their work and ignore their children. Unfortunately, I know many example, when children who spend their spare time on their own get to know the dark sides of life such as tobacco, alcohol and even drugs. 
All things considered, it is clear that it is a mistake for parents to think that gaining money for their children may replace their love, care and support. Regardless, the whole economical and self realisation problems they should be firstly parents and only then employees. 
"""

visualize(spacy_model, default_text)


