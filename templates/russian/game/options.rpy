﻿## Этот файл содержит некоторые опции которые можно изменить для настройки
## вашей игры на Ren'Py. Он содержит только самые часто используемые настройки...
## Их на самом деле гораздо больше.
##
## Строки, начинающиеся с двух знаков '#' являются комментариями, и вы
## не должны их раскомментировать. Строки, начинающиеся с одного
## знака '#' являются закоментированным кодом, и вы можете их
## раскомментировать в подходящих вам ситуациях.

init -1 python hide:

    ## Включать ли нам инструменты разработчика? Здесь нужно
    ## поставить False перед выпуском игры, чтобы
    ## пользователь не смог мошенничать, используя эти инструменты.

    config.developer = True

    ## Эти управляют шириной и высотой экрана.

    config.screen_width = 800
    config.screen_height = 600

    ## Это управляет заголовком окна, когда Ren'Py
    ## запущен в оконном режиме.

    config.window_title = u"PROJECT_NAME"

    # Эти управляют именем и версией игры, которые указываются
    # в журналах отладки.
    config.name = "PROJECT_NAME"
    config.version = "0.0"

    #########################################
    # Темы

    ## Затем, мы захотим вызвать функцию темы. theme.roundrect
    ## это тема, поддерживающая круглые прямоугольники.
    ## Пока что, это единственная тема.
    ##
    ## Функция темы берет несколько параметров, которые
    ## настраивают цветовую схему.

    theme.roundrect(

        ## Цвет простаивающего виджета.
        widget = "#003c78",

        ## Цвет сфокусированного виджета.
        widget_hover = "#0050a0",

        ## Цвет текста в виджете.
        widget_text = "#c8ffff",

        ## Цвет текста в выбранном виджете (Например,
        ## текущее значение настройки.)
        widget_selected = "#ffffc8",

        ## Цвет отключенного виджета.
        disabled = "#404040",

        ## Цвет текста отключенного виджета.
        disabled_text = "#c8c8c8",

        ## Цвет информационных меток.
        label = "#ffffff",

        ## Цвет рамки, содержащей виджеты.
        frame = "#6496c8",

        ## Если True, игровое окно скругляется. Если False,
        ## оно остается квадратным.
        rounded_window = False,

        ## Фон главного меню.
        ## Это может быть цвет, начинающийся с '#',
        ## или имя файла с изображением.
        ## В последнем случае, оно должно совпадать по
        ## ширине и высоте с размером игры.
        mm_root = "#dcebff",

        ## Фон внутриигрового меню.
        ## Это может быть цвет, начинающийся с '#',
        ## или имя файла с изображением.
        ## В последнем случае, оно должно совпадать по
        ## ширине и высоте с размером игры.
        gm_root = "#dcebff",

        ## И с темой покончено. Эта тема настроит разные стили,
        ## так что если мы хотим их изменить, нам придется
        ## сделать это ниже.
        )


    #########################################
    ## Эти настройки позволяют вам настроить окно,
    ## содержащее диалоги и текст "от автора", замещая его
    ## изображением.

    ## Фон окна. В Frame, числа символизируют размер
    ## левого/правого и верхнего/нижнего бордюров
    ## соответственно.

    # style.window.background = Frame("frame.png", 12, 12)

    ## Внешние поля - пространство, окружающее окно, на котором
    ## не рисуется фон.

    # style.window.left_margin = 6
    # style.window.right_margin = 6
    # style.window.top_margin = 6
    # style.window.bottom_margin = 6

    ## Внутренние поля - пространство внутри окна, где
    ## рисуется фон.

    # style.window.left_padding = 6
    # style.window.right_padding = 6
    # style.window.top_padding = 6
    # style.window.bottom_padding = 6

    ## Это минимальная высота окна, включая поля.

    # style.window.yminimum = 250


    #########################################
    ## Это позволит вам изменить расположение главного меню.

    ## Это работает так: мы находим точку-якорь внутри
    ## объекта и точку позиции (pos) на экране.
    ## Затем, мы размещаем объект так, чтобы эти точки совпадали.

    ## Якорь/pos можно задавать как целое или действительное число.
    ## Если целое, оно принимается как кол-во пикселей от
    ## левого верхнего угла. Если действительное, число
    ## принимается как доля размера объекта или экрана.

    # style.mm_menu_frame.xpos = 0.5
    # style.mm_menu_frame.xanchor = 0.5
    # style.mm_menu_frame.ypos = 0.75
    # style.mm_menu_frame.yanchor = 0.5


    #########################################
    ## Это позволяет настроить шрифт текста в Ren'Py.

    ## Файл, содержащий шрифт.

    # style.default.font = "DejaVuSans.ttf"

    ## Размер текста по умолчанию.

    # style.default.size = 22

    ## Заметьте, что это изменит стиль лишь некоторого
    ## текста. У других кнопок свои стили.


    #########################################
    ## Эти настройки позволят изменить некоторые звуки
    ## Ren'Py.

    ## Установите False если в игре нет звуковых эффектов.

    config.has_sound = True

    ## Установите False если в игре нет музыки.

    config.has_music = True

    ## Установите True если в игре есть озвучка. 

    config.has_voice = False

    ## Звуки при нажатии на кнопки и imagemap-ы.

    # style.button.activate_sound = "click.wav"
    # style.imagemap.activate_sound = "click.wav"

    ## Звуки при входе и выходе из игрового меню.

    # config.enter_sound = "click.wav"
    # config.exit_sound = "click.wav"

    ## Звук для проверки громкости.

    # config.sample_sound = "click.wav"

    ## Музыка, играющая в главном меню.

    # config.main_menu_music = "main_menu_theme.ogg"


    #########################################
    ## Справка.

    ## Это позволит настроить опцию справки в меню Ren'Py.
    ## Это могут быть:
    ## - Метка в сценарии. В этом случае эта метка вызывается
    ##   для показа помощи.
    ## - Имя файла отнсоительно основной директории.
    ##   Он будет открыт в веб-браузере.
    ## None. Помощь будет выключена.
    config.help = "README.html"


    #########################################
    ## Переходы.

    ## Используется при входе в игровое меню.
    config.enter_transition = None

    ## Используется при выходе из игрвого меню.
    config.exit_transition = None

    ## Используется между экранами игрового меню.
    config.intra_transition = None

    ## Используется при входе в игровое меню из главного.
    config.main_game_transition = None

    ## Используется при возвращении в главное меню из игры.
    config.game_main_transition = None

    ## Используется при переходе в главное меню из окна загрузки.
    config.end_splash_transition = None

    ## Используется при переходе в главное меню после окончания игры.
    config.end_game_transition = None

    ## Используется при загрузке игры.
    config.after_load_transition = None

    ## Используется при отображении окна.
    config.window_show_transition = None

    ## Используется при скрытии окна.
    config.window_hide_transition = None

    ## Используется при переходе в режим NVL сразу после режима ADV.
    config.adv_nvl_transition = dissolve

    ## Используется при переходе в режим ADV сразу после режима NVL.
    config.nvl_adv_transition = dissolve

    ## Используется при отображении yesno.
    config.enter_yesno_transition = None

    ## Используется при скрытии yesno.
    config.exit_yesno_transition = None

    ## Используется при входе в реплей.
    config.enter_replay_transition = None

    ## Используется при выходе из реплея.
    config.exit_replay_transition = None

    ## Используется при изменении изображения с помощью "say" с изобразительными атрибутами.
    config.say_attribute_transition = None

    #########################################
    ## Имя директории, где хранятся данные игры.
    ## (это необходимо задать рано, чтобы постоянная информация могла быть 
    ## найдена на стадии инициализации.)
python early:
    config.save_directory = "PROJECT_NAME-UNIQUE"

init -1 python hide:
    #########################################
    ## Стандартные значения настроек.

    ## Эти опции используются лишь при первом запуске игры.
    ## Чтобы применить их снова, удалите game/saves/persistent.

    ## Запустить в полноэкранном режиме?

    config.default_fullscreen = False

    ## Скорость текста по умолчанию, в знаках в секунду. 0 - бесконечность.

    config.default_text_cps = 0

    ## Время авто-режима по умолчанию.

    config.default_afm_time = 10

    #########################################
    ## Остальные настройки могут быть ниже.