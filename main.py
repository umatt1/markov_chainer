import numpy as np
import PySimpleGUI as sg
import clipboard


def generate_nth_order_markov_model(sentences, n=1):
    """
    sentences: list of statements to build markov model using
    n: integer of order of markov model. default = 1
    returns markov model dictionary {n length string tuples: string}
    """
    markov_model = {}
    for sentence in sentences:
        if sentence == "" or sentence == " ":
            continue
        sentence = sentence.split()
        for i in range(n):
            sentence.insert(0, "*S*")
        sentence.append("*E*")
        for i in range(0, len(sentence)-n):
            words = tuple(sentence[i:i+n])
            # check if words are in the markov model
            if words in markov_model.keys():
                # if they are, either increment the new word
                if sentence[i+n] in markov_model[words].keys():
                    markov_model[words][sentence[i+n]] += 1
                # or add the new word
                else:
                    markov_model[words][sentence[i+n]] = 1
            # if not, add to the markov model
            else:
                markov_model[words] = {}
                markov_model[words][sentence[i+n]] = 1
    return markov_model


def traverse_nth_order_markov_model(markov_model, n=1, seed=69420):
    """
    generate a read of markov model
    markov_model = dictionary of dictionaries
    n = order of model
    seed = seed for numpy
    return string
    """
    np.random.seed(seed)
    to_return = ""
    # start at the however many starts
    start = ("*S*",) * n
    item_counts = markov_model[start]
    total = 0
    for count in item_counts.keys():
        total += item_counts[count]
    item_probabilities = [markov_model[start][x]/total for x in markov_model[start].keys()]
    word = np.random.choice(list(item_counts.keys()), p=item_probabilities)
    while word != "*E*":
        to_return += (word + " ")
        start = list(start)
        start.pop(0)
        start.append(word)
        start = tuple(start)
        item_counts = markov_model[start]
        total = 0
        for count in item_counts.keys():
            total += item_counts[count]
        item_probabilities = [markov_model[start][x] / total for x in markov_model[start].keys()]
        word = np.random.choice(list(item_counts.keys()), p=item_probabilities)
    return to_return[:-1]

kanyeTweets = """Have you ever thought you were in love with someone but then realized you were just staring in a mirror for 20 minutes?
I hate when I'm on a flight and I wake up with a water bottle next to me like oh great now I gotta be responsible for this water bottle
I make awesome decisions in bike stores!!!
I specifically ordered persian rugs with cherub imagery!!! What do I have to do to get a simple persian rug with cherub imagery uuuuugh
Man... ninjas are kind of cool... I just don't know any personally
Sometimes I push the door close button on people running towards the elevator. I just need my own elevator sometimes. My sanctuary.
Floral arrangement is crazy nice right now ... these are manifique... I hope that's how it's spelled in France language lol!!!
Don't you hate when people clap to loud in the car... it's like yo this is a closed area... your clapping is waaay to loud!!! hahahahahaaa
My favorite unit of measurement is a 'shit load'
Fuck any game company that puts in-app purchases on kids games!!!
you may be talented, but you're not kanye west
Sometimes I get emotional over fonts
I wish I could run across a beach into my own arms
I need a room full of mirrors so I can be surrounded by winners.
I screen grabbed those pants and sent it to my style team #Wizwearscoolpants
I went to look at your twitter and you were wearing cool pants
You have distracted from my creative process
Super inspired by my visit to Ikea today , really amazing company... my mind is racing with the possibilities ...
I need this horse... Kings need horses
Mosquitos suck
Kim doesn't understand what a blessing I am to her
I'm so hype right now   everything has changed... have ya'll ever seen Tron? The end of the Tron where everything light up!!!
I always misspell genius SMH! irony!
truth is my goal. Controversy is my gym. I'll do a hundred reps of controversy for a 6 pack of truth
There's love stories. Pain happiness. It's 3 dementional. There's taste touch sound. It's the most entertaining for of entertainment. Just being. We believe time is a man made construct. Actually time and money are both man made currency. Because you can spend them both.
"""

