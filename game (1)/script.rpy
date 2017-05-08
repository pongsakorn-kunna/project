﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# image
image sukina_half = "images/sukina/character/sukina_half.png"
image bgblack_sukina = "images/sukina/background/black.png"
image bg1_sukina = "images/sukina/background/bg01.jpg"
image bg2_sukina = "images/sukina/background/bg02.jpg"
image bg3_sukina = "images/sukina/background/bg03.jpg"
image bg4_sukina = "images/sukina/background/bg04.jpg"
image sukina_happy = "sukina_happy.png"
image sukina_mask = "sukina_mask.png"
image sukina_shock = "sukina_shock.png"
image wolf_wall = "wolf_wall.jpg"
image horror_room = "horror_room.jpg"
image horror_room1 = "horror_room1.jpg"
image dark_room = "dark_room.jpg"
image dark_room2 = "dark_room2.jpg"
image dark_room3 = "dark_room3.jpg"
image tk = "city.jpg"
image gang = "gangster.jpg"
image gen_shock = "shock.png"
image gen = "genji.png"
image sni = "sni.png"
image dark_view = "dark_view1.jpg"
image leete_happy = "lol1.png"
image leete_shock = "lol2.png"
image leete_se = "lol4.png"
image door1 = "door1.jpg"
image begin_door = "begin_door.jpg"
image dark_room4 = "dark_room4.jpg"
image bg_1 = "bgA1.jpg"
image bg_2 = "bgA2.jpg"
image ag_1 = "angie_1.png"
image ag_2 = "angie_2.png"
image ag_3 = "angie_3.png"
image sukina_knife = "sukina_knife.png"
image sukina_nork = "sukina_nork.png"
image sukina_kill = "sukina_kill.png"
image ang_kill = "ang_kill.png"
image bgk_1 = "bg_katuai.jpg"
image bgk_2 = "bg_katuai2.jpg"
image k_1 = "tar1.png"
image k_2 = "tar2.png"
image k_3 = "tar3.png"
image house = "house.jpg"
image jail = "jail.jpg"
image ethan = "ethan.png"
image ethan2 = "tuck2.png"
image troll = "troll.jpg"
image tdie = "tdie.jpg"
# name of the character.
define sukina = Character("Sukina", color="#dd7002")
define C_6 = Character("Leete")
define C_4 = Character("Ethan")
define C_3 = Character("Katuai")
define C_2 = Character("Genji")
define C_1 = Character("Sukina")
define C_5 = Character("Angie")
define NPC = Character("Mr.Wolf")
#---------------------------------------- end of definition
define slow = Dissolve(.5)

init:
    $ fade = Fade(.5, 0, .5) # Fade to black and back.
# The game starts here.
screen main_menu:

    tag menu
    imagemap:
        ground 'bg1.jpg'
        hover 'bg2.jpg'
        
        hotspot(1060,309,220,78)action Start()
        hotspot(1060,387,220,87)action ShowMenu("load")
        hotspot(1033,474,247,95)action ShowMenu("preferences")
        hotspot(1060,569,220,96)action Quit(confirm = False)
    
