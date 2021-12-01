namespace SpriteKind {
    export const Selecter = SpriteKind.create()
    export const KOJAI = SpriteKind.create()
}
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    kojai_selector.x += 32
})
function KOJAI_remenb () {
	
}
controller.menu.onEvent(ControllerButtonEvent.Pressed, function () {
    for (let index = 0; index < 5; index++) {
        kojai_text.setOutline(1, 2)
        pause(100)
        kojai_text.setOutline(1, 4)
        pause(100)
        kojai_text.setOutline(1, 5)
        pause(100)
        kojai_text.setOutline(1, 7)
        pause(100)
        kojai_text.setOutline(1, 8)
        pause(100)
        kojai_text.setOutline(1, 10)
        pause(100)
    }
    kojai_text.setOutline(0, 0)
})
function KOJAI_BackSpace () {
    kojai_list = []
    kojai_conlist = 0
    for (let index = 0; index < kojai_inputedText.length - 1; index++) {
        kojai_conlist += 1
        kojai_KariText = "" + kojai_KariText + kojai_inputedText.charAt(kojai_conlist)
    }
    kojai_inputedText = kojai_KariText
}
controller.C.onEvent(ControllerButtonEvent.Pressed, function () {
    kojai_selector.say("" + kojai_selector.x + ", " + ("" + kojai_selector.y))
})
function KOJAI_NewBackSpace () {
    kojai_OldText = kojai_inputedText
    kojai_inputedText = ""
    kojai_conlist = 0
    for (let index = 0; index < kojai_OldText.length - 1; index++) {
        kojai_inputedText = "" + kojai_inputedText + kojai_OldText.charAt(kojai_conlist)
        kojai_conlist += 1
    }
}
function KOJAI_reset_to_board () {
    color.setColor(1, color.rgb(255, 255, 255))
    scene.setTile(2, assets.image`a`, false)
    scene.setTile(4, assets.image`ka`, false)
    scene.setTile(5, assets.image`sa`, false)
    scene.setTile(7, assets.image`ta`, false)
    scene.setTile(9, assets.image`na`, false)
    scene.setTile(11, assets.image`ha`, false)
    scene.setTile(6, assets.image`ma`, false)
    scene.setTile(8, assets.image`ya`, false)
    scene.setTile(10, assets.image`ra`, false)
    scene.setTile(3, assets.image`Space`, false)
    scene.setTile(15, assets.image`ModeChange`, false)
    scene.setTile(12, assets.image`Backspace`, false)
    scene.setTile(13, assets.image`Enter`, false)
    scene.setTile(14, assets.image`Left`, false)
    scene.setTile(1, assets.image`Right`, false)
    color.setColor(2, color.rgb(255, 100, 100))
    color.setColor(7, color.rgb(125, 255, 125))
    color.setColor(13, color.rgb(255, 255, 125))
    color.setColor(4, color.rgb(255, 200, 125))
}
function KOJAI_remenb2 () {
	
}
function KOJAI_CovertToList () {
	
}
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    kojai_selector.y += 32
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    kojai_selector.x += -32
})
function KOJAI_Dakuten () {
    kojai_OldText = kojai_inputedText
    kojai_inputedText = ""
    kojai_conlist = 0
    for (let index = 0; index < kojai_OldText.length - 1; index++) {
        kojai_inputedText = "" + kojai_inputedText + kojai_OldText.charAt(kojai_conlist)
        kojai_conlist += 1
    }
    if (kojai_OldText.charAt(kojai_OldText.length - 1) == "か") {
        kojai_inputedText = "" + kojai_inputedText + "が"
    } else if (kojai_OldText.charAt(kojai_OldText.length - 1) == "き") {
        kojai_inputedText = "" + kojai_inputedText + "ぎ"
    } else if (kojai_OldText.charAt(kojai_OldText.length - 1) == "く") {
        kojai_inputedText = "" + kojai_inputedText + "ぐ"
    } else if (kojai_OldText.charAt(kojai_OldText.length - 1) == "け") {
        kojai_inputedText = "" + kojai_inputedText + "げ"
    } else if (kojai_OldText.charAt(kojai_OldText.length - 1) == "こ") {
        kojai_inputedText = "" + kojai_inputedText + "ご"
    } else if (false) {
    	
    } else if (false) {
    	
    } else if (false) {
    	
    } else if (false) {
    	
    } else if (false) {
    	
    } else {
    	
    }
}
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    KOJAI_NewBackSpace()
    kojai_text.x += 24
})
function KOJAI_InputText (inputext: string) {
    kojai_inputedText = "" + kojai_inputedText + inputext
    console.log(kojai_inputedText)
    kojai_text.x += -24
    kojai_typemode = 0
    KOJAI_reset_to_board()
}
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    kojai_selector.y += -32
})
/**
 * type
 * 
 * 0 = ひらがな
 * 
 * 1 = カタカナ
 * 
 * 2 = Alphabet
 * 
 * 3 = 数字 123
 * 
 * 4 = 記号 @_-/
 */