bookOfGenesis = """1 In the beginning God created the heaven and the earth.
2 And the earth was without form and void, and darkness was upon the deep, and the Spirit of God moved upon the waters.
3 Then God said, Let there be light; And there was light.
4 And God saw the light that it was good, and God separated the light from the darkness.
5 And God called the Light, Day, and the darkness he called Night. So the evening and the morning were the first day.
6 ¶ Again God said, Let there be a firmament in the midst of the waters, and let it separate the waters from the waters.
7 Then God made the firmament, and separated the waters, which were under the firmament, from the waters which were above the firmament; and it was so.
8 And God called the firmament Heaven. So the Evening and the morning were the second day.
9 ¶ God said again, Let the waters under the heaven be gathered into one place, and let the dry land appear; and it was so.
10 And God called the dry land, Earth, and he called the gathering together of the waters, Seas; and God saw that it was good.
11 Then God said, Let the earth bud forth the bud of the herb, that seedeth seed, the fruitful tree, which beareth fruit according to his kind, which hath his seed in itself upon the earth; and it was so.
4
12 And the earth brought forth the bud of the herb, that seedeth seed according to his kind, also the tree that beareth fruit, which hath his seed in itself according to his kind; and God saw that it was good.
13 So the evening and the morning were the third day.
14 ¶ And God said, Let there be lights in the firmament of the heaven, to separate the day from the night, and let them be for signs, and for seasons, and for days, and years;
15 And let them be for lights in the firmament of the heaven to give light upon the earth; and it was so.
16 God then made two great lights, the greater light to rule the day, and the lesser light to rule the night; he made also the stars.
17 And God set them in the firmament of the heaven, to shine upon the earth,
18 And to rule in the day, and in the night, and to separate the light from the darkness; and God saw that it was good.
19 So the evening and the morning were the fourth day.
20 Afterward God said, Let the waters bring forth in abundance every creeping thing that hath life, and let the fowl fly upon the earth in the open firmament of the heaven.
21 Then God created the great whales, and everything living and moving, which the waters brought forth in abundance according to their kind, and every feathered fowl according to his kind; and God saw that it was good.
22 Then God blessed them, saying, Bring forth fruit and multiply, and fill the waters in the seas, and let the fowl multiply in the earth.
23 So the evening and the morning were the fifth day.
24 ¶ Moreover God said, Let the earth bring forth the living thing according to his kind, cattle, and that which creepeth, and the beast of the earth according to his kind; and it was so.
25 And God made the beast of the earth according to his kind, and the cattle according to his kind, and every creeping thing of the earth according to his kind; and God saw that it was good.
5

26 Furthermore God said, Let us make man in our image according to our likeness, and let them rule over the fish of the sea, and over the fowl of the heaven, and over the beasts, and over all the earth, and over everything that creepeth and moveth on the earth.
27 Thus God created the man in his image, in the image of God created he him; he created them male and female.
28 And God blessed them, and God said to them, Bring forth fruit, and multiply, and fill the earth, and subdue it, and rule over the fish of the sea, and over the fowl of the heaven, and over every beast that moveth upon the earth.
29 And God said, Behold, I have given unto you every herb bearing seed, which is upon all the earth, and every tree, wherein is the fruit of a tree bearing seed; that shall be to you for meat;
30 Likewise to every beast of the earth, and to every fowl of the heaven, and to everything that moveth upon the earth, which hath life in itself, every green herb shall be for meat; and it was so.
31 And God saw all that he had made, and lo, it was very good. So the evening and the morning were the sixth day.
Genesis 2
2 God resteth the seventh day, and sanctified it. 15 He sitteth man in the garden. 22 He createth the woman. 24 Marriage is ordained.
1 Thus the heavens and the earth were finished, and all the host of them.
2 For in the seventh day God ended his work which he had made, and the seventh day he rested from all his work, which he had made.
3 So God blessed the seventh day, and sanctified it, because that in it he had rested from all his work, which God had created and made.
6

4 ¶ These are the generations of the heavens and of the earth, when they were created, in the day that the LORD God made the earth and the heavens,
5 And every plant of the field, before it was in the earth, and every herb of the field, before it grew, for the LORD God had not caused it to rain upon the earth, neither was there a man to till the ground,
6 But a mist went up from the earth, and watered all the earth.
7 ¶ The LORD God also made the man of the dust of the ground, and breathed in his face breath of life, and the man was a living soul.
8 And the LORD God planted a garden Eastward in Eden, and there he put the man whom he had made.
9 (For out of the ground made the LORD God to grow every tree pleasant to the sight, and good for meat; the tree of life also in the midst of the garden, and the tree of knowledge of good and of evil.
10 And out of Eden went a river to water the garden, and from thence it was divided, and became into four heads.
11 The name of one is Pishon; the same compasseth the whole land of Havilah, where is gold.
12 And the gold of that land is good; there is Bdellium, and the Onyx stone. 13 And the name of the second river is Gihon; the same compasseth the whole
land of Cush.
14 The name also of the third river is Hiddekel; this goeth toward the Eastside of Asshur. And the fourth river is Perath.)
15 ¶ Then the LORD God took the man, and put him into the garden of Eden, that he might dress it and keep it.
16 And the LORD God commanded the man, saying, Thou shalt eat freely of every tree of the garden,
17 But of the tree of knowledge of good and evil, thou shalt not eat of it, for in the day that thou eatest thereof, thou shalt die the death.
7

18 Also the LORD God said, It is not good that the man should be himself alone; I will make him a help meet for him.
19 So the LORD God formed of the earth every beast of the field, and every fowl of the heaven, and brought them unto the man to see how he would call them; for howsoever the man named the living creature, so was the name thereof.
20 The man therefore gave names unto all cattle, and to the fowl of the heaven, and to every beast of the field, but for Adam found he not a help meet for him.
21 ¶ Therefore the LORD God caused a heavy sleep to fall upon the man, and while he slept, he took one of his ribs, and closed up the flesh instead thereof.
22 And the rib which the LORD God had taken from the man, made he a woman, and brought her to the man.
23 Then the man said, This now is bone of my bones, and flesh of my flesh. She shall be called woman, because she was taken out of man.
24 Therefore shall man leave his father and his mother, and shall cleave to his wife, and they shall be one flesh.
25 And they were both naked, the man and his wife, and were not ashamed.
Genesis 3
1 The woman seduced by the serpent, 6 enticeth her husband to sin. 8 They both flee from God. 14 They three are punished. 15 Christ is promised. 19 Man is dust. 22 Man is cast out of Paradise.
1 Now the serpent was more subtil than any beast of the field, which the LORD God had made. And he said to the woman, Yea, hath God indeed said, Ye shall not eat of every tree of the garden?
2 And the woman said unto the serpent, We eat of the fruit of the trees of the garden,
8

3 But of the fruit of the tree which is in the midst of the garden, God hath said, Ye shall not eat of it, neither shall ye touch it, lest ye die.
4 Then the serpent said to the woman, Ye shall not die at all,
5 But God doth know that when ye shall eat thereof, your eyes shall be opened, and ye shall be as gods, knowing good and evil.
6 So the woman (seeing that the tree was good for meat, and that it was pleasant to the eyes, and a tree to be desired to get knowledge) took of the fruit thereof, and did eat, and gave also to her husband with her, and he did eat.
7 Then the eyes of them both were opened, and they knew that they were naked, and they sewed fig tree leaves together, and made themselves breeches.
8 ¶ Afterward they heard the voice of the LORD God walking in the garden in the cool of the day, and the man and his wife hid themselves from the presence of the LORD God among the trees of the garden.
9 But the LORD God called to the man, and said unto him, Where art thou?
10 Who said, I heard thy voice in the garden, and was afraid, because I was naked, therefore I hid myself.
11 And he said, Who told thee that thou wast naked? Hast thou eaten of the tree, whereof I commanded thee that thou shouldest not eat?
12 Then the man said, The woman which thou gavest to be with me, she gave me of the tree, and I did eat.
13 And the LORD God said to the woman, Why hast thou done this? And the woman said, The serpent beguiled me, and I did eat.
14 ¶ Then the LORD God said to the serpent, Because thou hast done this, thou art cursed above all cattle, and above every beast of the field; upon thy belly shalt thou go, and dust shalt thou eat all the days of thy life.
15 I will also put enmity between thee and the woman, and between thy seed and her seed. He shall break thy head, and thou shalt bruise his heel.
16 ¶ Unto the woman he said, I will greatly increase thy sorrows, and thy conceptions. In sorrow shalt thou bring forth children, and thy desire shall be subject to thy husband, and he shall rule over thee.
9

17 ¶ Also to Adam he said, Because thou hast obeyed the voice of thy wife, and hast eaten of the tree, (whereof I commanded thee, saying, Thou shalt not eat of it) cursed is the earth for thy sake; in sorrow shalt thou eat of it all the days of thy life.
18 Thorns also and thistles shall it bring forth to thee; and thou shalt eat the herb of the field;
19 In the sweat of thy face shalt thou eat bread, till thou return to the earth, for out of it wast thou taken, because thou art dust, and to dust shalt thou return.
20 (And the man called his wife’s name Eve, because she was the mother of all living.)
21 Unto Adam also and to his wife did the LORD God make coats of skins, and clothed them.
22 ¶ And the LORD God said, Behold, the man is become as one of us, to know good and evil. And now lest he put forth his hand, and take also of the tree of life and eat and live forever,
23 Therefore the LORD God sent him forth from the garden of Eden, to till the earth, whence he was taken.
24 Thus he cast out man, and at the Eastside of the garden of Eden he set the Cherubims, and the blade of a sword shaken, to keep the way of the tree of life.
Genesis 4
1 The generation of mankind. 3 Cain and Abel offer sacrifice. 8 Cain killeth Abel. 23 Lamech a tyrant encourageth his fearful wives. 26 True religion is restored.
1 Afterward the man knew Eve his wife, which conceived and bare Cain, and said, I have obtained a man by the LORD.
10

2 And again she brought forth his brother Abel, and Abel was a keeper of sheep, and Cain was a tiller of the ground.
3 ¶ And in process of time it came to pass, that Cain brought an oblation unto the LORD of the fruit of the ground.
4 And Abel also himself brought of the firstfruits of his sheep, and of the fat of them, and the LORD had respect unto Abel, and to his offering,
5 But unto Cain and to his offering he had no regard. Wherefore Cain was exceeding wroth, and his countenance fell down.
6 Then the LORD said unto Cain, Why art thou wroth? And why is thy countenance cast down?
7 If thou do well, shalt thou not be accepted? And if thou doest not well, sin lieth at the door; also unto thee his desire shall be subject, and thou shalt rule over him.
8 ¶ Then Cain spake unto Abel his brother. And when they were in the field, Cain rose up against Abel his brother, and slew him.
9 Then the LORD said unto Cain, Where is Abel thy brother? Who answered, I cannot tell. Am I my brother’s keeper?
10 Again he said, What hast thou done? The voice of thy brother’s blood crieth unto me from the ground.
11 Now therefore thou art cursed from the earth, which hath opened her mouth to receive thy brother’s blood from thy hand.
12 When thou shalt till the ground, it shall not henceforth yield unto thee her strength; a vagabond and a renegade shalt thou be in the earth.
13 Then Cain said to the LORD, My punishment is greater than I can bear.
14 Behold, thou hast cast me out this day from the earth, and from thy face shall I be hid, and shall be a vagabond, and a renegade in the earth, and whosoever findeth me shall slay me.
15 Then the LORD said unto him, Doubtless whosoever slayeth Cain, he shall be punished sevenfold. And the LORD set a mark upon Cain, lest any man finding him should kill him.
11

16 Then Cain went out from the presence of the LORD, and dwelt in the land of Nod toward the Eastside of Eden.
17 Cain also knew his wife, which conceived and bare Enoch; and he built a city, and called the name of the city by the name of his son, Enoch.
18 And to Enoch was born Irad, and Irad begat Mehujael, and Mehujael begat Methushael, and Methushael begat Lamech.
19 ¶ And Lamech took him two wives: the name of the one was Adah, and the name of the other Zillah.
20 And Adah bare Jabal, who was the father of such as dwell in the tents, and of such as have cattle.
21 And his brother’s name was Jubal, who was the father of all that play on the harp and organs.
22 And Zillah also bare Tubal-Cain, who wrought cunningly every craft of brass and of iron; and the sister of Tubal-Cain was Naamah.
23 Then Lamech said unto his wives, Adah and Zillah, Hear my voice, ye wives of Lamech, hearken unto my speech, for I would slay a man in my wound; and a young man in my hurt;
24 If Cain shall be avenged sevenfold, truly Lamech seventy times sevenfold.
25 ¶ And Adam knew his wife again, and she bare a son, and she called his name Seth, for God, said she, hath appointed me another seed for Abel, because Cain slew him.
26 And to the same Seth also there was born a son, and he called his name Enosh. Then began men to call upon the Name of the LORD.
12

Genesis 5
1 The genealogy. 5 The age and death of Adam. 6 His succession unto Noah and his children. 24 Enoch was taken away.
1 This is the book of the generations of Adam. In the day that God created Adam, in the likeness of God made he him,
2 Male and female created he them, and blessed them, and called their name Adam in the day that they were created.
3 ¶ Now Adam lived a hundred and thirty years, and begat a child in his own likeness after his image, and called his name Seth.
4 And the days of Adam, after he had begotten Seth, were eight hundred years, and he begat sons and daughters.
5 So all the days that Adam lived, were nine hundred and thirty years, and he died.
6 And Seth lived a hundred and five years, and begat Enosh.
7 And Seth lived, after he begat Enosh, eight hundred and seven years, and begat sons and daughters.
8 So all the days of Seth were nine hundred and twelve years, and he died.
9 ¶ Also Enosh lived ninety years, and begat Kenan.
10 And Enosh lived after he begat Kenan, eight hundred and fifteen years, and begat sons and daughters.
11 So all the days of Enosh were nine hundred and five years, and he died
12 ¶ Likewise Kenan lived seventy years, and begat Mahalalel.
13 And Kenan lived, after he begat Mahalalel, eight hundred and forty years, and begat sons and daughters.
14 So all the days of Kenan were nine hundred and ten years, and he died. 15 ¶ Mahalalel also lived sixty and five years, and begat Jered.
13

16 Also Mahalalel lived, after he begat Jered, eight hundred and thirty years, and begat sons and daughters.
17 So all the days of Mahalalel were eight hundred ninety and five years, and he died.
18 ¶ And Jered lived a hundred sixty and two years, and begat Enoch.
19 Then Jered lived, after he begat Enoch, eight hundred years, and begat sons and daughters.
20 So all the days of Jered were nine hundred sixty and two years, and he died.
21 ¶ Also Enoch lived sixty and five years, and begat Methuselah.
22 And Enoch walked with God, after he begat Methuselah, three hundred years, and begat sons and daughters.
23 So all the days of Enoch were three hundred sixty and five years.
24 And Enoch walked with God; and he was no more seen, for God took him away.
25 Methuselah also lived a hundred eighty and seven years, and begat Lamech.
26 And Methuselah lived, after he begat Lamech, seven hundred eighty and two years, and begat sons and daughters.
27 So all the days of Methuselah were nine hundred sixty and nine years, and he died.
28 ¶ Then Lamech lived a hundred eighty and two years, and begat a son,
29 And called his name Noah, saying, This same shall comfort us concerning our work and sorrow of our hands, as touching the earth, which the LORD hath cursed.
30 And Lamech lived, after he begat Noah, five hundred ninety and five years, and begat sons and daughters.
31 So all the days of Lamech were seven hundred seventy and seven years, and he died.
14

32 And Noah was five hundred years old. And Noah begat Shem, Ham, and Japheth.
Genesis 6
3 God threateneth to bring the flood. 5 Man altogether corrupt. 6 God repenteth that he made him. 18 Noah and his are preserved in the Ark, which he was commanded to make.
1 So when men began to be multiplied upon the earth, and there were daughters born unto them,
2 Then the sons of God saw the daughters of men that they were fair, and they took them wives of all that they liked.
3 Therefore the LORD said, My Spirit shall not alway strive with man, because he is but flesh, and his days shall be a hundred and twenty years.
4 There were giants in the earth in those days, yea, and after that the sons of God came unto the daughters of men, and they had born them children, these were mighty men, which in old time were men of renown.
5 ¶ When the LORD saw that the wickedness of man was great in the earth, and all the imaginations of the thoughts of his heart were only evil continually,
6 Then it repented the LORD, that he had made man in the earth, and he was sorry in his heart.
7 Therefore the LORD said, I will destroy from the earth the man, whom I have created, from man to beast, to the creeping thing, and to the fowl of the heaven; for I repent that I have made them.
8 But Noah found grace in the eyes of the LORD.
9 ¶ These are the generations of Noah. Noah was a just and upright man in his time; and Noah walked with God.
15

10 And Noah begat three sons, Shem, Ham and Japheth.
11 The earth also was corrupt before God, for the earth was filled with cruelty.
12 Then God looked upon the earth, and behold, it was corrupt; for all flesh had corrupted his way upon the earth.
13 And God said unto Noah, An end of all flesh is come before me; for the earth is filled with cruelty through them; and behold, I will destroy them with the earth.
14 ¶ Make thee an Ark of pine trees; thou shalt make cabins in the Ark, and shalt pitch it within and without with pitch.
15 And thus shalt thou make it: The length of the Ark shall be three hundred cubits, the breadth of it fifty cubits, and the height of it thirty cubits.
16 A window shalt thou make in the Ark, and in a cubit shalt thou finish it above, and the door of the Ark shalt thou set in the side thereof; thou shalt make it with the low, second, and third room.
17 And I, behold, I will bring a flood of waters upon the earth to destroy all flesh, wherein is the breath of life under the heaven; all that is in the earth shall perish.
18 But with thee will I establish my covenant, and thou shalt go into the Ark, thou, and thy sons, and thy wife, and thy sons’ wives with thee.
19 And of every living thing of all flesh, two of every sort shalt thou cause to come into the Ark, to keep them alive with thee; they shall be male and female.
20 Of the fowls after their kind, and of the cattle after their kind, of every creeping thing of the earth after his kind, two of every sort shall come unto thee, that thou mayest keep them alive.
21 And take thou with thee of all meat that is eaten, and thou shalt gather it to thee; that it may be meat for thee and for them.
22 Noah therefore did according unto all that God commanded him, even so did he.
16

Genesis 7
1 Noah and his, enter into the Ark. 20 The flood destroyeth all the rest upon the earth.
1 And the LORD said unto Noah, Enter thou and all thy house into the Ark, for thee have I seen righteous before me in this age.
2 Of every clean beast thou shalt take to thee by sevens, the male and his female; but of unclean beasts by couples, the male and his female.
3 Of the fowls also of the heaven by sevens, male and female, to keep seed alive upon the whole earth.
4 For seven days hence I will cause it to rain upon the earth forty days and forty nights; and all the substance that I have made, will I destroy from off the earth.
5 Noah therefore did according unto all that the LORD commanded him.
6 And Noah was six hundred years old, when the flood of waters was upon the earth.
7 ¶ So Noah entered and his sons, and his wife, and his sons’ wives with him into the Ark, because of the waters of the flood.
8 Of the clean beasts, and of the unclean beasts, and of the fowls, and of all that creepeth upon the earth,
9 There came two and two unto Noah into the Ark, male and female, as God had commanded Noah.
10 And so after seven days, the waters of the flood were upon the earth.
11 ¶ In the six hundredth year of Noah’s life, in the second month, the seventeenth day of the month, in the same day were all the fountains of the great deep broken up, and the windows of heaven were opened,
12 And the rain was upon the earth forty days and forty nights.
13 In the selfsame day entered Noah with Shem, and Ham, and Japheth, the sons of Noah, and Noah’s wife, and the three wives of his sons with them into the Ark.
17

14 They and every beast after his kind, and all cattle after their kind, and every thing that creepeth and moveth upon the earth after his kind, and every fowl after his kind, even every bird of every feather.
15 For they came to Noah into the Ark, two and two, of all flesh wherein is the breath of life.
16 And they entering in, came male and female of all flesh, as God had commanded him; and the LORD shut him in.
17 Then the flood was forty days upon the earth, and the waters were increased, and bare up the Ark, which was lifted up above the earth.
18 The waters also waxed strong, and were increased exceedingly upon the earth, and the Ark went upon the waters.
19 The waters prevailed so exceedingly upon the earth, that all the high mountains, that are under the whole heaven, were covered.
20 Fifteen cubits upward did the waters prevail, when the mountains were covered.
21 Then all flesh perished that moved upon the earth, both fowl and cattle and beast, and everything that creepeth and moveth upon the earth, and every man.
22 Everything in whose nostrils the spirit of life did breath, whatsoever they were in the dry land, they died.
23 So he destroyed everything that was upon the earth, from man to beast, to the creeping thing, and to the fowl of the heaven, they were even destroyed from the earth. And Noah only remained, and they that were with him in the Ark.
24 And the waters prevailed upon the earth a hundred and fifty days.
18

Genesis 8
13 The flood ceaseth. 16 Noah is commanded to come forth of the Ark with his. 20 He sacrificeth to the LORD. 22 God promiseth that all things should continue in their first order.
1 Now God remembered Noah and every beast, and all the cattle that was with him in the Ark; therefore God made a wind to pass upon the earth, and the waters ceased.
2 The fountains also of the deep and the windows of heaven were stopped, and the rain from heaven was restrained,
3 And the waters returned from above the earth, going and returning, and after the end of the hundred and fiftieth day the waters abated.
4 And in the seventh month, in the seventeenth day of the month, the Ark rested upon the mountains of Ararat.
5 And the waters were going and decreasing until the tenth month; in the tenth month, and in the first day of the month, were the tops of the mountains seen.
6 ¶ So after forty days, Noah opened the window of the Ark which he had made;
7 And sent forth a raven, which went out going forth and returning, until the waters were dried up upon the earth.
8 Again he sent a dove from him, that he might see if the waters were diminished from off the earth.
9 But the dove found no rest for the sole of her foot, therefore she returned unto him into the Ark (for the waters were upon the whole earth) and he put forth his hand, and took her, and pulled her to him into the Ark.
10 And he abode yet other seven days, and again he sent forth the dove out of the Ark.
11 And the dove came to him in the evening, and lo, in her mouth was an olive leaf that she had plucked; whereby Noah knew that the waters were abated from off the earth.
19

12 Notwithstanding, he waited yet other seven days, and sent forth the dove, which returned not again unto him anymore.
13 ¶ And in the six hundredth and one year, in the first day of the first month, the waters were dried up from off the earth; and Noah removed the covering of the Ark, and looked, and behold, the upper part of the ground was dry.
14 And in the second month, in the seven and twentieth day of the month, was the earth dry.
15 ¶ Then God spake to Noah, saying,
16 Go forth of the Ark, thou, and thy wife, and thy sons, and thy sons’ wives with thee.
17 Bring forth with thee every beast that is with thee, of all flesh, both fowl and cattle, and every thing that creepeth and moveth upon the earth, that they may breed abundantly in the earth, and bring forth fruit and increase upon the earth.
18 So Noah came forth, and his sons, and his wife, and his sons’ wives with him.
19 Every beast, every creeping thing, and every fowl, all that moveth upon the earth, after their kinds went out of the Ark.
20 ¶ Then Noah built an altar to the LORD, and took of every clean beast, and of every clean fowl, and offered burnt offerings upon the altar.
21 And the LORD smelled a savor of rest; and the LORD said in his heart, I will henceforth curse the ground no more for man’s cause, for the imagination of man’s heart is evil, even from his youth; neither will I smite anymore all things living, as I have done.
22 Hereafter seed time and harvest, and cold and heat, and summer and winter, and day and night shall not cease, so long as the earth remaineth.
20

Genesis 9
1 The confirmation of marriage. 2 Man's authority over all creatures. 3 Permission of meats. 6 The power of the sword. 14 The rainbow is the sign of God's promise. 21 Noah is drunken, and mocked of his son, whom he curseth. 29 The age and death of Noah.
1 And God blessed Noah and his sons, and said to them, Bring forth fruit, and multiply, and replenish the earth.
2 Also the fear of you, and the dread of you shall be upon every beast of the earth, and upon every fowl of the heaven, upon all that moveth on the earth, and upon all the fishes of the sea; into your hand are they delivered.
3 Every thing that moveth and liveth, shall be meat for you; as the green herb, have I given you all things.
4 But flesh with the life thereof, I mean, with the blood thereof, shall ye not eat.
5 For surely I will require your blood, wherein your lives are; at the hand of every beast will I require it, and at the hand of man, even at the hand of a man’s brother will I require the life of man.
6 Who so sheadeth man’s blood, by man shall his blood be shed, for in the image of God hath he made man.
7 But bring ye forth fruit and multiply; grow plentifully in the earth, and increase therein.
8 ¶ God spake also to Noah and to his sons with him, saying,
9 Behold, I, even I establish my covenant with you, and with your seed after you,
10 And with every living creature that is with you, with the fowl, with the cattle, and with every beast of the earth with you, from all that go out of the Ark, unto every beast of the earth.
11 And my covenant will I establish with you, that from henceforth all flesh shall not be rooted out by the waters of the flood, neither shall there be a flood to destroy the earth anymore.
21

12 Then God said, This is the token of the covenant which I make between me and you, and between every living thing that is with you, unto perpetual generations.
13 I have set my bow in the cloud, and it shall be for a sign of the covenant between me and the earth.
14 And when I shall cover the earth with a cloud, and the bow shall be seen in the cloud,
15 Then will I remember my covenant, which is between me and you, and between every living thing in all flesh; and there shall be no more waters of a flood to destroy all flesh.
16 Therefore the bow shall be in the cloud, that I may see it, and remember the everlasting covenant between God, and every living thing in all flesh that is upon the earth.
17 God said yet to Noah, This is the sign of the covenant, which I have established between me and all flesh that is upon the earth.
18 ¶ Now the sons of Noah going forth of the Ark, were Shem and Ham and Japheth. And Ham is the father of Canaan.
19 These are the three sons of Noah, and of them was the whole earth overspread.
20 Noah also began to be a husbandman, and planted a vineyard.
21 And he drunk of the wine, and was drunken; and was uncovered in the midst
of his tent.
22 And when Ham the father of Canaan saw the nakedness of his father, he told his two brethren without.
23 Then took Shem and Japheth a garment, and put it upon both their shoulders, and went backward, and covered the nakedness of their father with their faces backward; so they saw not their father’s nakedness.
24 Then Noah awoke from his wine, and knew what his younger son had done unto him,
22

25 And said, Cursed be Canaan; a servant of servants shall he be unto his brethren.
26 He said moreover, Blessed be the LORD God of Shem, and let Canaan be his servant.
27 God persuaded Japheth, that he may dwell in the tents of Shem, and let Canaan be his servant.
28 ¶ And Noah lived after the flood three hundred and fifty years.
29 So all the days of Noah were nine hundred and fifty years, and he died.
Genesis 10
1 The increase of mankind by Noah and his sons. 10 The beginning of cities, countries and nations.
1 Now these are the generations of the sons of Noah, Shem, Ham, and Japheth; unto whom sons were born after the flood.
2 The sons of Japheth were Gomer, and Magog, and Madai, and Javan, and Tubal, and Meshech, and Tiras.
3 And the sons of Gomer: Ashkenaz, and Riphath, and Togarmah.
4 Also the sons of Javan: Elishah, and Tarshish, Kittim, and Dodanim.
5 Of these were the isles of the Gentiles divided in their lands, every man after his tongue, and after their families in their nations.
6 ¶ Moreover, the sons of Ham were Cush, and Mizraim, and Put, and Canaan. 7 And the sons of Cush: Seba, and Havilah, and Sabtah, and Raamah, and
Sabtecha; also the sons of Raamah were Sheba and Dedan.
8 And Cush begat Nimrod, who began to be mighty in the earth.
23

9 He was a mighty hunter before the LORD; wherefore it is said, As Nimrod the mighty hunter before the LORD.
10 And the beginning of his kingdom was Babel, and Erech, and Accad, and Calneh, in the land of Shinar.
11 Out of that land came Asshur, and built Nineveh, and the city Rehoboth, and Calah;
12 Resen also between Nineveh and Calah; this is a great city.
13 And Mizraim begat Ludim, and Anamim, and Lehabim, and Naphtuhim.
14 Pathrusim also, and Casluhim (out of whom came the Philistines) and Caphtorims.
15 Also Canaan begat Sidon his firstborn, and Heth,
16 And Jebusite, and Amorite, and Girgasite,
17 And Hivite, and Arkite, and Sinite,
18 And Arvadite, and Zemarite, and Hamathite; and afterward were the families of the Canaanites spread abroad.
19 Then the border of the Canaanites was from Sidon, as thou comest to Gerar until Azzah, and as thou goest unto Sodom, and Gomorrah, and Admah, and Zeboiim, even unto Lasha.
20 These are the sons of Ham according to their families, according to their tongues in their countries, and in their nations.
21 ¶ Unto Shem also the father of all the sons of Eber, and elder brother of Japheth were children born.
22 The sons of Shem were Elam, and Asshur, and Arpakshad, and Lud, and Aram.
23 And the sons of Aram: Uz, and Hul, and Gether, and Mash. 24 Also Arpakshad begat Shelah, and Shelah begat Eber.
24

25 Unto Eber also were born two sons; the name of the one was Peleg, for in his days was the earth divided; and his brother’s name was Joktan.
26 Then Joktan begat Almodad, and Sheleph, and Hazarmaveth, and Jerah, 27 And Hadoram, and Uzal, and Diklah,
28 And Obal, and Abimael, and Sheba,
29 And Ophir, and Havilah, and Jobab; all these were the sons of Joktan.
30 And their dwelling was from Mesha, as thou goest unto Sephar, a mount of the East.
31 These are the sons of Shem, according to their families, according to their tongues, in their countries and nations.
32 These are the families of the sons of Noah, after their generations among their people; and out of these were the nations divided in the earth after the flood.
Genesis 11
6 The building of Babel was the cause of the confusion of tongues. 10 The age and generation of Shem unto Abraham, 31 Abram's departure from Ur, with his father Terah, Sarah and Lot. 32 The age and death of Terah.
1 Then the whole earth was of one language and one speech.
2 And as they went from the East, they found a plain in the land of Shinar, and there they abode.
3 And they said one to another, Come, let us make brick, and burn it in the fire. So they had brick for stone, and slime had they instead of mortar.
4 Also they said, Go to, let us build us a city and a tower, whose top may reach unto the heaven, that we may get us a name, lest we be scattered upon the whole earth.
25

5 But the LORD came down, to see the city and tower, which the sons of men built.
6 And the LORD said, Behold, the people is one, and they all have one language, and this they begin to do, neither can they now be stopped from whatsoever they have imagined to do.
7 Come on, let us go down, and there confound their language, that everyone perceive not another’s speech.
8 So the LORD scattered them from thence upon all the earth, and they left off to build the city.
9 Therefore the name of it was called Babel, because the LORD did there confound the language of all the earth; from thence then did the LORD scatter them upon all the earth.
10 ¶ These are the generations of Shem: Shem was a hundred years old, and begat Arpakshad two years after the flood.
11 And Shem lived after he begat Arpakshad five hundred years, and begat sons and daughters.
12 Also Arpakshad lived five and thirty years, and begat Shelah.
13 And Arpakshad lived after he begat Shelah four hundred and three years, and begat sons and daughters.
14 And Shelah lived thirty years, and begat Eber.
15 So Shelah lived after he begat Eber four hundred and three years, and begat sons and daughters.
16 Likewise Eber lived four and thirty years, and begat Peleg.
17 So Eber lived after he begat Peleg four hundred and thirty years, and begat sons and daughters.
18 And Peleg lived thirty years, and begat Reu.
19 And Peleg lived after he begat Reu two hundred and nine years, and begat sons and daughters.
26

20 Also Reu lived two and thirty years, and begat Serug.
21 So Reu lived after he begat Serug two hundred and seven years, and begat sons and daughters.
22 Moreover Serug lived thirty years, and begat Nahor.
23 And Serug lived after he begat Nahor two hundred years, and begat sons and daughters.
24 And Nahor lived nine and twenty years, and begat Terah.
25 So Nahor lived after he begat Terah a hundred and nineteen years, and begat sons and daughters.
26 So Terah lived seventy years, and begat Abram, Nahor, and Haran.
27 Now these are the generations of Terah: Terah begat Abram, Nahor, and Haran; and Haran begat Lot.
28 Then Haran died before Terah his father in the land of his nativity, in Ur of the Chaldeans.
29 So Abram and Nahor took them wives. The name of Abram’s wife was Sarai, and the name of Nahor’s wife Milcah, the daughter of Haran, the father of Milcah, and the father of Iscah.
30 But Sarai was barren, and had no child.
31 Then Terah took Abram his son, and Lot the son of Haran, his son’s son, and Sarai his daughter in law, his son Abram’s wife; and they departed together from Ur of the Chaldeans, to go into the land of Canaan, and they came to Haran, and dwelt there.
32 So the days of Terah were two hundred and five years, and Terah died in Haran.
27

Genesis 12
1 Abram by God's commandment goeth to Canaan. 3 Christ is promised. 7 Abram buildeth Altars for exercise and declaration of his faith among the infidels. 10 Because of the dearth he goeth into Egypt. 15 Pharaoh taketh his wife, and is punished.
1 For the LORD had said unto Abram, Get thee out of thy country, and from thy kindred, and from thy father’s house unto the land that I will shew thee.
2 And I will make of thee a great nation, and will bless thee, and make thy name great, and thou shalt be a blessing.
3 I will also bless them that bless thee, and curse them that curse thee, and in thee shall all families of the earth be blessed.
4 So Abram departed, even as the LORD spake unto him, and Lot went with him. (And Abram was seventy and five years old, when he departed out of Haran.)
5 Then Abram took Sarai his wife, and Lot his brother’s son, and all their substance that they possessed, and the souls that they had gotten in Haran, and they departed to go to the land of Canaan; and to the land of Canaan they came.
6 ¶ So Abram passed through the land unto the place of Shechem, and unto the plain of Moreh (and the Canaanite was then in the land.)
7 And the LORD appeared unto Abram, and said, Unto thy seed will I give this land. And there built he an altar unto the LORD, which appeared unto him.
8 Afterward removing thence unto a mountain Eastward from Bethel, he pitched his tent having Bethel on the Westside, and Hai on the East; and there he built an altar unto the LORD, and called on the Name of the LORD.
9 Again Abram went forth going and journeying toward the South.
10 ¶ Then there came a famine in the land; therefore Abram went down into Egypt to sojourn there, for there was a great famine in the land.
11 And when he drew near to enter into Egypt, he said to Sarai his wife, Behold now, I know that thou art a fair woman to look upon;
28

12 Therefore it will come to pass, that when the Egyptians see thee, they will say, She is his wife; so will they kill me, but they will keep thee alive.
13 Say, I pray thee, that thou art my sister, that I may fare well for thy sake, and that my life may be preserved by thee.
14 ¶ Now when Abram was come into Egypt, the Egyptians beheld the woman, for she was very fair.
15 And the Princes of Pharaoh saw her, and commended her unto Pharaoh; so the woman was taken into Pharaoh’s house;
16 Who entreated Abram well for her sake, and he had sheep, and beeves, and he asses, and menservants, and maidservants, and she asses, and camels.
17 But the LORD plagued Pharaoh and his house with great plagues, because of Sarai Abram’s wife.
18 Then Pharaoh called Abram, and said, Why hast thou done this unto me? Wherefore didst thou not tell me, that she was thy wife?
19 Why saidst thou, She is my sister, that I should take her to be my wife? Now therefore behold thy wife, take her and go thy way.
20 And Pharaoh gave men commandment concerning him; and they conveyed him forth, and his wife, and all that he had.
Genesis 13
1 Abram departeth out of Egypt. 4 He calleth upon the Name of the LORD. 12 Lot departeth from him. 13 The wickedness of the Sodomites. 14 The promise made to Abram is renewed. 13 Abram buildeth an altar to the LORD.
1 Then Abram went up from Egypt, he, and his wife, and all that he had, and Lot with him toward the South.
2 And Abram was very rich in cattle, in silver and in gold.
29

3 And he went on his journey from the South toward Bethel, to the place where his tent had been at the beginning, between Bethel and Hai,
4 Unto the place of the altar, which he had made there at the first; and there Abram called on the Name of the LORD.
5 ¶ And Lot also, who went with Abram, had sheep, and cattle, and tents,
6 So that the land could not bear them, that they might dwell together, for their substance was great, so that they could not dwell together.
7 Also there was debate between the herdsmen of Abram’s cattle, and the herdsmen of Lot’s cattle. (And the Canaanites and the Perizzites dwelled at that time in the land.)
8 Then said Abram unto Lot, Let there be no strife, I pray thee, between thee and me, neither between my herdsmen and thy herdsmen, for we be brethren.
9 Is not the whole land before thee? Depart I pray thee from me; if thou wilt take the left hand, then I will go to the right; or if thou go to the right hand, then I will take the left.
10 So when Lot lifted up his eyes, he saw that all the plain of Jordan was watered everywhere; (for before the LORD destroyed Sodom and Gomorrah, it was as the garden of the LORD, like the land of Egypt, as thou goest unto Zoar.)
11 Then Lot chose unto him all the plain of Jordan, and took his journey from the East; and they departed the one from the other.
12 Abram dwelled in the land of Canaan, and Lot abode in the cities of the plain, and pitched his tent even unto Sodom.
13 Now the men of Sodom were wicked and exceeding sinners against the LORD.
14 ¶ Then the LORD said unto Abram, (after that Lot was departed from him) Lift up thine eyes now, and look from the place where thou art, Northward, and Southward, and Eastward, and Westward;
15 For all the land which thou seest, will I give unto thee, and to thy seed forever,
30

16 And I will make thy seed as the dust of the earth, so that if a man can number the dust of the earth, then shall thy seed be numbered.
17 Arise, walk through the land, in the length thereof, and breadth thereof; for I will give it unto thee.
18 Then Abram removed his tent, and came and dwelled in the plain of Mamre, which is in Hebron, and built there an altar unto the LORD.
Genesis 14
12 In the overthrow of Sodom, Lot is taken prisoner. 16 Abram delivereth him. 18 Melchizedek cometh to meet him. 23 Abram would not be enriched by the king of Sodom.
1 And in the days of Amraphel King of Shinar, Arioch King of Ellasar, Chedorlaomer King of Elam, and Tidal King of the nations;
2 These men made war with Bera King of Sodom, and with Birsha King of Gomorrah, Shinab King of Admah, and Shemeber King of Zeboiim, and the King of Bela, which is Zoar.
3 All these joined together in the valley of Siddim, which is the Salt Sea.
4 Twelve years were they subject to Chedorlaomer, but in the thirteenth year they rebelled.
5 And in the fourteenth year came Chedorlaomer, and the Kings that were with him, and smote the Rephaims in Ashteroth Karnaim, and the Zuzims in Ham, and the Emims in Shaveh Kiriathaim,
6 And the Horites in their mount Seir, unto the plain of Paran, which is by the wilderness.
7 And they returned and came to En-mishpat, which is Kadesh, and smote all the country of the Amalekites, and also the Amorites that dwelled in Hazezon- tamar.
31

8 Then went out the King of Sodom, and the King of Gomorrah, and the King of Admah, and the King of Zeboiim, and the King of Bela, which is Zoar; and they joined battle with them in the valley of Siddim;
9 To wit, with Chedorlaomer King of Elam, and Tidal King of nations, and Amraphel King of Shinar, and Arioch King of Ellasar; four Kings against five.
10 Now the valley of Siddim was full of slime pits; and the Kings of Sodom and Gomorrah fled and fell there, and the residue fled to the mountain.
11 Then they took all the substance of Sodom and Gomorrah, and all their vitailles, and went their way.
12 They took Lot also Abram’s brother’s son and his substance (for he dwelt at Sodom) and departed.
13 ¶ Then came one that had escaped, and told Abram the Hebrew, which dwelt in the plain of Mamre the Amorite, brother of Eshcol, and brother of Aner, which were confederate with Abram.
14 When Abram heard that his brother was taken, he brought forth of them that were born and brought up in his house, three hundred and eighteen, and pursued them unto Dan.
15 Then he and his servants divided themselves against them by night, and smote them, and pursued them unto Hobah, which is on the left side of Damascus,
16 And he recovered all the substance, and also brought again his brother Lot, and his goods, and the women also and the people.
17 ¶ After that he returned from the slaughter of Chedorlaomer and of the Kings that were with him, came the King of Sodom forth to meet him in the valley of Shaveh, which is the King’s dale.
18 And Melchizedek King of Salem brought forth bread and wine; and he was a Priest of the most high God.
19 Therefore he blessed him, saying, Blessed art thou, Abram, of God most high, Possessor of heaven and earth;
20 And blessed be the most high God, which hath delivered thine enemies into thy hand. And Abram gave him tithe of all.
32

21 Then the King of Sodom said to Abram, Give me the persons, and take the goods to thyself.
22 And Abram said to the King of Sodom, I have lifted up my hand unto the LORD the most high God, possessor of heaven and earth,
23 That I will not take of all that is thine, so much as a thread or shoe latchet, lest thou shouldest say, I have made Abram rich,
24 Save only that, which the young men have eaten, and the parts of the men which went with me, Aner, Eshcol, and Mamre; let them take their parts.
Genesis 15
1 The LORD is Abraham's defence and reward. 6 He is instilled by faith. 13 The servitude and deliverance out of Egypt is declared. 18 The Lord of Canaan is promised the fourth time.
1 After these things, the word of the LORD came unto Abram in a vision, saying, Fear not, Abram, I am thy buckler, and thy exceeding great reward.
2 And Abram said, O Lord GOD, what wilt thou give me, seeing I go childless, and the steward of my house is this Eliezer of Damascus?
3 Again Abram said, Behold, to me thou hast given no seed, wherefore lo, a servant of my house shall be my heir.
4 Then behold, the word of the LORD came unto him, saying, This man shall not be thy heir, but one that shall come out of thy own bowels, he shall be thy heir.
5 Moreover he brought him forth and said, Look up now unto heaven, and tell the stars, if thou be able to number them; and he said unto him, So shall thy seed be.
6 And Abram believed the LORD, and he counted that to him for righteousness.
33

7 Again he said unto him, I am the LORD, that brought thee out of Ur of the Chaldeans, to give thee this land to inherit it.
8 And he said, O Lord GOD, Whereby shall I know that I shall inherit it?
9 Then he said unto him, Take me a heifer of three years old, and a she goat of three years old, and a ram of three years old, a turtle dove also and a pigeon.
10 So he took all these unto him, and divided them into the midst, and laid every piece one against another; but the birds divided he not.
11 Then fowls fell on the carcasses, and Abram drove them away.
12 And when the sun went down, there fell a heavy sleep upon Abram; and lo, a very fearful darkness fell upon him.
13 Then he said to Abram, Know this of a surety, that thy seed shall be a stranger in a land that is not theirs, four hundred years, and shall serve them; and they shall entreat them evil.
14 Notwithstanding, the nation whom they shall serve, will I judge, and afterward shall they come out with great substance.
15 But thou shalt go unto thy fathers in peace, and shalt be buried in a good age. 16 And in the fourth generation they shall come hither again, for the wickedness
of the Amorites is not yet full.
17 Also when the sun went down, there was a darkness, and behold, a smoking furnace, and a firebrand, which went between those pieces.
18 In that same day the LORD made a covenant with Abram, saying, Unto thy seed have I given this land, from the river of Egypt unto the great river, the river Euphrates.
19 The Kenites, and the Kenizzites, and the Kadmonites,
20 And the Hittites, and the Perizzites, and the Rephaims,
21 The Amorites also, and the Canaanites, and the Girgashites, and the Jebusites.
34

Genesis 16
2 Sarai being barren giveth Hagar to Abram. 4 Which conceiveth and despiseth her dame; 6 And being ill handled, fleeth. 7 The Angel comforteth her. 11-12 The name and manners of her son. 13 She calleth upon the LORD, whom she findeth true.
1 Now Sarai Abram’s wife bare him no children, and she had a maid an Egyptian, Hagar by name.
2 And Sarai said unto Abram, Behold now, the LORD hath restrained me from child bearing. I pray thee go in unto my maid; it may be that I shall receive a child by her. And Abram obeyed the voice of Sarai.
3 Then Sarai Abram’s wife took Hagar her maid the Egyptian, after Abram had dwelled ten years in the land of Canaan, and gave her to her husband Abram for his wife.
4 ¶ And he went in unto Hagar, and she conceived, and when she saw that she had conceived, her dame was despised in her eyes.
5 Then Sarai said to Abram, Thou doest me wrong. I have given my maid into thy bosom, and she seeth that she hath conceived, and I am despised in her eyes; the LORD judge between me and thee.
6 Then Abram said to Sarai, Behold, thy maid is in thy hand; do with her as it pleaseth thee. Then Sarai dealt roughly with her, wherefore she fled from her.
7 ¶ But the Angel of the LORD found her beside a fountain of water in the wilderness, by the fountain in the way to Shur,
8 And he said, Hagar Sarai’s maid, whence comest thou? And whither wilt thou go? And she said, I flee from my dame Sarai.
9 Then the Angel of the LORD said to her, Return to thy dame, and humble thyself under her hands.
10 Again the Angel of the LORD said unto her, I will so greatly increase thy seed, that it shall not be numbered for multitude.
35

11 Also the Angel of the LORD said unto her, See, thou art with child, and shalt bear a son, and shalt call his name Ishmael, for the LORD hath heard thy tribulation.
12 And he shall be a wild man, his hand shall be against every man, and every man’s hand against him; and he shall dwell in the presence of all his brethren.
13 Then she called the name of the LORD that spake unto her, Thou God lookest on me; for she said, Have I not also here looked after him that seeth me?
14 Wherefore the well was called, Beer-lahai-roi; lo, it is between Kadesh and Bered.
15 ¶ And Hagar bare Abram a son, and Abram called his son’s name, which Hagar bare, Ishmael.
16 And Abram was fourscore and six years old, when Hagar bare him Ishmael.
Genesis 17
5 Abram's name is changed to confirm him in the promise. 8 The land of Canaan is the first time promised. 12 Circumcision instituted. 15 Sarai is named Sarah. 18 Abraham prayeth for Ishmael. 19 Isaac is promised. 23 Abraham and his house are circumcised.
1 When Abram was ninety years old and nine, the LORD appeared to Abram, and said unto him, I am God all sufficient; walk before me, and be thou upright,
2 And I will make my covenant between me and thee, and I will multiply thee exceedingly .
3 Then Abram fell on his face, and God talked with him, saying,
4 Behold, I make my covenant with thee, and thou shalt be a father of many nations,
5 Neither shall thy name anymore be called Abram, but thy name shall be Abraham; for a father of many nations have I made thee.
36

6 Also I will make thee exceeding fruitful, and will make nations of thee, yea, Kings shall proceed of thee.
7 Moreover I will establish my covenant between me and thee, and thy seed after thee in their generations, for an everlasting covenant, to be God unto thee and to thy seed after thee.
8 And I will give thee and thy seed after thee the land, wherein thou art a stranger, even all the land of Canaan, for an everlasting possession, and I will be their God.
9 ¶ Again God said unto Abraham, Thou also shalt keep my covenant, thou, and thy seed after thee in their generations.
10 This is my covenant which ye shall keep between me and you, and thy seed after thee, Let every man child among you be circumcised;
11 That is, ye shall circumcise the foreskin of your flesh, and it shall be a sign of the covenant between me and you.
12 And every man child of eight days old among you, shall be circumcised in your generations, as well he that is born in thy house, as he that is bought with money of any stranger, which is not of thy seed.
13 He that is born in thy house, and he that is bought with thy money, must needs be circumcised; so my covenant shall be in your flesh for an everlasting covenant.
14 But the uncircumcised man child, in whose flesh the foreskin is not circumcised, even that person shall be cut off from his people, because he hath broken my covenant.
15 ¶ Afterward God said unto Abraham, Sarai thy wife shalt thou not call Sarai, but Sarah shall be her name.
16 And I will bless her, and will also give thee a son of her, yea, I will bless her, and she shall be the mother of nations; Kings also of people shall come of her.
17 Then Abraham fell upon his face, and laughed, and said in his heart, Shall a child be born unto him, that is a hundred years old? And shall Sarah that is ninety years old, bear?
37

18 And Abraham said unto God, Oh, that Ishmael might live in thy sight.
19 Then God said, Sarah thy wife shall bear thee a son indeed, and thou shalt call his name Isaac; and I will establish my covenant with him for an everlasting covenant, and with his seed after him.
20 And as concerning Ishmael, I have heard thee; lo, I have blessed him, and will make him fruitful, and will multiply him exceedingly; twelve princes shall he beget, and I will make a great nation of him.
21 But my covenant will I establish with Isaac, which Sarah shall bear unto thee, the next year at this season.
22 And he left off talking with him, and God went up from Abraham.
23 ¶ Then Abraham took Ishmael his son, and all that were born in his house, and all that was bought with his money, that is, every man child among the men of Abraham’s house, and he circumcised the foreskin of their flesh in that selfsame day, as God had commanded him.
24 Abraham also himself was ninety years old and nine, when the foreskin of his flesh was circumcised.
25 And Ishmael his son was thirteen years old, when the foreskin of his flesh was circumcised.
26 The selfsame day was Abraham circumcised, and Ishmael his son;
27 And all the men of his house, both born in his house, and bought with money of the stranger, were circumcised with him.
38

Genesis 18
2 Abraham receiveth three Angels into his house. 10 Isaac is promised again. 12 Sarah laugheth. 18 Christ is promised to all nations. 19 Abraham taught his family to know God. 21 The destruction of Sodom is declared unto Abraham. 23 Abraham prayeth for them.
1 Again the LORD appeared unto him in the plain of Mamre, as he sat in his tent door about the heat of the day.
2 And he lifted up his eyes, and looked, and lo, three men stood by him, and when he saw them, he ran to meet them from the tent door, and bowed himself to the ground.
3 And he said, Lord, if I have now found favor in thy sight, go not, I pray thee, from thy servant.
4 Let a little water, I pray you, be brought, and wash your feet, and rest yourselves under the tree.
5 And I will bring a morsel of bread, that you may comfort your hearts, afterward ye shall go your ways; for therefore are ye come to your servant. And they said, Do even as thou hast said.
6 Then Abraham made haste into the tent unto Sarah, and said, Make ready at once three measures of fine meal, knead it, and make cakes upon the hearth.
7 And Abraham ran to the beasts, and took a tender and good calf, and gave it to the servant, who hasted to make it ready.
8 And he took butter and milk, and the calf which he had prepared, and set before them, and stood himself by them under the tree, and they did eat.
9 ¶ Then they said to him, Where is Sarah thy wife? And he answered, Behold, she is in the tent.
10 And he said, I will certainly come again unto thee according to the time of life; and lo, Sarah thy wife shall have a son. And Sarah heard in the tent door, which was behind him.
11 (Now Abraham and Sarah were old and stricken in age, and it ceased to be with Sarah after the manner of women.)
39

12 Therefore Sarah laughed within herself, saying, After I am waxed old, and my lord also, shall I have lust?
13 And the LORD said unto Abraham, Wherefore did Sarah thus laugh, saying, Shall I certainly bear a child, which am old?
14 (Shall anything be hard to the LORD? At the time appointed will I return unto thee, even according to the time of life, and Sarah shall have a son.)
15 But Sarah denied, saying, I laughed not; for she was afraid. And he said, It is not so, for thou laughed.
16 ¶ Afterward, the men did rise up from thence, and looked toward Sodom; and Abraham went with them to bring them on the way.
17 And the LORD said, Shall I hide from Abraham that thing which I do,
18 Seeing that Abraham shall be indeed a great and a mighty nation, and all the nations of the earth shall be blessed in him?
19 For I know him that he will command his sons and his household after him, that they keep the way of the LORD, to do righteousness and judgment, that the LORD may bring upon Abraham that he hath spoken unto him.
20 Then the LORD said, Because the cry of Sodom and Gomorrah is great, and because their sin is exceeding grievous,
21 I will go down now, and see whether they have done altogether according to that cry, which is come unto me; and if not, that I may know.
22 And the men turned thence, and went toward Sodom; but Abraham stood yet before the LORD.
23 Then Abraham drew near, and said, Wilt thou also destroy the righteous with the wicked?
24 If there be fifty righteous within the city, wilt thou destroy and not spare the place for the fifty righteous that are therein?
25 Be it far from thee from doing this thing, to slay the righteous with the wicked, and that the righteous should be even as the wicked, be it far from thee. Shall not the Judge of all the world do right?
40

26 And the LORD answered, If I shall find in Sodom fifty righteous within the city, then will I spare all the place for their sakes.
27 Then Abraham answered and said, Behold now, I have begun to speak unto my Lord, and I am but dust and ashes;
28 If there shall lack five of fifty righteous, wilt thou destroy all the city for five? And he said, If I find there five and forty, I will not destroy it.
29 And he yet spake to him again, and said, What if there shall be found forty there? Then he answered, I will not do it for forty’s sake.
30 Again he said, Let not my Lord now be angry, that I speak; What if thirty be found there? Then he said, I will not do it, if I find thirty there.
31 Moreover he said, Behold now, I have begun to speak unto my Lord, What if twenty be found there? And he answered, I will not destroy it for twenty’s sake.
32 Then he said, Let not my Lord be now angry, and I will speak but this once; What if ten be found there? And he answered, I will not destroy it for ten’s sake.
33 ¶ And the LORD went his way when he had left communing with Abraham, and Abraham returned unto his place.
Genesis 19
3 Lot receiveth two Angels into his house. 4 The filthy lusts of the Sodomites. 16 Lot is delivered. 24 Sodom is destroyed. 26 Lot's wife is made a pillar of salt. 33 Lot's daughters lie with their father, of whom come Moab and Ammon.
1 And in the evening there came two Angels to Sodom; and Lot sat at the gate of Sodom, and Lot saw them, and rose up to meet them, and he bowed himself with his face to the ground.
2 And he said, See my lords, I pray you turn in now into your servant’s house, and tarry all night, and wash your feet, and ye shall rise up early and go your ways. Who said, Nay, but we will abide in the street all night.
41

3 Then he pressed upon them earnestly, and they turned in to him, and came to his house, and he made them a feast, and did bake unleavened bread, and they did eat.
4 But before they went to bed, the men of the city, even the men of Sodom compassed the house round about, from the young even to the old, all the people from all quarters.
5 Who crying unto Lot said to him, Where are the men, which came to thee this night? Bring them out unto us, that we may know them.
6 Then Lot went out at the door unto them, and shut the door after him,
7 And said, I pray you, my brethren, do not so wickedly.
8 Behold now, I have two daughters, which have not known man; them will I bring out now unto you, and do to them as seemeth you good; only unto these men do nothing, for therefore are they come under the shadow of my roof.
9 Then they said, Away hence. And they said, He is come alone as a stranger, and shall he judge and rule? We will now deal worse with thee than with them. So they pressed sore upon Lot himself, and came to break the door.
10 But the men put forth their hand, and pulled Lot into the house to them, and shut to the door.
11 Then they smote the men that were at the door of the house with blindness, both small and great, so that they were weary in seeking the door.
12 ¶ Then the men said unto Lot, Whom hast thou yet here? Either son in law, or thy sons, or thy daughters, or whatsoever thou hast in the city, bring it out of this place.
13 For we will destroy this place, because the cry of them is great before the LORD, and the LORD hath sent us to destroy it.
14 Then Lot went out and spake unto his sons in law, which married his daughters, and said, Arise, get you out of this place, for the LORD will destroy the city; but he seemed to his sons in law as though he had mocked.
15 ¶ And when the morning arose, the Angels hasted Lot, saying, Arise, take thy wife and thy two daughters which are here, lest thou be destroyed in the punishment of the city.
42

16 And as he prolonged the time, the men caught both him and his wife, and his two daughters by the hands (the LORD being merciful unto him) and they brought him forth, and set him without the city.
17 ¶ And when they had brought them out, the Angel said, Escape for thy life; look not behind thee, neither tarry thou in all the plain; escape into the mountain, lest thou be destroyed.
18 And Lot said unto them, Not so, I pray thee, my Lord.
19 Behold now, thy servant hath found grace in thy sight, and thou hast magnified thy mercy, which thou hast shewed unto me in saving my life; and I cannot escape in the mountain, lest some evil take me, and I die;
20 See now this city hereby to flee unto, which is a little one; Oh let me escape thither, is it not a little one, and my soul shall live?
21 Then he said unto him, Behold, I have received thy request also concerning this thing, that I will not overthrow this city, for the which thou hast spoken.
22 Haste thee, save thee there, for I can do nothing till thou be come thither. Therefore the name of the city was called Zoar.
23 ¶ The sun did rise upon the earth, when Lot entered into Zoar.
24 Then the LORD rained upon Sodom and upon Gomorrah, brimstone and fire from the LORD out of heaven,
25 And overthrew those cities, and all the plain, and all the inhabitants of the cities; and that which grew upon the earth.
26 ¶ Now his wife behind him looked back, and she became a pillar of salt.
27 ¶ And Abraham rising up early in the morning went to the place, where he had stood before the LORD,
28 And looking toward Sodom and Gomorrah, and toward all the land of the plain, behold, he saw the smoke of the land mounting up as the smoke of a furnace.
43

29 ¶ But yet when God destroyed the cities of the plain, God thought upon Abraham, and sent Lot out from the midst of the destruction, when he overthrew the cities wherein Lot dwelled.
30 ¶ Then Lot went up from Zoar, and dwelt in the mountain with his two daughters; for he feared to tarry in Zoar, but dwelt in a cave, he and his two daughters.
31 And the elder said unto the younger, Our father is old, and there is not a man in the earth to come in unto us after the manner of all the earth.
32 Come, we will make our father drink wine, and lie with him, that we may preserve seed of our father.
33 So they made their father drink wine that night, and the elder went and lay with her father; but he perceived not, neither when she lay down, neither when she rose up.
34 And on the morrow the elder said to the younger, Behold, yesternight lay I with my father; let us make him drink wine this night also, and go thou and lie with him, that we may preserve seed of our father.
35 So they made their father drink wine that night also, and the younger arose, and lay with him; but he perceived not, when she lay down, neither when she rose up.
36 Thus were both the daughters of Lot with child by their father.
37 And the elder bare a son, and she called his name Moab; the same is the father of the Moabites unto this day.
38 And the younger bare a son also, and she called his name Ben-ammi; the same is the father of the Ammonites unto this day.
44

Genesis 20
1 Abraham dwelleth as a stranger in the land of Gerar. 2 Abimelech taketh away his wife. 3 God reproveth the King, 9 and the king Abraham. 11 Sarah is restored with great gifts. 17 Abraham prayeth, and the King and his are healed.
1 Afterward Abraham departed thence toward the South country, and dwelled between Kadesh and Shur, and sojourned in Gerar.
2 And Abraham said of Sarah his wife, She is my sister. Then Abimelech King of Gerar sent and took Sarah.
3 But God came to Abimelech in a dream by night, and said to him, Behold, thou art but dead, because of the woman, which thou hast taken, for she is a man’s wife.
4 (Notwithstanding Abimelech had not yet come near her) And he said, Lord, wilt thou slay even the righteous nation?
5 Said not he unto me, She is my sister? Yea, and she herself said, He is my brother; with an upright mind, and innocent hands have I done this.
6 And God said unto him by a dream, I know that thou didst this even with an upright mind, and I kept thee also that thou shouldest not sin against me; therefore suffered I thee not to touch her.
7 Now then deliver the man his wife again, for he is a Prophet, and he shall pray for thee, that thou mayest live; but if thou deliver her not again, be sure that thou shalt die the death, thou, and all that thou hast.
8 Then Abimelech rising up early in the morning, called all his servants, and told all these things unto them, and the men were sore afraid.
9 Afterward Abimelech called Abraham, and said unto him, What hast thou done unto us? And what have I offended thee, that thou hast brought on me and on my kingdom this great sin? Thou hast done things unto me that ought not to be done.
10 So Abimelech said unto Abraham, What sawest thou that thou hast done this thing?
45

11 Then Abraham answered, Because I thought thus, Surely the fear of God is not in this place, and they will slay me for my wife’s sake.
12 Yet in very deed she is my sister, for she is the daughter of my father, but not the daughter of my mother, and she is my wife;
13 Now when God caused me to wander out of my father’s house, I said then to her, This is thy kindness that thou shalt shew unto me in all places where we come, Say thou of me, He is my brother.
14 Then took Abimelech sheep and beeves, and menservants, and womenservants, and gave them unto Abraham, and restored him Sarah his wife.
15 And Abimelech said, Behold, my land is before thee; dwell where it pleaseth thee.
16 Likewise to Sarah he said, Behold, I have given thy brother a thousand pieces of silver; behold, he is the veil of thine eyes to all that are with thee, and to all others, and she was thus reproved.
17 ¶ Then Abraham prayed unto God, and God healed Abimelech, and his wife, and his maidservants, and they bare children.
18 For the LORD had shut up every womb of the house of Abimelech, because of Sarah Abraham’s wife.
Genesis 21
2 Isaac is born. 9 Ishmael mocketh Isaac. 14 Hagar is cast out with her son. 17 The Angel comforteth Hagar. 22 The covenant between Abimelech and Abraham. 33 Abraham called upon the LORD.
1 Now the LORD visited Sarah, as he had said, and did unto her according as he had promised.
2 For Sarah conceived, and bare Abraham a son in his old age, at the same season that God told him.
46

3 And Abraham called his son’s name that was born unto him, which Sarah bare him, Isaac.
4 Then Abraham circumcised Isaac his son, when he was eight days old, as God had commanded him.
5 So Abraham was a hundred years old, when his son Isaac was born unto him.
6 ¶ Then Sarah said, God hath made me to rejoice; all that hear will rejoice with me.
7 Again she said, Who would have said to Abraham, that Sarah should have given children suck? For I have born him a son in his old age.
8 Then the child grew and was weaned, and Abraham made a great feast the same day that Isaac was weaned.
9 ¶ And Sarah saw the son of Hagar the Egyptian (which she had born unto Abraham) mocking.
10 Wherefore she said unto Abraham, Cast out this bondwoman and her son, for the son of this bondwoman shall not be heir with my son Isaac.
11 And this thing was very grievous in Abraham’s sight, because of his son.
12 ¶ But God said unto Abraham, Let it not be grievous in thy sight for the child, and for thy bondwoman; in all that Sarah shall say unto thee, hear her voice, for in Isaac shall thy seed be called.
13 As for the son of the bondwoman, I will make him a nation also, because he is thy seed.
14 So Abraham arose up early in the morning, and took bread, and a bottle of water, and gave it unto Hagar, putting it on her shoulder, and the child also, and sent her away; who departing, wandered in the wilderness of Beer-sheba.
15 And when the water of the bottle was spent, she cast the child under a certain tree.
16 Then she went and sat her over against him afar off about a bowshot, for she said, I will not see the death of the child. And she sat down over against him, and lifted up her voice, and wept.
47

17 Then God heard the voice of the child, and the Angel of God called to Hagar from heaven, and said unto her, What aileth thee, Hagar? Fear not, for God hath heard the voice of the child where he is.
18 Arise, take up the child, and hold him in thy hand, for I will make of him a great people.
19 And God opened her eyes, and she saw a well of water; so she went and filled the bottle with water, and gave the boy drink.
20 So God was with the child, and he grew and dwelt in the wilderness, and was an archer.
21 And he dwelt in the wilderness of Paran, and his mother took him a wife out of the land of Egypt.
22 ¶ And at that same time Abimelech and Phichol his chief captain spake unto Abraham, saying, God is with thee in all that thou doest.
23 Now therefore swear unto me here by God, that thou wilt not hurt me, nor my children, nor my children’s children, thou shalt deal with me, and with the country, where thou hast been a stranger, according unto the kindness that I have shewed thee.
24 Then Abraham said, I will swear.
25 And Abraham rebuked Abimelech for a well of water, which Abimelech’s servants had violently taken away.
26 And Abimelech said, I know not who hath done this thing; also thou toldest me not, neither heard I of it but this day.
27 Then Abraham took sheep and beeves, and gave them unto Abimelech, and they two made a covenant.
28 And Abraham set seven lambs of the flock by themselves.
29 Then Abimelech said unto Abraham, What mean these seven lambs, which thou hast set by themselves?
30 And he answered, Because thou shalt receive of my hand these seven lambs, that it may be a witness unto me, that I have dug this well.
48

31 Wherefore the place is called Beer-sheba, because there they both sware.
32 Thus made they a covenant at Beer-sheba; afterward Abimelech and Phichol his chief captain rose up, and turned again unto the land of the Philistines.
33 ¶ And Abraham planted a grove in Beer-sheba, and called there on the Name of the LORD, the everlasting God.
34 And Abraham was a stranger in the Philistines’ land a long season.
Genesis 22
1-2 The faith of Abraham is proved in offering his son Isaac. 8 Isaac is a figure of Christ. 20 The generation of Nahor Abraham's brother of whom cometh Rebekah.
1 And after these things God did prove Abraham, and said unto him, Abraham. Who answered, Here am I.
2 And he said, Take now thy only son Isaac whom thou lovest, and get thee unto the land of Moriah, and offer him there for a burnt offering upon one of the mountains, which I will shew thee.
3 Then Abraham rose up early in the morning, and saddled his ass, and took two of his servants with him, and Isaac his son, and clove wood for the burnt offering, and rose up and went to the place, which God had told him.
4 ¶ Then the third day Abraham lifted up his eyes, and saw the place afar off,
5 And said unto his servants, Abide you here with the ass, for I and the child will go yonder and worship, and come again unto you.
6 Then Abraham took the wood of the burnt offering, and laid it upon Isaac his son, and he took the fire in his hand, and the knife; and they went both together.
49

7 Then spake Isaac unto Abraham his father, and said, My father. And he answered, Here am I, my son. And he said, Behold the fire and the wood, but where is the lamb for the burnt offering?
8 Then Abraham answered, My son, God will provide him a lamb for a burnt offering; so they went both together.
9 And when they came to the place which God had shewed him, Abraham built an altar there, and couched the wood, and bound Isaac his son, and laid him on the altar upon the wood.
10 And Abraham stretching forth his hand, took the knife to kill his son.
11 But the Angel of the LORD called unto him from heaven, saying, Abraham, Abraham. And he answered, Here am I.
12 Then he said, Lay not thine hand upon the child, neither do anything unto him; for now I know that thou fearest God, seeing for my sake thou hast not spared thine only son.
13 And Abraham lifting up his eyes, looked, and behold, there was a ram behind him caught by the horns in a bush; then Abraham went and took the ram, and offered him up for a burnt offering in the stead of his son.
14 And Abraham called the name of that place, Jehovah-jireh, as it is said this day, In the mount will the LORD be seen.
15 ¶ And the Angel of the LORD cried unto Abraham from heaven the second time,
16 And said, By myself have I sworn (saith the LORD) because thou hast done this thing, and hast not spared thine only son,
17 Therefore will I surely bless thee, and will greatly multiply thy seed, as the stars of the heaven, and as the sand which is upon the seashore, and thy seed shall possess the gate of his enemies.
18 And in thy seed shall all the nations of the earth be blessed, because thou hast obeyed my voice.
19 Then turned Abraham again unto his servants, and they rose up and went together to Beer-sheba; and Abraham dwelt at Beer-sheba.
50

20 ¶ And after these things one told Abraham, saying, Behold Milcah, she hath also born children unto thy brother Nahor;
21 To wit, Uz his eldest son, and Buz his brother, and Kemuel the father of Aram,
22 And Chesed, and Hazo, and Pildash, and Jidlaph, and Bethuel.
23 And Bethuel begat Rebekah; these eight did Milcah bear to Nahor, Abraham’s brother.
24 And his concubine called Reumah, she bare also Tebah, and Gaham, and Thahash and Maachah.
Genesis 23
2 Abraham lamenteth the death of Sarah. 4 He buyeth a field to bury her, of the Hittites. 13 The equity of Abraham. 19 Sarah is buried in Machpelah.
1 When Sarah was a hundred twenty and seven years old (so long lived she.)
2 Then Sarah died in Kirjath-arba; the same is Hebron in the land of Canaan; and Abraham came to mourn for Sarah and to weep for her.
3 ¶ Then Abraham rose up from the sight of his corpse, and talked with the Hittites, saying,
4 I am a stranger, and a foreigner among you; give me a possession of burial with you, that I may bury my dead out of my sight.
5 Then the Hittites answered Abraham, saying unto him,
6 Hear us, my lord, thou art a prince of God among us; in the chiefest of our sepulchers bury thy dead; none of us shall forbid thee his sepulcher, but thou mayest bury thy dead therein.
7 Then Abraham stood up, and bowed himself before the people of the land of the Hittites.
51

8 And he communed with them, saying, If it be your mind, that I shall bury my dead out of my sight, hear me, and entreat for me to Ephron the son of Zohar,
9 That he would give me the cave of Machpelah, which he hath in the end of his field; that he would give it me for as much money as it is worth, for a possession to bury in among you.
10 (For Ephron dwelt among the Hittites) Then Ephron the Hittite answered Abraham in the audience of all the Hittites that went in at the gates of his city, saying,
11 No, my lord, hear me: the field give I thee, and the cave, that therein is, I give it thee; even in the presence of the sons of my people give I it thee, to bury thy dead.
12 Then Abraham bowed himself before the people of the land,
13 And spake unto Ephron in the audience of the people of the country, saying, Seeing thou wilt give it, I pray thee, hear me: I will give the price of the field; receive it of me, and I will bury my dead there.
14 Ephron then answered Abraham, saying unto him,
15 My lord, hearken unto me; the land is worth four hundred shekels of silver,
what is that between me and thee? Bury therefore thy dead.
16 So Abraham hearkened unto Ephron, and Abraham weighed to Ephron the silver, which he had named, in the audience of the Hittites, even four hundred silver shekels of current money among merchants.
17 ¶ So the field of Ephron which was in Machpelah, and over against Mamre, even the field and the cave that was therein, and all the trees that were in the field, which were in all the borders round about, was made sure,
18 Unto Abraham for a possession, in the sight of the Hittites, even of all that went in at the gates of his city.
19 And after this, Abraham buried Sarah his wife in the cave of the field of Machpelah over against Mamre. The same is Hebron in the land of Canaan.
20 Thus the field and the cave that is therein, was made sure unto Abraham for a possession of burial by the Hittites.
52

Genesis 24
2 Abraham causeth his servant to swear to take a wife for Isaac in his own kindred, 12 The servant prayeth to God. 33 His fidelity toward his master. 50 The friends of Rebekah commit the matter to God. 58 They ask her consent, and she agreeth. 67 And is married to Isaac.
1 Now Abraham was old, and stricken in years, and the LORD had blessed Abraham in all things.
2 Therefore Abraham said unto his eldest servant of his house, which had the rule over all that he had. Put now thy hand under my thigh,
3 And I will make thee swear by the LORD God of the heaven, and God of the earth, that thou shalt not take a wife unto my son of the daughters of the Canaanites among whom I dwell;
4 But thou shalt go unto my country, and to my kindred, and take a wife unto my son Isaac.
5 And the servant said to him, What if the woman will not come with me to this land? Shall I bring thy son again unto the land from whence thou camest?
6 To whom Abraham answered, Beware that thou bring not my son thither again.
7 ¶ The LORD God of heaven, who took me from my father’s house, and from the land where I was born, and that spake unto me, and that sware unto me, saying, Unto thy seed will I give this land, he shall send his Angel before thee, and thou shalt take a wife unto my son from thence.
8 Nevertheless if the woman will not follow thee, then shalt thou be discharged of this my oath; only bring not my son thither again.
9 Then the servant put his hand under the thigh of Abraham his master, and sware to him for this matter.
10 ¶ So the servant took ten camels of the camels of his master, and departed, (for he had all his master’s goods in his hand,) and so he arose, and went to Aram Naharaim, unto the city of Nahor.
53

11 And he made his camels to lie down without the city by a well of water, at eventide about the time that the women come out to draw water.
12 And he said, O LORD God of my master Abraham, I beseech thee, send me good speed this day, and shew mercy unto my master Abraham.
13 Lo, I stand by the well of water, whiles the men’s daughters of this city come out to draw water.
14 Grant therefore that the maid, to whom I say, Bow down thy pitcher, I pray thee, that I may drink, if she say, Drink, and I will give thy camels drink also, may be she that thou hast ordained for thy servant Isaac; and thereby shall I know that thou hast shewed mercy on my master.
15 ¶ And now before he had left speaking, behold, Rebekah came out, the daughter of Bethuel, son of Milcah the wife of Nahor Abraham’s brother, and her pitcher upon her shoulder.
16 (And the maid was very fair to look upon, a virgin and unknown of man) and she went down to the well, and filled her pitcher, and came up.
17 Then the servant ran to meet her, and said, Let me drink, I pray thee, a little water of thy pitcher.
18 And she said, Drink sir; and she hasted, and let down her pitcher upon her hand and gave him drink.
19 And when she had given him drink, she said, I will draw water for thy camels also until they have drunken enough.
20 And she poured out her pitcher into the trough speedily, and ran again unto the well to draw water, and she drew for all his camels.
21 So the man wondered at her, and held his peace, to know whether the LORD had made his journey prosperous or not.
22 And when the camels had left drinking, the man took a golden habiliment of half a shekel weight, and two bracelets for her hands, of ten shekels weight of gold;
23 And he said, Whose daughter art thou? Tell me, I pray thee, Is there room in thy father’s house for us to lodge in?
54

24 Then she said to him, I am the daughter of Bethuel the son of Milcah whom she bare unto Nahor.
25 Moreover she said unto him, We have litter also and provender enough, and room to lodge in.
26 And the man bowed himself and worshipped the LORD,
27 And said, Blessed be the LORD God of my master Abraham, which hath not withdrawn his mercy and his truth from my master, for when I was in the way, the LORD brought me to my master’s brethren’s house.
28 And the maid ran and told them of her mother’s house according to these words.
29 ¶ Now Rebekah had a brother called Laban, and Laban ran unto the man to the well.
30 For when he had seen the earrings and the bracelets in his sister’s hands, and when he heard the words of Rebekah his sister, saying, Thus said the man unto me, then he went to the man, and lo, he stood by the camels at the well.
31 And he said, Come in thou blessed of the LORD; wherefore standest thou without, seeing I have prepared the house, and room for the camels?
32 ¶ Then the man came into the house, and he unsaddled the camels, and brought litter and provender for the camels, and water to wash his feet, and the men’s feet that were with him.
33 Afterward the meat was set before him, but he said, I will not eat, until I have said my message. And he said, Speak on.
34 Then he said, I am Abraham’s servant,
35 And the LORD hath blessed my master wonderfully, that he is become great; for he hath given him sheep, and beeves, and silver, and gold, and menservants, and maidservants, and camels, and asses.
36 And Sarah my master’s wife hath born a son to my master, when she was old, and unto him hath he given all that he hath.
37 Now my master made me swear, saying, Thou shalt not take a wife to my son of the daughters of the Canaanites, in whose land I dwell;
55

38 But thou shalt go unto my father’s house and to my kindred, and take a wife unto my son.
39 Then I said unto my master, What if the woman will not follow me?
40 Who answered me, The LORD, before whom I walk, will send his Angel with thee, and prosper thy journey, and thou shalt take a wife for my son of my kindred and my father’s house.
41 Then shalt thou be discharged of my oath, when thou comest to my kindred; and if they give thee not one, thou shalt be free from my oath.
42 So I came this day to the well, and said, O LORD, the God of my master Abraham, if thou now prosper my journey which I go;
43 Behold, I stand by the well of water, when a virgin cometh forth to draw water, and I say to her, Give me, I pray thee, a little water of thy pitcher to drink,
44 And she say to me, Drink thou, and I will also draw for thy camels, let her be the wife, which the LORD hath prepared for my master’s son.
45 And before I had made an end of speaking in my heart, behold, Rebekah came forth, and her pitcher on her shoulder, and she went down unto the well, and drew water. Then I said unto her, Give me drink, I pray thee.
46 And she made haste, and took down her pitcher from her shoulder, and said, Drink, and I will give thy camels drink also. So I drank, and she gave the camels drink also.
47 Then I asked her, and said, Whose daughter art thou? And she answered, The daughter of Bethuel Nahor’s son, whom Milcah bare unto him. Then I put the habiliment upon her face, and the bracelets upon her hands;
48 And I bowed down and worshipped the LORD, and blessed the LORD God of my master Abraham, which had brought me the right way to take my master’s brother’s daughter unto his son.
49 Now therefore, if ye will deal mercifully and truly with my master, tell me; and if not, tell me; that I may turn me to the right hand or to the left.
50 Then answered Laban and Bethuel, and said, This thing is proceeded of the LORD; we cannot therefore say unto thee, neither evil nor good.
56

51 Behold, Rebekah is before thee, take her and go, that she may be thy master’s son’s wife, even as the LORD hath said.
52 And when Abraham’s servant heard their words, he bowed himself toward the earth unto the LORD.
53 Then the servant took forth jewels of silver, and jewels of gold, and raiment, and gave to Rebekah; also unto her brother and to her mother he gave gifts.
54 Afterward they did eat and drink, both he, and the men that were with him, and tarried all night. And when they rose up in the morning, he said, Let me depart unto my master.
55 Then her brother and her mother answered, Let the maid abide with us, at the least ten days; then shall she go.
56 But he said unto them, Hinder you me not, seeing the LORD hath prospered my journey; send me away, that I may go to my master.
57 Then they said, We will call the maid, and ask her consent.
58 And they called Rebekah, and said unto her, Wilt thou go with this man? And she answered, I will go.
59 So they let Rebekah their sister go, and her nurse, with Abraham’s servant and his men.
60 And they blessed Rebekah, and said unto her, Thou art our sister, grow into thousand thousands, and thy seed possess the gate of his enemies.
61 ¶ Then Rebekah arose, and her maids, and rode upon the camels, and followed the man; and the servant took Rebekah, and departed.
62 Now Isaac came from the way of Beer-lahai-roi, (for he dwelt in the South country .)
63 And Isaac went out to pray in the field toward the evening; who lifted up his eyes and looked, and behold, the camels came.
64 Also Rebekah lifted up her eyes, and when she saw Isaac, she lighted down from the camel.
57

65 (For she had said to the servant, Who is yonder man, that cometh in the field to meet us? And the servant had said, It is my master.) So she took a veil, and covered her.
66 And the servant told Isaac all things that he had done.
67 Afterward Isaac brought her into the tent of Sarah his mother, and he took Rebekah, and she was his wife, and he loved her. So Isaac was comforted after his mother’s death.
Genesis 25
1 Abraham taketh Keturah to wife, and getteth many children. 5 Abraham giveth all his goods to Isaac. 8 He dieth. 12 The genealogy of Ishmael. 25 The birth of Jacob and Esau. 30 Esau selleth his birth right for a mess of pottage.
1 Now Abraham had taken him another wife called Keturah,
2 Which bare him Zimran, and Jokshan, and Medan, and Midian, and Ishbak, and Shuah.
3 And Jokshan begat Sheba, and Dedan. And the sons of Dedan were Asshurim, and Letushim, and Leummim.
4 Also the sons of Midian were Ephah, and Epher, and Hanoch, and Abida, and Eldaah. All these were the sons of Keturah.
5 ¶ And Abraham gave all his goods to Isaac,
6 But unto the sons of the concubines, which Abraham had, Abraham gave gifts, and sent them away from Isaac his son (while he yet lived) Eastward to the East country .
7 And this is the age of Abraham’s life, which he lived, a hundred seventy and five years.
58

8 Then Abraham yielded the spirit, and died in a good age, an old man, and of great years, and was gathered to his people.
9 And his sons Isaac and Ishmael buried him in the cave of Machpelah, in the field of Ephron son of Zohar the Hittite, before Mamre.
10 Which field Abraham bought of the Hittites, where Abraham was buried with Sarah his wife.
11 ¶ And after the death of Abraham, God blessed Isaac his son; and Isaac dwelt by Beer-lahai-roi.
12 ¶ Now these are the generations of Ishmael, Abraham’s son, whom Hagar the Egyptian, Sarah’s handmaid, bare unto Abraham.
13 And these are the names of the sons of Ishmael, name by name, according to their kindreds: the eldest son of Ishmael was Nebajoth, then Kedar, and Adbeel, and Mibsam,
14 And Mishma, and Dumah, and Massa,
15 Hadar, and Tema, Jetur, Naphish, and Kedemah.
16 These are the sons of Ishmael, and these are their names, by their towns and by their castles; to wit, twelve princes of their nations.
17 (And these are the years of the life of Ishmael, a hundred thirty and seven years, and he yielded up the spirit, and died, and was gathered unto his people.)
18 And they dwelt from Havilah unto Shur, that is towards Egypt, as thou goest to Asshur; Ishmael dwelt in the presence of all his brethren.
19 ¶ Likewise these are the generations of Isaac, Abraham’s son: Abraham begat Isaac,
20 And Isaac was forty years old, when he took Rebekah to wife, the daughter of Bethuel the Aramite of Paddan-aram, and sister to Laban the Aramite.
21 And Isaac prayed unto the LORD for his wife, because she was barren; and the LORD was entreated of him, and Rebekah his wife conceived,
22 But the children strove together within her; therefore she said, Seeing it is so, why am I thus? Wherefore she went to ask the LORD.
59

23 And the LORD said to her, Two nations are in thy womb; and two manner of people shall be divided out of thy bowels; and the one people shall be mightier than the other; and the elder shall serve the younger.
24 ¶ Therefore when her time of deliverance was fulfilled, behold, twins were in her womb.
25 So he that came out first was red, and he was all over as a rough garment, and they called his name Esau.
26 And afterward came his brother out, and his hand held Esau by the heel; therefore his name was called Jacob. Now Isaac was threescore years old when Rebekah bare them.
27 And the boys grew, and Esau was a cunning hunter, and lived in the fields, but Jacob was a plain man, and dwelt in tents.
28 And Isaac loved Esau, for venison was his meat, but Rebekah loved Jacob.
29 Now Jacob sod pottage, and Esau came from the field and was weary.
30 Then Esau said to Jacob, Let me eat, I pray thee, of that pottage so red, for I am weary. Therefore was his name called Edom.
31 And Jacob said, Sell me even now thy birthright.
32 And Esau said, Lo, I am almost dead, what is then this birthright to me?
33 Jacob then said, Swear to me even now. And he sware to him, and sold his birthright unto Jacob.
34 Then Jacob gave Esau bread and pottage of lentils; and he did eat and drink, and rose up, and went his way. So Esau contemned his birthright.
60

Genesis 26
1 God provideth for Isaac in the famine. 3 He reneweth his promise. 9 The King blameth him for denying his wife. 14 The Philistines hate him for his riches. 15 Stop his wells. 16 And drive him away. 24 God comforteth him. 31 He maketh alliance with Abimelech.
1 And there was a famine in the land besides the first famine that was in the days of Abraham. Wherefore Isaac went to Abimelech King of the Philistines unto Gerar.
2 For the LORD appeared unto him, and said, Go not down into Egypt, but abide in the land which I shall shew unto thee.
3 Dwell in this land, and I will be with thee, and will bless thee, for to thee, and to thy seed, I will give all these countries, and I will perform the oath which I sware unto Abraham thy father.
4 Also I will cause thy seed to multiply as the stars of heaven, and will give unto thy seed all these countries; and in thy seed shall all the nations of the earth be blessed,
5 Because that Abraham obeyed my voice and kept my ordinance, my commandments, my statutes, and my Laws.
6 ¶ So Isaac dwelt in Gerar.
7 And the men of the place asked him of his wife, and he said, She is my sister, for he feared to say, She is my wife, lest, said he, the men of the place should kill me, because of Rebekah, for she was beautiful to the eye.
8 So after he had been there a long time, Abimelech King of the Philistines looked out at a window, and lo, he saw Isaac sporting with Rebekah his wife.
9 Then Abimelech called Isaac, and said, Lo, she is of a surety thy wife, and why saidst thou, She is my sister? To whom Isaac answered, Because I thought this, It may be that I shall die for her.
10 Then Abimelech said, Why hast thou done this unto us? One of the people had almost lain by thy wife, so shouldest thou have brought sin upon us.
61

11 Then Abimelech charged all his people, saying, He that toucheth this man, or his wife, shall die the death.
12 Afterward Isaac sowed in that land, and found in the same year a hundredfold by estimation. And so the LORD blessed him.
13 And the man waxed mighty, and still increased, till he was exceeding great,
14 For he had flocks of sheep, and herds of cattle, and a mighty household, therefore the Philistines had envy at him.
15 In so much that the Philistines stopped and filled up with earth all the wells, which his father’s servants dug in his father Abraham’s time.
16 Then Abimelech said unto Isaac, Get thee from us, for thou art mightier than we a great deal.
17 ¶ Therefore Isaac departed thence and pitched his tent in the valley of Gerar, and dwelt there.
18 And Isaac returning, dug the wells of water, which they had dug in the days of Abraham his father, for the Philistines had stopped them after the death of Abraham; and he gave them the same names, which his father gave them.
19 Isaac’s servants then dug in the valley, and found there a well of living water.
20 But the herdsmen of Gerar did strive with Isaac’s herdsmen, saying, The water is ours. Therefore called he the name of the well Esek, because they were at strife with him.
21 Afterward they dug another well, and strove for that also, and he called the name of it Sitnah.
22 Then he removed thence, and dug another well, for the which they strove not; therefore called he the name of it Rehoboth, and said, Because the LORD hath now made us room, we shall increase upon the earth.
23 So he went up thence to Beer-sheba.
24 And the LORD appeared unto him the same night, and said, I am the God of Abraham thy father; fear not, for I am with thee, and will bless thee, and multiply thy seed for my servant Abraham’s sake.
62

25 Then he built an altar there, and called upon the Name of the LORD, and there spread his tent; where also Isaac’s servants dug a well.
26 ¶ Then came Abimelech to him from Gerar, and Ahuzzath one of his friends, and Phichol the captain of his army.
27 To whom Isaac said, Wherefore come ye to me, seeing ye hate me and have put me away from you?
28 Who answered, We saw certainly that the LORD was with thee, and we thought thus, Let there be now an oath between us, even between us and thee, and let us make a covenant with thee.
29 If thou shalt do us no hurt, as we have not touched thee, and as we have done unto thee nothing but good, and sent thee away in peace. Thou now, the blessed of the LORD, do this.
30 Then he made them a feast, and they did eat and drink.
31 And they rose up betimes in the morning, and sware one to another; then Isaac let them go, and they departed from him in peace.
32 And that same day Isaac’s servants came and told him of a well, which they had dug, and said unto him, We have found water.
33 So he called it Shibah; therefore the name of the city is called Beer-sheba unto this day.
34 ¶ Now when Esau was forty years old, he took to wife Judith, the daughter of Beeri a Hittite, and Bashemath the daughter of Elon a Hittite also.
35 And they were a grief of mind to Isaac and to Rebekah.
63

Genesis 27
28 Jacob getteth the blessing from Esau by his mother's counsel. 38 Esau by weeping, moveth his father to pity him. 41 Esau hateth Jacob and threateneth his death. 43 Rebekah sendeth Jacob away.
1 And when Isaac was old, and his eyes were dim (so that he could not see) he called Esau his eldest son, and said unto him, My son. And he answered him, I am here.
2 Then he said, Behold, I am now old, and know not the day of my death;
3 Wherefore now, I pray thee take thy instruments, thy quiver and thy bow, and
get thee to the field, that thou mayest take me some venison.
4 Then make me savory meat, such as I love, and bring it me that I may eat, and that my soul may bless thee, before I die.
5 (Now Rebekah heard, when Isaac spake to Esau his son) and Esau went into the field to hunt for venison, and to bring it.
6 ¶ Then Rebekah spake unto Jacob her son, saying, Behold, I have heard thy father talking with Esau thy brother, saying,
7 Bring me venison, and make me savory meat, that I may eat and bless thee before the LORD, afore my death.
8 Now therefore, my son, hear my voice in that which I command thee.
9 Get thee now to the flock, and bring me thence two good kids of the goats, that I may make pleasant meat of them for thy father, such as he loveth.
10 Then thou shalt bring it to thy father, and he shall eat, to the intent that he may bless thee before his death.
11 But Jacob said to Rebekah his mother, Behold, Esau my brother is rough, and I am smooth.
12 My father may possibly feel me, and I shall seem to him to be a mocker, so shall I bring a curse upon me, and not a blessing.
64

13 But his mother said unto him, Upon me be thy curse, my son; only hear my voice, and go and bring me them.
14 So he went and fetched them, and brought them to his mother; and his mother made pleasant meat, such as his father loved.
15 And Rebekah took fair clothes of her elder son Esau, which were in her house, and clothed Jacob her younger son;
16 And she covered his hands and the smooth of his neck with the skins of the kids of the goats.
17 Afterward she put the pleasant meat and bread, which she had prepared, in the hand of her son Jacob.
18 ¶ And when he came to his father, he said, My father. Who answered, I am here. Who art thou, my son?
19 And Jacob said to his father, I am Esau thy firstborn; I have done as thou badest me, arise, I pray thee, sit up and eat of my venison, that thy soul may bless me.
20 Then Isaac said unto his son, How hast thou found it so quickly my son? Who said, Because the LORD thy God brought it to my hand.
21 Again said Isaac unto Jacob, Come near now, that I may feel thee, my son, whether thou be that my son Esau or not.
22 Then Jacob came near to Isaac his father, and he felt him and said, The voice is Jacob’s voice, but the hands are the hands of Esau.
23 (For he knew him not, because his hands were rough as his brother Esau’s hands; wherefore he blessed him.)
24 Again he said, Art thou that my son Esau? Who answered, Yea.
25 Then said he, Bring it me hither, and I will eat of my son’s venison, that my soul may bless thee. And he brought it to him, and he ate; also he brought him wine, and he drank.
26 Afterward his father Isaac said unto him, Come near now, and kiss me, my son.
65

27 And he came near and kissed him. Then he smelled the savor of his garments, and blessed him, and said, Behold, the smell of my son is as the smell of a field, which the LORD hath blessed.
28 God give thee therefore of the dew of heaven, and the fatness of the earth, and plenty of wheat and wine.
29 Let people be thy servants, and nations bow unto thee; be lord over thy brethren, and let thy mother’s children honor thee. Cursed be he that curseth thee, and blessed be he that blesseth thee.
30 ¶ And when Isaac had made an end of blessing Jacob, and Jacob was scarce gone out from the presence of Isaac his father, then came Esau his brother from his hunting,
31 And he also prepared savory meat, and brought it to his father, and said unto his father, Let my father arise, and eat of his son’s venison, that thy soul may bless me.
32 But his father Isaac said unto him, Who art thou? And he answered, I am thy son, even thy firstborn Esau.
33 Then Isaac was stricken with a marvelous great fear, and said, Who and where is he that hunted venison, and brought it me, and I have eaten of all before thou camest? And I have blessed him, therefore he shall be blessed.
34 When Esau heard the words of his father, he cried out with a great cry and bitter, out of measure, and said unto his father, Bless me, even me also, my father.
35 Who answered, Thy brother came with subtilty, and hath taken away thy blessing.
36 Then he said, Was he not justly called Jacob? For he hath deceived me these two times. He took my birthright, and lo, now hath he taken my blessing. Also he said, Hast thou not reserved a blessing for me?
37 Then Isaac answered, and said unto Esau, Behold, I have made him thy lord, and all his brethren have I made his servants; also with wheat and wine have I furnished him, and unto thee now what shall I do, my son?
38 Then Esau said unto his father, Hast thou but one blessing my father? Bless me, even me also, my father. And Esau lifted up his voice, and wept.
66

39 Then Isaac his father answered, and said unto him, Behold, the fatness of the earth shall be thy dwelling place, and thou shalt have of the dew of heaven from above.
40 And by thy sword shalt thou live, and shalt be thy brother’s servant. But it shall come to pass, when thou shalt get the mastery, that thou shalt break his yoke from thy neck.
41 ¶ Therefore Esau hated Jacob, because of the blessing, wherewith his father blessed him. And Esau thought in his mind, The days of mourning for my father will come shortly, then I will slay may brother Jacob.
42 And it was told to Rebekah of the words of Esau her elder son, and she sent and called Jacob her younger son, and said unto him, Behold, thy brother Esau is comforted against thee, meaning to kill thee;
43 Now therefore my son, hear my voice, arise, and flee thou to Haran to my brother Laban,
44 And tarry with him a while until thy brother’s fierceness be swayed,
45 And till thy brother’s wrath turn away from thee, and he forget the things, which thou hast done to him. Then will I send and take thee from thence. Why should I be deprived of you both in one day?
46 Also Rebekah said to Isaac, I am weary of my life, for the daughters of Heth. If Jacob take a wife of the daughters of Heth like these of the daughters of the land, what availeth it me to live?
Genesis 28
1 Isaac forbiddeth Jacob to take a wife of the Canaanites. 6 Esau taketh a wife of the daughters of Ishmael against his father's will. 12 Jacob in the way of Haran seeth a ladder reaching to heaven. 14 Christ is promised. 20 Jacob asketh of God only meat and clothing.
1 Then Isaac called Jacob and blessed him, and charged him, and said unto him, Take not a wife of the daughters of Canaan.
67

2 Arise, get thee to Paddan-aram to the house of Bethuel thy mother’s father, and thence take thee a wife of the daughters of Laban thy mother’s brother.
3 And God all sufficient bless thee, and make thee to increase, and multiply thee, that thou mayest be a multitude of people,
4 And give thee the blessing of Abraham, even to thee and to thy seed with thee, that thou mayest inherit the land (wherein thou art a stranger,) which God gave unto Abraham.
5 Thus Isaac sent forth Jacob, and he went to Paddan-aram unto Laban son of Bethuel the Aramite, brother to Rebekah, Jacob’s and Esau’s mother.
6 ¶ When Esau saw that Isaac had blessed Jacob, and sent him to Paddan-aram, to fetch him a wife thence, and given him a charge when he blessed him, saying, Thou shalt not take a wife of the daughters of Canaan,
7 And that Jacob had obeyed his father and his mother, and was gone to Paddan- aram;
8 Also Esau seeing that the daughters of Canaan displeased Isaac his father,
9 Then went Esau to Ishmael, and took unto the wives, which he had, Mahalath the daughter of Ishmael, Abraham’s son, the sister of Nabajoth, to be his wife.
10 ¶ Now Jacob departed from Beer-sheba, and went to Haran,
11 And he came unto a certain place, and tarried there all night, because the sun was down, and took of the stones of the place, and laid under his head and slept in the same place.
12 Then he dreamed, and behold, there stood a ladder upon the earth, and the top of it reached up to heaven; and lo, the Angels of God went up and down by it.
13 And behold, the LORD stood above it, and said, I am the LORD God of Abraham thy father, and the God of Isaac; the land, upon the which thou sleepest, will I give thee and thy seed.
14 And thy seed shall be as the dust of the earth, and thou shalt spread abroad to the West, and to the East, and to the North, and to the South, and in thee and in thy seed shall all the families of the earth be blessed.
68

15 And lo, I am with thee, and will keep thee whithersoever thou goest, and will bring thee again into this land; for I will not forsake thee until I have performed that which I have promised thee.
16 ¶ Then Jacob awoke out of his sleep, and said, Surely the LORD is in this place, and I was not aware.
17 And he was afraid, and said, How fearful is this place! This is none other but the house of God, and this is the gate of heaven.
18 Then Jacob rose up early in the morning, and took the stone that he had laid under his head, and set it up as a pillar, and poured oil upon the top of it.
19 And he called ye name of that place Bethel; notwithstanding the name of the city was at the first called Luz.
20 Then Jacob vowed a vow, saying, If God will be with me, and will keep me in this journey which I go, and will give me bread to eat, and clothes to put on;
21 So that I come again unto my father’s house in safety, then shall the LORD be my God.
22 And this stone, which I have set up as a pillar, shall be God’s house, and of all that thou shalt give me, will I give the tenth unto thee.
Genesis 29
13 Jacob cometh to Laban and serveth seven years for Rachel. 23 Leah brought to his bed instead of Rachel. 27 He serveth seven years more for Rachel. 30 Leah conceiveth and beareth four sons.
1 Then Jacob lifted up his feet and came into the East country.
2 And as he looked about, behold there was a well in the field, and lo, three flocks of sheep lay thereby (for at that well were the flocks watered) and there was a great stone upon the well’s mouth.
69

3 And thither were all the flocks gathered, and they rolled the stone from the well’s mouth, and watered the sheep, and put the stone again upon the well’s mouth in his place.
4 And Jacob said unto them, My brethren, whence be ye? And they answered, We are of Haran.
5 Then he said unto them, Know ye Laban the son of Nahor? Who said, We know him.
6 Again he said unto them, Is he in good health? And they answered, He is in good health, and behold, his daughter Rachel cometh with the sheep.
7 Then he said, Lo, it is yet high day, neither is it time that the cattle should be gathered together. Water ye the sheep and go feed them.
8 But they said, We may not, until all the flocks be brought together, and till men roll the stone from the well’s mouth, that we may water the sheep.
9 ¶ While he talked with them, Rachel also came with her father’s sheep, for she kept them.
10 And as soon as Jacob saw Rachel the daughter of Laban his mother’s brother, and the sheep of Laban his mother’s brother, then came Jacob near, and rolled the stone from the well’s mouth, and watered the flock of Laban his mother’s brother.
11 And Jacob kissed Rachel, and lifted up his voice and wept.
12 (For Jacob told Rachel, that he was her father’s brother, and that he was Rebekah’s son.) Then she ran and told her father.
13 And when Laban heard tell of Jacob his sister’s son, he ran to meet him, and embraced him and kissed him, and brought him to his house. And he told Laban all these things.
14 To whom Laban said, Well, thou art my bone and my flesh. and he abode with him the space of a month.
15 ¶ For Laban said unto Jacob, Though thou be my brother, shouldest thou therefore serve me for nought? Tell me, what shall be thy wages?
70

16 Now Laban had two daughters, the elder called Leah, and the younger called Rachel.
17 And Leah was tender eyed, but Rachel was beautiful and fair.
18 And Jacob loved Rachel, and said, I will serve thee seven years for Rachel thy younger daughter.
19 Then Laban answered, It is better that I give her thee, than that I should give her to another man; abide with me.
20 And Jacob served seven years for Rachel, and they seemed unto him but a few days, because he loved her.
21 ¶ Then Jacob said to Laban, Give me my wife, that I may go in to her, for my term is ended.
22 Wherefore Laban gathered together all the men of the place, and made a feast.
23 But when the evening was come, he took Leah his daughter and brought her to him, and he went in unto her.
24 And Laban gave his maid Zilpah to his daughter Leah, to be her servant.
25 But when the morning was come, behold, it was Leah. Then said he to Laban, Wherefore hast thou done thus to me? Did not I serve thee for Rachel? Wherefore then hast thou beguiled me?
26 And Laban answered, It is not the manner of this place, to give the younger before the elder.
27 Fulfill seven years for her, and we will also give thee this for the service, which thou shalt serve me yet seven years more.
28 Then Jacob did so, and fulfilled her seven years, so he gave him Rachel his daughter to be his wife.
29 Laban also gave to Rachel his daughter Bilhah his maid to be her servant.
30 So entered he in to Rachel also, and loved also Rachel more than Leah, and served him yet seven years more.
71

31 ¶ When the LORD saw that Leah was despised, he made her fruitful, but Rachel was barren.
32 And Leah conceived and bare a son, and she called his name Reuben, for she said, Because the LORD hath looked upon my tribulation; now therefore my husband will love me.
33 And she conceived again and bare a son, and said, Because the LORD heard that I was hated, he hath therefore given me this son also, and she called his name Simeon.
34 And she conceived again and bare a son, and said, Now at this time will my husband keep me company, because I have borne him three sons. Therefore was his name called Levi.
35 Moreover she conceived again and bare a son, saying, Now will I praise the LORD. Therefore she called his name Judah, and left bearing.
Genesis 30
4-9 Rachel and Leah being both barren, give their maids unto their husband, and they bear him children. 25 Leah giveth mandrakes to Rachel that Jacob might lie with her. 27 Laban is enriched for Jacob’s sake. 43 Jacob is made very rich.
1 And when Rachel saw that she bare Jacob no children, Rachel envied her sister, and said unto Jacob, Give me children, or else I die.
2 Then Jacob’s anger was kindled against Rachel, and he said, Am I in God’s stead, which hath withholden from thee the fruit of the womb?
3 And she said, Behold my maid Bilhah, go in to her, and she shall bear upon my knees, and I shall have children also by her.
4 Then she gave him Bilhah her maid to wife, and Jacob went in to her. 5 So Bilhah conceived and bare Jacob a son.
72

6 Then said Rachel, God hath given sentence on my side, and hath also heard my voice, and hath given me a son. Therefore called she his name, Dan.
7 And Bilhah Rachel’s maid conceived again, and bare Jacob the second son.
8 Then Rachel said, With excellent wrestlings have I wrestled with my sister, and have gotten the upper hand. And she called his name, Naphtali.
9 And when Leah saw that she had left bearing, she took Zilpah her maid, and gave her Jacob to wife.
10 And Zilpah Leah’s maid bare Jacob a son.
11 Then said Leah, A company cometh! And she called his name, Gad.
12 Again Zilpah Leah’s maid bare Jacob another son.
13 Then said Leah, Ah, blessed am I, for the daughters will bless me. And she called his name, Asher.
14 ¶ Now Reuben went in the days of the wheat harvest, and found mandrakes in the field and brought them unto his mother Leah. Then said Rachel to Leah, Give me, I pray thee, of thy son’s mandrakes.
15 But she answered her, Is it a small matter for thee to take my husband, except thou take my son’s mandrakes also? Then said Rachel, Therefore he shall sleep with thee this night for thy son’s mandrakes.
16 And Jacob came from the field in the evening, and Leah went out to meet him, and said, Come in to me, for I have bought and paid for thee with my son’s mandrakes. And he slept with her that night.
17 And God heard Leah and she conceived, and bare unto Jacob the fifth son.
18 Then said Leah, God hath given me my reward, because I gave my maid to my husband, and she called his name Issachar.
19 After, Leah conceived again, and bare Jacob the sixth son.
20 Then Leah said, God hath endowed me with a good dowry; now will my husband dwell with me, because I have borne him six sons. And she called his name Zebulun.
73

21 After that, she bare a daughter, and she called her name Dinah.
22 ¶ And God remembered Rachel, and God heard her, and opened her womb.
23 So she conceived and bare a son, and said, God hath taken away my rebuke.
24 And she called his name Joseph, saying, The LORD will give me yet another son.
25 ¶ And as soon as Rachel had borne Joseph, Jacob said to Laban, Send me away that I may go unto my place and to my country.
26 Give me my wives and my children, for whom I have served thee, and let me go; for thou knowest what service I have done thee.
27 To whom Laban answered, If I have now found favor in thy sight, tarry; I have perceived that the LORD hath blessed me for thy sake.
28 Also he said, Appoint unto me thy wages, and I will give it thee.
29 But he said unto him, Thou knowest, what service I have done thee, and in
what taking thy cattle hath been under me.
30 For the little, that thou hadst before I came, is increased into a multitude, and the LORD hath blessed thee by my coming. But now when shall I travel for mine own house also?
31 Then he said, What shall I give thee? And Jacob answered, Thou shalt give me nothing at all. If thou wilt do this thing for me, I will return, feed, and keep thy sheep;
32 I will pass through all thy flocks this day, and separate from them all the sheep with little spots and great spots, and all black lambs among the sheep, and the great spotted, and little spotted among the goats; and it shall be my wages.
33 So shall my righteousness answer for me hereafter, when it shall come for my reward before thy face, and every one that hath not little or great spots among the goats, and black among the sheep, the same shall be theft with me.
34 Then Laban said, Go to, would God it might be according to thy saying.
35 Therefore he took out the same day the he goats that were party colored and
with great spots, and all the she goats with little and great spots, and all that had 74

white in them, and all the black among the sheep, and put them in the keeping of his sons.
36 And he set three days journey between himself and Jacob. And Jacob kept the rest of Laban’s sheep.
37 ¶ Then Jacob took rods of green poplar, and of hazel, and of the chestnut tree, and pilled white strakes in them, and made the white appear in the rods.
38 Then he put the rods, which he had pilled, in the gutters and watering troughs, when the sheep came to drink, before the sheep. (For they were in heat, when they came to drink.)
39 And the sheep were in heat before the rods, and afterward brought forth young of party color, and with small and great spots.
40 And Jacob parted these lambs, and turned the faces of the flock towards those lambs party colored, and all manner of black, among the sheep of Laban; so he put his own flocks by themselves, and put them not with Laban’s flock.
41 And in every ramming time of the stronger sheep, Jacob laid the rods before the eyes of the sheep in the gutters, that they might conceive before the rods.
42 But when the sheep were feeble, he put them not in; and so the feebler were Laban’s, and the stronger Jacob’s.
43 So the man increased exceedingly, and had many flocks, and maidservants, and menservants, and camels and asses.
Genesis 31
Laban's children murmur against Jacob. 3 God Commandeth him to return to his country. 13-14 The care by God for Jacob. 19 Rachel stealeth her father's idols. 23 Laban followeth Jacob. 44 The covenant between Laban and Jacob.
1 Now he heard the words of Laban’s sons, saying, Jacob hath taken away all that was our fathers, and of our father’s goods hath he gotten all this honor.
75

2 Also Jacob beheld the countenance of Laban, that it was not towards him as in times past;
3 And the LORD had said unto Jacob, Turn again into the land of thy fathers, and to thy kindred, and I will be with thee.
4 Therefore Jacob sent and called Rachel and Leah to the field unto his flock.
5 Then said he unto them, I see your father’s countenance, that it is not towards me as it was wont, and the God of my father hath been with me.
6 And ye know that I have served your father with all my might.
7 But your father hath deceived me, and changed my wages ten times; but God suffered him not to hurt me.
8 If he thus said, The spotted shall be thy wages, then all the sheep bare spotted; and if he said thus, The party colored shall be thy reward, then bare all the sheep party colored.
9 Thus hath God taken away your father’s substance, and given it me.
10 ¶ For in ramming time I lifted up mine eyes and saw in a dream, and behold, the he goats leaped upon the she goats, that were party colored with little and great spots spotted.
11 And the Angel of God said to me in a dream, Jacob. And I answered, Lo, I am here.
12 And he said, Lift up now thine eyes, and see all the he goats leaping upon the she goats that are party colored, spotted with little and great spots; for I have seen all that Laban doeth unto thee.
13 I am the God of Bethel, where thou anointedst the pillar, where thou vowedst a vow unto me. Now arise, get thee out of this country and return unto the land where thou wast born.
14 Then answered Rachel and Leah, and said unto him, Have we anymore portion and inheritance in our father’s house?
15 Doeth not he count us as strangers? For he hath sold us, and hath eaten up and consumed our money.
76

16 Therefore all the riches, which God hath taken from our father, is ours and our children’s; now then whatsoever God hath said unto thee, do it.
17 ¶ Then Jacob rose up, and set his sons and his wives upon camels.
18 And he carried away all his flocks, and all his substance which he had gotten, to wit, his riches, which he had gotten in Paddan-aram, to go to Isaac his father unto the land of Canaan.
19 When Laban was gone to sheer his sheep, then Rachel stole her father’s idols.
20 Thus Jacob stole away the heart of Laban the Aramite, for he told him not that he fled.
21 So fled he with all that he had, and he rose up, and passed the river, and set his face toward mount Gilead.
22 And the third day after was it told Laban, that Jacob fled.
23 Then he took his brethren with him, and followed after him seven days journey, and overtook him at mount Gilead.
24 And God came to Laban the Aramite in a dream by night, and said unto him, Take heed that thou speak not to Jacob ought save good.
25 ¶ Then Laban overtook Jacob, and Jacob had pitched his tent in the mount, and Laban also with his brethren pitched upon mount Gilead.
26 Then Laban said to Jacob, What hast thou done? Thou hast even stolen away my heart and carried away my daughters as though they had been taken captives with the sword.
27 Wherefore didst thou flee so secretly and steal away from me, and didst not tell me, that I might have sent thee forth with mirth and with songs, with timbrel and with harp?
28 But thou hast not suffered me to kiss my sons and my daughters! Now thou hast done foolishly in doing so.
29 I am able to do you evil, but the God of your father spake unto me yesternight, saying, Take heed that thou speak not to Jacob ought save good.
77

30 Now though thou wentest thy way, because thou greatly longedst after thy father’s house, yet wherefore hast thou stolen my gods?
31 Then Jacob answered, and said to Laban, Because I was afraid, and thought that thou wouldest have taken thy daughters from me.
32 But with whom thou findest thy gods, let him not live. Search thou before our brethren what I have of thine, and take it to thee, (but Jacob wist not that Rachel had stolen them.)
33 Then came Laban into Jacob’s tent, and into Leah’s tent, and into the two maid’s tents, but found them not. So he went out of Leah’s tent, and entered into Rachel’s tent.
34 (Now Rachel had taken the idols, and put them in the camel’s litter, and sat down upon them) and Laban searched all the tent, but found them not.
35 Then said she to her father, My lord, be not angry that I cannot rise up before thee, for the custom of women is upon me. So he searched, but found not the idols.
36 ¶ Then Jacob was wroth, and chode with Laban; Jacob also answered and said to Laban, What have I trespassed? What have I offended, that thou hast pursued after me?
37 Seeing thou hast searched all my stuff, what hast thou found of all thy household stuff? Put it here before my brethren and thy brethren, that they may judge between us both.
38 This twenty years I have been with thee; thy ewes and thy goats have not cast their young, and the rams of thy flock have I not eaten.
39 Whatsoever was torn of beasts, I brought it not unto thee, but made it good myself. Of my hand didst thou require it, were it stolen by day or stolen by night.
40 I was in the day consumed with heat, and with frost in the night, and my sleep departed from my eyes.
41 Thus have I been twenty years in thy house, and served thee fourteen years for thy two daughters, and six years for thy sheep, and thou hast changed my wages ten times.
78

42 Except the God of my father, the God of Abraham, and the fear of Isaac had been with me, surely thou hadst sent me away now empty. But God beheld my tribulation, and the labor of my hands, and rebuked thee yesternight.
43 Then Laban answered, and said unto Jacob, These daughters are my daughters, and these sons are my sons, and these sheep are my sheep, and all that thou seest, is mine, and what can I do this day unto these my daughters, or to their sons which they have borne?
44 Now therefore come and let us make a covenant, I and thou, which may be a witness between me and thee.
45 Then took Jacob a stone, and set it up as a pillar;
46 And Jacob said unto his brethren, Gather stones. Who brought stones, and
made a heap, and they did eat there upon the heap.
47 And Laban called it Jegar-sahadutha, and Jacob called it Galeed.
48 For Laban said, This heap is witness between me and thee this day. Therefore he called the name of it Galeed.
49 Also he called it Mizpah, because he said, The LORD look between me and thee, when we shall be departed one from another,
50 If thou shalt vex my daughters, or shalt take wives beside my daughters, there is no man with us, behold, God is witness between me and thee.
51 Moreover Laban said to Jacob, Behold this heap, and behold the pillar, which I have set between me and thee;
52 This heap shall be witness, and the pillar shall be witness, that I will not come over this heap to thee, and that thou shalt not pass over this heap and this pillar unto me for evil.
53 The God of Abraham, and the God of Nahor, and the God of their father be judge between us. But Jacob sware by the fear of his father Isaac.
54 Then Jacob did offer a sacrifice upon the mount, and called his brethren to eat bread; and they did eat bread, and tarried all night in the mount.
55 And early in the morning Laban rose up and kissed his sons and his daughters, and blessed them, and Laban departing, went unto his place again.
79

Genesis 32
1 God comforteth Jacob by his Angels. 9-10 He prayeth unto God confessing his unworthiness. 13 He sendeth presents unto Esau. 24-28 He wrestled with God who nameth him Israel.
1 Now Jacob went forth on his journey, and the Angels of God met him.
2 And when Jacob saw them, he said, This is God’s host; and called the name of the same place Mahanaim.
3 Then Jacob sent messengers before him to Esau his brother, unto the land of Seir into the country of Edom;
4 To whom he gave commandment, saying, Thus shall ye speak to my lord Esau: Thy servant Jacob saith thus, I have been a stranger with Laban, and tarried unto this time;
5 I have beeves also and asses, sheep, and menservants, and womenservants, and have sent to shew my lord, that I may find grace in thy sight.
6 ¶ So the messengers came again to Jacob, saying, We came unto thy brother Esau, and he also cometh against thee and four hundred men with him.
7 Then Jacob was greatly afraid, and was sore troubled, and divided the people that was with him, and the sheep, and the beeves, and the camels into two companies.
8 For he said, If Esau come to the one company and smite it, the other company shall escape.
9 ¶ Moreover Jacob said, O God of my father Abraham, and God of my father Isaac, LORD, which saidst unto me, Return unto thy country and to thy kindred, and I will do thee good,
80

10 I am not worthy of the least of all the mercies, and all the truth, which thou hast shewed unto thy servant; for with my staff came I over this Jordan, and now have I gotten two bands.
11 I pray thee, Deliver me from the hand of my brother, from the hand of Esau; for I fear him, lest he will come and smite me, and the mother upon the children.
12 For thou saidst, I will surely do thee good, and make thy seed as the sand of the sea, which cannot be numbered for multitude.
13 ¶ And he tarried there the same night, and took of that which came to hand, a present for Esau his brother:
14 Two hundred she goats and twenty he goats, two hundred ewes and twenty rams,
15 Thirty milch camels with their colts, forty kine, and ten bullocks, twenty she asses and ten foals.
16 So he delivered them into the hand of his servants, every drove by themselves, and said unto his servants, Pass before me, and put a space between drove and drove.
17 And he commanded the foremost, saying, If Esau my brother meet thee, and ask thee, saying, Whose servant art thou? And whither goest thou? And whose are these before thee?
18 Then thou shalt say, They be thy servant Jacob’s; it is a present sent unto my lord Esau. And behold, he himself also is behind us.
19 So likewise commanded he the second and the third, and all that followed the droves, saying, After this manner, ye shall speak unto Esau, when ye find him.
20 And ye shall say moreover, Behold, thy servant Jacob cometh after us (for he thought, I will appease his wrath with the present that goeth before me, and afterward I will see his face; it may be that he will accept me.)
21 So went the present before him, but he tarried that night with the company.
22 And he rose up the same night, and took his two wives, and his two maids, and his eleven children, and went over the ford Jabbok.
23 And he took them, and sent them over the river, and sent over that he had.
81

24 ¶ Now when Jacob was left himself alone, there wrestled a man with him unto the breaking of the day.
25 And he saw that he could not prevail against him, therefore he touched the hollow of his thigh, and the hollow of Jacob’s thigh was loosed, as he wrestled with him.
26 And he said, Let me go, for the morning appeareth. Who answered, I will not let thee go except thou bless me.
27 Then said he unto him, What is thy name? And he said, Jacob.
28 Then said he, Thy name shall be called Jacob no more, but Israel; because thou hast had power with God, thou shalt also prevail with men.
29 Then Jacob demanded, saying, Tell me, I pray thee, thy name. And he said, Wherefore now doest thou ask my name? And he blessed him there
30 And Jacob called the name of the place, Peniel; for, said he, I have seen God face to face, and my life is preserved.
31 And the sun rose up to him as he passed Peniel, and he halted upon his thigh.
32 Therefore the children of Israel eat not of the sinew that shrank in the hollow of the thigh, unto this day, because he touched the sinew that shrank in the hollow of Jacob’s thigh.
Genesis 33
4 Esau and Jacob meet and are agreed. 11 Esau receiveth his gifts. 19 Jacob buyeth a possession; 20 And buildeth an altar.
1 And as Jacob lifted up his eyes, and looked, behold, Esau came, and with him four hundred men. And he divided the children to Leah, and to Rachel, and to the two maids.
82

2 And he put the maids, and their children foremost, and Leah, and her children after, and Rachel and Joseph hindermost.
3 So he went before them and bowed himself to the ground seven times, until he came near to his brother.
4 Then Esau ran to meet him, and embraced him, and fell on his neck, and kissed him, and they wept.
5 And he lifted up his eyes, and saw the women, and the children, and said, Who are these with thee? And he answered, They are the children whom God of his grace hath given thy servant.
6 Then came the maids near, they and their children, and bowed themselves.
7 Leah also with her children came near and made obeisance; and after Joseph and Rachel drew near, and did reverence.
8 Then he said, What meanest thou by all this drove, which I met? Who answered, I have sent it, that I may find favor in the sight of my lord.
9 And Esau said, I have enough, my brother; keep that thou hast to thyself.
10 But Jacob answered, Nay, I pray thee, if I have found grace now in thy sight, then receive my present at my hand, for I have seen thy face, as though I had seen the face of God, because thou hast accepted me.
11 I pray thee take my blessing, that is brought thee, for God hath had mercy on me, and therefore I have all things. So he compelled him, and he took it.
12 And he said, Let us take our journey and go, and I will go before thee.
13 Then he answered him, My lord knoweth, that the children are tender, and the ewes and kin with young under my hand. And if they should overdrive them one day, all the flock would die.
14 Let now my lord go before his servant, and I will drive softly, according to the pass of the cattle, which is before me, and as the children be able to endure, until I come to my lord unto Seir.
15 Then Esau said, I will leave then some of my folk with thee. And he answered, what needeth this? Let me find grace in the sight of my lord.
83

16 ¶ So Esau returned, and went his way that same day unto Seir.
17 And Jacob went forward toward Succoth, and built him a house, and made
booths for his cattle; therefore he called the name of the place Succoth.
18 ¶ Afterward, Jacob came safe to Shechem a city, which is in the land of Canaan, when he came from Paddan-aram, and pitched before the city.
19 And there he bought a parcel of ground, where he pitched his tent, at the hand of the sons of Hamor Shechem’s father, for a hundred pieces of money.
20 And he set up there an altar, and called it, The mighty God of Israel.
Genesis 34
Dinah is ravished. 8 Hamor asketh her in marriage for his son. 22 The Shechemites are circumcised at the request of Jacob’s sons, and the persuasion of Hamor. 25 The whoredom is revenged. 28Jacobreprovethhissons.
1 Then Dinah the daughter of Leah, which she bare unto Jacob, went out to see the daughters of that country.
2 Whom when Shechem the son of Hamor the Hivite lord of that country saw, he took her, and lay with her, and defiled her.
3 So his heart clave unto Dinah the daughter of Jacob, and he loved the maid, and spake kindly unto the maid.
4 Then said Shechem to his father Hamor, saying, Get me this maid to wife.
5 (Now Jacob heard that he had defiled Dinah his daughter, and his sons were with his cattle in the field, therefore Jacob held his peace, until they were come.)
6 ¶ Then Hamor the father of Shechem went out unto Jacob to commune with him.
84

7 And when the sons of Jacob were come out of the field and heard it, it grieved the men, and they were very angry, because he had wrought villainy in Israel, in that he had lain with Jacob’s daughter, which thing ought not to be done.
8 And Hamor communed with them, saying, the soul of my son Shechem longeth for your daughter; give her him to wife, I pray you.
9 So make affinity with us; give your daughters unto us, and take our daughters unto you,
10 And ye shall dwell with us, and the land shall be before you; dwell, and do your business in it, and have your possessions therein.
11 Shechem also said unto her father and unto her brethren, Let me find favor in your eyes, and I will give whatsoever ye shall appoint me.
12 Ask of me abundantly both dowry and gifts, and I will give as ye appoint me, so that ye give me the maid to wife.
13 Then the sons of Jacob answered Shechem and Hamor his father, talking among themselves deceitfully, because he had defiled Dinah their sister,
14 And they said unto them, We cannot do this thing, to give our sister to an uncircumcised man, for that were a reproof unto us.
15 But in this will we consent unto you, if ye will be as we are, that every man child among you be circumcised;
16 Then will we give our daughters to you, and we will take your daughters to us, and will dwell with you, and be one people.
17 But if ye will not hearken unto us to be circumcised, then will we take our daughter and depart.
18 Now their words pleased Hamor, and Shechem Hamor’s son.
19 And the young man deferred not to do the thing because he loved Jacob’s daughter. He was also the most set by of all his father’s house.
20 ¶ Then Hamor and Shechem his Son went unto the gate of their city, and communed with the men of their city, saying,
85

21 These men are peaceable with us; and that they may dwell in the land, and do their affairs therein (for behold, the land hath room enough for them.) Let us take their daughters to wives, and give them our daughters.
22 Only herein will the men consent unto us for to dwell with us, and to be one people, if all the men children among us be circumcised as they are circumcised.
23 Shall not their flocks and their substance and all their cattle be ours? Only let us consent herein unto them, and they will dwell with us.
24 And unto Hamor, and Shechem his son hearkened all that went out of the gate of his city, and all the men children were circumcised, even all that went out of the gate of his city.
25 And on the third day (when they were sore) two of the sons of Jacob, Simeon and Levi, Dinah’s brethren took either of them his sword and went into the city boldly, and slew every male.
26 They slew also Hamor and Shechem his son with the edge of the sword, and took Dinah out of Shechem’s house, and went their way.
27 Again, the other sons of Jacob came upon the dead, and spoiled the city, because they had defiled their sister.
28 They took their sheep and their beeves, and their asses, and whatsoever was in the city, and in the fields.
29 Also they carried away captive and spoiled all their goods, and all their children and their wives, and all that was in the houses.
30 Then Jacob said to Simeon and Levi, Ye have troubled me, and made me stink among the inhabitants of the land, as well the Canaanites, as the Perizzites, and I being few in number, they shall gather themselves together against me, and slay me, and so shall I, and my house be destroyed.
31 And they answered, Should he abuse our sister as a whore?
86

Genesis 35
1 Jacob at God’s commandment goeth up to Bethel to build an altar. 2 He reformeth his household. 5 God maketh the enemies of Jacob afraid. 8 Deborah dieth. 12 The land of Canaan is promised him. 18 Rachel dieth in labor. 22 Reuben lieth with his father’s concubine. 23 The sons of Jacob. 29 The death of Isaac.
1 Then God said to Jacob, Arise, go up to Bethel and dwell there, and make there an altar unto God, that appeared unto thee, when thou fleddest from Esau thy brother.
2 Then said Jacob unto his household and to all that were with him, Put away the strange gods that are among you, and cleanse yourselves, and change your garments;
3 For we will rise and go up to Bethel, and I will make an altar there unto God, which heard me in the day of my tribulation, and was with me in the way which I went.
4 And they gave unto Jacob all the strange gods, which were in their hands, and all their earrings which were in their ears, and Jacob hid them under an oak, which was by Shechem.
5 Then they went on their journey, and the fear of God was upon the cities that were round about them, so that they did not follow after the sons of Jacob.
6 ¶ So came Jacob to Luz, which is in the land of Canaan, (the same is Bethel) he and all the people that was with him.
7 And he built there an altar, and had called the place, The God of Bethel, because that God appeared unto him there, when he fled from his brother.
8 Then Deborah Rebekah’s nurse died, and was buried beneath Bethel under an oak; and he called the name of it Allon Bacuth.
9 ¶ Again God appeared unto Jacob, after he came out of Paddan-aram, and blessed him.
10 Moreover God said unto him, Thy name is Jacob; thy name shall be no more called Jacob, but Israel shall be thy name. And he called his name Israel.
87

11 Again God said unto him, I am God all sufficient; grow and multiply; a nation and a multitude of nations shall spring of thee, and Kings shall come out of thy loins.
12 Also I will give the land, which I gave to Abraham and Isaac, unto thee, and unto thy seed after thee will I give that land.
13 So God ascended from him in the place where he had talked with him.
14 And Jacob set up a pillar in the place where he talked with him, a pillar of stone, and poured drink offering thereon; also he poured oil thereon.
15 And Jacob called the name of the place where God spake with him, Bethel.
16 ¶ Then they departed from Bethel, and when there was about half a days journey of ground to come to Ephrath, Rachel travailed, and in travailing she was in peril.
17 And when she was in pains of her labor, the midwife said unto her, Fear not, for thou shalt have this son also.
18 Then as she was about to yield up the ghost (for she died) she called his name Ben-oni; but his father called him Benjamin.
19 Thus died Rachel and was buried in the way to Ephrath, which is Bethlehem.
20 And Jacob set a pillar upon her grave; this is the pillar of Rachel’s grave unto this day.
21 ¶ Then Israel went forward, and pitched his tent beyond Migdal-eder.
22 Now when Israel dwelt in that land, Reuben went, and lay with Bilhah his father’s concubine, and it came to Israel’s ear. And Jacob had twelve sons.
23 The sons of Leah: Reuben Jacob’s eldest son, and Simeon, and Levi, and Judah, and Issachar, and Zebulun.
24 The sons of Rachel: Joseph and Benjamin.
25 And the sons of Bilhah Rachel’s maid: Dan and Naphtali.
26 And the sons of Zilpah Leah’s maid: Gad and Asher. These are the sons of Jacob, which were born him in Paddan-aram.
88

27 ¶ Then Jacob came unto Isaac his father to Mamre a city of Arbah. This is Hebron, where Abraham and Isaac were strangers.
28 And the days of Isaac were a hundred and fourscore years.
29 And Isaac gave up the ghost and died, and was gathered unto his people, being old and full of days; and his sons Esau and Jacob buried him.
Genesis 36
2 The wives of Esau. 7 Jacob and Esau are rich. 9 The genealogy of Esau. 24 The finding of mules.
1 Now these are the generations of Esau, which is Edom.
2 Esau took his wives of the daughters of Canaan: Adah the daughter of Elon a Hittite, and Aholibamah the daughter of Anah, the daughter of Zibeon a Hivite;
3 And took Basemath Ishmael’s daughter, sister of Nebajoth.
4 And Adah bare unto Esau, Eliphaz; and Basemath bare Reuel;
5 Also Aholibamah bare Jeush, and Jaalam, and Korah. These are the sons of Esau which were born to him in the land of Canaan.
6 So Esau took his wives and his sons, and his daughters, and all the souls of his house, and his flocks, and all his cattle, and all his substance, which he had gotten in the land of Canaan, and went into another country from his brother Jacob.
7 For their riches were so great, that they could not dwell together, and the land, wherein they were strangers, could not receive them because of their flocks.
8 Therefore dwelt Esau in mount Seir; this Esau is Edom.
9 ¶ So these are the generations of Esau father of Edom in mount Seir.
89

10 These are the names of Esau’s sons: Eliphaz, the son of Adah, the wife of Esau, and Reuel the son of Basemath, the wife of Esau.
11 And the sons of Eliphaz were Teman, Omar, Zepho, and Gatam, and Kenaz.
12 And Timna was concubine to Eliphaz Esau’s son, and bare unto Eliphaz, Amalek. These be the sons of Adah Esau’s wife.
13 ¶ And these are the sons of Reuel: Nahath, and Zerah, Shammah, and Mizzah. These were the sons of Basemath Esau’s wife.
14 ¶ And these were the sons of Aholibamah the daughter of Anah, daughter of Zibeon Esau’s wife: for she bare unto Esau, Jeush, and Jaalam, and Korah.
15 ¶ These were Dukes of the sons of Esau. The sons of Eliphaz, the firstborn of Esau: Duke Teman, Duke Omar, Duke Zepho, Duke Kenaz,
16 Duke Korah, Duke Gatam, Duke Amalek. These are the Dukes that came of Eliphaz in the land of Edom; these were the sons of Adah.
17 ¶ And these are the sons of Reuel Esau’s son: Duke Nahath, Duke Zerah, Duke Shammah, Duke Mizzah. These are the Dukes that came of Reuel in the land of Edom; these are the sons of Basemath Esau’s wife.
18 ¶ Likewise these were the sons of Aholibamah Esau’s wife: Duke Jeush, Duke Jaalam, Duke Korah. These Dukes came of Aholibamah, the daughter of Anah Esau’s wife.
19 These are the children of Esau, and these are the Dukes of them. This Esau is Edom.
20 ¶ These are the sons of Seir the Horite, which inhabited the land before Lotan, and Shobal, and Zibeon, and Anah.
21 And Dishon, and Ezer, and Dishan. These are the Dukes of the Horites, the sons of Seir in the land of Edom.
22 And the sons of Lotan were, Hori and Hemam; and Lotan’s sister was Timna.
23 And the sons of Shobal were these: Alvan, and Manahath, and Ebal, Shepho, and Onam.
90

24 And these are the sons of Zibeon: both Aiah, and Anah. This was Anah that found mules in the wilderness, as he fed his father Zibeon’s asses.
25 And the children of Anah were these: Dishon and Aholibamah, the daughter of Anah.
26 Also these are the sons of Dishan: Hemdan, and Eshban, and Ithran, and Cheran.
27 The sons of Ezer are these: Bilhan, and Zaavan, and Akan.
28 The sons of Dishan are these: Uz, and Aran.
29 These are the Dukes of the Horites: Duke Lotan, Duke Shobal, Duke Zibeon, Duke Anah,
30 Duke Dishon, Duke Ezer, Duke Dishan. These be the Dukes of the Horites, after their Dukedoms in the land of Seir.
31 ¶ And these are the Kings that reigned in the land of Edom, before there reigned any King over the children of Israel.
32 Then Bela the son of Beor reigned in Edom, and the name of his city was Dinhabah.
33 And when Bela died, Jobab the son of Zerah of Bozrah reigned in his stead.
34 When Jobab also was dead, Husham of the land of Temani reigned in his stead.
35 And after the death of Husham, Hadad the son of Bedad, which slew Midian in the field of Moab, reigned in his stead, and the name of his city was Avith.
36 When Hadad was dead, then Samlah of Masrekah reigned in his stead.
37 When Samlah was dead, Shaul of Rehoboth by the river, reigned in his stead. 38 When Shaul died, Baal-hanan the son of Achbor reigned in his stead.
39 And after the death of Baal-hanan the son of Achbor, Hadad reigned in his stead, and the name of his city was Pau; and his wife’s name was Mehetabel the daughter of Matred, the daughter of Mezahab.
91

40 Then these are the names of the Dukes of Esau according to their families, their places and by their names: Duke Timna, Duke Alvah, Duke Jetheth,
41 Duke Aholibamah, Duke Elah, Duke Pinon,
42 Duke Kenaz, Duke Teman, Duke Mibzar,
43 Duke Magdiel, Duke Iram. These be the Dukes of Edom, according to their habitations, in the land of their inheritance. This Esau is the father of Edom.
Genesis 37
2 Joseph accuseth his brethren. 5 He dreameth and is hated of his brethren. 28 They sell him to the Ishmaelites. 34 Jacob bewaileth Joseph.
1 Jacob now dwelt in the land, wherein his father was a stranger, in the land of Canaan.
2 These are the generations of Jacob. When Joseph was seventeen years old, he kept sheep with his brethren, and the child was with the sons of Bilhah, and with the sons of Zilpah, his father’s wives. And Joseph brought unto their father their evil saying.
3 Now Israel loved Joseph more than all his sons, because he begat him in his old age; and he made him a coat of many colors.
4 So when his brethren saw that their father loved him more than all his brethren, then they hated him, and could not speak peaceably unto him.
5 ¶ And Joseph dreamed a dream, and told his brethren, who hated him so much the more.
6 For he said unto them, Hear, I pray you, this dream which I have dreamed.
7 Behold now, we were binding sheaves in the midst of the field, and lo, my sheaf arose and also stood upright; and behold, your sheaves compassed round about, and did reverence to my sheaf.
92

8 Then his brethren said to him, What, shalt thou reign over us, and rule us? Or shalt thou have altogether dominion over us? And they hated him so much the more, for his dreams, and for his words.
9 ¶ Again he dreamed another dream, and told it his brethren, and said, Behold, I have had one dream more, and behold, the sun and the moon and eleven stars did reverence to me.
10 Then he told it unto his father and to his brethren, and his father rebuked him, and said unto him, What is this dream, which thou hast dreamed? Shall I, and thy mother, and thy brethren come indeed and fall on the ground before thee?
11 And his brethren envied him, but his father noted the saying.
12 ¶ Then his brethren went to keep their father’s sheep in Shechem.
13 And Israel said unto Joseph, Do not thy brethren keep in Shechem? Come and I will send thee to them.
14 And he answered him, I am here. Then he said unto him, Go now, see whether it be well with thy brethren, and how the flocks prosper, and bring me word again. So he sent him from the valley of Hebron, and he came to Shechem.
15 ¶ Then a man found him, for lo, he was wandering in the field, and the man asked him, saying, What seekest thou?
16 And he answered, I seek my brethren; tell me, I pray thee, where they keep sheep.
17 And the man said, they are departed hence; for I heard them say, Let us go unto Dothan. Then went Joseph after his brethren, and found them in Dothan.
18 And when they saw him afar off, even before he came at them, they conspired against him for to slay him.
19 For they said one to another, Behold, this dreamer cometh.
20 Come now therefore, and let us slay him, and cast him into some pit, and we will say, A wicked beast hath devoured him; then we shall see, what will come of his dreams.
93

21 But when Reuben heard that, he delivered him out of their hands, and said, Let us not kill him.
22 Also Reuben said unto them, Shed not blood, but cast him into this pit that is in the wilderness, and lay no hand upon him. Thus he said, that he might deliver him out of their hand, and restore him to his father again.
23 ¶ Now when Joseph was come unto his brethren, they stripped Joseph out of his coat, his party colored coat that was upon him.
24 And they took him, and cast him into a pit, and the pit was empty, without water in it.
25 Then they sat them down to eat bread. And they lifted up their eyes and looked, and behold, there came a company of Ishmaelites from Gilead, and their camels laden with spicery, and balm, and myrrh, and were going to carry it down into Egypt.
26 Then Judah said unto his brethren, What availeth it, if we slay our brother, though we keep his blood secret?
27 Come and let us sell him to the Ishmaelites, and let not our hands be upon him; for he is our brother and our flesh. And his brethren obeyed.
28 Then the Midianites merchant men passed by, and they drew forth, and lifted Joseph out of the pit, and sold Joseph unto the Ishmaelites for twenty pieces of silver. Who brought Joseph into Egypt.
29 ¶ Afterward Reuben returned to the pit, and behold, Joseph was not in the pit; then he rent his clothes,
30 And returned to his brethren, and said, The child is not yonder, and I, whither shall I go?
31 And they took Joseph’s coat, and killed a kid of the goats, and dipped the coat in the blood.
32 So they sent that party colored coat, and they brought it unto their father, and said, This have we found; see now, whether it be thy son’s coat, or not.
33 Then he knew, it and said, It is my son’s coat. A wicked beast hath devoured him. Joseph is surely torn in pieces.
94

34 And Jacob rent his clothes, and put sackcloth about his loins, and sorrowed for his son a long season.
35 Then all his sons and all his daughters rose up to comfort him, but he would not be comforted, but said, Surely I will go down into the grave unto my son mourning. So his father wept for him.
36 And the Midianites sold him into Egypt unto Potiphar a Eunuch of Pharaoh’s, and his chief steward.
Genesis 38
2 The marriage of Judah. 7-9 The trespass of Er and Onan, and the vengeance of God that came thereupon. 18 Judah lieth with his daughter in law Tamar. 24 Tamar is judged to be burned for whoredom. 29-30 The birth of Pharez and Zerah.
1 And at that time Judah went down from his brethren, and turned in to a man called Hirah an Adullamite.
2 And Judah saw there the daughter of a man called Shua a Canaanite; and he took her [to wife], and went in unto her.
3 So she conceived and bare a son, and he called his name Er.
4 And she conceived again and bare a son, and she called his name Onan.
5 Moreover she bare yet a son, whom she called Shelah; and Judah was at Chezib when she bare him.
6 Then Judah took a wife to Er his firstborn son, whose name was Tamar.
7 Now Er the firstborn of Judah, was wicked in the sight of the LORD, therefore
the LORD slew him.
8 Then Judah said to Onan, Go in unto thy brother’s wife, and do the office of a kinsman unto her, and raise up seed unto thy brother.
95

9 And Onan knew that the seed should not be his. Therefore when he went in unto his brother’s wife, he spilled it on the ground, lest he should give seed unto his brother.
10 And it was wicked in the eyes of the LORD, which he did; wherefore he slew him also.
11 Then said Judah to Tamar his daughter in law, Remain a widow in thy father’s house, till Shelah my son grows up (for he thought thus, Lest he die as well as his brethren.) So Tamar went and dwelt in her father’s house.
12 ¶ And in process of time also the daughter of Shua Judah’s wife died. Then Judah, when he had left mourning, went up to his sheep shearers to Timnah, he, and his neighbor Hirah the Adullamite.
13 And it was told Tamar, saying, Behold, thy father in law goeth up to Timnah, to shear his sheep.
14 Then she put her widow’s garments off from her, and covered her with a veil, and wrapped herself, and sat down in Pethah-enaim, which is by the way to Timnah, because she saw that Shelah was grown, and she was not given unto him to wife.
15 When Judah saw her, he judged her to be a whore, for she had covered her face.
16 And he turned to the way towards her, and said, Come, I pray thee, let me lie with thee. (For he knew not that she was his daughter in law.) And she answered, What wilt thou give me for to lie with me?
17 Then said he, I will send thee a kid of the goats from the flock. And she said, Well, if thou wilt give me a pledge, till thou send it?
18 Then he said, What is the pledge that I shall give thee? And she answered, Thy signet, and thy cloak, and thy staff that is in thy hand. So he gave it her, and lay by her, and she was with child by him.
19 Then she rose, and went and put her veil from her and put on her widow’s raiment.
20 Afterward Judah sent a kid of the goats by the hand of his neighbor the Adullamite, for to receive his pledge from the woman’s hand, but he found her not.
96

21 Then asked he the men of that place, saying, Where is the whore, that sat in Enaim by the wayside? And they answered, There was no whore here.
22 He came therefore to Judah again, and said, I cannot find her, and also the men of the place said, There was no whore there.
23 Then Judah said, Let her take it to her, lest we be shamed. Behold, I sent this kid, and thou hast not found her.
24 ¶ Now after three months, one told Judah, saying, Tamar thy daughter in law hath played the whore, and lo, with playing the whore, she is great with child. Then Judah said, Bring ye her forth and let her be burned.
25 When she was brought forth, she sent to her father in law, saying, By the man, unto whom these things pertain, am I with child. And said also, Look, I pray thee, whose these are, the seal, and the cloak, and the staff.
26 Then Judah knew them, and said, She is more righteous than I, for she hath done it because I gave her not to Shelah my son. So he lay with her no more.
27 ¶ Now, when the time was come that she should be delivered, behold, there were twins in her womb.
28 And when she was in travail, the one put out his hand, and the midwife took and bound a red thread about his hand, saying, This is come out first.
29 But when he plucked his hand back again, lo, his brother came out, and the midwife said, How hast thou broken the breach upon thee? And his name was called Pharez.
30 And afterward came out his brother that had the red thread about his hand, and his name was called Zerah.
97

Genesis 39
1 Joseph is sold to Potiphar. 2 God prospereth him. 7 Potiphar's wife tempteth him. 13-20 He is accused and cast in prison. 21 God sheweth him favor.
1 Now Joseph was brought down into Egypt; and Potiphar a Eunuch of Pharaoh’s (and his chief steward an Egyptian) bought him at the hand of the Ishmaelites, which had brought him thither.
2 And the LORD was with Joseph, and he was a man that prospered and was in the house of his master the Egyptian.
3 And his master saw that the LORD was with him, and that the LORD made all that he did to prosper in his hand.
4 So Joseph found favor in his sight, and served him, and he made him ruler of his house, and put all that he had in his hand.
5 And from that time that he had made him ruler over his house and over all that he had, the LORD blessed the Egyptian’s house for Joseph’s sake; and the blessing of the LORD was upon all that he had in the house, and in the field.
6 Therefore he left all that he had in Joseph’s hand, and took account of nothing, that was with him, save only of the bread, which he did eat. And Joseph was a fair person, and well favored.
7 ¶ Now therefore after these things, his master’s wife cast her eyes upon Joseph, and said, Lie with me.
8 But he refused and said to his master’s wife, Behold, my master knoweth not what he hath in the house with me, but hath committed all that he hath to my hand.
9 There is no man greater in this house than I, neither hath he kept anything from me, but only thee, because thou art his wife. How then can I do this great wickedness and so sin against God?
10 And albeit she spake to Joseph day by day, yet he hearkened not unto her, to lie with her, or to be in her company.
11 Then on a certain day Joseph entered into the house to do his business, and there was no man of the household in the house;
98

12 Therefore she caught him by his garment, saying, Sleep with me. But he left his garment in her hand and fled, and got him out.
13 Now when she saw that he had left his garment in her hand, and was fled out,
14 She called unto the men of her house, and told them, saying, Behold, he hath brought in a Hebrew unto us to mock us. Who came in to me for to have slept with me, but I cried with a loud voice.
15 And when he heard that I lifted up my voice and cried, he left his garment with me, and fled away, and got him out.
16 So she laid up his garment by her, until her lord came home.
17 Then she told him according to these words, saying, The Hebrew servant, which thou hast brought unto us, came in to me, to mock me.
18 But as soon as I lifted up my voice and cried, he left his garment with me, and fled out.
19 Then when his master heard the words of his wife, which she told him, saying, After this manner did thy servant to me, his anger was kindled.
20 And Joseph’s master took him and put him in prison, in the place, where the king’s prisoners lay bound; and there he was in prison.
21 ¶ But the LORD was with Joseph, and shewed him mercy, and got him favor in the sight of the master of the prison.
22 And the keeper of the prison committed to Joseph’s hand all the prisoners that were in the prison, and whatsoever they did there, that did he.
23 And the keeper of the prison looked unto nothing that was under his hand, seeing that the LORD was with him; for whatsoever he did, the LORD made it to prosper.
99

Genesis 40
8 The interpretation of dreams is of God. 12-19 Joseph expoundeth the dreams of the two prisoners. 23 The ingratitude of the butler.
1 And after these things, the butler of the King of Egypt and his baker offended their lord the King of Egypt.
2 And Pharaoh was angry against his two officers, against the chief butler, and against the chief baker.
3 Therefore he put them in ward in his chief steward’s house, in the prison and place where Joseph was bound.
4 And the chief steward gave Joseph charge over them, and he served them; and they continued a season in ward.
5 ¶ And they both dreamed a dream, either of them his dream in one night, each one according to the interpretation of his dream, both the butler and the baker of the King of Egypt, which were bound in the prison.
6 And when Joseph came in unto them in the morning, and looked upon them, behold, they were sad.
7 And he asked Pharaoh’s officers, that were with him in his master’s ward, saying, Wherefore look ye so sadly today?
8 Who answered him, We have dreamed, each one a dream, and there is none to interpret the same. Then Joseph said unto them, Are not interpretations of God? Tell them me now.
9 So the chief butler told his dream to Joseph, and said unto him, In my dream, behold, a vine was before me,
10 And in the vine were three branches. And as it budded, her flower came forth, and the clusters of grapes waxed ripe.
11 And I had Pharaoh’s cup in my hand, and I took the grapes, and wrung them into Pharaoh’s cup, and I gave the cup into Pharaoh’s hand.
12 Then Joseph said unto him, This is the interpretation of it: The three branches are three days.
100

13 Within three days shall Pharaoh lift up thy head, and restore thee unto thy office, and thou shalt give Pharaoh’s cup into his hand after the old manner, when thou wast his butler.
14 But have me in remembrance with thee, when thou art in good case, and shew mercy, I pray thee, unto me, and make mention of me to Pharaoh, that thou mayest bring me out of this house.
15 For I was stolen away by theft out of the land of the Hebrews, and here also have I done nothing, wherefore they should put me in the dungeon.
16 And when the chief baker saw that the interpretation was good, he said unto Joseph, Also I thought in my dream that I had three white baskets on my head.
17 And in the uppermost basket there was of all manner baked meats for Pharaoh, and the birds did eat them out of the basket upon my head.
18 Then Joseph answered, and said, This is the interpretation thereof: The three baskets are three days;
19 Within three days shall Pharaoh take thy head from thee, and shall hang thee on a tree, and the birds shall eat thy flesh from off thee.
20 ¶ And so the third day, which was Pharaoh’s birthday, he made a feast unto all his servants; and he lifted up the head of the chief butler, and the head of the chief baker among his servants.
21 And he restored the chief butler unto his butlership, who gave the cup into Pharaoh’s hand,
22 But he hanged the chief baker, as Joseph had interpreted unto them. 23 Yet the chief butler did not remember Joseph, but forgot him.
101

Genesis 41
26 Pharaoh's dreams are expounded by Joseph. 40 He is made ruler over all Egypt. 43 Joseph's name is changed. 50 He hath two sons Manasseh and Ephraim. 54 The famine beginneth throughout the world.
1 And two years after, Pharaoh also dreamed, and behold, he stood by a river,
2 And lo, there came out of the river seven goodly kine and fat fleshed, and they fed in a meadow;
3 And lo, seven other kine came up after them out of the river, evil favored and lean fleshed, and stood by the other kine upon the brink of the river.
4 And the evil favored and lean fleshed kine did eat up the seven well favored and fat kine. So Pharaoh awoke.
5 Again he slept, and dreamed the second time; and behold, seven ears of corn grew upon one stalk, rank and goodly.
6 And lo, seven thin ears, and blasted with the East wind, sprang up after them; 7 And the thin ears devoured the seven rank and full ears. Then Pharaoh
awaked, and lo, it was a dream.
8 Now when the morning came, his spirit was troubled, therefore he sent and called all the soothsayers of Egypt, and all the wise men thereof, and Pharaoh told them his dreams, but none could interpret them to Pharaoh.
9 Then spake the chief butler unto Pharaoh, saying, I call to mind my faults this day .
10 Pharaoh being angry with his servants, put me in ward in the chief steward’s house, both me, and the chief baker.
11 Then we dreamed a dream in one night, both I, and he; we dreamed each man according to the interpretation of his dream.
12 And there was with us a young man, a Hebrew, servant unto the chief steward, whom when we told, he declared our dreams to us, to everyone he declared according to his dream.
102

13 And as he declared unto us, so it came to pass; for he restored me to my office, and hanged him.
14 Then sent Pharaoh, and called Joseph, and they brought him hastily out of prison, and he shaved him, and changed his raiment, and came to Pharaoh.
15 Then Pharaoh said to Joseph, I have dreamed a dream, and no man can interpret it, and I have heard say of thee, that when thou hearest a dream, thou canst interpret it.
16 And Joseph answered Pharaoh, saying, Without me; God shall answer for the wealth of Pharaoh.
17 And Pharaoh said unto Joseph, In my dream, behold, I stood by the bank of the river;
18 And lo, there came up out of the river seven fat fleshed, and well favored kine, and they fed in the meadow.
19 Also lo, seven other kine came up after them, poor and very evil favored, and lean fleshed, I never saw the like in all the land of Egypt, for evil favored;
20 And the lean and evil favored kine did eat up the first seven fat kine.
21 And when they had eaten them up, it could not be known that they had eaten them, but they were still as evil favored, as they were at the beginning. So did I awake.
22 Moreover I saw in my dream, and behold, seven ears sprang out of one stalk, full and fair.
23 And lo, seven ears, withered, thin, and blasted with the East wind, sprang up after them.
24 And the thin ears devoured the seven good ears. Now I have told the soothsayers, and none can declare it unto me.
25 ¶ Then Joseph answered Pharaoh, Both Pharaoh’s dreams are one. God hath shewed Pharaoh what he is about to do.
26 The seven good kine are seven years, and the seven good ears are seven years; this is one dream.
103

27 Likewise the seven thin and evil favored kine, that came out after them, are seven years, and the seven empty ears blasted with the East wind, are seven years of famine.
28 This is the thing which I have said unto Pharaoh, that God hath shewed unto Pharaoh, what he is about to do.
29 Behold, there come seven years of great plenty in all the land of Egypt.
30 Again, there shall arise after them seven years of famine, so that all the plenty shall be forgotten in the land of Egypt, and the famine shall consume the land;
31 Neither shall the plenty be known in the land, by reason of this famine that shall come after, for it shall be exceeding great.
32 And therefore the dream was doubled unto Pharaoh the second time, because the thing is established by God, and God hasteth to perform it.
33 Now therefore let Pharaoh provide for a man of understanding and wisdom, and set him over the land of Egypt.
34 Let Pharaoh make and appoint officers over the land, and take up the fifth part of the land of Egypt in the seven plenteous years.
35 Also let them gather all the food of these good years that come, and lay up corn under the hand of Pharaoh for food, in the cities, and let them keep it.
36 So the food shall be for the provision of the land, against the seven years of famine, which shall be in the land of Egypt, that the land perish not by famine.
37 ¶ And the saying pleased Pharaoh and all his servants.
38 Then said Pharaoh unto his servants, Can we find such a man as this, in
whom is the Spirit of God?
39 The Pharaoh said to Joseph, For as much as God hath shewed thee all this,
there is no man of understanding, or of wisdom like unto thee.
40 Thou shalt be over my house, and at thy word shall all my people be armed, only in the king’s throne will I be above thee.
41 Moreover Pharaoh said to Joseph, Behold, I have set thee over all the land of Egypt.
104

42 And Pharaoh took off his ring from his hand, and put it upon Joseph’s hand, and arrayed him in garments of fine linen, and put a golden chain about his neck.
43 So he set him upon the best chariot that he had, save one. And they cried before him, Abrek, and placed him over all the land of Egypt.
44 Again Pharaoh said unto Joseph, I am Pharaoh, and without thee shall no man lift up his hand or his foot in all the land of Egypt.
45 And Pharaoh called Joseph’s name Zaphenath-paneah; and he gave him to wife Asenath the daughter of Poti-pherah Prince of On. Then went Joseph abroad in the land of Egypt.
46 ¶ And Joseph was thirty years old when he stood before Pharaoh King of Egypt. And Joseph departing from the presence of Pharaoh, went throughout all the land of Egypt.
47 And in the seven plenteous years the earth brought forth store.
48 And he gathered up all the food of the seven plenteous years, which were in the land of Egypt, and laid up food in the cities. The food of the field, that was round about every city, laid he up in the same.
49 So Joseph gathered wheat, like unto the sand of the sea in multitude out of measure, until he left numbering, for it was without number.
50 Now unto Joseph were born two sons (before the years of famine came) which Asenath the daughter of Poti-pherah prince of On bare unto him.
51 And Joseph called the name of the firstborn Manasseh. For God, said he, hath made me forget all my labor and all my father’s household.
52 Also he called the name of the second, Ephraim, For God, said he, hath made me fruitful in the land of my affliction.
53 ¶ So the seven years of the plenty that was in the land of Egypt were ended.
54 Then began the seven years of famine to come, according as Joseph had said. And the famine was in all lands, but in all the land of Egypt was bread.
105

55 At the length all the land of Egypt was famished, and the people cried to Pharaoh for bread. And Pharaoh said unto all the Egyptians, Go to Joseph; what he saith to you, do ye.
56 When the famine was upon all the land, Joseph opened all places, wherein the store was, and sold unto the Egyptians, for the famine waxed sore in the land of Egypt.
57 And all countries came to Egypt to buy corn of Joseph, because the famine was sore in all lands.
Genesis 42
3 Joseph's brethren come into Egypt to buy corn. 7 He knoweth them, and trieth them. 24-25 Simeon is put in prison. 34 The others go to fetch Benjamin.
1 Then Jacob saw that there was food in Egypt, and Jacob said unto his sons, Why gaze ye one upon another?
2 And he said, Behold, I have heard that there is food in Egypt, Get you down thither, and buy us food thence, that we may live and not die.
3 ¶ So went Joseph’s ten brethren down to buy corn of the Egyptians.
4 But Benjamin Joseph’s brother, would not Jacob send with his brethren, for he said, Lest death should befall him.
5 And the sons of Israel came to buy food among them that came, for there was famine in the land of Canaan.
6 Now Joseph was governor of the land, who sold to all the people of the land. Then Joseph’s brethren came, and bowed their face to the ground before him.
7 And when Joseph saw his brethren, he knew them, and made himself strange toward them, and spake to them roughly, and said unto them, Whence come ye? Who answered, Out of the land of Canaan, to buy vitaille.
106

8 (Now Joseph knew his brethren, but they knew not him.
9 And Joseph remembered the dreams, which he dreamed of them) and he said
unto them, Ye are spies, and are come to see the weakness of the land.
10 But they said unto him, Nay, my lord, but to buy vitaille thy servants are
come.
11 We are all one man’s sons; we mean truly, and thy servants are not spies.
12 But he said unto them, Nay, but ye are come to see the weakness of the land.
13 And they said, We thy servants are twelve brethren, the sons of one man in the land of Canaan; and behold, the youngest is this day with our father, and one is not.
14 Again Joseph said unto them, This is it that I spake unto you, saying, Ye are spies.
15 Hereby ye shall be proved: by the life of Pharaoh, ye shall not go hence, except your youngest brother come hither.
16 Send one of you which may fetch your brother, and ye shall be kept in prison, that your words may be proved, whether there be truth in you. Or else by the life of Pharaoh ye are but spies.
17 So he put them in ward three days.
18 Then Joseph said unto them the third day, This do, and live, for I fear God;
19 If ye be true men, let one of your brethren be bound in your prison house; and go ye, carry food for the famine of your houses;
20 But bring your younger brother unto me, that your words may be tried, and that ye die not. And they did so.
21 ¶ And they said one to another, We have verily sinned against our brother, in that we saw the anguish of his soul, when he besought us, and we would not hear him; therefore is this trouble come upon us.
22 And Reuben answered them, saying, Warned I not you, saying, Sin not against the child, and ye would not hear? And lo, his blood is now required.
107

23 (And they were not aware that Joseph understood them, for he spake unto them by an interpreter.)
24 Then he turned from them, and wept, and turned to them again, and communed with them, and took Simeon from among them, and bound him before their eyes.
25 ¶ So Joseph commanded that they should fill their sacks with wheat, and put every man’s money again in his sack, and give them vitaille for the journey. And thus did he unto them.
26 And they laid their vitaille upon their asses, and departed thence.
27 And as one of them opened his sack for to give his ass provender in the Inn, he espied his money; for lo, it was in his sack’s mouth.
28 Then he said unto his brethren, My money is restored; for lo, it is even in my sack. And their heart failed them, and they were astonished, and said one to another, What is this, that God hath done unto us?
29 ¶ And they came unto Jacob their father unto the land of Canaan, and told him all that had befallen them, saying,
30 The man, who is lord of the land, spake roughly to us, and put us in prison as spies of the country.
31 And we said unto him, We are true men, and are not spies.
32 We be twelve brethren, sons of our father; one is not, and the youngest is this
day with our father in the land of Canaan.
33 Then the lord of the country said unto us, Hereby shall I know if ye be true men: Leave one of your brethren with me, and take food for the famine of your houses and depart,
34 And bring your youngest brother unto me, that I may know that ye are not spies, but true men; so will I deliver you your brother, and ye shall occupy in the land.
35 ¶ And as they emptied their sacks, behold, every man’s bundle of money was in his sack; and when they and their father saw the bundles of their money, they were afraid.
108

36 Then Jacob their father said to them, Ye have robbed me of my children: Joseph is not, and Simeon is not, and ye will take Benjamin. All these things are against me.
37 Then Reuben answered his father, saying, Slay my two sons, if I bring him not to thee again; deliver him to my hand, and I will bring him to thee again.
38 But he said, My son shall not go down with you, for his brother is dead, and he is left alone. If death come unto him by the way which ye go, then ye shall bring my gray head with sorrow unto the grave.
Genesis 43
13 Jacob suffereth Benjamin to depart with his children. 18 Simeon is delivered out of prison. 30 Joseph goeth aside and weepeth. 32 They feast together.
1 Now great famine was in the land.
2 And when they had eaten up the vitaille, which they had brought from Egypt,
their father said unto them, Turn again, and buy us a little food.
3 And Judah answered him, saying, The man charged us by an oath, saying,
Never see my face, except your brother be with you.
4 If thou wilt send our brother with us, we will go down, and buy thee food;
5 But if thou wilt not send him, we will not go down; for the man said unto us, Look me not in the face, except your brother be with you.
6 And Israel said, Wherefore dealt ye so evil with me, as to tell the man, whether ye had yet a brother or not?
7 And they answered, The man asked straitly of ourselves and of our kindred, saying, Is your father yet alive? Have ye any brother? And we told him according to these words. Could we know certainly that he would say, Bring your brother down?
109

8 Then said Judah to Israel his father, Send the boy with me, that we may rise and go, and that we may live, and not die, both we, and thou, and our children.
9 I will be surety for him; of my hand shalt thou require him. If I bring him not to thee, and set him before thee, then let me bear the blame forever.
10 For except we had made this tarrying, doubtless by this we had returned the second time.
11 Then their father Israel said unto them, If it must needs be so now, do thus: take of the best fruits of the land in your vessels, and bring the man a present, a little rosen, and a little honey, spices and myrrh, nuts, and almonds;
12 And take double money in your hand, and the money, that was brought again in your sack’s mouths; carry it again in your hand, lest it were some oversight.
13 Take also your brother and arise, and go again to the man.
14 And God almighty give you mercy in the sight of the man, that he may deliver you your other brother, and Benjamin. But I shall be robbed of my child, as I have been.
15 ¶ Thus the men took this present, and took twice so much money in their hand with Benjamin, and rose up, and went down to Egypt, and stood before Joseph.
16 And when Joseph saw Benjamin with them, he said to his steward, Bring these men home and kill meat, and make ready; for the men shall eat with me at noon.
17 And the man did as Joseph bade, and brought the men unto Joseph’s house.
18 Now when the men were brought into Joseph’s house, they were afraid, and said, Because of the money, that came in our sack’s mouths at the first time, are we brought, that he may pick a quarrel against us, and lay something to our charge, and bring us in bondage and our asses.
19 Therefore came they to Joseph’s steward, and communed with him at the door of the house.
20 And said, Oh sir, we came indeed down hither at the first time to buy food,
110

21 And as we came to an Inn and opened our sacks, behold, every man’s money was in his sack’s mouth, even our money in full weight, but we have brought it again in our hands.
22 Also other money have we brought in our hands to buy food, but we cannot tell, who put our money in our sacks.
23 And he said, Peace be unto you, fear not. Your God, and the God of your father hath given you that treasure in your sacks; I had your money. And he brought forth Simeon to them.
24 So the man led them into Joseph’s house, and gave them water to wash their feet, and gave their asses provender.
25 And they made ready their present against Joseph came at noon, (for they heard say, that they should eat bread there.)
26 When Joseph came home, they brought the present into the house to him, which was in their hands, and bowed down to the ground before him.
27 And he asked them of their prosperity, and said, Is your father the old man, of whom ye told me, in good health? Is he yet alive?
28 Who answered, Thy servant our father is in good health; he is yet alive. And they bowed down, and made obeisance.
29 And he lifting up his eyes, beheld his brother Benjamin, his mother’s son, and said, Is this your younger brother, of whom ye told me? And he said, God be merciful unto thee, my son.
30 And Joseph made haste (for his affection was inflamed toward his brother, and sought where to weep) and entered into his chamber, and wept there.
31 Afterward he washed his face, and came out, and refrained himself, and said, Set on meat.
32 And they prepared for him by himself, and for them by themselves, and for the Egyptians, which did eat with him, by themselves, because the Egyptians might not eat bread with the Hebrews, for that was an abomination unto the Egyptians.
33 So they sat before him, the eldest according unto his age, and the youngest according unto his youth. And the men marveled among themselves.
111

34 And they took messes from before him, and sent to them, but Benjamin’s mess was five times so much as any of theirs. And they drank, and had of the best drink with him.
Genesis 44
15 Joseph accuseth his brother of theft. 33 Judah offereth himself to be servant for Benjamin.
1 Afterward he commanded his steward, saying, Fill the men’s sacks with food, as much as they can carry, and put every man’s money in his sack’s mouth.
2 And put my cup, I mean, the silver cup, in the sack’s mouth of the youngest, and his corn money. And he did according to the commandment that Joseph gave him.
3 And in the morning the men were sent away, they, and their asses.
4 And when they went out of the city not far off, Joseph said to his steward, Up, follow after the men, and when thou doest overtake them, say unto them, Wherefore have ye rewarded evil for good?
5 Is that not the cup, wherein my lord drinketh? And in the which he doeth divine and prophesy? Ye have done evil in so doing.
6 ¶And when he overtook them, he said these words unto them.
7 And they answered him, Wherefore saith my lord such words? God forbid that thy servants should do such a thing.
8 Behold, the money which we found in our sacks’ mouths, we brought again to thee out of the land of Canaan. How then should we steal out of thy lord’s house silver or gold?
9 With whomsoever of thy servants it be found, let him die, and we also will be my lord’s bondmen.
112

10 And he said, Now then let it be according unto your words; he with whom it is found, shall be my servant, and ye shall be blameless.
11 Then at once every man took down his sack to the ground, and everyone opened his sack.
12 And he searched, and began at the eldest, and left at the youngest. And the cup was found in Benjamin’s sack.
13 Then they rent their clothes, and laded every man his ass, and went again into the city.
14 ¶ So Judah and his brethren came to Joseph’s house (for he was yet there) and they fell before him on the ground.
15 Then Joseph said unto them, What act is this, which ye have done? Know ye not that such a man as I, can divine and prophesy?
16 Then said Judah, What shall we say unto my lord? What shall we speak? And how can we justify ourselves? God hath found out the wickedness of thy servants; behold, we are servants to my lord, both we, and he, with whom the cup is found.
17 But he answered, God forbid, that I should do so, but the man, with whom the cup is found, he shall be my servant, and go ye in peace unto your father.
18 ¶ Then Judah drew near unto him, and said, O my lord, let thy servant now speak a word in my lord’s ears, and let not thy wrath be kindled against thy servant; for thou art even as Pharaoh.
19 My lord asked his servants, saying, Have ye a father, or a brother?
20 And we answered my lord, We have a father that is old, and a young child, which he begat in his age. And his brother is dead, and he alone is left of his mother, and his father loveth him.
21 Now thou saidst unto thy servants, Bring him unto me, that I may set mine eyes upon him.
22 And we answered my lord, The child cannot depart from his father, for if he leave his father, his father would die.
113

23 Then saidst thou unto thy servants, Except your younger brother come down with you, look in my face no more.
24 So when we came unto thy servant our father, and shewed him what my lord had said,
25 And our father said unto us, Go again, buy us a little food,
26 Then we answered, We cannot go down. But if our youngest brother go with us, then will we go down; for we may not see the man’s face, except our youngest brother be with us.
27 Then thy servant my father said unto us, Ye know that my wife bare me two sons,
28 And the one went out from me, and I said, Of a surety he is torn in pieces, and I saw him not since.
29 Now ye take this also away from me, if death take him, then ye shall bring my gray head in sorrow to the grave.
30 Now therefore, when I come to thy servant my father, and the child be not with us (seeing that his life dependeth on the child’s life.)
31 Then when he shall see that the child is not come, he will die. So shall thy servants bring the gray head of thy servant our father with sorrow to the grave.
32 Doubtless thy servant became surety for the child to my father, and said, If I bring him not unto thee again, then I will bear the blame unto my father forever.
33 Now therefore, I pray thee, let me thy servant abide for the child, as a servant to my lord, and let the child go up with his brethren.
34 For how can I go up to my father, if the child be not with me, unless I would see the evil that shall come on my father?
114

Genesis 45
1 Joseph maketh himself known to his brethren. 8 He sheweth that all was done by God's providence. 18 Pharaoh commandeth him to send for his father. 24 Joseph exhorteth his brethren to concord. 27 Jacob rejoiceth.
1 Then Joseph could not refrain himself before all that stood by him, but he cried, Have forth every man from me. And there tarried not one with him, while Joseph uttered himself unto his brethren.
2 And he wept and cried, so that the Egyptians heard, the house of Pharaoh heard also.
3 Then Joseph said to his brethren, I am Joseph! Doeth my father yet live? But his brethren could not answer him, for they were astonished at his presence.
4 Again, Joseph said to his brethren, Come near, I pray you, to me. And they came near. And he said, I am Joseph your brother, whom ye sold into Egypt.
5 Now therefore be not sad, neither grieved with yourselves, that ye sold me hither; for God did send me before you for your preservation.
6 For now two years of famine have been through the land, and five years are behind, wherein neither shall be earing nor harvest.
7 Wherefore God sent me before you to preserve your posterity in this land, and to save you alive by a great deliverance.
8 Now then you sent not me hither, but God, who hath made me a father unto Pharaoh, and lord of all his house, and ruler throughout all the land of Egypt.
9 Haste you and go up to my father, and tell him, Thus saith thy son Joseph, God hath made me lord of all Egypt. Come down to me; tarry not.
10 And thou shalt dwell in the land of Goshen, and shalt be near me, thou and thy children, and thy children’s children, and thy sheep, and thy beasts, and all that thou hast.
11 Also I will nourish thee there (for yet remain five years of famine) lest thou perish through poverty, thou and thy household, and all that thou hast.
115

12 And behold, your eyes do see, and the eyes of my brother Benjamin, that my mouth speaketh to you.
13 Therefore tell my father of all my honor in Egypt, and of all that ye have seen; and make haste, and bring my father hither.
14 Then he fell on his brother Benjamin’s neck, and wept, and Benjamin wept on his neck.
15 Moreover, he kissed all his brethren, and wept upon them. And afterward his brethren talked with him.
16 ¶ And the tidings came unto Pharaoh’s house, so that they said, Joseph’s brethren are come, and it pleased Pharaoh well, and his servants.
17 Then Pharaoh said unto Joseph, Say to thy brethren, This do ye, lade your beasts and depart, go to the land of Canaan,
18 And take your father, and your households, and come to me, and I will give you the best of the land of Egypt, and ye shall eat of the fat of the land.
19 And I command thee, Thus do ye, take you chariots out of the land of Egypt for your children, and for your wives, and bring your father and come.
20 Also regard not your stuff, for the best of all the land of Egypt is yours.
21 And the children of Israel did so; and Joseph gave them chariots according to the commandment of Pharaoh, he gave them vitaille also for the journey.
22 He gave them all, none except, change of raiment, but unto Benjamin he gave three hundred pieces of silver, and five suits of raiment.
23 And unto his father likewise he sent ten he asses laden with the best things of Egypt, and ten she asses laden with wheat, and bread and meat for his father by the way.
24 So sent he his brethren away, and they departed, and he said unto them, Fall not out by the way.
25 ¶ Then they went up from Egypt, and came unto the land of Canaan unto Jacob their father,
116

26 And told him, saying, Joseph is yet alive, and he also is governor over all the land of Egypt. And Jacob’s heart failed, for he believed them not.
27 And they told him all the words of Joseph, which he had said unto them, but when he saw the chariots, which Joseph had sent to carry him, then the spirit of Jacob their father revived.
28 And Israel said, I have enough; Joseph my son is yet alive. I will go and see him before I die.
Genesis 46
2 God assureth Jacob of his journey into Egypt. 27 The number of his family when he went into Egypt. 29 Joseph meeteth his father. 34 He teacheth his brethren what to answer to Pharaoh.
1 Then Israel took his journey with all that he had, and came to Beer-sheba, and offered sacrifice unto the God of his father Isaac.
2 And God spake unto Israel in a vision by night, saying, Jacob, Jacob. Who answered, I am here.
3 Then he said, I am God, the God of thy father; fear not to go down into Egypt, for I will there make of thee a great nation.
4 I will go down with thee into Egypt, and I will also bring thee up again, and Joseph shall put his hand upon thine eyes.
5 Then Jacob rose up from Beer-sheba; and the sons of Israel carried Jacob their father, and their children, and their wives in the chariots, which Pharaoh had sent to carry him.
6 And they took their cattle and their goods, which they had gotten in the land of Canaan, and came into Egypt, both Jacob and all his seed with him,
7 His sons and his sons’ sons with him, his daughters and his sons’ daughters, and all his seed brought he with him into Egypt.
117

8 ¶ And these are the names of the children of Israel, which came into Egypt, even Jacob and his sons: Reuben, Jacob’s firstborn.
9 And the sons of Reuben: Hanoch, and Phallu, and Hezron, and Carmi.
10 ¶ And the sons of Simeon: Jemuel, and Jamin, and Ohad, and Jachin, and Zohar; and Shaul the son of a Canaanitish woman.
11 ¶ Also the sons of Levi: Gershon, Kohath, and Merari.
12 ¶ Also the sons of Judah: Er, and Onan, and Shelah, and Pharez, and Zerah; (but Er and Onan died in the land of Canaan.) And the sons of Pharez were Hezron and Hamul.
13 ¶ Also the sons of Issachar: Tola, and Phuvah, and Job, and Shimron.
14 ¶ Also the sons of Zebulun: Sered, and Elon, and Jahleel.
15 These be the sons of Leah, which she bare unto Jacob in Paddan-aram, with his daughter Dinah. All the souls of his sons and his daughters were thirty and three.
16 ¶ Also the sons of Gad: Ziphion, and Haggi, Shuni, and Ezbon, Eri, and Arodi, and Areli.
17 ¶ Also the sons of Asher: Jimnah, and Ishvah, and Isui, and Beriah, and Serah their sister. And the sons of Beriah: Heber, and Malchiel.
18 These are the children of Zilpah, whom Laban gave to Leah his daughter; and these she bare unto Jacob, even sixteen souls.
19 The sons of Rachel Jacob’s wife were Joseph and Benjamin.
20 ¶ And unto Joseph in the land of Egypt were born Manasseh, and Ephraim,
which Asenath the daughter of Poti-pherah prince of On bare unto him.
21 ¶ Also the sons of Benjamin: Belah, and Becher, and Ashbel, Gera, and Naaman, Ehi, and Rosh, Muppim, and Huppim, and Ard.
22 These are the sons of Rachel, which were born unto Jacob, fourteen souls in all.
23 ¶ Also the sons of Dan: Hushim.
118

24 ¶ Also the sons of Naphtali: Jahzeel, and Guni, and Jezer, and Shillem.
25 These are the sons of Bilhah, which Laban gave unto Rachel his daughter, and she bare these to Jacob, in all, seven souls.
26 All the souls, that came with Jacob into Egypt, which came out of his loins (beside Jacob’s sons’ wives) were in the whole, threescore and six souls.
27 Also the sons of Joseph, which were born him in Egypt, were two souls; so that all the souls of the house of Jacob, which came into Egypt, are seventy.
28 ¶ Then he sent Judah before him unto Joseph, to direct his way unto Goshen, and they came into the land of Goshen.
29 Then Joseph made ready his chariot, and went up to Goshen to meet Israel his father; and presented himself unto him, and fell on his neck, and wept upon his neck a good while.
30 And Israel said unto Joseph, Now let me die, since I have seen thy face, and that thou art yet alive.
31 Then Joseph said to his brethren, and to his father’s house, I will go up and shew Pharaoh, and tell him, My brethren and my father’s house, which were in the land of Canaan, are come unto me,
32 And the men are shepherds, and because they are shepherds, they have brought their sheep and their cattle, and all that they have.
33 And if Pharaoh call you, and ask you, What is your trade?
34 Then ye shall say, Thy servants are men occupied about cattle, from our childhood even unto this time, both we and our fathers, that ye may dwell in the land of Goshen; for every sheep keeper is an abomination unto the Egyptians.
119

Genesis 47
7 Jacob cometh before Pharaoh, and telleth him his age. 11 The land of Goshen is given him. 22 The idolatrous priests have living of the King. 28 Jacob's age when he dieth. 30 Joseph wearieth to bury him with his fathers.
1 Then came Joseph and told Pharaoh, and said, My father, and my brethren, and their sheep, and their cattle, and all that they have, are come out of the land of Canaan, and behold, they are in the land of Goshen.
2 And Joseph took part of his brethren, even five men, and presented them unto Pharaoh.
3 Then Pharaoh said unto his brethren, What is your trade? And they answered Pharaoh, Thy servants are shepherds, both we and our fathers.
4 They said moreover unto Pharaoh, For to sojourn in the land are we come, for thy servants have no pasture for their sheep, so sore is the famine in the land of Canaan. Now therefore, we pray thee, let thy servants dwell in the land of Goshen.
5 Then spake Pharaoh to Joseph, saying, Thy father and thy brethren are come unto thee.
6 The land of Egypt is before thee; in the best place of the land make thy father and thy brethren dwell, let them dwell in the land of Goshen; and if thou knowest that there be men of activity among them, make them rulers over my cattle.
7 Joseph also brought Jacob his father, and set him before Pharaoh. And Jacob saluted Pharaoh.
8 Then Pharaoh said unto Jacob, How old art thou?
9 And Jacob said unto Pharaoh, The whole time of my pilgrimage is a hundred and thirty years; few and evil have the days of my life been, and I have not attained unto the years of the life of my fathers, in the days of their pilgrimages.
10 And Jacob took leave of Pharaoh, and departed from the presence of Pharaoh.
120

11 ¶ And Joseph placed his father, and his brethren, and gave them possession in the land of Egypt, in the best of the land, even in the land of Rameses, as Pharaoh had commanded.
12 ¶ And Joseph nourished his father, and his brethren, and all his father’s household with bread, even to the young children.
13 ¶ Now there was no bread in all the land, for the famine was exceeding sore, so that the land of Egypt, and the land of Canaan were famished by reason of the famine.
14 And Joseph gathered all the money, that was found in the land of Egypt, and in the land of Canaan, for the corn which they bought, and Joseph laid up the money in Pharaoh’s house.
15 So when money failed in the land of Egypt, and in the land of Canaan, then all the Egyptians came unto Joseph, and said, Give us bread, for why should we die before thee? For our money is spent.
16 Then said Joseph, Bring your cattle, and I will give you for your cattle, if your money be spent.
17 So they brought their cattle unto Joseph, and Joseph gave them bread for the horses, and for the flocks of sheep, and for the herds of cattle, and for the asses; so he fed them with bread for all their cattle that year.
18 But when the year was ended, they came unto him the next year, and said unto him, We will not hide from my lord, that since our money is spent, and my lord hath the herds of the cattle; there is nothing left in the sight of my lord, but our bodies and our ground.
19 Why shall we perish in thy sight, both we, and our land? Buy us and our land for bread, and we and our land will be bond to Pharaoh; therefore give us seed, that we may live and not die, and that the land go not to waste.
20 So Joseph bought all the land of Egypt for Pharaoh, for the Egyptians sold every man his ground, because the famine was sore upon them. So the land became Pharaoh’s.
21 And he removed the people unto the cities, from one side of Egypt even to the other.
121

22 Only the land of the Priests bought he not, for the Priests had an ordinance of Pharaoh, and they did eat their ordinance, which Pharaoh gave them; wherefore they sold not their ground.
23 Then Joseph said unto the people, Behold, I have bought you this day, and your land for Pharaoh; lo, here is seed for you, sow therefore the ground.
24 And of the increase ye shall give the fifth part unto Pharaoh, and four parts shall be yours for the seed of the field, and for your meat, and for them of your households, and for your children to eat.
25 Then they answered, Thou hast saved our lives; let us find grace in the sight of my lord, and we will be Pharaoh’s servants.
26 Then Joseph made it a law over the land of Egypt unto this day, that Pharaoh should have the fifth part, except the land of the Priests only, which was not Pharaoh’s.
27 ¶ And Israel dwelt in the land of Egypt, in the country of Goshen. And they had their possessions therein, and grew and multiplied exceedingly.
28 Moreover, Jacob lived in the land of Egypt seventeen years, so that the whole age of Jacob was a hundred forty and seven years.
29 Now when the time drew near that Israel must die, he called his son Joseph, and said unto him, If I have now found grace in thy sight, put thy hand now under my thigh, and deal mercifully and truly with me. Bury me not, I pray thee, in Egypt.
30 But when I shall sleep with my fathers, thou shalt carry me out of Egypt, and bury me in their burial. And he answered, I will do as thou hast said.
31 Then he said, Swear unto me. And he sware unto him. And Israel worshipped towards the bed’s head.
122

Genesis 48
1 Joseph with his two sons visiteth his sick father. 3 Jacob rehearseth God's promise. 5 He receiveth Joseph's sons as his. 19 He preferreth the younger. 21 He prophesieth their return to Canaan.
1 Again after this, one said to Joseph, Lo, thy father is sick. Then he took with him his two sons, Manasseh and Ephraim.
2 Also one told Jacob, and said, Behold, thy son Joseph is come to thee, and Israel took his strength unto him and sat upon the bed.
3 Then Jacob said unto Joseph, God almighty appeared unto me at Luz in the land of Canaan, and blessed me.
4 And he said unto me, Behold, I will make thee fruitful, and will multiply thee, and will make a great number of people of thee, and will give this land unto thy seed after thee for an everlasting possession.
5 ¶ And now thy two sons, Manasseh and Ephraim, which are born unto thee in the land of Egypt, before I came to thee into Egypt, shall be mine; as Reuben and Simeon are mine.
6 But thy linage, which thou hast begotten after them, shall be thine; they shall be called after the names of their brethren in their inheritance.
7 Now when I came from Paddan, Rachel died upon my hand in the land of Canaan, by the way when there was but half a days journey of ground to come to Ephrath; and I buried her there in the way to Ephrath; the same is Bethlehem.
8 Then Israel beheld Joseph’s sons and said, Whose are these?
9 And Joseph said unto his father, They are my sons, which God hath given me here. Then he said, I pray thee, bring them to me, that I may bless them;
10 (For the eyes of Israel were dim for age, so that he could not see well.) Then he caused them to come to him, and he kissed them and embraced them.
11 And Israel said unto Joseph, I had not thought to have seen thy face; yet lo, God hath shewed me also thy seed.
123

12 And Joseph took them away from his knees, and did reverence down to the ground.
13 Then took Joseph them both, Ephraim in his right hand toward Israel’s left hand, and Manasseh in his left hand toward Israel’s right hand, so he brought them unto him.
14 But Israel stretched out his right hand, and laid it on Ephraim’s head, which was the younger, and his left hand upon Manasseh’s head (directing his hands of purpose) for Manasseh was the elder.
15 ¶ Also he blessed Joseph, and said, The God, before whom my fathers Abraham and Isaac did walk, the God, which hath fed me all my life long unto this day, bless thee.
16 The Angel, which hath delivered me from all evil, bless the children, and let my name be named upon them, and the name of my fathers Abraham and Isaac, that they may grow as fish into a multitude in the midst of the earth.
17 But when Joseph saw that his father laid his right hand upon the head of Ephraim, it displeased him; and he stayed his father’s hand to remove it from Ephraim’s head to Manasseh’s head.
18 And Joseph said unto his father, Not so, my father, for this is the eldest; put thy right hand upon his head.
19 But his father refused, and said, I know well, my son, I know well; he shall be also a people, and he shall be great likewise. But his younger brother shall be greater than he, and his seed shall be full of nations.
20 So he blessed them that day, and said, In thee Israel shall bless, and say, God make thee as Ephraim and as Manasseh. And he set Ephraim before Manasseh.
21 Then Israel said unto Joseph, Behold, I die, and God shall be with you, and bring you again unto the land of your fathers.
22 Moreover, I have given unto thee one portion above thy brethren, which I got out of the hand of the Amorite by my sword and by my bow.
124

Genesis 49
1 Jacob blesseth all his sons by name. 10 He telleth them that Christ shall come out of Judah. 29 He will be buried with his fathers. 33 He dieth.
1 Then Jacob called his sons, and said, Gather yourselves together, that I may tell you what shall come to you in the last days.
2 Gather yourselves together, and hear, ye sons of Jacob, and hearken unto Israel your father.
3 ¶ Reuben my eldest son, thou art my might, and the beginning of my strength, the excellency of dignity, and the excellency of power;
4 Thou wast light as water, thou shalt not be excellent, because thou wentest up to thy father’s bed; then didst thou defile my bed, thy dignity is gone.
5 ¶ Simeon and Levi, brethren in evil, the instruments of cruelty are in their habitations.
6 Into their secret let not my soul come; my glory, be not thou joined with their assembly; for in their wrath they slew a man, and in their self will they dug down a wall.
7 Cursed be their wrath, for it was fierce; and their rage, for it was cruel. I will divide them in Jacob, and scatter them in Israel.
8 ¶ Thou Judah, thy brethren shall praise thee; thy hand shall be in the neck of thine enemies; thy father’s sons shall bow down unto thee.
9 Judah as a Lion’s whelp shalt thou come up from the spoil, my son. He shall lie down and couch as a Lion, and as a Lioness; Who shall stir him up?
10 The Scepter shall not depart from Judah, nor a Lawgiver from between his feet, until Shiloh come, and the people shall be gathered unto him.
11 He shall bind his ass foal unto the vine, and his ass’s colt unto the best vine. He shall wash his garment in wine, and his cloak in the blood of grapes.
12 His eyes shall be red with wine, and his teeth white with milk.
125

13 ¶ Zebulun shall dwell by the seaside; and he shall be a haven for ships, and his border shall be unto Sidon.
14 ¶ Issachar shall be a strong ass, couching down between two burdens;
15 And he shall see that rest is good, and that the land is pleasant, and he shall
bow his shoulder to bear, and shall be subject unto tribute.
16 ¶ Dan shall judge his people as one of the tribes of Israel.
17 Dan shall be a serpent by the way, an adder by the path, biting the horse heels, so that his rider shall fall backward.
18 O LORD, I have waited for thy salvation.
19 ¶ Gad, a host of men shall overcome him, but he shall overcome at the last.
20 ¶ Concerning Asher, his bread shall be fat, and he shall give pleasures for a king.
21 ¶ Naphtali shall be a hind let go, giving goodly words.
22 ¶ Joseph shall be a fruitful bough, even a fruitful bough by the wellside; the
small boughs shall run upon the wall.
23 And the archers grieved him, and shot against him, and hated him.
24 But his bow abode strong, and the hands of his arms were strengthened, by the hands of the mighty God of Jacob, of whom was the feeder appointed, by the stone of Israel,
25 Even by the God of thy father, who shall help thee, and by the almighty, who shall bless thee with heavenly blessings from above, with blessings of the deep that lieth beneath, with blessings of the breasts, and of the womb.
26 The blessings of thy father shall be stronger than the blessings of my elders, unto the end of the hills of the world; they shall be on the head of Joseph, and on the top of the head of him that was separate from his brethren.
27 ¶ Benjamin shall ravin as a wolf; in the morning he shall devour the prey, and at night he shall divide the spoil.
126

28 ¶ All these are the twelve tribes of Israel, and thus their father spake unto them, and blessed them. Every one of them blessed he with a several blessing.
29 And he charged them and said unto them, I am ready to be gathered unto my people; bury me with my fathers in the cave, that is in the field of Ephron the Hittite,
30 In the cave that is in the field of Machpelah, besides Mamre in the land of Canaan, which cave Abraham bought with the field of Ephron the Hittite for a possession to bury in.
31 There they buried Abraham and Sarah his wife. There they buried Isaac and Rebekah his wife, and there I buried Leah.
32 The purchase of the field and the cave that is therein, was bought of the children of Heth.
33 Thus Jacob made an end of giving charge to his sons, and plucked up his feet into the bed, and gave up the ghost, and was gathered to his people.
Genesis 50
13 Jacob is buried. 19 Joseph forgiveth his brethren. 23 He seeth his children's children. 25 He dieth.
1 Then Joseph fell upon his father’s face and wept upon him, and kissed him.
2 And Joseph commanded his servants the physicians to embalm his father, and the physicians embalmed Israel.
3 So forty days were accomplished (for so long did the days of them that were embalmed last) and the Egyptians bewailed him seventy days.
4 And when the days of his mourning were past, Joseph spake to the house of Pharaoh, saying, If I have now found favor in your eyes, speak, I pray you, in the ears of Pharaoh, and say,
127

5 My father made me swear, saying, Lo, I die; bury me in my grave, which I have made me in the land of Canaan. Now therefore let me go, I pray thee, and bury my father; and I will come again.
6 Then Pharaoh said, Go up and bury thy father, as he made thee to swear.
7 ¶ So Joseph went up to bury his father, and with him went all the servants of
Pharaoh, both the elders of his house, and all the elders of the land of Egypt.
8 Likewise all the house of Joseph, and his brethren, and his father’s house; only
their children, and their sheep, and their cattle left they in the land of Goshen.
9 And there went up with him both chariots and horsemen; and they were an exceeding great company.
10 And they came to Goren Atad, which is beyond Jordan, and there they made a great and exceeding sore lamentation; and he mourned for his father seven days.
11 And when the Canaanites the inhabitants of the land saw the mourning in Goren Atad, they said, This is a great mourning unto the Egyptians. Wherefore the name thereof was called Abel Mizraim, which is beyond Jordan.
12 So his sons did unto him, according as he had commanded them;
13 For his sons carried him into the land of Canaan, and buried him in the cave of the field of Machpelah, which cave Abraham bought with the field, to be a place to bury in, of Ephron the Hittite besides Mamre.
14 ¶ Then Joseph returned into Egypt, he and his brethren, and all that went up with him to bury his father, after that he had buried his father.
15 And when Joseph’s brethren saw that their father was dead, they said, It may be that Joseph will hate us, and will pay us again all the evil which we did unto him.
16 Therefore they sent unto Joseph, saying, Thy father commanded before his death, saying,
17 Thus shall ye say unto Joseph, Forgive now, I pray thee, the trespass of thy brethren, and their sin, for they rewarded thee evil. And now, we pray thee, forgive the trespass of the servants of thy father’s God. And Joseph wept, when they spake unto him.
128

18 Also his brethren came unto him, and fell down before his face, and said, Behold, we be thy servants.
19 To whom Joseph said, Fear not, for am not I under God?
20 When ye thought evil against me, God disposed it to good, that he might bring to pass, as it is this day, and save much people alive.
21 Fear not now therefore, I will nourish you, and your children; and he comforted them, and spake kindly unto them.
22 ¶ So Joseph dwelt in Egypt, he, and his father’s house. And Joseph lived a hundred and ten years.
23 And Joseph saw Ephraim’s children, even unto the third generation; also the sons of Machir the son of Manasseh were brought upon Joseph’s knees.
24 And Joseph said unto his brethren, I am ready to die, and God will surely visit you, and bring you out of this land, unto the land which he sware unto Abraham, unto Isaac, and unto Jacob.
25 And Joseph took an oath of the children of Israel, saying, God will surely visit you, and ye shall carry my bones hence.
26 So Joseph died, when he was a hundred and ten years old; and they embalmed him, and put him in a chest in Egypt."""