label start:
    ## NPC มาพูด
    play sound "horror_sound.mp3"
    scene wolf_wall with fade
    NPC "ยินดีต้อนรับเข้าสู่เกมส์ ของกระผม "
    NPC "กระผม Mr. wolf"
    NPC "หลายๆคนคงจะสงสัยว่าทำไมอยู่ดีๆถึงมาอยู่ที่นี้"
    NPC "เพราะว่า "
    NPC "ถ้าพวกคุณมาอยู่ที่นี้แล้วแสดงว่าคุณมันคือ เศษขยะสังคม"
    NPC "ไม่ๆ ไม่สิ เรียกเศษขยะสังคมยังไม่ได้ เลย ฮ่า ฮ่า ฮ่า"
    NPC "ขอโทษครับผมอาจจะพูดแรงไปหน่อย"
    NPC "ล้อเล่นหน่ะครับ ฮ่า ฮ่า ฮ่า "
    NPC "ที่พวกคุณมาอยู่ที่นี้ เพราะว่า มีคนโหวดพวกคุณมาให้อยู่ร่วมสนุกกับเกมส์ของผม "
    NPC "ผู้ที่เหลือรอดจะมีเพียง 1 คนเท่านั้นซึ่ง คนคนนั้นจะได้รับรางวัล"
    NPC "คือการปล่อยตัวออกจากที่นี้ "
    NPC "ส่วนคนที่แพ้หน่ะหรอครับ "
    NPC "อ๊ะๆ !! ดูก่อนครับ ที่คอของพวกท่านจะมีชิพ ฝังอยู่"
    NPC "ซึ่งชิพนั้นจะมี พิษของงู ไทปัน ถ้าหากคุณถูกโหวดให้แพ้ หรือ ใน 1 วันไม่มีใครตาย "
    NPC "ทางเราจะขอสุ่มผู้ โชคดีที่จะได้เพลิดเพลินกับ พิษตัวนี้ นะครับ ฮ่า ฮ่า อ่า"
    NPC "ขอให้สนุกนะครับ"
    scene horror_room 
    ##.........................................................ของโอ
    ## เล่าเรื่องว่าจาก 100 คน เหลือ อยุ่ 7 คน
    "วันแล้ววันเล่า"
    "ก็มีคนตายเรื่อยๆ ทุกคนก็ได้แต่หวังว่าวันนี้จะไม่ใช่เรา"
    "และใช้ชีวิตอยู่แบบหวาดระแวง"
    "จนเหลืออยู่ 7คนสุดท้าย"
    stop sound fadeout 1
    ##ประหวัติ
    "คนแรก Sukina"
    scene bg1_sukina with fade
    show sukina_happy at right
    play sound "sukina_music1.mp3" noloop fadein 5 fadeout 5

    "สุกินะ..."
    sukina "ชื่อของผม.. คือ 'สุกินะ'"
    sukina "คนอื่นๆในชั้นเรียนมักกลัวผม"
    sukina "เพียงเพราะผม แค่ทักทายพวกเขา.. ด้วยวิธีของผม"
    sukina "ก็อาจมีใช้กำลังบ้างในบางครั้ง "
    show sukina_happy at left
    sukina "คนพวกนี้มันโง่ พอผมเห็นแล้วก็อดจะชกหน้าไม่ได้"
    sukina "..."
    sukina "แต่ก็ไม่มีใครกล้ายุ่งอะไรกับผมหรอก เพราะอะไรนะ"
    sukina "อาจเพราะพ่อผมเป็นประธานของบริษัทใหญ่ และมีอำนาจไงหละ"
    sukina "พวกมันเลยกลัวผมฟ้องพ่อ แล้วจะโดนทำร้าย "
    sukina "เคยมีคนมาลองดีแล้ว ตอนนี้หรอ..."
    sukina "มันโดนฝังไปแล้ว.."
    stop sound fadeout 1
    scene bgblack_sukina with fade
    ##........................................................จบ
    "คนที่สอง Genji"
    play sound "CloZee - Koto.mp3"
    scene gang with fade
    show gen
    "Genji เป็นหัวหน้าอาชญากรที่มีอิทธิพลมากที่สุดในญี่ปุ่น"
    "องค์กรของเขาครอบคลุมธุรกิจทุกอย่างในเขตโตเกียว "
    with slow
    scene tk with fade
    show gen
    "ทั้งการการค้ายาเสพติด การส่งออกน้ำมัน สถานบันเทิง การพนันผิดกฎหมาย และการค้าโสเภณี"
    "และด้วยการขัดผลประโยชน์ทางธุรกิจกับแก๊งค์อื่น"
    show sni
    " จึงทำให้หลายองค์กรอยากกำจัดเขา"
    scene bgblack_sukina with fade
    stop sound fadeout 1
    ##........................................................จบ
    "คนที่สาม Katuai"
    play sound "PETIT BISCUIT - Alone.mp3"
    scene bgk_1 with fade 
    show k_1 at right
    "Katuai เป็นเด็กน้อยใสซื่อบริสุทธิ์"
    "เขาอาศัยอยู่ในป่าตัวคนเดียว เพราะพ่อแม่ของเขาแยกทางกันแล้วทิ้งเขาไว้ที่กระท่อมนั้นคนเดียว"
    "เขามีชีวิตรอดมาทุกวันนี้เพราะเขาเก็บของป่า กินมาโดยตลอด"
    stop sound fadeout 1.5
    play sound "Thunder & Lightning Sound Effects [High Quality].mp3"
    "แต่แล้ว"
    scene bgk_2 with fade
    stop sound fadeout 1
    play sound "Vincent - Her.mp3"
    show k_2    
    "โชคชะตาก็เล่นตลก อยู่ดีๆ Katuai ก็โดนตำรวจจับข้อหาบุกรุกพื้นที่ป่าสงวน"
    "และเขาไม่สามารถสู้คดีได้เลย"
    scene bgk_2 with fade 
    show k_1
    "เพราะเขาเป็นคนใสซื่อมากๆ เขาได้ดูดซับนิสัยเลวๆในคุกมามากจนเขา พลั้งมือ ฆ่าทักโทษในคุกเป็นจำนวนมาก"
    "จนทำให้ผู้คุม ถึงกับทำอะไรไม่ได้หรือนี้อาจจะเป็นเหตุผลที่ทำให้เขามาอยู่ในเกมส์นี้ก็เป็นได้"
    stop sound fadeout 1
    scene bgblack_sukina with fade
    ##........................................................จบ
    "คนที่สี่ Ethan"
    play sound "Sadness.mp3"
    scene house with fade
    show ethan
    "Ethan คือ ลูกของบ้านเศรษฐีหลังนี้ พ่อทำงานเกี่ยวข้องกับธุรกิจมืด และเป็นผู้มีอิทธิพลในเมืองแห่งนี้"
    "ทุกคนในบ้านล้วนมีงานอดิเรกแปลกๆ รวมถึง Ethan"

    scene jail with fade
    show ethan at left
    "ใต้บ้านของEthanมีห้องขัง ที่ใช่ทารุณกรรม ทรมาณลูกหนี้ของพ่อ Ethan"
    "ซึ่ง Ethan มีหน้าที่ทรมาณลูกหนี้ของพ่อนั้นเอง"
    "ทำให้ทุกคนในบ้านนี้ล้วนโดนหมายหัวจากผู้ที่โกรธแค้นในการกระทำของบ้านนี้"
    stop sound fadeout 1
    scene bgblack_sukina with fade
    ##........................................................จบ
    "คนที่ห้า Angie"
    play sound "EXGF - We Are The Hearts.mp3"
    scene bg_1 
    show ag_1 at left
    #play sound "TokyoGhoul.mp3" fadein 1
    "Angie เป็นผู้หญิงที่มีรูปร่างที่สวยงาม และมีฐานะที่ร่ำรวย"
    "จึงมีชายหนุ่มที่เข้าหา Angie เป็นจำนวนมาก "
    "แต่ชายหนุ่มที่เข้ามาจีบ Angie ทุกคนนั้นหายตัวไปอย่งลึกลับ ไม่มีใครรู้ว่าหายไปไหน"
    with slow
    
    #2
    scene bg_2 
    show ag_2 at right
    "Angie จึงตกเป็นผู้ต้องสงสัยในการหายตัวไปของชายหนุ่มพวกนั้น และถูกเชิญไปให้ปากคำกับตำรวจหลายรอบ"
    "แต่ก็ไม่มีหลักฐานที่บ่งบอกว่า Angie เป็นคนทำ "
    "Angie จึงรอดจากข้อกล่าวหา"
    stop sound fadeout 1
    ##........................................................จบ
    play sound "Horror Piano Theme.mp3"
    scene bgblack_sukina with fade
    "คนที่หก Leete"
    scene dark_view with fade
    show leete_happy
    "Leete เธอคือสายลับที่ถูกส่งมาทำภาระกิจเพื่อตามหาตัวตนที่แท้จริงของ Mr.wolf"
    "ก่อนที่เธอจะเข้ามารับภาระกิจนี้ เธอถูกหมั่นใส้โดยเพื่อนร่วมงานเพราะเหตุผลที่ว่า...."
    "เธอชอบทำตัว เลียแข่งเลียขาของผู้ใหญ่ผู้โตจนทำให้หลายๆคนหมั่นใส้"
    "และนั้นอาจจะเป็นเหตุผลที่เธอถูกหลอกเข้ามารับภาระกิจนี้ก็เป็นได้ ....."
    stop sound fadeout 1
    #ประหวัติ
    ##........................................................จบ
    
    ##........................................................จบเกริ่น
  
    #----------------------------------------จบตัวละคร
    ## ใส่ชื่อของ User 
    play sound "Petit Biscuit - Jungle (Official Audio).mp3"
    scene bgblack_sukina
    "และคนที่เจ็ด"
    $ player_name = renpy.input("Input your name:")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name="Hideko"
    stop sound fadeout 1.5
    ##........................................จบใส่ชื่อ  
    
    ## ตัวละคร คนที่6 ตาย
    play music "Dark Ambient Playlist.mp3"
    
    scene horror_room with fade #หาฉากมาเปลี่ยน
    "ณ ขณะที่ทุกคนกำลังใช้ชีวิติประจำวันนั้น"
    NPC "อ๊ะ อ้าวววว ไม่มีใครตายเลยหนิ งั้นวันนี้ เอาอีกละกันเนอะครับ"
    NPC "ฮ่า ฮ่า ฮ่า"
    play sound "Woman screaming - Sound Effect.mp3"
    scene horror_room1 
    C_6 "อ๊าก!!!!"
    C_6 "ช่วยด้วย!!!!!"
    stop sound fadeout 2
    play sound "Sad Violin - MLG Sound Effects (HD).mp3"
    "ทุกๆคนได้แต่มอง Leete ตาย โดยที่ไม่สามารถช่วยอะไรได้"
    "......."
    "สุดท้ายก็ไม่มีใครสามารถช่วย Leete ได้"
    stop sound fadeout 1
    ##.......................จบ 
    ## ตัวเลือกแรก ให้เลือกว่าอยากได้  partner เป็นใคร หรือไม่มีก็ได้ ให้ทำ ตัวเลือกมา 
    scene dark_room with fade
    #โชว์ตัวละครหน้าเครียด 2-3 ตัว
    "ทุกคนกำลังตกอยู่ในช่วงจิตตกอย่างหนักอยู่ที่คุณแล้วว่า"
    scene dark_room with fade
    "%(player_name)s คุณจะเลือกอยู่กับใคร (เลือกเพื่อ ชนะเกมส์)"
    menu:           ##ใส่ชื่อแทนเลข 1 2 3 4 5 เอาว่า user จะเลือกคู่กับใคร
        "Sukina กับ Genji ":
            jump continue_1
        "Katuai กับ Ethan ":
            jump continue_1
        "Angie":
            jump continue_1
        "อยู่ด้วยตัวคนเดียว ":
            jump continue_1
    ## อย่าลืมบอกอิมทำตัวเลือกที่ User ไม่อยากอยุ่กับพวกนี้
    ##.......................................จบตัวเลือกแรก