// How2typemode
// 
// 0 = 初期状態
// 
// 1 = "あ"を押した状態
// 
// 2 = "か"を押した状態
// 
// 3 = "い"を押した... と続いていく
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (kojai_selector.x == 16 && kojai_selector.y == 113) {
        kojai_type += 1
        if (kojai_type == 5) {
            kojai_type = 0
        }
    }
    if (kojai_selector.x == 16 && kojai_selector.y == 49) {
        KOJAI_InputText(" ")
    }
    if (kojai_typemode == 0) {
        if (kojai_selector.x == 80 && kojai_selector.y == 81) {
            kojai_typemode = 5
            KOJAI_remenb()
            color.setColor(1, color.rgb(200, 230, 255))
            scene.setTile(2, assets.image`na`, false)
            scene.setTile(4, assets.image`ni`, false)
            scene.setTile(5, assets.image`nu`, false)
            scene.setTile(7, assets.image`ne`, false)
            scene.setTile(9, assets.image`no`, false)
            scene.setTile(11, assets.image`Blank`, false)
            scene.setTile(6, assets.image`Blank`, false)
            scene.setTile(8, assets.image`Blank`, false)
            scene.setTile(10, assets.image`Blank`, false)
        }
        if (kojai_selector.x == 80 && kojai_selector.y == 113) {
            kojai_typemode = 8
            KOJAI_remenb()
            color.setColor(1, color.rgb(200, 230, 255))
            scene.setTile(2, assets.image`ya`, false)
            scene.setTile(4, assets.image`ma`, false)
            scene.setTile(5, assets.image`ya`, false)
            scene.setTile(7, assets.image`Blank`, false)
            scene.setTile(9, assets.image`Blank`, false)
            scene.setTile(11, assets.image`Blank`, false)
            scene.setTile(6, assets.image`se`, false)
            scene.setTile(8, assets.image`su`, false)
            scene.setTile(10, assets.image`u`, false)
        }
        if (kojai_selector.x == 48 && kojai_selector.y == 81) {
            kojai_typemode = 4
            KOJAI_remenb()
            color.setColor(1, color.rgb(200, 230, 255))
            scene.setTile(2, assets.image`ta`, false)
            scene.setTile(4, assets.image`chi`, false)
            scene.setTile(5, assets.image`tsu`, false)
            scene.setTile(7, assets.image`te`, false)
            scene.setTile(9, assets.image`to`, false)
            scene.setTile(11, assets.image`Blank`, false)
            scene.setTile(6, assets.image`Blank`, false)
            scene.setTile(8, assets.image`Blank`, false)
            scene.setTile(10, assets.image`Blank`, false)
        }
        if (kojai_selector.x == 112 && kojai_selector.y == 49) {
            KOJAI_remenb()
            kojai_typemode = 3
            color.setColor(1, color.rgb(200, 230, 255))
            scene.setTile(2, assets.image`sa`, false)
            scene.setTile(4, assets.image`si`, false)
            scene.setTile(5, assets.image`su`, false)
            scene.setTile(7, assets.image`se`, false)
            scene.setTile(9, assets.image`so`, false)
            scene.setTile(11, assets.image`Blank`, false)
            scene.setTile(6, assets.image`Blank`, false)
            scene.setTile(8, assets.image`Blank`, false)
            scene.setTile(10, assets.image`Blank`, false)
        }
        if (kojai_selector.x == 80 && kojai_selector.y == 49) {
            kojai_typemode = 2
            color.setColor(1, color.rgb(200, 230, 255))
            scene.setTile(2, assets.image`ka`, false)
            scene.setTile(4, assets.image`ki`, false)
            scene.setTile(5, assets.image`ku`, false)
            scene.setTile(7, assets.image`ke`, false)
            scene.setTile(9, assets.image`ko`, false)
            scene.setTile(11, assets.image`Blank`, false)
            scene.setTile(6, assets.image`Blank`, false)
            scene.setTile(8, assets.image`Blank`, false)
            scene.setTile(10, assets.image`Blank`, false)
        }
        if (kojai_selector.x == 48 && kojai_selector.y == 49) {
            kojai_typemode = 1
            color.setColor(1, color.rgb(200, 230, 255))
            scene.setTile(2, assets.image`a`, false)
            scene.setTile(4, assets.image`i`, false)
            scene.setTile(5, assets.image`u`, false)
            scene.setTile(7, assets.image`e`, false)
            scene.setTile(9, assets.image`o`, false)
            scene.setTile(11, assets.image`Blank`, false)
            scene.setTile(6, assets.image`Blank`, false)
            scene.setTile(8, assets.image`Blank`, false)
            scene.setTile(10, assets.image`Blank`, false)
            KOJAI_remenb()
        } else if (kojai_selector.x == 144 && kojai_selector.y == 113) {
            if (controller.B.isPressed()) {
                music.powerUp.play()
                kojai_KOJAI2 = sprites.create(assets.image`KOJAI`, SpriteKind.KOJAI)
                effects.confetti.startScreenEffect(1500)
                pause(1500)
                kojai_KOJAI2.destroy(effects.hearts, 500)
            }
        } else if (kojai_selector.x == 144 && kojai_selector.y == 49) {
            KOJAI_NewBackSpace()
            kojai_text.x += 24
        } else {
        	
        }
    } else if (kojai_typemode == 1) {
        for (let index = 0; index < 1; index++) {
            if (kojai_selector.x == 48 && kojai_selector.y == 49) {
                KOJAI_InputText("あ")
                kojai_selector.setPosition(48, 49)
            }
            if (kojai_selector.x == 80 && kojai_selector.y == 49) {
                KOJAI_InputText("い")
                kojai_selector.setPosition(48, 49)
            }
            if (kojai_selector.x == 112 && kojai_selector.y == 49) {
                KOJAI_InputText("う")
                kojai_selector.setPosition(48, 49)
            }
            if (kojai_selector.x == 48 && kojai_selector.y == 81) {
                KOJAI_InputText("え")
                kojai_selector.setPosition(48, 49)
            }
            if (kojai_selector.x == 80 && kojai_selector.y == 81) {
                KOJAI_InputText("お")
                kojai_selector.setPosition(48, 49)
            }
        }
    } else if (kojai_typemode == 2) {
        for (let index = 0; index < 1; index++) {
            if (kojai_selector.x == 48 && kojai_selector.y == 49) {
                KOJAI_InputText("か")
                kojai_selector.setPosition(80, 49)
            }
            if (kojai_selector.x == 80 && kojai_selector.y == 49) {
                KOJAI_InputText("き")
                kojai_selector.setPosition(80, 49)
            }
            if (kojai_selector.x == 112 && kojai_selector.y == 49) {
                KOJAI_InputText("く")
                kojai_selector.setPosition(80, 49)
            }
            if (kojai_selector.x == 48 && kojai_selector.y == 81) {
                KOJAI_InputText("け")
                kojai_selector.setPosition(80, 49)
            }
            if (kojai_selector.x == 80 && kojai_selector.y == 81) {
                KOJAI_InputText("こ")
                kojai_selector.setPosition(80, 49)
            }
        }
    } else if (kojai_typemode == 3) {
        for (let index = 0; index < 1; index++) {
            if (kojai_selector.x == 48 && kojai_selector.y == 49) {
                KOJAI_InputText("さ")
                kojai_selector.setPosition(112, 49)
            }
            if (kojai_selector.x == 80 && kojai_selector.y == 49) {
                KOJAI_InputText("し")
                kojai_selector.setPosition(112, 49)
            }
            if (kojai_selector.x == 112 && kojai_selector.y == 49) {
                KOJAI_InputText("す")
                kojai_selector.setPosition(112, 49)
            }
            if (kojai_selector.x == 48 && kojai_selector.y == 81) {
                KOJAI_InputText("せ")
                kojai_selector.setPosition(112, 49)
            }
            if (kojai_selector.x == 80 && kojai_selector.y == 81) {
                KOJAI_InputText("そ")
                kojai_selector.setPosition(112, 49)
            }
        }
    } else if (kojai_typemode == 4) {
        for (let index = 0; index < 1; index++) {
            if (kojai_selector.x == 48 && kojai_selector.y == 49) {
                KOJAI_InputText("た")
                kojai_selector.setPosition(112, 81)
            }
            if (kojai_selector.x == 80 && kojai_selector.y == 49) {
                KOJAI_InputText("ち")
                kojai_selector.setPosition(112, 81)
            }
            if (kojai_selector.x == 112 && kojai_selector.y == 49) {
                KOJAI_InputText("つ")
                kojai_selector.setPosition(112, 81)
            }
            if (kojai_selector.x == 48 && kojai_selector.y == 81) {
                KOJAI_InputText("て")
                kojai_selector.setPosition(112, 81)
            }
            if (kojai_selector.x == 80 && kojai_selector.y == 81) {
                KOJAI_InputText("と")
                kojai_selector.setPosition(112, 81)
            }
        }
    } else if (kojai_typemode == 9) {
        for (let index = 0; index < 1; index++) {
            if (kojai_selector.x == 48 && kojai_selector.y == 49) {
                KOJAI_InputText("ら")
                kojai_selector.setPosition(80, 81)
            }
            if (kojai_selector.x == 80 && kojai_selector.y == 49) {
                KOJAI_InputText("り")
                kojai_selector.setPosition(80, 81)
            }
            if (kojai_selector.x == 112 && kojai_selector.y == 49) {
                KOJAI_InputText("る")
                kojai_selector.setPosition(80, 81)
            }
            if (kojai_selector.x == 48 && kojai_selector.y == 81) {
                KOJAI_InputText("れ")
                kojai_selector.setPosition(80, 81)
            }
            if (kojai_selector.x == 80 && kojai_selector.y == 81) {
                KOJAI_InputText("ろ")
                kojai_selector.setPosition(80, 81)
            }
        }
        if (kojai_selector.x == 48 && kojai_selector.y == 113) {
            KOJAI_Dakuten()
            KOJAI_remenb2()
        }
        if (kojai_selector.x == 80 && kojai_selector.y == 113) {
        	
        }
    } else if (kojai_typemode == 8) {
        for (let index = 0; index < 1; index++) {
            if (kojai_selector.x == 48 && kojai_selector.y == 49) {
                KOJAI_InputText("や")
                KOJAI_remenb2()
            }
            if (kojai_selector.x == 80 && kojai_selector.y == 49) {
                KOJAI_InputText("ゆ")
                KOJAI_remenb2()
            }
            if (kojai_selector.x == 112 && kojai_selector.y == 49) {
                KOJAI_InputText("よ")
                KOJAI_remenb2()
            }
        }
        if (kojai_selector.x == 48 && kojai_selector.y == 113) {
            KOJAI_InputText("わ")
            KOJAI_remenb2()
        }
        if (kojai_selector.x == 80 && kojai_selector.y == 113) {
            KOJAI_InputText("を")
            KOJAI_remenb2()
        }
        if (kojai_selector.x == 112 && kojai_selector.y == 113) {
            KOJAI_InputText("ん")
            KOJAI_remenb2()
        }
    } else if (kojai_typemode == 5) {
        for (let index = 0; index < 1; index++) {
            if (kojai_selector.x == 48 && kojai_selector.y == 49) {
                KOJAI_InputText("な")
                KOJAI_remenb2()
            }
            if (kojai_selector.x == 80 && kojai_selector.y == 49) {
                KOJAI_InputText("に")
                KOJAI_remenb2()
            }
            if (kojai_selector.x == 112 && kojai_selector.y == 49) {
                KOJAI_InputText("ぬ")
                KOJAI_remenb2()
            }
            if (kojai_selector.x == 48 && kojai_selector.y == 81) {
                KOJAI_InputText("ね")
                KOJAI_remenb2()
            }
            if (kojai_selector.x == 80 && kojai_selector.y == 81) {
                KOJAI_InputText("の")
                KOJAI_remenb2()
            }
        }
    } else {
    	
    }
})
let kojai_KOJAI2: Sprite = null
let kojai_OldText = ""
let kojai_KariText = ""
let kojai_conlist = 0
let kojai_list: number[] = []
let kojai_text: TextSprite = null
let kojai_selector: Sprite = null
let kojai_typemode = 0
let kojai_type = 0
let kojai_inputedText = ""
kojai_inputedText = "Abc"
kojai_type = 0
kojai_typemode = 0
kojai_selector = sprites.create(assets.image`Selecter`, SpriteKind.Selecter)
kojai_text = textsprite.create("KOJAI")
kojai_selector.setPosition(48, 49)
kojai_text.setPosition(164, 10)
kojai_text.setMaxFontHeight(25)
scene.setTileMap(assets.image`flickboard`, TileScale.ThirtyTwo)
KOJAI_reset_to_board()
game.onUpdate(function () {
    kojai_text.setText(kojai_inputedText)
    kojai_text.setBorder(1, 13)
})
forever(function () {
    if (kojai_selector.x == 16 && kojai_selector.y == 81) {
        if (controller.A.isPressed()) {
            kojai_text.x += 1.75
        }
    }
    if (kojai_selector.x == 144 && kojai_selector.y == 81) {
        if (controller.A.isPressed()) {
            kojai_text.x += -1.75
        }
    }
})
forever(function () {
    if (kojai_selector.x < -15) {
        kojai_selector.x = 144
    }
    if (175 < kojai_selector.x) {
        kojai_selector.x = 16
    }
    if (kojai_selector.y < 18) {
        kojai_selector.y = 113
    }
    if (144 < kojai_selector.y) {
        kojai_selector.y = 49
    }
})
