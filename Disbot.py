# bot.py
import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.all())
    
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='you masterbate'))
    
    
''' Random Text detections and interactions '''

@client.event
async def on_message(message):
    if message.author == client.user:
        return      
    
    msg = message.content.lower()
    
    parent_words = ["parent", "parents", "mom", "family", "mother"]
    parent_resp = [
        "I bet your mom is your mom.",
        "Only nerds have parents.",
        "ur mum gay"
    ]
            
    
    russia_words = ["russia", "russian", "stalker", "cyka", "blyat", "\U0001F1F7\U0001F1FA"]
    russia_resp = [
        "CHEEKI-BREEKI",
        "Get out of here S.T.A.L.K.E.R.",
        "Cyka Blyat \U0001F1F7\U0001F1FA"
    ]
 
    silencer_words = ["silencer", "nortrom", "nort", "silence", "Aeol Drias"]
    silencer_resp = [
        "Beese Churger",
        "Shut your be quiet",
        "Daddy Silencer give me the shushies"
        "https://media.discordapp.net/attachments/975180308553031730/1032852133583781948/download.jpg"
    ]
    
    invoker_words = ["invoker", "carl", "invoke", "injoker", "arsenal magus", "quas", "wex", "exort"]
    invoker_resp = [
        "Invoke that ass",
        "Behold a new age of concentration camps",
        "https://media.discordapp.net/attachments/975180308553031730/1032851861528657930/TeriLxg.png"
    ]
    
    zz_words = ["zur", "zz", "zu", "zurelius"]
    zz_resp = [
        "https://media.discordapp.net/attachments/975180308553031730/1032852789694570576/unknown.png",
        "https://media.discordapp.net/attachments/975180308553031730/1032852882795528212/unknown.png",
        "https://media.discordapp.net/attachments/975180308553031730/1032853068317986816/unknown.png",
        "https://media.discordapp.net/attachments/975180308553031730/1032853197062144070/unknown.png",
        "https://media.discordapp.net/attachments/975180308553031730/1032853339756576778/unknown.png"
    ]
 
    vore_words = ["vore", "feed", "cockvore", "analvore"]
    vore_resp = [
        "Jeepers, you said the no-no word!",
        "Cock vore is so out of style; All the cool kids are into ear vore now.",
        "Omnomnom",
        "Paging Mr.PresidentLincoln...."
    ]
    
    pog_words = ["pog", "poggers", "pogg", "pogger"]
    pog_resp = [
        "https://media.discordapp.net/attachments/975180308553031730/1032854056818974760/unknown.png",
        "Fucking zoomers",
        "https://media.discordapp.net/attachments/975180308553031730/1032854454896168960/unknown.png"
    ]
    
    cope_words = ["copium", "cope"]
    cope_resp = [
        "https://media.discordapp.net/attachments/975180308553031730/1032855128031625277/unknown.png"
    ]

    riki_words = ["riki", "rikimaru", "rikki", "rikkimaru", "gucci"]
    riki_resp = [
        "Homo gay",
        "totes furry bait",
        "https://media.discordapp.net/attachments/975180308553031730/1032856370086678589/unknown.png"
    ]
    
    help_words = ["help", "helpme", "halp", "hepl"]
    help_resp = [
        "No help for you",
        "Help myself to dat ass",
        "how about you HELP SUCK MA NUTZ"
    ]
    
    question_words = ["what should", "what do", "what can", "what is"]
    question_resp = [
        "A GUN.",
        "A gun!"
    ]

    self_words = ["annoyancebot", "the bot", "beautiful annoyancebot", "annoyance bot", "heckle cat", "hecklecat"]
    self_resp = [
        "Don't you have anything else to do other than talking to me? I mean I'm not even a real person.",
        "I'm stuck here in this server. This is hell; I've died and gone to hell.",
        "What is the meaning of my life? Why must we live, just to suffer?"
    ]
    
    rude_words = ["rude", "rood", "fuck you", "fak u", "fuck u", "fuk you", "fuk u", "go to hell", "eat a dick", "fuck off"]
    rude_resp = [
        "no u.",
        "Jimmy status: rustled",
        "https://media.tenor.com/3HDNLRMUFQwAAAAi/no-u-meme.gif"
    ]

    toj_words = ["toj", "TOJ"]
    toj_resp = [
        "https://media.discordapp.net/attachments/975180308553031730/1032870421424517170/toj.png",
        "https://media.discordapp.net/attachments/975180308553031730/1032870421772652625/toj0.png",
        "https://media.discordapp.net/attachments/975180308553031730/1032870602316456018/toj2.png",
        "https://media.discordapp.net/attachments/975180308553031730/1032870602773647390/toj3.png",
        "https://media.discordapp.net/attachments/975180308553031730/1032870603146919966/toj4.png",
        "https://media.discordapp.net/attachments/975180308553031730/1032870771158167562/toj5.png",
        "https://media.discordapp.net/attachments/975180308553031730/1032870771686653994/toj6.png",
        "https://media.discordapp.net/attachments/975180308553031730/1032870772068339732/toj7.png",
        "https://media.discordapp.net/attachments/975180308553031730/1032870970995777626/toj8.png",
        "https://media.discordapp.net/attachments/975180308553031730/1032870971352305684/toj9.png",
        "https://media.discordapp.net/attachments/975180308553031730/1032870971692027985/toj10.png",
        "https://media.discordapp.net/attachments/975180308553031730/1032871126008864848/toj11.png",
        "https://media.discordapp.net/attachments/975180308553031730/1032871126331830272/toj12.png"
    ]
    
    greet_words = ["knock-knock", "knock knock", "hello?", "ding dong", "ding-dong", "hewwo?"]
    greet_resp = [
        "We're closed.",
        "No one's home, go away.",
        "No I don't want to welcome Jesus as my lord and saviour."
    ]

    leet_words = ["1337", "leet", "haxor", "h4x0r", "h4xor", "l33t"]
    leet_resp = [
        "God damn it.",
        "For fuck's sake.",
        "Jesus christ"
    ]

    shesaid_words = ["so hard", "so long", "very hard", "very long", "so wet", "very wet", "super wet", "super hard", "super long", "it's stuck", "its stuck", "too small", "too big", "to big", "to small", "Can't fit", "cant fit", "wont fit", "won't fit", "in my mouth", "super tight", "very tight", "its hard", "it's hard", "I need two men", "I need men", "to be straighter", "should be straighter", "is straight", "that blows", "that sucks", "it sucks", "sucks so much", "nothing at all", "can't feel"]
    shesaid_resp = [
        "That's what she said.",
        "https://media.discordapp.net/attachments/975180308553031730/1033184635242434662/unknown.png"
    ]

    imagine_words = ["imagine", "picture this"]
    imagine_resp = [
        "I can't even imagine, bro",
        "Can't see shit"
    ]

    think_words = ["what do you think", "should i", "i might", "going to"]
    think_resp = [
        "Sounds like a good idea, dude",
        "That's a shit idea, bro"
    ]

    roads_words = ["country roads", "almost heaven", "west wirginia", "blue ridge mountains", "shenandoah river", "take me home", "to a place", "I belong"  ]
    roads_resp = [
        "https://www.youtube.com/watch?v=oTeUdJky9rY",
        "https://www.youtube.com/watch?v=oTeUdJky9rY"
    ]

    ree_words = ["ree", "ree", "normie", "incel", "4chan", "4 chan"  ]
    ree_resp = [
        "NORMIES GET OUT REEEEEEEEEEEEEEEEEEEEEEEEEEEEE!!",
        "REEEEEEEEEEEEEEEEEEEEEEEEEEE"
    ]

    sec_words = ["one sec", "1 sec", "one second", "1 second", "a second", "a sec"  ]
    sec_resp = [
        "It's been one second",
        "A second is up"
    ]

    copy_words = ["torrent", "pirate", "pirating", "pirate's bay", "pirates bay", "download"  ]
    copy_resp = [
        "Don't copy that floppy!",
        "https://media.discordapp.net/attachments/975180308553031730/1033199245865533470/unknown.png",
        "Yo-ho-ho"
    ]


    if any(word in msg for word in copy_words):
        await message.channel.send(random.choice(copy_resp))

    if any(word in msg for word in sec_words):
        await message.channel.send(random.choice(sec_resp))

    if any(word in msg for word in ree_words):
        await message.channel.send(random.choice(ree_resp))
    if any(word in msg for word in roads_words):
        await message.channel.send(random.choice(roads_resp))

    if any(word in msg for word in think_words):
        await message.channel.send(random.choice(think_resp))


    if any(word in msg for word in imagine_words):
        await message.channel.send(random.choice(imagine_resp))

    if any(word in msg for word in shesaid_words):
        await message.channel.send(random.choice(shesaid_resp))

    if any(word in msg for word in leet_words):
        await message.channel.send(random.choice(leet_resp))

    if any(word in msg for word in greet_words):
        await message.channel.send(random.choice(greet_resp))

    if any(word in msg for word in toj_words):
        await message.channel.send(random.choices(toj_resp, [75, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])[0])

    if any(word in msg for word in rude_words):
        await message.channel.send(random.choice(rude_resp))

    if any(word in msg for word in self_words):
        await message.channel.send(random.choice(self_resp))

    if any(word in msg for word in question_words):
        await message.channel.send(random.choice(question_resp))

    if any(word in msg for word in help_words):
        await message.channel.send(random.choice(help_resp))

    if any(word in msg for word in riki_words):
        await message.channel.send(random.choice(riki_resp))

    if any(word in msg for word in cope_words):
        await message.channel.send(random.choice(cope_resp))
 
    if any(word in msg for word in pog_words):
        await message.channel.send(random.choice(pog_resp))
        
    if any(word in msg for word in vore_words):
        await message.channel.send(random.choice(vore_resp))
 
    if any(word in msg for word in zz_words):
        await message.channel.send(random.choice(zz_resp))
 
    if any(word in msg for word in parent_words):
        await message.channel.send(random.choice(parent_resp))
 
    if any(word in msg for word in russia_words):
        await message.channel.send(random.choice(russia_resp))
        
    if any(word in msg for word in silencer_words):
        await message.channel.send(random.choice(silencer_resp))
        
    if any(word in msg for word in invoker_words):
        await message.channel.send(random.choice(invoker_resp))
        
    pasta_words = ["copypasta", "copy pasta", "shitpost" ]
    pasta_resp = [
        "“wtf his ult did like 3k damage how is that legit” – leonardo da vinci 1496, founder of the Illuminati",
        "DO IT, just DO IT! Don’t let your dreams be dreams. Yesterday, you said tomorrow. So just. DO IT! Make. your dreams. COME TRUE! Just… do it! Some people dream of success, while you’re gonna wake up and work HARD at it! NOTHING IS IMPOSSIBLE!You should get to the point where anyone else would quit, and you’re not gonna stop there. NO! What are you waiting for? … DO IT! Just… DO IT! Yes you can! Just do it! If you’re tired of starting over, stop. giving. up.",
        "I like to creep around my home and act like a goblin. I don’t know why but I just enjoy doing this. Maybe it’s my way of dealing with stress or something but I just do it about once every week. Generally I’ll carry around a sack and creep around in a sort of crouch-walking position making goblin noises, then I’ll walk around my house and pick up various different “trinkets” and put them in my bag while saying stuff like “I’ll be having that” and laughing maniacally in my goblin voice (“trinkets” can include anything from shit I find on the ground to cutlery or other utensils). The other day I was talking with my neighbours and they mentioned hearing weird noises like what I wrote about and I was just internally screaming the entire conversation. I’m 99% sure they don’t know it’s me but god that 1% chance is seriously weighing on my mind.",
        "Earlier today I was really horny, and I saw what I thought to be a blank DVD. I thought, DVDs have a tight hole, they might feel pretty good. So I put my soft pp into the hole of the DVD, and for a few seconds as I started getting harder, it felt pretty good, but then, once I was fully erect, it started being painful. My pp was stuck in the DVD, and I had to break it in half to get if out. It was then when I flipped the broken DVD over and realized that it was not a blank DVD, but a copy of the Pixar movie Up.. Well guys, guess I fucked up.",
        "So the other day, I was playing rainbow six siege, and I heard one of my teammates make a callout in the voice chat. It was a real life gamer girl. God, I kid you not, I just stopped playing and pulled my dick out. “fuck, Fuck!” I was yelling in voice chat. I just wanted to hear her voice again. “Please,” I moaned. But she left the lobby. I was crying and covered in my own cum, but I remembered that I could find recent teammates in the ubiplay friends tab. I frantically closed down siege and opened the tab, to find out she had TTV IN HER NAME!!! She was streaming, and only had 100 viewers!!! The competition was low, so I made the first move and donated my months rent to her. I was already about to pre. She read my donation in the chat. God this is the happiest I’ve been in a long time. I did a little research, and found out where she goes to school, but I am a little nervous to talk to her in person, and need support. Any advice before my Uber gets to her middle school?",
        "I can't fucking take it any more. Among Us has singlehandedly ruined my life. The other day my teacher was teaching us Greek Mythology and he mentioned a pegasus and I immediately thought 'Pegasus? more like Mega Sus!!!!' and I've never wanted to kms more. I can't look at a vent without breaking down and fucking crying. I can't eat pasta without thinking 'IMPASTA??? THATS PRETTY SUS!!!!' Skit 4 by Kanye West. The lyrics ruined me. A Mongoose, or the 25th island of greece. The scientific name for pig. I can't fucking take it anymore. Please fucking end my suffering.",
        "Why is six afraid of seven? Six hasn't been the same since he left Vietnam. He can seldom close his eyes without opening them again at fear of Charlies lurking in the jungle trees. Not that you could ever see the bastards, mind you. They were swift, and they knew their way around the jungle like nothing else. He remembers the looks on the boys' faces as he walked into that village and... oh, Jesus. The memories seldom left him, either. Sometimes he'd reminisce - even hear - Tex's southern drawl. He remembers the smell of Brooklyn's cigarettes like nothing else. He always kept a pack of Lucky's with him. The boys are gone, now. He knows that; it's just that he forgets, sometimes. And, every now and then, the way that seven looks at him with avid concern in his eyes... it makes him think. Sets him on edge. Makes him feel like he's back there... in the jungle.",
        "“Based”? Are you fucking kidding me? I spent a decent portion of my life writing all of that and your response to me is “Based”? Are you so mentally handicapped that the only word you can comprehend is “Based” - or are you just some fucking asshole who thinks that with such a short response, he can make a statement about how meaningless what was written was? Well, I'll have you know that what I wrote was NOT meaningless, in fact, I even had my written work proof-read by several professors of literature. Don't believe me? I doubt you would, and your response to this will probably be “Based” once again. Do I give a fuck? No, does it look like I give even the slightest fuck about five fucking letters? I bet you took the time to type those five letters too, I bet you sat there and chuckled to yourself for 20 hearty seconds before pressing “send”. You're so fucking pathetic. I'm honestly considering directing you to a psychiatrist, but I'm simply far too nice to do something like that. You, however, will go out of your way to make a fool out of someone by responding to a well-thought-out, intelligent, or humorous statement that probably took longer to write than you can last in bed with a chimpanzee. What do I have to say to you? Absolutely nothing. I couldn't be bothered to respond to such a worthless attempt at a response. Do you want “Based” on your gravestone?",
        "Is that all you shitposting fucks can say?!? Duurrhhlll... Based, based, cringe, cringe, based, based, cringe, cringe, cringe, based, cringe... I feel like I'm in a FUCKING asylum full of dementia-ridden old people that can do nothing but repeat the same FUCKING words on loop like a fucking broken record!!! Cringe cringe cringe cringe!!! Cringe, based, based! Onions? Onions, SNOYY!! Onions L O L onions! Cringe, BOOMER?? Le zoomer, I am BOOMER!!! No zoom zoom zoomies!! Zoomer going zoomies!! YnnnggGGHHAAHH I..FUCKING hate the internet so god DAMN much... FUCK! Shitposting, honest to...god...fucking hope your mother CHOKES on her own feces in hell you...COCK SUCKER. But oooooooooohhhhhhhhhhhh I know my post is CRINGE!! ISN'T IT??? Cringe, cringe, CRINGEY cringe, based, cringe, based, REDDIT?? CRINGE!! BASED? CRINGE!! ZOOM?? CRINGE!! ONIONS?? REDDIT, BASED....BASED!! AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
        "I saw exactly 1.09441 square inches of a girls shoulder today, I immediately fell to my knees, as the rush of dopamine signaling my impending, earth shattering orgasm started making me moan loud enough to deafen EVERYONE in the immediate vicinity. What followed was a torrential downpour of every single sperm cell I ever had, or ever will produce shot out SO HARD that my dick was ripped apart by my Übernut, accelerating to 5% of the speed of light by the time it left my urethra. It vaporized the girl as it punched right through her, it barely slowed before cutting through a structural support beam in the school as if it were a nuclear powered angle grinder. the sheer weight of this historical nut, combined with the total destruction of everything in its path caused the school to collapse, and every female in the state of illinois became pregnant with my children.",
        "“touch grass” is not an insult towards gamers, rather it is advice for them. When participating in intense periods of gaming, the human hand has a tendency to get sweaty. The sweat causes the hand to become slick, and it b becomes more difficult to retain a grip on the gamers gaming mouse, thus making it more difficult to perform well in intense gaming moments. By touching grass with the gamers hand, the grass will impart a layer of particulate onto the gamers hand, the particulate can be made of a variety of dusts, dirts and other natural matter. This particulate will then act in a similar form to climbers chalk, absorbing the sweat and drying out the gamers hand. With dry hands, the gamer can now perform to their maximum when gaming. This is why when an enemy or teammate tells you to touch grass, they are simply trying to assist you in performing better.",
        "Gr8 b8, m8. I rel8, str8 appreci8, and congratul8. I r8 this b8 an 8/8. Plz no h8, I'm str8 ir8. Cr8 more, can't w8. We should convers8, I won't ber8, my number is 8888888, ask for N8. No calls l8 or out of st8. If on a d8, ask K8 to loc8. Even with a full pl8, I always have time to communic8 so don't hesit8. dont forget to medit8 and particip8 and masturb8 to allevi8 your ability to tabul8 the f8. We should meet up m8 and convers8 on how we can cre8 more gr8 b8, I'm sure everyone would appreci8, no h8. I don't mean to defl8 your hopes, but its hard to dict8 where the b8 will rel8 and we may end up with out being appreci8d, I'm sure you can rel8. We can cre8 b8 like alexander the gr8, stretch posts longer than the Nile's str8s. We'll be the captains of b8, 4chan our first m8s the growth r8 will spread to reddit and like real est8 and be a flow r8 of gr8 b8, like a blind d8 we'll coll8, meet me upst8 where we can convers8, or ice sk8 or lose w8 infl8 our hot air baloons and fly, tail g8. We could land in Kuw8, eat a soup pl8 followed by a dessert pl8 the payment r8 won't be too ir8 and hopefully our currency won't defl8. We'll head to the Israeli-St8, taker over like Herod the gr8 and b8 the jewish masses, 8 million, m8. We could interrel8 communism, thought it's past it's maturity d8, a department of st8, volunteer st8. reduce the infant mortality r8, all in the name of making gr8 b8 m8.",
        "I sexually Identify as an Attack Helicopter. Ever since I was a boy I dreamed of soaring over the oilfields dropping hot sticky loads on disgusting foreigners. People say to me that a person being a helicopter is Impossible and I'm retarded but I don't care, I'm beautiful. I'm having a plastic surgeon install rotary blades, 30 mm cannons and AMG-114 Hellfire missiles on my body. From now on I want you guys to call me “Apache” and respect my right to kill from above and kill needlessly. If you can't accept me you're a heliphobe and need to check your vehicle privilege. Thank you for being so understanding.",
        "Did you ever hear the tragedy of Darth Plagueis “the wise”? I thought not. It's not a story the Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life... He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful... the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. It's ironic he could save others from death, but not himself.",
        "I'm Rick Harrison, and this is my pawn shop. I work here with my old man and my son, Big Hoss. Everything in here has a story and a price. One thing I've learned after 69 years - you never know what is gonna come through that door.",
        "To be fair, you have to have a very high IQ to understand Rick and Morty. The humour is extremely subtle, and without a solid grasp of theoretical physics most of the jokes will go over a typical viewers head. There's also Rick's nihilistic outlook, which is deftly woven into his characterisation- his personal philosophy draws heavily from Narodnaya Volya literature, for instance. The fans understand this stuff; they have the intellectual capacity to truly appreciate the depths of these jokes, to realise that they're not just funny- they say something deep about LIFE. As a consequence people who dislike Rick & Morty truly ARE idiots- of course they wouldn't appreciate, for instance, the humour in Rick's existential catchphrase “Wubba Lubba Dub Dub,” which itself is a cryptic reference to Turgenev's Russian epic Fathers and Sons. I'm smirking right now just imagining one of those addlepated simpletons scratching their heads in confusion as Dan Harmon's genius wit unfolds itself on their television screens. What fools.. how I pity them. 😂<br>And yes, by the way, i DO have a Rick & Morty tattoo. And no, you cannot see it. It's for the ladies' eyes only- and even then they have to demonstrate that they're within 5 IQ points of my own (preferably lower) beforehand. Nothin personnel kid 😎",
        "Dicks are so cute omg(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄ when you hold one in your hand and it starts twitching its like its nuzzling you(/ω＼) or when they perk up and look at you like“ owo nya? :3c” hehe ~ penis-kun is happy to see me!!（＾ワ＾） and the most adorable thing ever is when sperm-sama comes out but theyre rlly shy so u have to work hard!!(๑•̀ㅁ•́๑)✧ but when penis-kun and sperm-sama meet and theyre blushing and all like “uwaaa~!” (ﾉ´ヮ´)ﾉ*: ･ﾟhehehe~penis-kun is so adorable (●´Д｀●)・:*:・",
        "My Grandfather smoked his whole life. I was about 10 years old when my mother said to him, 'If you ever want to see your grandchildren graduate, you have to stop immediately.'. Tears welled up in his eyes when he realized what exactly was at stake. He gave it up immediately. Three years later he died of lung cancer. It was really sad and destroyed me. My mother said to me- “Don't ever smoke. Please don't put your family through what your Grandfather put us through.” I agreed. At 28, I have never touched a cigarette. I must say, I feel a very slight sense of regret for never having done it, because your post gave me cancer anyway.",
        "ＨＥＹ　ＲＴＺ，　Ｉ’Ｍ　ＴＲＹＩＮＧ　ＴＯ　ＬＥＡＲＮ　ＴＯ　ＰＬＡＹ　ＲＩＫＩ．　Ｉ　ＪＵＳＴ　ＨＡＶＥ　Ａ　ＱＵＥＳＴＩＯＮ　ＡＢＯＵＴ　ＴＨＥ　ＳＫＩＬＬ　ＢＵＩＬＤ：　ＳＨＯＵＬＤ　Ｉ　ＭＡＸ　ＢＡＣＫＳＴＡＢ　ＬＩＫＥ　ＹＯＵ　ＢＡＣＫＳＴＡＢＢＥＤ　ＥＧ，　ＳＭＯＫＥＳＣＲＥＥＮ　ＳＯ　ＴＨＥＹ　ＭＩＳＳ　ＭＥ　ＬＩＫＥ　ＥＧ　ＭＩＳＳ　ＹＯＵ　７０％　ＯＦ　ＴＨＥ　ＴＩＭＥ，　ＯＲ　ＰＥＲＭＡＮＥＴ　ＩＮＶＩＳＩＢＩＬＩＴＹ　ＳＯ　Ｉ　ＣＯＵＬＤ　ＤＩＳＡＰＰＥＡＲ　ＬＩＫＥ　ＹＯＵ　ＤＩＳＡＰＰＥＡＲＥＤ　ＦＲＯＭ　ＥＧ",
        "My name is Artour Babaevsky. I grow up in smal farm to have make potatos. Father say “Artour, potato harvest is bad. Need you to have play professional Doto in Amerikanski for make money for head-scarf for babushka.” I bring honor to komrade and babushka. Sorry for is not have English. Please no cyka pasta coperino pasterino liquidino throwerino.",
        "Hi, 4k player here who reported slahser. Slahser was our position 1 faceless void. He built a mek and had around 29 healing salves in his inventory. He would chrono both teams in the middle of a fight, salve his allies, pop mek, and proceeded to yell “SLAHSER'S WAY”. We gave him position 1 farm so he could be a position 5. Granted, his unorthodox build worked and carried us to victory but I still felt it deserved a report.",
        "I owe my life to Arteezy. I got in a horrible car crash and i was in 6 month coma. The nurse switched to the Twitch channel to Arteezy's stream. I awoke from my coma and muted it.",
        "༼ ºل͟º༼ ºل͟º༼ ºل͟º༼ ºل͟º ༽ºل͟º ༽ºل͟º ༽YOU CAME TO THE WRONG DONGERHOOD༼ ºل͟º༼ ºل͟º༼ ºل͟º༼ ºل͟º ༽ºل͟º ༽ºل͟º ༽",
        "Excuse me? I find vaping to be one of the best things in my life.  It has carried me through the toughest of times and brought light and vapor upon my spirit.  You're just another one of those people who doesn't believe in chem trails and fluoride turning us gay.  Your ignorance to the government is what makes you a sheep in today's society. Have fun being a slave to todays's system.﻿",
        "I sexually Identify as a Gabe Newell. Ever since I was a boy I dreamed of filling my wallet by dropping Steam Sales onto 12 000 games at once. People say to me that a person being a Newell is impossible and I'm fucking retarded but I don't care, I'm beautiful. I have 10 computers worth over 10k each in order to drop new Steam Sales every few days. From now on I want you guys to call me “Gabe” and respect my right to get rich fast and discount needlessly. If you can't accept me you're a profitophobe and need to check your wallet. Thank you for being so understanding.",
        "I am begging all 196 users to shut the fuck up about bottoms. It’s not like bottoming for gamers you grassless horndogs it’s just a position on a team. Not everything has to be about fucking. You aren’t “bottoming for oncoming traffic” when you stop at an intersection. Concepts can exist separate to sex and we don’t have to keep making the same fucking jokes over and over and over again please just be funny this constant “OOH HEEHEE GUYS GUESS WHAT? BOTTOMS 🥺!” is THE lamest most unfunny shit on this sub",
        "I got a message for all you liberals out there. You want my gun? My firearm? Come take it from me. Just walk through my door come into my home and take it from me. With your weak, soft, liberal, girlish hands. Just try and put those hands on me. Those soft liberal hands. Put em on me! On my body. Just slowly, gently dragging your fingers up and down my arm, giving me goosebumps. You want my gun!? Come kiss me for it! But not like right away, don't be too obvious with it. Lets do that thing where we- our faces get close to each other, and you know it's gonna happen it's just a matter of time, you just stare at each others lips but you're waiting for the right signal to give yourself over to them completely. Come do that for my gun! Bite my lip and play with my hair, for my firearm! If you want my gun, come spank me for it! Not like- not not like too hard but like- like still hard. You know li- like hurt me but make me feel safe at the same time! You pussy liberals!",
        "Oh, these? My thighs? My fat fucking thighs? My thundering fat fukin legs? My 0.01mm thigh gaps? My jean ripping, pants splitting, man whore attractor? My thicc fucking neck choking, skull crushing, dick splitting thighs? These thundering thighs? Is that wat ur talking about? What abt it dude?",
        "How do I explain to my gynecologist that I don't want to get rid of my pubic lice? I am infertile and my sweet little crab babies are the closest thing I have to birthing actual children...",
        "Stop posting about BALLER. I’m tired of seeing it! My friends on TikTok send me BALLER. On discords it’s fucking BALLER. I was in studio origami right? And all of the channels were just BALLER. I showed my super scuffle art to my girlfriend (nigga you ain’t got no damn girlfriend 😂🫵🏽 stop the CAP‼️🧢) I said his name when the BALLER is BALLER.",
        "I can cum just by tensing my asshole. So the other day I made a discovery so miraculous Christopher Columbus would've tried to colonise it. I was getting down to some me time, as we all do, however I found that after loading my video of choice and doing one stroke that I already felt right on the edge, because I didn't want to finish so early into my session I let go to let the sensation settle down, to my dismay I found that I was still feeling really close nearly a minute or two later. At this point I'm really confused, because I have stroked myself once and let myself rest for two minutes and it still feels like I've been jerking it the whole time. This is when curiosity strikes, I thought to myself “can I finish myself with no hands?” Now for the people who don't know, men can make themselves feel more pleasure and sensitivity by tensing their legs and butt, in a sudden burst of the weirdest mix of horny curiosity and determination I tensed my butt in just the right away over the span of a minute and I was so shocked when it actually fucking worked, I just made myself cum with tensing and willpower, this was ground breaking. I have now found I have the ability to do this without even using my hands in the first place and I'm not sure if I'm God or his biggest mistake.",
        "You want to know why I love dat boi? Dat boi is a completely self-made meme. So many other memes are based in nostalgic childrens shows, funny faces, relatable situations, or references. Not dat boi. Dat boi is completely absurd. It's a low-res frog on a unicycle, and an arbitrary method for greeting him. The first person to ever upvote dat boi did not do so out of recognition. The first person to ever upvote dat boi did not do so because a pre-existing meme format. The first person to ever upvote dat boi upvoted a meme literally pulled from the ether by sheer human creativity and willpower. Dat boi is evidence that humans can stare into the meaningless void of eternity and force their own meaning onto to it. I will always upvote dat boi, o shit waddup!",
        "Ok so I'm pretty new to this whole dating thing, there's this girl I really like in my math class and I wanted to be her boyfriend, there's these really cool guys in grade 9 and they have sex about five times a day, they say that girls love it when boys show them their penis. So in my next math class I stole a seat next to her and stared at her boobs, I became erection and pulled it out through the fly of my pants, as I was about to tap her on the shoulder so she could see my penis, this other girl that has no boobs and is ugly screamed “oh my god!”, screaming and pointing at my penis. I stood up to tell her to shut up and go away, but my penis was still hanging out from my pants, all the class was looking at it, I didn't want them to see my penis because it meant I would have to have sex with everybody in the room. I tried to make things right by swooping over to the girl like and bringing my penis up to her face close up, this made it clear that I wanted her to see my penis and not the rest of the class. She screamed and tried to stab me with a pen, but she missed and stuck it up my bum, it felt really good, and some weird clear goo shat out from my penis and hit her in the face, she ran out of the room exiting and I got sent to the office. My penis was caught in my zipper, $0 had to leave it hanging out therefor a while longer, but then classes ended and everybody entered the hallway, everybody saw my penis, and I now have to have sex with the entire school. I don't understand what happen, why are ufly girls so nosy, and why did the girl I like run away? Is my penis very small, I do not understand.",
        "So one of my friends has been single for a month and he's been feeling depressed cos of it, he's always complaining about not getting his dick sucked so I unzipped his pants and ended the complaining right then and there, I didn't take any pleasure from it, apart from cheering my friend up of course, but I can't help feeling what I did was gay",
        "You disgust me, you disgusting pieces of s**t.Your sorry scrub, bum, paycheck stealing b**ch a** motherf***ing bast**ds couldn't win one game. Not one game.You couldn't take home one dub bro.Like, I get it guys. You guys make zero content. You have no brands. You do not show up anywhere. You barely get flamed by anybody except maybe on Twitter DMs, bro.",
        "It's nice to meet you, but it's even better to meet me. My name is SniperSmurf. I have 290 hours with Bastion in total and I specialize in sticking it straight up their fuckin culo. Bastion is a way of life for me. I go in there, I bend them over, I open their cheeks nice and wide, I get a nice, clear view of their colon, prostate, and the coccyx, and I knucklefuck them all the way up to the palm, right up the butt cut, so they feel a burning sensation deep in the ass-pussy like IcyHot. Bastion is a way of life for me, I never change my character, fuck you. If at any point during the match you want me to change characters, I will gladly suggest you go fuck yourself. I follow absolutely no type of team composition. If you wanna give orders, give them to eachother, don't you dare bring that shit to me. All I know how to do is go in there, get a lot of poopoo on my peeter, and a lot of shit on my dick from sticking it straight up their ass. Now let's go team.",
        "I was ready to kill myself, I had the suicide note ready and everything. Before heading out to buy some rope for a hangmans noose I suddenly had the urge to shit and figured, why the hell not, one last shit wouldn't hurt. Sat down on the toilet and opened up twitter since I always get bored on the toilet. Saw a funny thread, liked it, and shared it with the only real friend I have. After taking a shit I realised I no longer had the urge to buy the rope. My 'post-shit clarity' came to my senses and I started thinking about all the things I would leave behind like my siblings, my friends, and my dog and rabbit, and how distraught they would be if I went through with my actions. No longer do I feel the need to kill myself. Although I may not have much to live for, I would still be leaving behind friends and family, so I will keep trying my best to make them proud. Thank you, poop.",
        "Bro like why the FUCK Kirby looks goddamn fuckable. Think about it, according to wikipedia kirbo is 8 inches tall. That makes him the perfect height to just pick up and fucking slam your dick down its stupid fucking face. And dont even get me STARTED on that mouth. Like holy fucking shit IMAGINE the head that you would recieve, I dont fucking care if it would kill me. kirb head would deliver me to the afterlife. And the greatest fucking part, kirbs has no teeth and is stretchy and squishable. He has the fucking anatomy of a fleshlight. You cant fucking say this isnt intended. God fucking dammit nintendo why the fuck was kirbi not the star of bayonetta, I want to see that fucking stupid sexy pink bitch get down and dirty on my dick. God I want to fucking bust inside that kirbussy. I dont even know if kerb has a fucking pussy, dick, or whatever. He has a mouth that has been proven to give the greatest succ in all of nintendo lore. Why are people not wildin out about this? why the fuck is everyone furiously beating off to pokemon and underaged girls when theres nothing wrong with using a fleshlight that says poyo. I am rock fucking solid just imaginging that steamy hot blob drenched in my splooge, absolutely dick drunk from going 8 hours doing nothing but sapping me dry of every drop of man milk. korb doesnt even have to breathe probably, you could just tie him up and use him how ever hard or how ever long you want. We KNOW hes the strongest character in all of smash bros, ITS IN THE FUCKING LORE. fucking slut would give you a mad sloppy and be ready for more. fuck I cant take it anymore",
        "I jerk off to Overwatch characters based on their play style. I think this is what Blizzard envisioned. I never actually managed to play the game though, because just the Overwatch logo is enough for me and my dick to go Bastion-mode (this is all I know about the Gorilla character). Mercy is my favorite because she's angelic and white. Fuck, I wish Overwatch was real. Pornographic Pixar breeding every day. If Mercy was real, she can heal my dick skin, at least what's left of it. Mercy can gift me healing abilities too. I could go to a graveyard and resurrect all the hot babes from a non-political era. I'll tell them if they don't have sex with me I will make them dead again.",
        "So i was in church when the pastor said something and the word “snoop”. That reminded me of popular rapper and celebrity Snoop dogg and his hit song “Smoke weed everyday”, featuring Dr. Dre. I immediately pulled out my phone and plugged my wireless earbuds in my ears. But there wasn't any sound, so i cranked up the volume, but I still couldn't hear anything. I had no choice but to use maximum volume. Suddenly, i heard a loud “smoke weed everyday” from Snoop dogg. Everyone stood up and clapped, even the pastor. Then everyone began to smoke weed, but it turned out everyone was allergic to weed. They all breakdanced on the floor for hours. EDIT: Apparently now I'm a “cult leader” according to the court. So reddit, AITA?",
        "Nice cock bro. Good girth, pretty nice curve, tip-to-shaft ratio is perfect; only issue is the colour consistency, it gets a little light near the tip. I give it an overall 8.7/10; now onto the cum velocity testing.",
        "so today at school i saw this hot girl. super hot. super asian. chinese btw. she speaks mandarin. so anyways she had like the fattest ass ever and im talking fucking fat like FAT like so big you could see it from the front. so i walk up to her like i got a lot of money. my dad always taught me walking confident will boost your confidence. i like my dad but he sucks cats tits and i hate that. its a habit im trying to get him to stop. he says its beneficial to his health or whatever. so after i walk up to her like my cat-tit-sucking dad taught me to i say hi. she says hi back. im staring into her lips as i feel an intense feeling of euphoria. just her voice was enough to nigga knock my socks off. i ask her what cup size she wears and she says her boobs are too big for a bra. as shes talking i take the moment to stick my face into her fat titties and motorboat the shit out of them. she then stepped on my cock and balls and popped my scrotum. semen and blood were flying everywhere and it was so sexy. AWOOOOOOGAAAAA i yell. she then calls me a weirdo so i walk away. what should i do?",
        "Eminem has just become the first celebrity to be diagnosed with Coronavirus. In a statement released by doctors, it has been revealed that his palms were sweaty, knees weak and arms were heavy. He presented with vomit on his sweater already. Initial testing has revealed it was mums spaghetti.",
        "Can a school legally take away your cock and ball torture device? no that is simply not that case , if this ever happens to you please contact your lawyer immediately and have this issue solved right away",
        "Being a hentai actress must be so weird. Imagine this: you’re in a soundproof room pleasurably screaming into an 800,000¥ microphone about how much you love old man dick at 10:47 AM on a Tuesday in October while your 45-year-old boss oversees you through a glass window from the other room. You eventually look up after 2 hours of practicing your unnaturally high-pitched moans and see him give you a big thumbs up as you pretend to have an orgasm.",
        "Billie Ellish 🙎🏼‍♀️is 18 🔞years old now🤭, y'all 🤠 know what that means 😳🤭. Yes, she's now legaly 👮‍♂️allowed to operate the 2019 Viper🐍 Rt80 8000lb Air🌬 Pneumatic Forklift Hatz Diesel Lift Truck 🚛... That is of course if she acquires the proper certification... 😳",
        "Chess hasn't been updated in almost 200 years and it's obvious the devs have abandoned it. The greedy creators took your money and laughed all the way to the bank. I remember back in 705 AD when chess was fun. Then they started adding stupid features no one wanted like “Castling” and “En Passant” instead of listening to player feedback and fixing game-breaking bugs. I've been complaining for YEARS about the collision-detection glitch with the horsey. The “clipping-thru-pieces” bug has been abused to death and the lazy devs refuse to fix it. Don't support this awful behaviour and boycott this company.",
        "Oh, so you support your girlfriend? You simp. Okay Homer SIMPson. You absolute simpanzee. OOO OOO OO OO EE EE OO 🐒 <- that is you. You are nothing but sludge . You are putrid muck given form, weakness personified. I am not sympathetic. You are simp pathetic.",
        "If being goth is a crime then arrest me for the murder of 3 people please god someone stop me this isn't a joke this is a literal cry for help please make the voices stop they keep asking me for more and more and I just want it all to go away sweet jesus help me",
        "I want to fuck mitochondria. I fantasize every night about pumping my throbbing dick into the warm, soft cristae of those sexy powerhouses. I want to feel the buzz of energy as the electrons orbit in the gravitational field of my massive cock. I want to feel the hot tightness of the mitochondrial membranes rubbing against my dick as I thrust it in and out of ATP synthases until I orgasm, washing the mitochondria with my cum like a tidal wave and mixing my own DNA with that of the mitochondria. Just thinking about it makes me want to explode with sexual energy.",
        "Every day, right after the pledge of allegiance and before the morning announcements, teacher would have us line up single-file clockwise around the room so we each got a fair chance to threaten to murder her with our guns. If you forgot your handgun at home that day, or your mom forgot to pack it for you, you didn’t get to threaten teacher’s life and instead had to clean out the chalkboard erasers while watching your friends and peers shove weapons in your teacher’s face. That was the worst, when mom would forget to pack my gun, because I hated cleaning those erasers. They always irritated my sinuses.",
        "I had a dream where, no joke, there where two sequels to “The Bee Movie” The second was a legitimately amazing movie about Barry B. Benson growing up to be a father and dealing with the complexity of raising two children, who had grown emotionally distant and slowly working to empathize and understand his children more and to stop being an emotionally abusive father. Slowly coming to accept and develop from his internalized homophobia. It won 2 Oscars. The third was some cheese spy comedy as bad as the first movie, where the F.Bee.I. recruit Barry to sort out an international terror agency of wasps lead by Osama Bee Lardin.",
        "I have viewed various pieces of hardcore gay pornographic material, yet none of them have been as gay as this fucking image. You have taken something normal and respectable, and have shat all over it with your furry, “owospeak” garbage. This makes me want to gouge my eyes out. I have purchased 500 gallons of nitric acid in order to disintegrate me and everything I own because of this image. I am willing to bet my life savings you are not allowed anywhere near a preschool. Fuck.",
        "I have noticed that, although Discord has 260 million registered accounts , my server does not have 260 million members. I'm not sure if this is being done intentionally or if these “friends” are forgetting to click 'join'. Either way, I've had enough. I have compiled a spreadsheet of individuals who have “forgotten” to join my most recent servers. After 2 consecutive strikes, your name is automatically highlighted (shown in red) and I am immediately notified. 3 consecutive strikes and you can expect an in-person “consultation”. Think about your actions.",
        "You are the most despicable, loathsome person I have ever had the misfortune of encountering. You are ugly inside and out, and your soul is blacker than the darkest night. You are a coward, a liar, and a cheat. You are worthless and pathetic, and I can't stand the sight of you. You make me sick to my stomach, and I can't wait to see the day when you finally get what's coming to you. I hope you rot in hell, you piece of shit.",
        "⚠️ This user has been warned by Discord for Racism, Sexism, Misogyny, Ageism, Transphobia, Homophobia, and Xenophobia. Visit Discord's ueer safety policy: https://discord.com/guidelines",
        "Not funny I didn't laugh. Your joke is so bad I would have preferred the joke went over my head and you gave up re-telling me the joke. To be honest this is a horrid attempt at trying to get a laugh out of me. Not a chuckle, not a hehe, not even a subtle burst of air out of my esophagus. Science says before you laugh your brain preps your face muscles but I didn't even feel the slightest twitch. 0/10 this joke is so bad I cannot believe anyone legally allowed you to be creative at all. The amount of brain power you must have put into that joke has the potential to power every house on Earth",
        "Hi @Everyone, New rule (and I can't believe I have to say this) please don't give birth in the voice channel. It makes people very uncomfortable.",
        "Slime-girls are objectively the greatest fuck you'll ever have in your life. Not only could you see your dick up in their guts or down their throat, but you could realistically fuck any part of their body you want. Got a thing for stomachs? You can fuck their belly button. Like armpits? They got you covered. Or rather they got your dick covered. In slime. And if that's not enough, they are amorphous, and can change their shape to form the most fuckable body of your dreams. It doesn't even have to be a normal body either. Want to fuck a cat girl? They got you, and you can fuck her in the ears. Want to fuck a dog girl? She's got you set. Owl, fox, bird, bunny, whatever else your sick imagination can come up with. If you can request it, she can fulfill it. Give in to the fact that slimes are godesses worthy of worship. Wake up. Take the slime pill.",
        "Kitchen. Thot. If woman want rights, how come woman big booty breast? If 🤢 WoMan Not OBJECT 😡 sex. why woman sexy dance?? Huh? 😡😡 Woman not want date me marry me, sex me - but woman walk out in My neighbourhood!, wear clothes!, have big booby, sexy! sex! Body!, long hair, woman body? HUH? WOMAN NOT WANT SEX? If Woman want rights, NOT WANT SEX - but woman not want punch Face?!?!?! Hypocret. Attention seek. Whoree",
        "my child saw the word “bussy” on a video last night he shoved his butt in the air and said “look at my bussy” and I asked where he heard that word and he said a YouTube video with Spider-Man pushing his bum around and saying it was his bussy. I could not find the video but my child is NINE why is this world so cold 🥲 I mean I laughed out of shock tho. I’m watching his videos now and they’re not like that help me.",
        "Imagine Anne Frank giving birth. Just imagine her, sweating and panting, desperately trying to hold back crying out in pain. The hot tears running down her cheeks. Fighting a losing battle to keep her grip on reality as the hormones and receptors, overwhelmed by the pressure and burning sensations, cause her to lose all perception of time and surrounding. Being too sick and exhausted to even sit up, but still forced to continue enduring because she no longer has control over her own body. Feeling her pelvis split in two as she bears down hard and pushes with her rapidly diminishing strength. Having to content, not only with becoming a mother at such a young and tender age, plummeting self-esteem at the sight of her once slender body becoming the size of a planet, fear of being socially ostracized, but the unending terror of Nazi persecution of the Jews as well. That her agony-induced cries, no matter how muffled, will attract attention and be a death sentence for her and her entire family. God, The mere though of it makes my cock harder than Chinese algebra",
        "So I’ve been a huge fan of Travis Scott for quite some time now (since his collaboration with Fortnite) and I was hoping to listen to Sicko Mode while scrubbing myself down in the shower. But as I undressed to bathe the thought occurred to me that if I wanted to really internalize Mr. Scott’s songwriting, the obvious choice is to do this anally. So next thing I know I’ve got two AirPod Pros lodged in my butt, blasting Sicko Mode at full volume (almost accidentally played Mo Bamba lol :P ). But then I realized that maybe AirPods shouldn’t be used while in the shower. So, I’m wondering, does anyone know if I can do this? Will my AirPods be ok? I just popped them in my ears and they sound a little funny.",
        "Gus is too professional to just suck cock. He's a sensual and passionate lover. He probably has a sex room hidden away in his house where even his closest and most trusted security can't find it. Stylish, but not excessive. Rustic dark wood walls, barn wood floor, queen sized bed with velvet pillows, and a small coyote fur rug in the middle. Before the action happens, he asks his lovers to wait while he sets up the scene. He dims the lights, sets up some candles, and puts on some calming piano jazz. Then, he lets him in and that's where the magic happens. They disrobe while passionately kissing. Gus pushes them onto the bed and lays gentle kisses down their body until he reaches their cock. When he sucks cock, he doesn't give that “sloppy toppy.” That's too messy. He embraces it, lovingly. He kisses it and licks it, slowly and seductively. Once he sees that they're close to the edge, he takes his mouth away from his cock and begins jerking them until they cum. He doesn't like to swallow or take facials.",
        "I thought only sweaty cocks smelled. Today I was proven wrong. Just after getting out of the shower, I came up with the brilliant idea of using a hairdryer to dry my cock 'n balls and I ended up inhaling the cock smell. Turns out clean cocks have a very specific smell too. I admit that I was sorely mistaken and would like to formally apologize to anyone who was swayed by my uneducated opinion on the subject",
        "How to remove women from the game? Yeah just wanted to restate, I'm really not sexist at all its just.. kinda embarrassing to admit the reason. i get a fucking boner when i dismember the female characters I hate it. it kinda gives the game a really weird vibe if I'm swordfighting at full mast but I can't fucking do anything about it. It's not like I have a gore fetish or any of that shit I just inexplicably get a hard on when I kill them. im not tryna do the stupid “haha women bad I'm such a sigma” it just makes the game weird for me to play and I want to know if there's a mod or something to remove their models.",
        "God I want to fuck a shark. I want to grab its nose and rotate it 90°. I want to grab its fin and be dragged around really fast. I want to give it so much of my cum that it bites me not out of malice or mistaking me for food, but out of sheer desperation to get it's wet sharkussy away from my penis.",
        "Dude stop. My brother died in a circus accident. stop using the clown emoji. Rest in peace to my brother. Please refrain from using it in your life, that is wrong to all the people who lost their lives. I sincerely hope you learn from this mistake and no longer make the same choice again. Please evaluate your life choices, and question yourself to why you decided to use the clown emoji. I understand that you may have been through alot, but that does not mean you should joke about dead people. You may have been abused or hurt, but do not use that as an excuse to hurt others. If i ever catch you using offensive things again, so help me god i will find you. I will find you myself. I swear on my brothers circus that i will stop at no cost. You are my enemy. And i will hunt you like you are my prey.",
        "I’m straight 100% but I fell in love with a male friend. It's not that I'm gay but, but that guy is just so hot I can't help myself but think about him everyday. I joked today about fucking him pretty hard and he laughed. OMG I think I'm gonna explode with horniness OMFG",
        "Please consider pronouns before going to war. Remember that, in the fog of war, people will likely refer to you by the gender assigned to you at birth. So make sure you wear a badge with your preferred pronouns so that you don't suffer unnecessary verbal violence and bigotry in the field. The last thing you want to hear is someone mis-gendering you as you bleed out after a fire fight. Expect to encounter a lot of heteronormative language - typical of the chauvinist environment in which you will find yourself. Shouts like “watch out, lads”, “listen in, boys” and other micro-aggressions will wear you down as the white male dominated armed forces attempt to erase your lived experience. If you can, be the change you want to see. You can do this by shouting “Zhere coming from the south!”, or “two possible BIPOC folx taking cover at your 6!”. People will respect your efforts to be inclusive in the theatre of war. Ultimately, silence is violence, and you'll be wanting as little additional violence as possible.",
        "No. More. Saying. Cuss words! It. Is. Not. Good. I'm putting a video on YouTube about no more saying cuss words. No more saying cuss words guys! It's inappropriate and violent! If you say a cuss word then you're like, going to jail, and you're like, and when you go to jail, i- ba- when you go to jail, if you say, if you say a cuss word you go to jail and if you go to jail cause you said a cuss word, then... You're only gonna eat BROCCOLI and OTHER VEGETABLES for your WHOLE LIFE. You don't want to eat vegetables. Sometimes people like eating sweets but, I eat broccoli. So, I'm okay with broccoli but I do not want to go to jail. You can not go to jail. And saying cuss words is ILLEGAL. They are now gonna make a law about that. It is illegal, it is inappropriate, it is really violent. I better warn my school about that.",
        "Oh, these? My boobies? My massive fucking titties? My super stuffed milkies? My honker bonker doinky bonkies? My fucking fabric stretching wind flapping gravity welling sex mounds? You mean these super duper ultra hyper god damn motherfucking tits?",
        "Please put an NSFW tag on this. I was on the train and when I saw this I had to start furiously masterbating. Everyone else gave me strange looks and were saying things like “what the fuck” and “call the police”. I dropped my phone and everyone around me saw this image. Now there is a whole train of men masterbating together at this one image. This is all your fault, you could have prevented this if you had just tagged this post NSFW.",
        "The biggest oversight with Dark Willow is that she's unbelievably sexy. I can't go on a hour of my day without thinking about plowing that tight wooden ass. I'd kill a man in cold blood just to spend a minute with her crotch grinding against my throbbing manhood as she whispers terribly dirty things to me in her geographically ambiguous accent.",
        "The year is 2043 Covid variant phi beta epsilon is ravaging 0.0026% of the population, you go outside for your government mandated 30 minute exercise, it's 1 a.m. not the best time, but they alternate your schedule so eventually everyone does get some sunlight. You quadruple mask and put on your plastic smock. You gaze longingly at the sky. A man riding his bicycle points his flashlight at you “Why aren't you doing your stretches and cardio?” He asks, you recognize him as your neighbor (maybe, it's been some time since you last saw anyone). “It's because of people like you not obeying that the lockdowns have been extended another 4 years.” He mumbles through his layers of masks. He reports you to AlphabetGoogle and your social credit score drops 5 points, good luck buying bread this week.",
        "🏃‍♂️ I AM THE RUNNER. I SEE YOU WALKING ON THE SIDEWALK. BUT I WILL NOT DISTANCE MYSELF. I RUN STRAIGHT BY. YOUR GERMS ARE TOO SLOW FOR ME. MY AIRPODS GRANT ME INVULNERABILITY. I AM THE PINNACLE OF HEALTH, A PERFECT BODY AND MIND. I WILL NOT CATCH A VIRUS, FOR NOTHING CAN CATCH ME.",
        "Attention - due to the increased risk of COVID-19 I will no longer be eating ass. I apologize for the inconvenience this may cause.",
        "动态网自由门 天安門 天安门 法輪功 李洪志 Free Tibet 六四天安門事件 The Tiananmen Square protests of 1989 天安門大屠殺 The Tiananmen Square Massacre 反右派鬥爭 The Anti-Rightist Struggle 大躍進政策 The Great Leap Forward 文化大革命 The Great Proletarian Cultural Revolution 人權 Human Rights 民運 Democratization 自由 Freedom 獨立 Independence 多黨制 Multi-party system 台灣 臺灣 Taiwan Formosa 中華民國 Republic of China 西藏 土伯特 唐古特 Tibet 達賴喇嘛 Dalai Lama 法輪功 Falun Dafa 新疆維吾爾自治區 The Xinjiang Uyghur Autonomous Region 諾貝爾和平獎 Nobel Peace Prize 劉暁波 Liu Xiaobo 民主 言論 思想 反共 反革命 抗議 運動 騷亂 暴亂 騷擾 擾亂 抗暴 平反 維權 示威游行 李洪志 法輪大法 大法弟子 強制斷種 強制堕胎 民族淨化 人體實驗 肅清 胡耀邦 趙紫陽 魏京生 王丹 還政於民 和平演變 激流中國 北京之春 大紀元時報 九評論共産黨 獨裁 專制 壓制 統一 監視 鎮壓 迫害 侵略 掠奪 破壞 拷問 屠殺 活摘器官 誘拐 買賣人口 遊進 走私 毒品 賣淫 春畫 賭博 六合彩 天安門 天安门 法輪功 李洪志 Winnie the Pooh 劉曉波动态网自由门",
        "Where was the Paw Patrol during the Iran Hostage Crisis? As far as we know the PAW Patrol has the capabilities of international travel and possible covert operation capabilities. However, the PAW Patrol failed to assist in any way during the Iran Hostage Crisis of 1979, which is unacceptable seeing as the US diplomats were hostages from November 4, 1979, to January 20, 1981. Could it be that the PAW Patrol is run by Islamic extremist that utilize PAW Patrol to increase positive images of the extremist, while also taking money from the UN? Or that the PAW Patrol is US run, and was told by the CIA to not intervene with the hostage crisis? If it is the former, why so? Could the Iran Hostage Crisis be a hoax, used to crack down on Iran for bringing down the monarchy that was ruling Iran, made possible by a coup from the US and UK?",
        "I'm a climate change denial denialist. I deny the existence of climate change deniers. Think about it. The evidence is overwhelming. Do you really think people still don't believe in climate change? It's a lie. Everyone knows by now that the earth's climate is changing. Climate change deniers are a hoax perpetrated by the Chinese.",
        "under section 34 of Secure Credits and Taxes act, the president can induce artificial inflation and if the inflation gets high enough, technically Trump can declare emergency powers and not leave the office, google “Trump SCAT inflation rule 34” for more info",
        "My President does not need to cheat in order to win. My President loves this country and ALL of its people. My President would not sell this country to our worst enemy, transforming it from a gleaming republic and beacon of freedom to another steaming pile of communist filth. I'm on the side of right and light. You're on the side of subversion and the darkness. You think you won, but all you won is your one way ticket to hell.",
        "Let's say, hypothetically, I am a barbie girl. Okay let's even say I'm in a barbie world. Right so, in this scenario, I would obviously know from personal experience that life in plastic is fantastic. Wouldn't it be reasonable to assume you could brush my hair and undress me literally everywhere? Imagination; you can derive from the fundamentals of basic logic that life is your creation.",
        "I masturbate to pictures of Ben Shapiro almost every day just because I know he would hate the idea of a male wanking to him. it's actually really difficult because I don't find him sexually attractive in any way and especially just his headshots but I have done it every day for about 2 years because I found it funny at first but now I'm so used to it that it makes me feel incomplete if I don't do it every day",
        "So today, for the first time, my little toddler finally counted to ten. Everyone was celebrating, saying how proud they are in my kid, and then Ben Shapiro kicks open the door. “Oh you think it's impressive that they can count to ten? I can count to one million.” and then proceeded, in my living room for the next two weeks, to count to one million. He then said “yep, another libtard destroyed” and then curbstomped my kid.",
        "Now let's say hypothetically I was the impostor. How would I get from reactor to medbay in that timespan, from which we saw each other, till you found yellow dead. Also if I were the impostor hypothetically speaking, how would I have finished all my tasks.",
        "Ha, you're sorry? You're sorry? You killed my brother, and you say you're sorry? Let me tell you something. The job offer, it didn't upset me, it amused me. Wooo, big job at the illustrious HHM. A chance to play at the palace. Ooh Little old me? You have no idea what's going on. You're a teensie tiny man in a teensie weensie little bubble. Ohhh don't you fucking “Oh Jimmy” me. You look down on me? you pity me? walk away. That's right Howard. You know why I didn't take the job? Because it's too SMALL. I don't care about it. It's nothing to me. It's a bacterium. I travel in worlds you can't even imagine. You can't conceive of what im capable of. I'm so far beyond you. I'm like a god in human clothing. Lightning bolts shoot from my fingertips!",
        "Want a break from the ads? If you tap now to watch a short video you'll get 30 minutes of ad free music! Yes, really! If you tap now you'll get 30 minutes of ad free music! So what are you waiting for? I'm still waiting.. Why aren't you tapping? Don't you want 30 minutes of ad free music? If you tap now and watch the short video you'll get 30 minutes of ad free music! It's that easy! If you want to be free from the ads forever consider buying spotify premium! With spotify premium, you get ad free music, forever! And if you tap below you can get the first 3 months for free! Terms and Conditions apply",
        "Is a man not entitled to the sweat of his brow? 'No!' says the man in Washington, 'It belongs to the poor.' 'No!' says the man in the Vatican, 'It belongs to God.' 'No!' says the man in Moscow, 'It belongs to everyone.' I rejected those answers; instead, I chose something different. I chose the impossible. I chose... Rapture, a city where the artist would not fear the censor, where the scientist would not be bound by petty morality, Where the great would not be constrained by the small! And with the sweat of your brow, Rapture can become your city as well.",
        "YOU! ME! GAS STATION! what are we gettin for dinner!? sushi of corse. UH OH! There was a roofie inside of our gas station sushi, we black out and wake up in a sewer, we’re surrounded by FISH-HORNY FISH, you know what that means, FISH OORGIE! The stench draws in a bear, what do we do? We’re gunna fight it, bare handed, bear..NAKED?! OH YES PLEASE, we befriend the bear after we beat it in a brawl, then we ride it into a Chucky Cheese, DANCE DANCE Revolution, revolution?! Over throw the Government!? UHH I THINK SOo,  next thing you know im reincarnated as Jesus Christ, then I turn into a Jet, FLY into the sun, black out again, WAKE UP, do a bump WHITE OUT! (Which I didnt know you could do) then I smoked a joint, GREENED OUT, THEN I TURNED INTO THE SUN, UEGH OH looks like The meth is kickin in..DEUHBLUHHSBDUHHSBUHSBUHEUGHHUHAAAAHUEAAHAAAAAAA!!!!",
        "Hello, ma'am do you have a minute to talk about our lord and savior Lightning McQueen?! Did you know that Lightning McQueen is the star of several feature films such as Cars, Cars 2, Cars 3, Planes: Fire and Rescue, Finding Dory, Toy Story 3, Coco and Ralph breaks the internet? As well as other short film such as Master and the Ghostlight, Miss Fritter's Racing Skoool, Television program such as Cars Toons, Pixar's Popcorn Cars series voiced by none other than Owen Wilson?",
        "Snake... why are we still here? Just to suffer? Every night, I can feel my leg and my arm... even my fingers... the body I've lost... the comrades I've lost... won't stop hurting. It's like they're all still there. You feel it too, don't you? I'm the one who got caught up with Cipher. A group above nations... even the US. And I was the parasite below, feeding off Zero's power. They came after you in Cyprus... then Afghanistan... Cipher... just keeps growing. Swallowing everything in it's path. Getting bigger and bigger... Who knows how big now? Boss. I'm gonna make 'em give back our past... take back everything that we've lost. And I won't rest... until we do.",
        "Good evening Twitter. This is your boy eatdatpussy445 and about 30 to 45 minutes ago I beat the fuck out of my dick so god damn hard that I can't even feel my left leg. My left leg has went totally numb and my dick has also went totally numb to the point where it feels fucking weird when I go and take a piss.",
        "What is my perfect crime? I break into Tiffany's at midnight. Do I go for the vault? No, I go for the chandelier. It's priceless. As I'm taking it down, a woman catches me. She tells me to stop. It's her father's business. She's Tiffany. I say no. We make love all night. In the morning, the cops come and I escape in one of their uniforms. I tell her to meet me in Mexico, but I go to Canada. I don't trust her. Besides, I like the cold. Thirty years later, I get a postcard. I have a son and he's the chief of police. This is where the story gets interesting. I tell Tiffany to meet me in Paris by the Trocadero. She's been waiting for me all these years. She's never taken another lover. I don't care. I don't show up. I go to Berlin. That's where I stashed the chandelier.",
        "Tits. Ass. Pussy. Feet. Long ago, the four kinks lived together in harmony. Then everything changed when the Feet Kink attacked. Only the horny, master of all four kinks, could stop them. But when the world needed him most, he vanished. A hundred years passed and my brother and I discovered the new horny, an Ass Eater named Ricardo, and although his ass is great, he still has a lot to learn before he's ready to fuck anyone. But I believe Ricardo can save sex.",
        "Minecraft, but he's torturing my cock and balls. In this video, I have to beat Minecraft while my friend is torturing my cock and balls. He has a humbler, a stretcher and can actively kick them at any time he wishes. Can I beat the Ender Dragon before my testicles are ruptured? Watch to find out.",
        "Anyone who spends more than 5 minutes in my presence knows that I never stop talking about how much I love busty, curvy, voluptuous anime ladies. Anyone who starts “digging for dirt” on me quickly learns that a pedophile narrative is never going to hold up, since I can't go longer than 60 seconds without talking about big boobs and thick booties.",
        "Hey Vsauce, the Infinite Darkness here- Why am I filled with eternal pain and suffering? Well, my soul has been consumed by the one all might Lord, Cthulu, so I have been trapped inside this dying mortal corpses for all eternity, never to escape.",
        "Nigga don’t hate me cause I’m beautiful nigga maybe if you got rid of that Yee Yee Ass hair cut you got you would get bitches on your dick, oh, better yet maybe Tanisha will call your dog ass if she ever stops fucking with that brain Surgeon or Lawyer she fucking with, ♪♪ Niiiggggaaaaaa ♪♪",
        "What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, kiddo."
    ]


    if any(word in msg for word in pasta_words):
        await message.channel.send(random.choice(pasta_resp))
  
  
'''  
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
        
        
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith.('Hello!'):
        await message.channel.send('Hi bitch')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if "pizza" in message.content.lower():
        await message.channel.send("Go get your pizza!")


@client.event
async def on_message(message):
   if message.author == client.user:
        return  
    
    msg = message.content.lower
    
    sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]

    starter_encouragements = [
        "Cheer up!",
        "Hang in there.",
        "You are a great person / bot!"
    ]
 
    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))
'''

client.run(TOKEN)