label continue_1:
    scene dark_room2 with fade
    ## เล่าเรื่องต่อ บอกว่า คนที่ 4 ตาย เกิดปัญหา ทุกคนไม่เชื่อ คนที่ 3
    "หลังจากเหตุการณ์ที่ Leete ตาย"
    show sukina_happy
    "Sukina ก็ได้คิดแผนที่อยากจะออกไปจากที่นี้ โดย การจับกลุ่มกัน"
    C_1 "ฉันว่านี้มันมากเกินพอแล้วนะ"
    C_1 "ช่วยกันหาทางออกและหาที่กบดานของไอ่ Mr. wolf  เถอะ"
    C_1 "ทุกคนจะได้รอด แล้วเกมส์บ้านี่ จะได้จบๆซะที"
    scene dark_room2 with fade 
    "แต่แล้วในขณะที่ทุกคนกำลังหาทางออก และเบาะแสของ Mr.Wolf "
    "ก็ได้เกิดเหตุการณ์ไม่คาดฝันขึ้น"
    scene dark_room3 with fade
    play sound "Crash.mp3"
    ""
    ""
    stop sound fadeout 0
    play sound "Terrifying Female Scream Sound Effect.mp3"
    C_4 "โอ้ย !!!! "
    stop sound fadeout 1
    play sound "Running Sound Effect.mp3"
    scene dark_room2 with fade
    stop sound fadeout 0
    ""
    show sukina_shock
    show gen_shock at right
    show ag_2 at left
    "ทุกคนก็รีบมุ่งหน้าไปที่เสียงนั้น"
    scene tdie with fade
    "แต่แล้วก็ได้พบกับ ร่างของ Ethan"
    ""
    scene dark_room
    show k_1
    "ทุกคนก็ได้มุงสายตาไปที่ Katuai"    
    "เพราะว่าทั้งสองคนอยู่ในพื้นที่ใกล้ๆกันขณะช่วยกันหาเบาะเเส" 
    ##........................................จบเล่า
    ## ทำตัวเลือก ให้Userว่า จะเลือกเชื่อ 3 หรือไม่เชื่อ 
    scene dark_room
    show k_2
    C_3 "ผมไม่ได้ทำนะครับเชื่อผมสิ"
    "ถึง Katuai จะพูดไปแบบนั้นแต่มันก็ไม่ได้ทำให้ทุกคนเชื่อเลย "  
    "Katuai เข้ามาหาคุณ"
    C_3 "%(player_name)s ฉันไม่ได้ทำนะเชื่อฉันเถอะ"
    menu :
        "%(player_name)s อยู่ที่คุณแล้ว จะเชื่อ หรือ ไม่เชื่อ Katuai เขาอาจจะไม่ใช่คนร้ายก็ได้นะคิดดีๆ"
        "จำนวนคนที่น้อยลง ยิ่งทำให้คุณเสี่ยง"
        "ฉันเชื่อเขา":
            jump continue_2_1
        "ขอโทษนะฉันไม่เชื่อใจนาย":
            jump continue_2_2
    ##.......................................จยตัวเลือก 
    ## ผ่านไปอีกคืน คนที่ 2 ตาย 
    ##เล่าเรื่องเมื่อเลือก เชื่อ 
