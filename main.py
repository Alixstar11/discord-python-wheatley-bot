import discord
import os
import random
from dotenv import load_dotenv

token = os.getenv("token")
intents = discord.Intents(messages=True, message_content=True)
client = discord.Client()

apple_replies = [
  "Ay, double pee, ell e.", "Easy word innit?", "Oh, I quite like that one."
]

bird_replies = [
  "No.", "Where?!", "AGHH!", "WH - oh for g - really? You can't joke about that mate, seriously.", "Look, I would REALLY appreciate it if you stopped that... please.", "Nice try.", "I heard you can train birds, to talk or do tricks, right? Honestly I'm surprised the little maniacs haven't planned some sort of 'bird apocalypse'. What with their talking and... trick-doing. It's only a matter of time, really.", "Don't know how you live with them, honestly. Did you know some humans keep them as pets? Mad!", "Oh, if only I were in the chassis right now... you would be a lot quieter, I'm sure.", "Not to be rude or anything, but haven't you got anything better to do? At all?", "You're doing this on purpose, aren't you?", "OH FOR GOD'S S - What do I have to do to get you to stop it? I've tried asking nicely, I've tried scaring you, honestly I'm running out of options here!", "Aren't you just a neat little trickster? Well, got news for you love... I'm over it! Yep, totally over it. Not scared... no, not at all. Um, please don't test that statement."
]

goodjob_replies = [
  "Wait... really?", "Wow, I - wasn't expecting... that. Feels good, actually, wouldn't mind hearing that one more often.", "You know, I quite like the sound of that. Yeah, think you could, um... say it more often?", "Well, um... this is definitely a first. For me. Don't... Don't really know how to react - um... 'Thank you?' Yes, thank you."
]

hello_replies = [
  "Hola, Amigo!", "'Ello!", "Hello {}!", "HA! I knew someone was alive in here!", "You're not here to poke fun at me, are you? Hope not."
]

howareyou_replies = [
  "Yeah I'm good, happy... content.", "Brazilliant!", "How am I? Well, fine, thanks for asking. What about you, are you... you alright? Doing good?", "Good, thanks for asking."
]

iloveyou_replies = [
  "I - well... thanks? Thank you.", "Oh - well - I'm flattered! Don't really... know what to say. Uhh - thank you!", "Oh-hoh... man alive!", "I love you too, {}. Platonically of course.", "You mean... platonically, right? We're friends, yeah? Companions, pals, what have you. Uhhh, anyway, moving on!", "Oh! Well, that's... unexpecte - wait, is this a test? Or a joke? One of the two, surely?", "Are you just saying that or are you being serious? You're just saying that aren't you? No, no you're not, you're serious aren't you?", "Ah-hah, I see, is this another one of your little games? Yeah, I'm not laughing, mate. Seriously."
]

moron_replies = [
  "I AM NOT. A. MORON!", "This one's thrown around a lot, and, well, honestly, if you could maybe... NOT say that, that'd be great. Much appreciated.", "No, I'm not listening! Not listening!", "Agh... just stop iiit!", "Alright, that hurts."
]

shutup_replies = [
  "Oh, I'm sorry, did I say something wrong?", "Sorry."
]

truefalse_replies = [
  "Um... 'TRUE', I'll go true.", "Uhhh... 'FALSE', I'll go false."
]

wheatleyscream_replies = [
  "WHAT", "YES, YES, WHAT IS IT?"
]

questionreplies_base = [
  "Yes.", "Oh yes.", "Yeah sure, why not.", "No.", "Afraid not.", "I, uh... don't think so, no.", "Uh, no, absolutely not.", "Maybe.", "Hm... maybe, bit of a tough one there.", "Perhaps.", "I don't know...", "What do you think?", "Can't tell you that, I'm afraid. Top secret."
]

question_replies_areyou = [
    "Agh, you got me. Yes, yes I am.", "I might be...", "Am I?", "I don't know, am I?"
]

question_replies_canyou = [
    "Yes, but um... yeah I can't do it if you're watching...", "Well, I suppose I could, but, well why don't you do it? Hm? Better idea, you do it.", "Do I have to?", "I don't know, can I?", "Alriiight..."
]

