@namespace
class SpriteKind:
    Selecter = SpriteKind.create()
    KOJAI = SpriteKind.create()

def on_right_pressed():
    kojai_selector.x += 32
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_menu_pressed():
    for index in range(5):
        kojai_text.set_outline(1, 2)
        pause(100)
        kojai_text.set_outline(1, 4)
        pause(100)
        kojai_text.set_outline(1, 5)
        pause(100)
        kojai_text.set_outline(1, 7)
        pause(100)
        kojai_text.set_outline(1, 8)
        pause(100)
        kojai_text.set_outline(1, 10)
        pause(100)
    kojai_text.set_outline(0, 0)
controller.menu.on_event(ControllerButtonEvent.PRESSED, on_menu_pressed)

def KOJAI_BackSpace():
    global kojai_list, kojai_conlist, kojai_KariText, kojai_inputedText
    kojai_list = []
    kojai_conlist = 0
    for index2 in range(len(kojai_inputedText) - 1):
        kojai_conlist += 1
        kojai_KariText = "" + kojai_KariText + kojai_inputedText.char_at(kojai_conlist)
    kojai_inputedText = kojai_KariText

def on_c_pressed():
    kojai_selector.say("" + str(kojai_selector.x) + ", " + str(kojai_selector.y))
controller.C.on_event(ControllerButtonEvent.PRESSED, on_c_pressed)

def KOJAI_remenb():
    pass
def KOJAI_NewBackSpace():
    global kojai_OldText, kojai_inputedText, kojai_conlist
    kojai_OldText = kojai_inputedText
    kojai_inputedText = ""
    kojai_conlist = 0
    for index3 in range(len(kojai_OldText) - 1):
        kojai_inputedText = "" + kojai_inputedText + kojai_OldText.char_at(kojai_conlist)
        kojai_conlist += 1
def KOJAI_reset_to_board():
    color.set_color(1, color.rgb(255, 255, 255))
    scene.set_tile(2, assets.image("""
        a
    """), False)
    scene.set_tile(4, assets.image("""
        ka
    """), False)
    scene.set_tile(5, assets.image("""
        sa
    """), False)
    scene.set_tile(7, assets.image("""
        ta
    """), False)
    scene.set_tile(9, assets.image("""
        na
    """), False)
    scene.set_tile(11, assets.image("""
        ha
    """), False)
    scene.set_tile(6, assets.image("""
        ma
    """), False)
    scene.set_tile(8, assets.image("""
        ya
    """), False)
    scene.set_tile(10, assets.image("""
        ra
    """), False)
    scene.set_tile(3, assets.image("""
        Space
    """), False)
    scene.set_tile(15, assets.image("""
        ModeChange
    """), False)
    scene.set_tile(12, assets.image("""
        Backspace
    """), False)
    scene.set_tile(13, assets.image("""
        Enter
    """), False)
    scene.set_tile(14, assets.image("""
        Left
    """), False)
    scene.set_tile(1, assets.image("""
        Right
    """), False)
    color.set_color(2, color.rgb(255, 100, 100))
    color.set_color(7, color.rgb(125, 255, 125))
    color.set_color(13, color.rgb(255, 255, 125))
    color.set_color(4, color.rgb(255, 200, 125))
def KOJAI_CovertToList():
    pass

def on_down_pressed():
    kojai_selector.y += 32
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def KOJAI_remenb2():
    pass

def on_left_pressed():
    kojai_selector.x += -32
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def KOJAI_Dakuten():
    global kojai_OldText, kojai_inputedText, kojai_conlist
    kojai_OldText = kojai_inputedText
    kojai_inputedText = ""
    kojai_conlist = 0
    for index4 in range(len(kojai_OldText) - 1):
        kojai_inputedText = "" + kojai_inputedText + kojai_OldText.char_at(kojai_conlist)
        kojai_conlist += 1
    if kojai_OldText.char_at(len(kojai_OldText) - 1) == "か":
        kojai_inputedText = "" + kojai_inputedText + "が"
    elif kojai_OldText.char_at(len(kojai_OldText) - 1) == "き":
        kojai_inputedText = "" + kojai_inputedText + "ぎ"
    elif kojai_OldText.char_at(len(kojai_OldText) - 1) == "く":
        kojai_inputedText = "" + kojai_inputedText + "ぐ"
    elif kojai_OldText.char_at(len(kojai_OldText) - 1) == "け":
        kojai_inputedText = "" + kojai_inputedText + "げ"
    elif kojai_OldText.char_at(len(kojai_OldText) - 1) == "こ":
        kojai_inputedText = "" + kojai_inputedText + "ご"
    elif False:
        pass
    elif False:
        pass
    elif False:
        pass
    elif False:
        pass
    elif False:
        pass
    else:
        pass