label continue_2_1:
    scene dark_room with fade
    "หลังจากที่คุณได้บอกว่าเชื่อ Katuai ก็เข้ามาหาคุณแล้วพูดว่า...."
    show k_1
    C_3 "ขอบคุณนะที่เชื่อใจฉัน"
    C_3 "ฉันไม่ได้ทำจริงๆดังนั้นฉันไม่ใช่ ฆาตกรแน่นอน"
    
    ##เล่าเรื่องต่อ ว่า 3 โดนฆ่า
    scene bgblack_sukina with fade
    "หลังจากคืนที่ Ethan ตาย "
    "ก็ไม่มีใครตายเพราะเป็นไปตามกฎของ Mr. wolf ว่า...."
    "ทุกคืนจะต้องมีคนตาย"
    "พอรุ่งเช้า ทุกคนก็ได้แยกย้ายหาเบาะแสอีกครั้ง"
    scene dark_room4 with fade
    ""
    ""
    "ขณะที่ทุกคนกำลังหาเบาะเเสอยู่นั้นก็ได้มีเสียงดังเกิดขึ้น"
    play sound "Windshield_Hit_With_Bar.mp3"
    ""
    stop sound fadeout 0
    play sound "Man screaming sound effect 1.mp3"
    C_3 "โอ้ย !!!!! "
    C_3 "อย่า..อย่าทำ....ผม "
    C_3 "................"
    stop sound fadeout 0.5
    play sound "Running Sound Effect.mp3"
    ""
    ""
    "ทุกคนต่างก็วิ่งไปหาที่มาของเสียงนั้นพอไปถึง...."
    stop sound fadeout 0
    show gen
    show ag_2 at right
    show sukina_shock at left
    scene dark_room4
    ""
    show k_3
    "คุณได้แต่ยืนมอง Katuai ตายด้วยความสงสาร ทั้งๆที่คนที่เหลือมองด้วยความหวาดกลัว"
    "ว่าใครจะเป็นคนต่อไป แล้วใครหล่ะคือ ฆาตกรตัวจริง......."
    scene bgblack_sukina with fade
    jump continue_3 #ตายเสร็จ กลับสู่เนื้อเรื่องหลัก
   ##เล่าเรื่องเมื่อเลือก ไม่เชื่อ 