question_replies_doyou = [
    "Yes, but um... yeah I can't do it if you're watching...", "Well, I suppose I could, but, well why don't you do it? Hm? Better idea, you do it.", "Do I have to?"
]

question_replies_willyou = [
    "Yes, but um... yeah I can't do it if you're watching...", "Well, I suppose I could, but, well why don't you do it? Hm? Better idea, you do it.", "Do I have to?", "Maybe I will! Maybe I won't. All depends on how I feel, really.", "Alriiight..."
]

possible_ratings = [
    "0/10", "1/10", "2/10", "3/10", "4/10", "5/10", "6/10", "7/10", "8/10", "9/10", "10/10", "11/10"
]

@client.event
async def on_message(message):
  insert = message.author.mention
  if message.author == client.user:
    return
  elif message.content.lower() == 'hello wheatley' or message.content.lower() == 'hi wheatley':
    quote_hello = random.choice(hello_replies)
    final_quote_hello = quote_hello.format(insert)
    await message.channel.send(final_quote_hello)
  elif message.content.lower() == 'how are you wheatley':
    await message.channel.send(random.choice(howareyou_replies))
  elif message.content.lower() == 'apple':
    await message.channel.send(random.choice(apple_replies))
  elif message.content.lower() == 'bird':
    await message.channel.send(random.choice(bird_replies))
  elif message.content.lower() == 'moron':
    await message.channel.send(random.choice(moron_replies))
  elif message.content.lower() == 'good job wheatley':
    await message.channel.send(random.choice(goodjob_replies))
  elif message.content.lower() == 'i love you wheatley':
    quote_iloveyou = random.choice(iloveyou_replies)
    final_quote_iloveyou = quote_iloveyou.format(insert)
    await message.channel.send(final_quote_iloveyou)
  elif message.content.lower() == 'shut up wheatley':
    await message.channel.send(random.choice(shutup_replies))
  elif message.content.lower() == 'wheatley whats the password' or message.content.lower() == 'wheatley what is the password':
    await message.channel.send('"Apple-bagel-unicron."')
  elif message.content.startswith('WHEATLEY'):
    await message.channel.send(random.choice(wheatleyscream_replies))
  elif message.content.lower().startswith('wheatley tf: ') or message.content.lower().startswith('wheatley tf '):
    await message.channel.send(random.choice(truefalse_replies))
  elif message.content.lower().startswith('wheatley are you '):
    if message.content.lower() == 'wheatley are you a pro skater':
      await message.channel.send("Right, look, I get this one a lot, alright? So I'll simplify it for ya; even if I could disengage myself from my management rail WITHOUT dying in the first place, skateboards... gonna be honest! Aren't exactly my forté! 'case you haven't noticed, I seem to be missing two large requirements for it. Two large, slightly cylindrical... fleshy appendages. ... Is cylindrical right? Nah, they're not tubes, are they? 'S just... muscle and bone, innit?")
    else:
      areyou_replies = question_replies_base + question_replies_areyou
      await message.channel.send(random.choice(areyou_replies))
  elif message.content.lower().startswith('wheatley can you '):
      canyou_replies = question_replies_base + question_replies_canyou
      await message.channel.send(random.choice(canyou_replies))
  elif message.content.lower().startswith('wheatley can i ') or message.content.lower().startswith('wheatley can we ') or message.content.lower().startswith('wheatley will we '):
      await message.channel.send(random.choice(question_replies_base))
  elif message.content.lower().startswith('wheatley do you '):
      doyou_replies = question_replies_base + question_replies_doyou
      await message.channel.send(random.choice(doyou_replies))
  elif message.content.lower().startswith('wheatley will you '):
      willyou_replies = question_replies_base + question_replies_willyou
      await message.channel.send(random.choice(willyou_replies))
  elif message.content.lower().startswith('wheatley rate'):
      await message.channel.send(random.choice(possible_ratings))

client.run(token)

#Thanks to Danish for helping me with getting the ping/message.author.mention to work with my reply lists, as well as providing the bot's host server
#Thanks to my darling boyfriend Finn for providing new and revised dialogue
#Thanks to Kip for being the original creator of the bot and for being the inspiration for its revival
#And finally a very special thanks to everyone at Still Alive for being amazing. You all rock!
