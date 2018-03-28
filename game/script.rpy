# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define L = Character("Leyla", color="#72a3ff")
define C = Character("Cyrus", color="#ffb871")
define S = Character("Sophia", color="#8cffc5")
define E = Character("Elaine", color="#ea4f6c")

define ph = Character("Phone", color="#e0e0e0")
define ph_shake = Character("Phone", kind=ph, show_window_transform=Shake(None, 1.5, dist=10))

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    play ambient "music/ambiance-heavy-rain-loop.ogg"
    scene black

    show text "We first met on a quiet, rainy afternoon." with Dissolve(2):
        xalign 0.5 yalign 0.5
    pause 1.0
    hide text with Dissolve(2)

    scene bg city1 rain
    with dissolve
    play music "music/Poem for the Different Future.ogg"

    "In this bustling, hectic city there was rarely a quiet moment."
    
    "Where the sounds ebbed enough that you could look around and decide, \'ah, the city has gone to sleep for the day\'."
    
    
    "When the night truly took hold and laid all the noise to rest."
    
    "Instead late night and early morning blended together, so it was never quite late enough to be asleep before it became early enough to be awake."
    
    "The bright lights and thick smog enveloped the city from dusk to dawn."
    
    "But there {i}was{/i} a time when the city fell silent. One specific event that made the hum of the crowd fade and the buzz of the streets disappear."
    
    "When the rain came."
    
    "While most cities tend to empty out anyways when it rains- as people clamour to stay dry- this was different."
    
    "The rain was odd in this city, punctual and ritualistic."
    
    "It only ever arrived at two specific times, exactly at noon or exactly at midnight. Not a second earlier or later."
    
    "And it would last exactly four hours, like clockwork, before silently leaving."
    
    "It had no rhyme or reason for when it appeared. Seasons, temperature, humidity were all nonfactors." 
    
    "It could be the middle of summer, on the hottest and driest day the city had ever seen, and no one would bat an eye if the rain appeared."
    
    "And it never came in close succession, there were always severaal days, weeks, or even months in between each day of rain."
    
    "And finally, there was \'the calm\'."
    
    "When the rain began, people started to empty off the streets, just like in most other cities."
    
    "But in this city, it was a bit different. People began to empty and didn't stop until every last person was inside. Within half an hour, not a single, errant soul could be seen outside."
    
    "And it stayed that way for the entirety of the rainfall. It didn't matter what plans people had, what appointments were missed, everyone stayed inside."
    
    "And the rain would continue without pause."
     
    "\'The calm\' wasn't just the people, but the entire city. As if a thick blanket had been thrown over it, muffling sound, and space, and time."
    
    "As if the city was frozen for those four hours." 
    
    "It wasn't just engagements or schedules that were set aside, it was accidents, disasters, illness, any concievable event in reality that could make a person go outside."

    "During the rain, they all softly ceased to occur, curled up in a corner and postponed until after the droplets halted."

    "The outside world became a cut off space, isolated from the experience of all the citizens that continued to go about their day indoors."
    
    "And no one noticed."
    
    "Or rather, they refused to notice."
    
    "The rain never forced them inside, that would be too direct, too easy for the subconscious to object."
    
    "It was a suggestion." 
    
    "The desire to stay dry, the howl of the cold and call of a warm bed, the laziness of a gray afternoon, the sound of raindrops on the window pane, the convenience of canceled meetings and early days off."
    
    "Amplified, reinforced, and then gently tucked into the corner of their minds, as if putting a child to sleep after a long day."
    
    "And if the rest of reality just happened to leisurely stretch into a lull, so that those four hours remained uneventful and quiet, well that just made the languidness more appealing."
    
    "So it was, one autumn day, exactly at noon, the rain rolled in."
    
    "The streets cleared out, the automobiles grew quiet, and the din of the city gave way to the steady pattering of the rain."
    
    "And in the gray, midday light the outside world seemed completely devoid of people."
    
    "Almost."
    
    show leyla neutral with dissolve
    
    "At the edge of the downtown district, under the awning of a closed down restaurant, stood a girl quietly watching the rain."
    
    hide leyla neutral with dissolve
    show cyrus sigh with dissolve
    
    "On the opposite end of the city, holding a pink umbrella with a clumsily hand-stitched teddy bear, ran a boy hurriedly."
    
    hide cyrus sigh with dissolve
    show sophia neutral with dissolve
    
    "In the middle of the city park, situated at the edge of the apartment complexes, strolled a girl blithely through the storm."
    
    hide sophia neutral with dissolve
    
    show haruha neutral at slightright with dissolve 
    pause 0.3
    hide haruha neutral with dissolve
    
    show nino neutral at center with dissolve
    pause 0.3
    hide nino neutral with dissolve
    
    show sabata neutral at slightleft with dissolve 
    pause 0.3
    hide sabata neutral with dissolve
    
    show sera neutral at center with dissolve
    pause 0.3
    hide sera neutral with dissolve    

    "And scattered throughout the city, few and far between, were others. And they were there in the rain. And yet they were not there."
    
    "Like the rain and outside world, they were cut off. As the city and citizens continued to turn, never noticing."
    
    "Normally, when the rain came, it drove everyone indoors, creating small bubbles of activity inside buildings, houses, stores- but outside those bubbles the rain emptied the world."
    
    "Normally... but to those who were abnormal..."
    
    "For the rain didn't drive what was normal inside, but revealed what was abnormal lying beneath the surface."
    
    "And those who were \'abnormal\' while the city spun by in its daily, usual routine..."
    
    "Became \'normal\' when the rain washed away the thin exterior of the city."
    
    scene black
    with dissolve
    
    play music "music/New-Paradise_loop.ogg" fadeout 2.0 fadein 2.0
    pause 1.0
    stop ambient fadeout 1.0
    
    scene bg room1 night
    with dissolve
    
    "The room was dark and silent, save the faint babble from the TV in the corner."

    "The dull haze from the screen pulsed calmly across the room, the news anchor on the monitor chattered away like background noise."
    
    "Outside of the window, the city was aglow in bright lights and sounds."
    
    show leyla calm with dissolve
    L "..."
    
    "A girl sat lazily, with her legs sprawled across the whole length of the small couch, arm draped over the headrest."
    
    "Though she occassionally glanced at the televsion, she didn't see it. Her gaze went absently through the glowing screen, mind elsewhere."
    
    "Her free hand, unoccupied with lolling across the back of the couch, fiddled with a small, wooden sphere."
    
    show leyla neutral
    
    "As the clock ticked on the wall and the seconds rolled by, a strange ambience filled the room."
    
    "A feeling as if time were being stretched, or something thin and whispy was swirling just out of view."
    
    "If an onlooker had peeked into this room, they would see nothing out of the ordinary."
    
    "A girl on the couch, arm draped over the back, gaze flickering through the objects in the room, TV chattering in the background."
    
    "If they peeked in a second time, they would feel a creeping sense of unease."
    
    "A {size=+10}{font=zalgo.ttf} vo i d{/font}{/size} on the couch, arm draped over the back, gaze flickering through the objects in the room, TV chattering in the background."
    
    "If they peeked in a third time, they would feel a sense blankness, idly closing the door and walking away, forgetting it existed."
    
    "An empty couch, a flickering TV, dry noise and muted air."
    
    "The girl looked out of the window, watching lights streak past as cars careened across the labyrinth of concrete and steel. Her eyes drifted towards the black sky."
    
    "Moonless and starless, but filled with light and pollution."
    
    "So different from her own hometown."
    
    "The noise of the television briefly jerked into focus, the jabbering of the news metamorphosing into words."
    
    "{color=#e0e0e0}News Anchor{/color}" "And this marks the fifth case in the last month. As before, the individuals reappeared after a few days with no discernable injuries and claiming to have no memory from when they went missing."
     
    "{color=#e0e0e0}News Anchor{/color}" "Authorities have yet to release an official statement, however they are not ruling out foul play."
    
    "{color=#e0e0e0}News Anchor{/color}" "Though there have been no casualties in these cases of what the public is referring to as 'spiriting away', there is growing concern over the increase in victims."
    
    "{color=#e0e0e0}News Anchor{/color}" "This case marks the largest group yet, with ten people reported missing. Coupled with the lack of evidence, many people have begun expressing concern over the lack of progress in investigations."
    
    show leyla calm
    
    L ".....so they didn't get all of them."
    
    "{color=#e0e0e0}News Anchor{/color}" "Perhaps the most arresting development surrounding these disappearances comes not from the victims themselves, but the spread of an online group called the Eye of the Night who have..."
    
    "The words from the television grated back into mushy noise as the relevant news gave way to gossip and sensationalism."
    
    show leyla neutral
    
    "Leyla finally set down the small wooden sphere- which had morphed into a small wooden cube in the meantime, detachable puzzle pieces sliding and clicking into different positions- and picked up the remote."
    
    "The news anchor had called in another specialist of some sort, psychology or what not, and the two were exaggeratedly explaining the significance of mob mentality or such, but it wasn't more than background noise at this point."
    
    "The TV turned off with a click as Leyla set the remote down, standing up and stretching."
    
    "No matter how long she had spent in \'this\' side of the city, it was always interesting to see how its residents attempted to reason about its abnormal happenings."
    
    "Though to be fair, just as many of the residents of '\that\' side of the city rode equally misguided trains of thoughts, trying to figure out how the workings of this side operated."

    "The news was wrong, of course." 
    
    "It wasn't ten people that went missing this time, it was fourteen. And it wasn't that there were no casualties and the victims returned home in a few days."
    
    "The ones who returned were the only ones that existed on this side anymore."
    
    "Though perhaps what was more concerning was the increasing difference between how many disappeared and how many returned. In that sense the news was correct."
    
    "The first time, all of the missing victims had returned home, oblivious. But each time it seemed like more slipped through the cracks."
    
    "At this rate, it might not be long before some{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5} troublesome event or another caused her to be dragged in as well."
    
    play ambient "music/Vintage Phone Ringing.mp3"
    
    ph_shake "{size=+20}RING! RING!!{/size}"
    
    show leyla surprised with vpunch
    L "!!"
    
    "Leyla jumped, smashing her leg against the corner of the coffee table, which was just the convenient height of \'too low to see in your peripheral when you were about to crash into it\'."
    
    "The sudden, shrill cry of the phone had shot through the silence, ripping the last thought from her mind."
        
    show leyla exasperated
    
    "Speak of the devil."
    
    "Gingerly rubbing the side of her leg, she fumbled over to the phone and picked it up."
    
    stop ambient
    
    L "Hello?"
    
    ph "{size=+10}F{w=0.2}I{w=0.2}N{w=0.2}A{w=0.2}L{w=0.2}L{w=0.2}Y{w=0.2}!{/size} Do you have ANY idea how many times I've called trying to get ahold of you?!"
    
    "Yep."
    
    show leyla sigh
    
    L "I would've thought the automated message telling you the number you called doesn't exist was a big enough hint."
    
    ph "I didn't spend three weeks nagging you to finally get a phone just so you could turn around and phase it out of reality every few days!"
    
    show leyla smile1
    
    L "So you admit it was nagging."
    
    ph "Not the point and you know it."

    # This ends the game.
    
    show leyla neutral
    
    L "Speaking of my phone, I distinctly remember not having one right now, so what is it doing back in my room and ringing?"
    
    ph "I had to run a gauntlet of nightmares to find it, but I did. So stop making things in your room dissappear or I swear I am going to start camping in your damn apartment."
    
    "Gauntlet of nightmares was actually a pretty tame description for a human, so it was almost surprising that she had managed to find it."
    
    "And knowing Sophia, she would almost certainly make good on that last threat."
    
    show leyla sigh
    
    L "Well fine, I know better than to argue with you when you get like this."
    
    L "So, what was so important that you simultaneously couldn't be bothered to come find me in person and yet decided to run around in an abyss looking for a phone?"
    
    S "Can you come to Central Park? We need help."
    
    show leyla annoyed2
    
    "Leyla paused, her relative nonchalance slowly giving way to suspicion."
    
    L "Now that... is a bit farfetched."
    
    "The possibility that the humans might be having issues with the current situation wasn't farfetched, but that they were having issues even with Sophia there- was."
    
    S "Do you really think I would've spent the last thirty minutes digging out your phone if I was kidding?!"
    
    show leyla surprised2
    
    "Thirty minutes...that was probably a new record, impressive. She briefly considered hiding things a bit more thoroughly next time."
    
    S "And I would've just gone to you myself but I need to stay here, they're having a hard time keeping it contained. But I can't do that {i}and{/i} purge this thing so-"
    
    show leyla annoyed2
    
    L "Are you saying it's gotten bad enough that you can't just eliminate the source?"
    
    "Sophia was talented, frighteningly so. An anomoly that she couldn't just destroy would have set off every alarm Leyla had set up around the city."
    
    S "That... I mean, technically no but... the situation is a bit... delicate..."
    
    "The irritation in Sophia's voice earlier faded into uneasiness, and not a bit of guilt." 
    
    "So it {i}was{/i} something that she could handle herself."
    
    "As to why she didn't, well there were a few possibilities and most of them were particularly annoying."
    
    show leyla annoyed
    
    L "Sophia."
    
    "Leyla's voice was flat and expectant, like a mother waiting for an explanation from a particularly evasive child after they had knocked over an expensive vase."
    
    S "I promise it won't take very long! And there's only two other people here besides me, so I promise I can keep them out of your way!"
    
    "And like a child trying to sidestep the issue, Sohpia launched into reassurances, words picking up pace after each sentence."
    
    S "And I'll be here too, so it's not like anything can accidentally escape or you have to worry about collateral damage. And-"
    
    show leyla sigh 
    
    "Leyla let out a particularly audible sigh, making sure the phone could pick it up."
    
    L "Alright, fine." 
    
    L "You can explain everything in full detail later. I'll go help."
    
    S "Thanks, teach! I promise it'll be super quick."
    
    "There was a pause."
    
    S "...uh, that being said...could you wait, like, 10 minutes before heading over?"
    
    show leyla neutral
    
    L "...why?"
    
    S "Um... cause I need a little bit to finish up reinforcements to this barrier..."
    
    L "..."
    
    S "And the other's are due to swap out for breaks then, so they'll be out of the way more easily..."
    
    show leyla neutral2
    
    L "..."
    
    S "And uh... {size=-10}Elaine is finally going on break then too.{/size}"
    
    show leyla angry with vpunch
    
    L "Sophia!"
    
    S "...!"
    
    "Leyla could almost feel the other girl flinch through the silence, and in any other situation she might have relented, but not this one."
    
    L "Is {i}THAT{/i} why you haven't just destroyed the anomoly already?! Because that ignorant, prejudiced-"
    
    S "I know! I know! But teach, it's not that simple! Elaine isn't a bad person, she's just been through a lot and she's cautious! And maybe a little paranoid... but that's not the point!"
    
    show leyla annoyed
    
    L "Oh, then what {i}is{/i} the point, pray tell?"
       
    L "That the other members of your little organization are so scared of shadows in the dark they'd rather close their eyes and cover their ears than spend even a single second trying to understand things?"
    
    S "Teach!"
    
    show leyla annoyed2
    
    L "..."
    
    S "They're not like that- {i}you{/i} know they're not like that! I'm not saying everyone is always right or that they don't jump to conclusions but-!"
    
    S "...Just, I'm sure I can make everyone understand with a bit of time... And a lot of effort."
    
    S "And...and, you've met some of them! Elaine is just... a lot of them have gone through a lot. But like, they're good people! And a lot of them like you, you know that! Even those who've lost a lot..."
    
    S "And just... can we not fight about this right now?" 
    
    S "I know, Elaine has a lot of... biases. But I'm sure I can make her understand over time."
    
    S "And I just... I just need your help for a little bit. It'll just be in and out, and I promise I'll be back afterwards."
    
    S "This is the last case we've got, I've taken care of all the others. So I can get to all those lessons I've been putting off!"
    
    S "And like... just... please?"
    
    "Sophia's voice trailed off, pleading in tone."
    
    "And though she would have buried anyone who said she had a soft spot for her student six feet under, it was blatantly obvious to everyone that Leyla did."
    
    "Blantantly obvious to everyone, including Sophia."
    
    show leyla sigh
    
    "Leyla let the silence stretch out a bit longer, making sure Sophia understood that she still wasn't happy about this, then finally sighed."
    
    L "Haaah...fine. I did technically already agree to this earlier."
    
    S "...! Thanks, teach! I promise it'll be done and over with before you know it."
    
    "The absolute shift in tone that Sophia was capable of doing on a dime was sort of impressive, in its own naive manner."
    
    show leyla smile2
    
    L "So the robot finally remembered that it needs to pretend to rest to keep up the illusion of being flesh and blood?"
    
    show leyla smile1

    S "Teach!"
    
    "But the insult didn't carry any weight, and the mood from earlier had dissapated."
    
    S "...I mean, it's true I haven't actually seen her eat in the last ten hours... actually I think she was on duty even before I showed up... but still!"
    
    "Elaine's implacability was a common topic even among her own subordinates, both as a source of wonder and ire." 
    
    "Leyla's comment was mostly in jest, offering a way out of the previous subject, which Sophia gladly took."
    
    S "Anyways, they'll be swapping shifts in about ten minutes, so I'll see you then."
    
    show leyla smile4
    
    L "...sure, I'll head over in a bit then. Bye."
    
    ph "k-chk!"
    
    show leyla smile1
    
    "Leyla set the phone back down into the receiver slowly, eyeing it bemusedly."
    
    "She had always had detractors, but after she took on a human as a student, she had basically set off a hornet's nest. Not that it mattered to her."
    
    show leyla neutral2
    
    "She had never been one for whatever vague political grabs at power those around her were always trying to position themselves for."
    
    "It was just a shame they kept trying to use her as one of their pieces. A shame fo them, of course."
    
    "Those who overstepped their boundaries learned their lesson far too late, but it had served to curb the others."
    
    "And human or not, Sophia was undoubtedly the most talented Shifter she would ever meet in this lifetime."
    
    "For all the greivances that she had expressed with humans and their small-mindedness, she knew that the same applied to many of her own."
    
    "After all, it was that blindness that made them ignore a once in a millenia opportunity simply because it had shown up on this side instead of their own."
    
    play sound "music/clock-chimes.mp3"
    
    show leyla neutral
    
    "In the distance, the faint but heavy chime of the old clock tower tolled out the midnight call- a rare piece of history that hadn't been mowed down with the modernization of the city in years past."
    
    "Leyla glanced at the clock. It was normally about a 30 minute walk from her apartment to Central Park, 40 minutes if you counted the time it took to get down the stairs and navigate out of the maze of complexes in the area."
    
    show leyla smile4

    "Normally anyways, but she always took the expedited route."
    
    show leyla neutral

    "She shuffled over to coffee table, where the small, wooden puzzle sat and picked it up, pressing it against the palm of her hand snugly."
    
    show leyla neutral2 red
    
    "There was pause, as if a second had somehow been drawn out into a minute, the feel of air being suctioned out and then a snap, as if reality had flicked back like a rubber band."
    
    show leyla neutral
    
    "Her hand was empty."
    
    "Without missing a beat, Leyla walked over to the window and pushed it open."
    
    scene black
    with wipedown
    play music "music/Stage-Door.mp3" fadeout 2.0 fadein 1.0
    
    pause 2.0
    
    scene bg city2 night
    with wipedown
    
    play ambient "music/wind01.mp3"
    
    "The night air came rushing in, cold and biting. It was, after all, still winter."
    
    show leyla neutral with dissolve
    
    "Leyla stepped onto the windowsill, one hand grabbing the edge of the window and one outstretched."
    
    show leyla calm
    
    "For a brief, inescapable second, it seemed as if all of the sound in the city had frozen save for the wind."
    
    "There was an almost monstrous howl as if the wind were all being sucked and compressed into the area around her."
    
    show leyla wind1
    
    "And then it snapped back, like a spring and everything rushed back to normal."
    
    show leyla wind2
    
    "Everything except for the small area around her."
    
    "The air around her whirred and whined, like an animal."
    
    show leyla wind4
    
    L "Shh, shh hush. I'm right here, your anchor is right here. Thank you for answering so quickly."
    
    show leyla wind3
    
    L "I need a bit of a shortcut to the park, accompany me for a while."
    
    "The wind whistled and then stopped, as if the air, right down to the individual atoms, had frozen in place."
    
    "Then, before you could blink it swirled into a gale, yipping and howling, pulling on her arms and legs."
    
    "Leyla pushed herself up completely onto the windowsill, then stepped off."
    
    hide leyla wind3 with dissolve
    
    scene bg city2 night falling
    
    "Gravity grabbed her immediately, pulling and clawing her towards the concrete ground."
    
    "The air rushed as her body collapsed into freefall, and then wrapped around her as it pulled her sharply to the side."
    
    "And she was still falling, but no longer towards the ground."
    
    "Sophia had often asked her what it felt like to \'fly\', being one of the few concepts she had no affinity for."
    
    "And Leyla had repeatedly explained that, because humans have such vivid imaginations, thinking of it as flying made it harder to grasp the concept."
    
    "One things humans did, astoudingly well, was conjure up sensations of events they had never experienced." 
    
    "Flying, to Sophia, was gliding, twisting and speeding through the air."
    
    "Weightless and agile, like swimming through frictionless water with jetpacks."
    
    "This, was about as polar opposite as it got. The best way she had been able to explain it in words was- falling into the sky."
    
    "As if gravity had shifted directions, and a huge mass was pulling at you from your destination."
    
    "Any change in direction wasn't controlled, but as if the entire world turned sharply and you were wrenched in that direction, hurtling down- but into empty space rather than the floor."
    
    "Like walking off the roof of a building and falling, but combined with a rollercoaster."
    
    "It was a disconcerting experience for most people, Leyla had discovered. She quite enjoyed it though."
    
    "She imagined that the appeal of skydiving must be quite similar for humans."
    
    "The rush of stepping off of extreme heights wasn't what scared people from doing it, it was the impending knowledge of the ground rushing up to meet you in an excruciating end to the freefall."
    
    "Take that away, and suddenly thousands of thrill-seekers flocked to the experience."
    
    scene black
    with wiperight
    
    pause 1.0
    
    scene bg city3 night falling
    with wiperight
    
    "The city nightscape flew past with a dizzying speed."
    
    "If there was one thing she didn't particularly like about traveling like this, it would be the city skyline."
    
    "In wide open areas, free-falling like this was simple and exhilarating. But in this crowded metropolis, the varied building and high-rises obstructed the path, like craggy rocks reaching up."
    
    "She had to be careful in manuevering to avoid them as she plunged horizontally, and if there was one thing that was difficult about this type of \'flying\', it was manuevering."
    
    "Angling above the high-rises was difficult too. The higher into the sky she went, the harder it became to control her trajectory."
    
    "The howling, sprinting wind from the other side was like an excited dog, and the sky was an open field it wanted to romp through."
    
    "Even at this height, sometimes the wind would try to jerk off course and run off into the void of a night sky above."
    
    "But she held it steady, and far down below, a quiet change began to occur in the city as the park drew near."
    
    scene black
    with wipedown
    
    pause 1.0
    
    play music "music/Strange-Zone_Looping.mp3" fadeout 2.0 fadein 1.0
    
    scene bg city3 night empty
    with wipedown
    
    "As her destination approached, Leyla gradually angled herself towards the ground, wresting the excited winds into a soft, slow breeze."
    
    "And by the time she was within sight of the ground, the city had become a empty, desolate gallery."
    
    "All of the streets were devoid of people and activity."
    
    "It almost seemed as if she had turned into an abandoned part of town, if it weren't for the hectic noise and lights coming from behind, just a few dozen feet away."
    
    "It was like a small bubble of emptiness in the chaotic and boisterous nightlife of the city, quietly engulfing the area around the park."
    
    "Somewhat like when the rain arrived, though on a much smaller scale."
    
    "It didn't force anyone out of the area, but rather people would simply get the urge to take another route, find a club in another area- a reticent suggestion nestled in the back of their mind."
    
    show leyla wind2 with dissolve
    
    "Leyla alighted on the ground once she was far enough into the bubble that no prying eyes would see her land."
    
    "The wind around her gave her a final whiny, tugging her arms lightly upwards, towards the night sky."
    
    show leyla wind4
    
    L "I'm sorry, I have work tonight so I can't play with you."
    
    show leyla wind3
    
    L "Thank you for taking me here though, I'll make sure to find time for a stroll through the sky next time."
    
    "The breeze around her swirled, almost like an animal circling happily, then faded into silence."
    
    stop ambient fadeout 1.0
    
    show leyla smile1
    
    "Without the sound of the wind, the silence of the area fully settled like a heavy blanket."
    
    show leyla neutral
    
    "Leyla glanced behind her at the large clock tower- about five minutes to go still." 
    
    "The park was just around the corner, but it would be troublesome to arrive while Elaine was still around."
    
    "For the time being, she was close enough to do some quick reconnaissance on the anomaly without getting into range of the other humans."
    
    show leyla calm
    
    "Leyla closed her eyes and steadied her breath, reaching out mentally for the familiar tug of energy from the other side."
    
    scene bg city3 night invert
    show leyla calm
    with expandout
    
    "Almost immediately, the area near the park burst out with energy. The swirling forces radiated out before suddenly crashing into the surrounding barrier, collapsing back in on itself."
    
    "It was considerably larger than many of the previous anomalies, another troublesome trend. And given the purity of the energy, unmuddled by human thoughts, it must have appeared very recently."
    
    "She could understand why they were having Sophia contain it. It would've taken an entire unit of their normal grunts to manage it, during a time when they needed manpower elsewhere."
    
    "What she couldn't understand, then and now, was their shortsightedness when it came to actually resolving the issue. This was a large anomaly, but Sophia could have destroyed it on her own easily."
    
    "Some of the other commanders were lenient enough to not nitpick over {i}how{/i} she did it, but Elaine was about as flexible as a steel wall, behind a titanium vault, buried under ten tons of cement...at the bottom of the ocean."
    
    "Any power she perceived as originating from the other side, even if it was being used for their sake, by someone who {i}was{/i} human, was strictly forbidden."
    
    "And so, this situation."
    
    "Shaking off her irritation, Leyla sharped her focus, probing into the barrier. There was a brief resistance, then she was let through when Sophia realized who was trying to get in."
    
    "It also doubled as her arrival announcement to her student."
    
    "An anomaly of this size wasn't, strictly speaking, impossible. However, it would be very difficult for it to appear without a catalyst of some sort."
    
    "Knowing Sophia, she had probably already found whatever it was that first let the anomaly manifest. So her job should simply be to send it back to the other side."
    
    "Luckily, even from this distance, it was obvious that this was a physical anomaly. It had a physical form or force, existed in the world of senses."
    
    "{i}Ousia{/i}, as those from the other side would recognize it, though to the humans it was simply an anomaly. Something that didn't belong on this side."
    
    "Even though if a non-physical anomaly had manifested- one born from a thought, an emotion, or, worst of all, a {i}belief{/i}- it would be magnitudes harder to deal with."
    
    
    
    return