def on_b_pressed():
    KOJAI_NewBackSpace()
    kojai_text.x += 24
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def KOJAI_InputText(inputext: str):
    global kojai_inputedText, kojai_typemode
    kojai_inputedText = "" + kojai_inputedText + inputext
    print(kojai_inputedText)
    kojai_text.x += -24
    kojai_typemode = 0
    KOJAI_reset_to_board()

def on_up_pressed():
    kojai_selector.y += -32
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

"""

type

0 = ひらがな

1 = カタカナ

2 = Alphabet

3 = 数字 123

4 = 記号 @_-/

"""
# How2typemode
# 
# 0 = 初期状態
# 
# 1 = "あ"を押した状態
# 
# 2 = "か"を押した状態
# 
# 3 = "い"を押した... と続いていく

def on_a_pressed():
    global kojai_type, kojai_typemode, kojai_KOJAI2
    if kojai_selector.x == 16 and kojai_selector.y == 113:
        kojai_type += 1
        if kojai_type == 5:
            kojai_type = 0
    if kojai_selector.x == 16 and kojai_selector.y == 49:
        KOJAI_InputText(" ")
    if kojai_typemode == 0:
        if kojai_selector.x == 80 and kojai_selector.y == 81:
            kojai_typemode = 5
            KOJAI_remenb()
            color.set_color(1, color.rgb(200, 230, 255))
            scene.set_tile(2, assets.image("""
                na
            """), False)
            scene.set_tile(4, assets.image("""
                ni
            """), False)
            scene.set_tile(5, assets.image("""
                nu
            """), False)
            scene.set_tile(7, assets.image("""
                ne
            """), False)
            scene.set_tile(9, assets.image("""
                no
            """), False)
            scene.set_tile(11, assets.image("""
                Blank
            """), False)
            scene.set_tile(6, assets.image("""
                Blank
            """), False)
            scene.set_tile(8, assets.image("""
                Blank
            """), False)
            scene.set_tile(10, assets.image("""
                Blank
            """), False)
        if kojai_selector.x == 80 and kojai_selector.y == 113:
            kojai_typemode = 8
            KOJAI_remenb()
            color.set_color(1, color.rgb(200, 230, 255))
            scene.set_tile(2, assets.image("""
                ya
            """), False)
            scene.set_tile(4, assets.image("""
                chi
            """), False)
            scene.set_tile(5, assets.image("""
                tsu
            """), False)
            scene.set_tile(7, assets.image("""
                Blank
            """), False)
            scene.set_tile(9, assets.image("""
                Blank
            """), False)
            scene.set_tile(11, assets.image("""
                Blank
            """), False)
            scene.set_tile(6, assets.image("""
                i
            """), False)
            scene.set_tile(8, assets.image("""
                ra
            """), False)
            scene.set_tile(10, assets.image("""
                i
            """), False)
        if kojai_selector.x == 48 and kojai_selector.y == 81:
            kojai_typemode = 4
            KOJAI_remenb()
            color.set_color(1, color.rgb(200, 230, 255))
            scene.set_tile(2, assets.image("""
                ta
            """), False)
            scene.set_tile(4, assets.image("""
                chi
            """), False)
            scene.set_tile(5, assets.image("""
                tsu
            """), False)
            scene.set_tile(7, assets.image("""
                te
            """), False)
            scene.set_tile(9, assets.image("""
                to
            """), False)
            scene.set_tile(11, assets.image("""
                Blank
            """), False)
            scene.set_tile(6, assets.image("""
                Blank
            """), False)
            scene.set_tile(8, assets.image("""
                Blank
            """), False)
            scene.set_tile(10, assets.image("""
                Blank
            """), False)
        if kojai_selector.x == 112 and kojai_selector.y == 49:
            KOJAI_remenb()
            kojai_typemode = 3
            color.set_color(1, color.rgb(200, 230, 255))
            scene.set_tile(2, assets.image("""
                sa
            """), False)
            scene.set_tile(4, assets.image("""
                si
            """), False)
            scene.set_tile(5, assets.image("""
                su
            """), False)
            scene.set_tile(7, assets.image("""
                se
            """), False)
            scene.set_tile(9, assets.image("""
                so
            """), False)
            scene.set_tile(11, assets.image("""
                Blank
            """), False)
            scene.set_tile(6, assets.image("""
                Blank
            """), False)
            scene.set_tile(8, assets.image("""
                Blank
            """), False)
            scene.set_tile(10, assets.image("""
                Blank
            """), False)
        if kojai_selector.x == 80 and kojai_selector.y == 49:
            kojai_typemode = 2
            color.set_color(1, color.rgb(200, 230, 255))
            scene.set_tile(2, assets.image("""
                ka
            """), False)
            scene.set_tile(4, assets.image("""
                ki
            """), False)
            scene.set_tile(5, assets.image("""
                ku
            """), False)
            scene.set_tile(7, assets.image("""
                ke
            """), False)
            scene.set_tile(9, assets.image("""
                ko
            """), False)
            scene.set_tile(11, assets.image("""
                Blank
            """), False)
            scene.set_tile(6, assets.image("""
                Blank
            """), False)
            scene.set_tile(8, assets.image("""
                Blank
            """), False)
            scene.set_tile(10, assets.image("""
                Blank
            """), False)
        if kojai_selector.x == 48 and kojai_selector.y == 49:
            kojai_typemode = 1
            color.set_color(1, color.rgb(200, 230, 255))
            scene.set_tile(2, assets.image("""
                a
            """), False)
            scene.set_tile(4, assets.image("""
                i
            """), False)
            scene.set_tile(5, assets.image("""
                う0
            """), False)
            scene.set_tile(7, assets.image("""
                e
            """), False)
            scene.set_tile(9, assets.image("""
                o
            """), False)
            scene.set_tile(11, assets.image("""
                Blank
            """), False)
            scene.set_tile(6, assets.image("""
                Blank
            """), False)
            scene.set_tile(8, assets.image("""
                Blank
            """), False)
            scene.set_tile(10, assets.image("""
                Blank
            """), False)
            KOJAI_remenb()
        elif kojai_selector.x == 144 and kojai_selector.y == 113:
            if controller.B.is_pressed():
                music.power_up.play()
                kojai_KOJAI2 = sprites.create(assets.image("""
                    KOJAI
                """), SpriteKind.KOJAI)
                effects.confetti.start_screen_effect(1500)
                pause(1500)
                kojai_KOJAI2.destroy(effects.hearts, 500)
        elif kojai_selector.x == 144 and kojai_selector.y == 49:
            KOJAI_NewBackSpace()
            kojai_text.x += 24
        else:
            pass
    elif kojai_typemode == 1:
        for index5 in range(1):
            if kojai_selector.x == 48 and kojai_selector.y == 49:
                KOJAI_InputText("あ")
                kojai_selector.set_position(48, 49)
            if kojai_selector.x == 80 and kojai_selector.y == 49:
                KOJAI_InputText("い")
                kojai_selector.set_position(48, 49)
            if kojai_selector.x == 112 and kojai_selector.y == 49:
                KOJAI_InputText("う")
                kojai_selector.set_position(48, 49)
            if kojai_selector.x == 48 and kojai_selector.y == 81:
                KOJAI_InputText("え")
                kojai_selector.set_position(48, 49)
            if kojai_selector.x == 80 and kojai_selector.y == 81:
                KOJAI_InputText("お")
                kojai_selector.set_position(48, 49)
    elif kojai_typemode == 2:
        for index6 in range(1):
            if kojai_selector.x == 48 and kojai_selector.y == 49:
                KOJAI_InputText("か")
                kojai_selector.set_position(80, 49)
            if kojai_selector.x == 80 and kojai_selector.y == 49:
                KOJAI_InputText("き")
                kojai_selector.set_position(80, 49)
            if kojai_selector.x == 112 and kojai_selector.y == 49:
                KOJAI_InputText("く")
                kojai_selector.set_position(80, 49)
            if kojai_selector.x == 48 and kojai_selector.y == 81:
                KOJAI_InputText("け")
                kojai_selector.set_position(80, 49)
            if kojai_selector.x == 80 and kojai_selector.y == 81:
                KOJAI_InputText("こ")
                kojai_selector.set_position(80, 49)
    elif kojai_typemode == 3:
        for index7 in range(1):
            if kojai_selector.x == 48 and kojai_selector.y == 49:
                KOJAI_InputText("さ")
                kojai_selector.set_position(112, 49)
            if kojai_selector.x == 80 and kojai_selector.y == 49:
                KOJAI_InputText("し")
                kojai_selector.set_position(112, 49)
            if kojai_selector.x == 112 and kojai_selector.y == 49:
                KOJAI_InputText("す")
                kojai_selector.set_position(112, 49)
            if kojai_selector.x == 48 and kojai_selector.y == 81:
                KOJAI_InputText("せ")
                kojai_selector.set_position(112, 49)
            if kojai_selector.x == 80 and kojai_selector.y == 81:
                KOJAI_InputText("そ")
                kojai_selector.set_position(112, 49)
    elif kojai_typemode == 4:
        for index8 in range(1):
            if kojai_selector.x == 48 and kojai_selector.y == 49:
                KOJAI_InputText("た")
                KOJAI_remenb2()
            if kojai_selector.x == 80 and kojai_selector.y == 49:
                KOJAI_InputText("ち")
                KOJAI_remenb2()
            if kojai_selector.x == 112 and kojai_selector.y == 49:
                KOJAI_InputText("つ")
                KOJAI_remenb2()
            if kojai_selector.x == 48 and kojai_selector.y == 81:
                KOJAI_InputText("て")
                KOJAI_remenb2()
            if kojai_selector.x == 80 and kojai_selector.y == 81:
                KOJAI_InputText("と")
                KOJAI_remenb2()
    elif kojai_typemode == 9:
        for index9 in range(1):
            if kojai_selector.x == 48 and kojai_selector.y == 49:
                KOJAI_InputText("ら")
                KOJAI_remenb2()
            if kojai_selector.x == 80 and kojai_selector.y == 49:
                KOJAI_InputText("り")
                KOJAI_remenb2()
            if kojai_selector.x == 112 and kojai_selector.y == 49:
                KOJAI_InputText("る")
                KOJAI_remenb2()
            if kojai_selector.x == 48 and kojai_selector.y == 81:
                KOJAI_InputText("れ")
                KOJAI_remenb2()
            if kojai_selector.x == 80 and kojai_selector.y == 81:
                KOJAI_InputText("ろ")
                KOJAI_remenb2()
        if kojai_selector.x == 48 and kojai_selector.y == 113:
            KOJAI_Dakuten()
            KOJAI_remenb2()
        if kojai_selector.x == 80 and kojai_selector.y == 113:
            pass
    elif kojai_typemode == 8:
        for index10 in range(1):
            if kojai_selector.x == 48 and kojai_selector.y == 49:
                KOJAI_InputText("や")
                KOJAI_remenb2()
            if kojai_selector.x == 80 and kojai_selector.y == 49:
                KOJAI_InputText("ゆ")
                KOJAI_remenb2()
            if kojai_selector.x == 112 and kojai_selector.y == 49:
                KOJAI_InputText("よ")
                KOJAI_remenb2()
        if kojai_selector.x == 48 and kojai_selector.y == 113:
            KOJAI_InputText("わ")
            KOJAI_remenb2()
        if kojai_selector.x == 80 and kojai_selector.y == 113:
            KOJAI_InputText("を")
            KOJAI_remenb2()
        if kojai_selector.x == 112 and kojai_selector.y == 113:
            KOJAI_InputText("ん")
            KOJAI_remenb2()
    elif kojai_typemode == 5:
        for index11 in range(1):
            if kojai_selector.x == 48 and kojai_selector.y == 49:
                KOJAI_InputText("な")
                KOJAI_remenb2()
            if kojai_selector.x == 80 and kojai_selector.y == 49:
                KOJAI_InputText("に")
                KOJAI_remenb2()
            if kojai_selector.x == 112 and kojai_selector.y == 49:
                KOJAI_InputText("ぬ")
                KOJAI_remenb2()
            if kojai_selector.x == 48 and kojai_selector.y == 81:
                KOJAI_InputText("ね")
                KOJAI_remenb2()
            if kojai_selector.x == 80 and kojai_selector.y == 81:
                KOJAI_InputText("の")
                KOJAI_remenb2()
    else:
        pass
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