label continue_2_2:
    scene dark_room with fade
    show k_2
    C_3 "แล้วนายจะรู้ว่าเลือกอะไรลงไป !! "
    scene bgblack_sukina with fade
    "หลังจากคืนที่ Ethan ตาย "
    "ก็ไม่มีใครตายเพราะเป็นไปตามกฎของ Mr. wolf ว่า...."
    "ทุกคืนจะต้องมีคนตาย"
    "พอรุ่งเช้า ทุกคนก็ได้แยกย้ายหาเบาะแสอีกครั้ง"
    scene dark_room4 with fade
    ""
    ""
    "ขณะที่ทุกคนกำลังหาเบาะเเสอยู่นั้นก็ได้มีเสียงดังเกิดขึ้น"
    play sound "Windshield_Hit_With_Bar.mp3"
    ""
    stop sound fadeout 0
    play sound "Man screaming sound effect 1.mp3"
    C_3 "โอ้ย !!!!! "
    C_3 "อย่า..อย่าทำ....ผม "
    C_3 "ฉันว่าแล้ว....ต้องเป็นนา........."
    C_3 "..................................."
    stop sound fadeout 1
    play sound "Running Sound Effect.mp3"
    "ทุกคนต่างก็วิ่งไปหาที่มาของเสียงนั้นพอไปถึง...."
    scene dark_room4 with fade
    stop sound fadeout 0
    show gen
    show ag_2 at right
    show sukina_shock at left
    scene dark_room4 
    ""
    show k_3
    "คนที่เหลือได้แต่ยืนมอง Katuai ตายไป ต่อหน้าต่อตาโดยที่ทำอะไรไม่ได้เลย"
    "เมื่อ Katuai ตายแล้ว ใครหล่ะ คือฆาตกรตัวจริง....."
    scene bgblack_sukina with fade
    jump continue_3 #ตายเสร็จ กลับสู่เนื้อเรื่องหลัก
   ##.................................จบเล่าเรื่อง