layout = [[sg.Text("Type/Paste text below, with different entries separated by a newline")],
          [sg.Multiline(kanyeTweets, key='-TEXT-', size=(100, 20))],
          [sg.Button("Paste"), sg.Button("Clear"), sg.Button("Reload Kanye Tweets"), sg.Button("Load Book of Genesis")],
          [sg.Text("What order of markov model to use? (1 or 2 is a safe bet)")],
          [sg.Input(1, key='-N-')],
          [sg.Text("What seed to use? (type your favorite number :D)")],
          [sg.Input("3", key='-S-')],
          [sg.Button('Choose Random Seed')],
          [sg.Button('Ok'), sg.Button('Quit')]]

window = sg.Window('Markov Chainer', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    elif event == "Paste":
        window['-TEXT-'].update(clipboard.paste())
    elif event == "Clear":
        window['-TEXT-'].update("")
    elif event == "Choose Random Seed":
        window['-S-'].update(np.random.randint(5000))
    elif event == "Reload Kanye Tweets":
        window['-TEXT-'].update(kanyeTweets)
    elif event == "Load Book of Genesis":
        window['-TEXT-'].update(bookOfGenesis)
    else:
        # run through markov chain here
        text = values["-TEXT-"].split("\n")
        markov_model = generate_nth_order_markov_model(text, int(values["-N-"]))
        print(markov_model)
        string = traverse_nth_order_markov_model(markov_model, n=int(values["-N-"]), seed=int(values["-S-"]))
        print(string)
        sg.popup(string)

window.close()