kojai_KOJAI2: Sprite = None
kojai_OldText = ""
kojai_KariText = ""
kojai_conlist = 0
kojai_list: List[number] = []
kojai_text: TextSprite = None
kojai_selector: Sprite = None
kojai_typemode = 0
kojai_type = 0
kojai_inputedText = ""
kojai_inputedText = "Abc"
kojai_type = 0
kojai_typemode = 0
kojai_selector = sprites.create(assets.image("""
    Selecter
"""), SpriteKind.Selecter)
kojai_text = textsprite.create("KOJAI")
kojai_selector.set_position(48, 49)
kojai_text.set_position(164, 10)
kojai_text.set_max_font_height(25)
scene.set_tile_map(assets.image("""
    flickboard
"""), TileScale.THIRTY_TWO)
KOJAI_reset_to_board()

def on_on_update():
    kojai_text.set_text(kojai_inputedText)
    kojai_text.set_border(1, 13)
game.on_update(on_on_update)

def on_forever():
    if kojai_selector.x == 16 and kojai_selector.y == 81:
        if controller.A.is_pressed():
            kojai_text.x += 1.75
    if kojai_selector.x == 144 and kojai_selector.y == 81:
        if controller.A.is_pressed():
            kojai_text.x += -1.75
forever(on_forever)

def on_forever2():
    if kojai_selector.x < -15:
        kojai_selector.x = 144
    if 175 < kojai_selector.x:
        kojai_selector.x = 16
    if kojai_selector.y < 18:
        kojai_selector.y = 113
    if 144 < kojai_selector.y:
        kojai_selector.y = 49
forever(on_forever2)