label continue_3:
    scene bgblack_sukina with fade
    "หลังจากผ่านคืนที่เเสนเศร้านั้นไป "
    scene dark_room2 with fade
    "พอรุ่งเช้าทุกคนก็ต้องจำใจแยกไปหาเบาะแสต่อ"
    "ทันใดนั้น Angie ก็เข้ามาถามคุณว่า......"
    show ag_1
    C_5 "%(player_name)s ให้ฉันอยู่กับคุณได้ไหม"
    menu:
        C_5 "ฉันไม่ไว้ใจไอ่ Sukina นั้นเลย......."
        "เอาสิ":
            jump continue_4_1
        "ไม่หล่ะขอบใจ":
            jump continue_4_2
    ##..............................จบ ตัวเลือก 
label continue_4_1: ##รับ 5,   1 ตาย
    scene dark_room2 with fade
    show ag_1
    C_5 "ขอบใจนะนายนี้น่าเชื่อถือที่สุดแล้ว"
    scene dark_room2
    "ทุกคนก็แยกย้ายไปตามปกติ"
    "ทันใดนั้นก็ได้ยินเสียงดังออกมา"
    scene begin_door with fade
    play sound "Small_Glass_Pane_Shatter.mp3"
    ""
    stop sound fadeout 0
    play sound "Man screaming sound effect 1.mp3"
    "โอ้ยยย !!!! "
    "มันเป็นเสียงดังจากในห้องห้องหนึ่ง"
    stop sound fadeout 1
    scene door1 with fade
    scene door1
    show ag_2
    play sound "Running Sound Effect.mp3"
    ""
    "พอคุณวิ่งมาถึงหน้าห้อง คุณพบกับ Angie"
    stop sound fadeout 0
    C_5 "ฉันได้ยินเสียงของ Sukina ดังมาจากในห้องหน่ะ"
    menu:
        C_5 "ประตูมันล๊อกด้วย นายช่วยเป็นคนผลักประตูให้ ฉันหน่อยได้ไหม?"
        "หลีกไปฉันทำเอง":
            jump continue_end_1
        "ไม่หล่ะฉันขอรอตรงนี้ดีกว่า":
            jump continue_end_2
label continue_end_1:
    #เล่าเรื่อง เมื่อเปิดประตู
    #userตาย 5รอด
    scene door1 with fade
    "คุณได้ พุ่งเข้าหาประตูอย่างแรง"
    play sound "Glass_Windows_Breaking.mp3"
    "ประตูพังลง"
    scene bgblack_sukina with fade
    stop sound fadeout 0
    play sound "sound_knife.mp3"
    "แต่แล้วคุณก็ถูกมีดที่อยู่บนประตูลงมา เสียบเข้ากลางหัว..."
    "ฉึบ !! "
    stop sound fadeout 0
    stop music fadeout 1
    scene troll
    play sound "Funny Laugh SOUND EFFECT.mp3"
    "ขอเเสดงความเสียใจด้วยนะครับ คุณไม่รอด "
    "ดังนั้นผู้ที่ clear เกมส์นี้ได้คือ Angie"
    "ขอแสดงความยินดีกับเขาด้วยนะครับ"
    "....You Die...."
    stop sound fadeout 0
    jump ending_1 #จบเกม
label continue_end_2:
    #เล่าเรื่อง เมื่อ   ไม่เปิดประตู
    # 5ตาย user รอด
    scene door1 with fade
    show ag_3
    C_5 "ชิ !!"
    "Angie ไม่พอใจคุณ"
    "คุณเดินกลับไป หาเบาะเเสของคุณต่อ แต่ แล้ว"
    play sound "Terrifying Female Scream Sound Effect.mp3"
    scene door1 with fade 
    show ang_kill
    " Angie ก็พุ่งเข้ามาจะเอามีดเสียบคุณ"
    stop sound fadeout 0
    menu:
        "หลบ":
            jump end_1
        "รับมีดนั้นไว้ ด้วยความกล้า":
            jump end_2
label end_1:
    scene bgblack_sukina with fade
    "หลังจากที่คุณกลิ้งหลบ"
    play sound "Object_Toss_and_Smash_Glass.mp3"
    "หัวคุณไปโดน ก้อนหินทำให้คุณสลบและถูกฆ่าในที่สุด"
    stop sound fadeout 0
    stop music fadeout 1
    scene troll
    play sound "Funny Laugh SOUND EFFECT.mp3"
    "ขอเเสดงความเสียใจด้วยนะครับ คุณไม่รอด "
    "ดังนั้นผู้ที่ clear เกมส์นี้ได้คือ Angie"
    "ขอแสดงความยินดีกับเขาด้วยนะครับ"
    "....You Die...."
    stop sound fadeout 0
    jump ending_1 
label end_2:
    scene bgblack_sukina with fade
    "คุณรับมีดนั้นด้วยความกล้าหาญ"
    "และได้ สวนมีดนั้นกลับไป "
    play sound "sound_knife.mp3"
    "ฉึก !!! "
    stop sound fadeout 0
    "Angie ตาย ทำให้คุณเป็นฝ่ายชนะเกมส์นี้"
    "ยินดีด้วยนะครับ"
    ".......You win......."
    jump ending_2 
label end_3:
    stop sound fadeout 0
    play sound "Object_Toss_and_Smash_Glass.mp3"
    "หลังจากที่คุณหลบ"
    stop sound fadeout 0
    scene door1 with fade
    show sukina_kill
    "Sukina พยายามพุ่งมาทำร้ายคุณ"
    scene bgblack_sukina with fade
    "แต่แล้วก็เกิดเหตุไม่คาดฝันขึ้น"
    ""
    play sound "Small_Glass_Pane_Shatter.mp3"
    scene door1 with fade
    stop sound fadeout 0
    show sukina_nork
    "อยู่ดีๆ Sukina ก็ หมดสะติและล้มลง"
    scene door1 
    show gen 
    C_2 "ฉันเจอเบาะแสของ Mr.wolf แล้ว ไปกันเถอะ %(player_name)s "
    jump ending_3
label continue_4_2: ##ไม่รับ 5, 1 ฆ่า 5
    scene dark_room2 with fade
    show ag_3
    C_5 "น่าเสียดายนะ เห้ออออ"
    "แล้วทุกคนก็แยกย้ายไปตามปกติ"
    scene dark_room2 
    "ทันใดนั้นก็ได้ยินเสียงดังออกมา"
    play sound "Terrifying Female Scream Sound Effect.mp3"
    "โอ้ยยย !!!! "
    "มันเป็นเสียงดังจากในห้องห้องหนึ่ง"
    stop sound fadeout 0
    play sound "Running Sound Effect.mp3"
    "พอคุณวิ่งมาถึงหน้าห้อง คุณพบกับ Sukina"
    scene door1 with fade
    stop sound fadeout 0
    show sukina_knife
    "ในมือของ Sukina นั้นมี มีดอยู่"
    
    C_1 "Angie พยายามจะทำร้ายฉัน ฉันแค่ปกป้องตัวเองเท่านั้นเองนะ"    
    menu: 
        "ฉันไม่เชื่อใจใครอีกแล้ว !!! ":
            jump continue_end_3
        "ปล่อยผ่านไปเพราะคิดว่าเป็นการป้องกันตัว":
            jump continue_end_4
label continue_end_3:
    scene door1 with fade
    ##show sukina พุ่ง 
    "Sukina พุ่งเข้ามาทำร้ายคุณด้วยความหวาดกลัว"
    show sukina_kill
    play sound "Terrifying Female Scream Sound Effect.mp3"
    menu:
        "หลบ":
            jump end_3
        "รับมีดนั้นไว้ ด้วยความกล้า":
            jump end_4

label end_4:
    stop sound fadeout 0
    scene bgblack_sukina with fade
    "คุณรับมีดนั้นด้วยความกล้าหาญ"
    "และได้ สวนมีดนั้นกลับไป "
    play sound "sound_knife.mp3"
    "ฉึก !!! "
    stop sound fadeout 0
    "Sukina ตาย ทำให้คุณเป็นฝ่ายชนะเกมส์นี้"
    "ยินดีด้วยนะครับ"
    ".......You win......."
    jump ending_2 
    
label continue_end_4:
    #ปล่อย 1 ไว้ 
    #เล่าเรื่องต่อ ผ่านไป 1 คืนจะมีคนตาย
    scene door1 with fade
    "หลังจากคุณปล่อย Sukina ไป"
    "ทุกคนก็พยายามเร่งเพื่อที่จะหาเบาะเเส สานไปถึง Mr. wolf "
    "แต่แล้วก็หาไม่ทัน ถึงเวลาสุ่มตัวผู้โชคดีที่ได้รับ พิษ"
    ""
    "และผู้โชคดีก็คือ คุณนั้นเอง !!! "
    stop music fadeout 1
    scene troll
    play sound "Funny Laugh SOUND EFFECT.mp3"
    "ดังนั้นผู้ที่ Clear เกมส์นี้ได้คือ Sukina"
    "ขอแสดงความยินดีกับเขาด้วยนะครับ"
    "....You Die...."
    stop sound fadeout 1
    jump ending_1
    
    
label ending_1: #ทำเพื่อให้เกมเชื่อมไปจบได้ ไม่ Error
    "....Bad end...."
    stop music fadeout 1
    jump end
label ending_2:
    "....Good end...."
    stop music fadeout 1
    jump end
label ending_3:
    "To be continue......"
    stop music fadeout 1
    jump end
label end:
    scene bgblack_sukina with fade
    $ renpy.movie_cutscene("ending720.mpg")
    
    return
