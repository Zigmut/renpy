init python:
    LAUNCHER_RPYS = set(['options.rpy', 'strings.rpy', 'transupdate.rpy', 'choose_theme.rpy', 'archiver.rpy', 'project.rpy', 'script_version.rpy', 'new.rpy', 'themes_data.rpy', 'opts.rpy', 'interface.rpy', 'projectsdir.rpy', 'distribute.rpy', 'script.rpy', 'editor.rpy'])

    TRANSLATION_STRINGS = [

        u"Developer Menu",
        u"Return to the developer menu",
        u"Skip Mode",
        u"Fast Skip Mode",
        u"Please click to continue.",
        u"Start Game",
        u"Load Game",
        u"Preferences",
        u"Help",
        u"Quit",
        u"Return",
        u"Save Game",
        u"Main Menu",
        u"Are you sure you want to quit?",
        u"Are you sure you want to return to the main menu?\nThis will lose unsaved progress.",
        u"Begin Skipping",
        u"Empty Slot.",
        u"Previous",
        u"Next",
        u"Yes",
        u"No",
        u"Loading will lose unsaved progress.\nAre you sure you want to do this?",
        u"Are you sure you want to overwrite your save?",
        u"The error message was:",
        u"You may want to try saving in a different slot, or playing for a while and trying again later.",
        u"Save Failed.",
        u"Continue Game",
        u"Test",
        u"Left",
        u"Right",
        u"Up",
        u"Down",
        u"Not Assigned",
        u"Select/Dismiss",
        u"Rollback",
        u"Hold to Skip",
        u"Joystick Mapping",
        u"Move the joystick or press a joystick button to create the mapping. Click the mouse to remove the mapping.",
        u"Toggle Skip",
        u"Hide Text",
        u"Menu",
        u"Display",
        u"Window",
        u"Fullscreen",
        u"Transitions",
        u"All",
        u"Some",
        u"None",
        u"Skip",
        u"Seen Messages",
        u"All Messages",
        u"After Choices",
        u"Stop Skipping",
        u"Keep Skipping",
        u"Text Speed",
        u"Auto-Forward Time",
        u"Music Volume",
        u"Sound Volume",
        u"Joystick...",
        u"Joystick Configuration",
        u"Voice Volume",
        u"Auto",
        u"Quick",
        u"The patterns did not match any files, so no archive was created.",
        u"Archiving Files...",
        u"Success",
        u"The files have been added to the archive, and moved into the \"archived\" directory. Future runs of the archiver will archive files in both the \"game\" and \"archived\" directories.",
        u"Archiver",
        u"The archiver allows you to obfuscate your game by including files in an archive file.",
        u"Archive Name:",
        u"The name of the archive to create.",
        u"Include Patterns:",
        u"Files matching these patterns are included in the archive.",
        u"Exclude Patterns:",
        u"Files matching these patterns are excluded from the archive.",
        u"Archive",
        u"Build the archive.",
        u"Cancel",
        u"Archive Name",
        u"The name of the archive file to create, without the .rpa extension.\n\nThe \"data\" archive is loaded automatically. Other archives must be added to config.archives.",
        u"Include Patterns",
        u"This is a space-separated list of file patterns. Files matching these patterns are added to the archive.\n\nAsterisks (*) can be used as a wildcard.",
        u"This is a space-separated list of file patterns. Files matching these patterns are excluded from the archive. If a file is matched by both an exclude and include pattern, the exclude takes precedence.\n\nAsterisks (*) can be used as a wildcard.",
        u"Scanning Files...",
        u"Could not modify options.rpy. Perhaps it was changed too much.",
        u"Theme changed to %s.",
        u"Planetarium",
        u"The options.rpy file does not exist in the game directory, so this launcher cannot change the theme.",
        u"Themes control the basic look of interface elements. You'll be able to pick a color scheme next.",
        u"Choose Theme",
        u"Please choose a color scheme for your project.",
        u"Choose Color Scheme",
        u"Building Distributions",
        u"I've just performed a lint on your project. If it contains errors, you should say no and fix them.\nPlease also check {a=http://www.renpy.org/wiki/renpy/Download_Ren'Py}www.renpy.org{/a} to see if updates or fixes are available.\n\nDo you want to continue?",
        u"Base Name:",
        u"Used to generate the names of directories and archive files.",
        u"Executable Name:",
        u"Used to generate the names of executables and runnable programs.",
        u"Ignore Extensions:",
        u"Files with these extensions will not be included in the distributions.",
        u"Documentation Extensions:",
        u"Files with these extensions will be treated as documentation, when building the Macintosh application.",
        u"Distributions to Build:",
        u"Windows x86",
        u"Zip distribution for the 32-bit Windows platform.",
        u"Linux x86",
        u"Tar.Bz2 distribution for the Linux x86 platform.",
        u"Macintosh Universal",
        u"Single application distribution for the Macintosh x86 and ppc platforms.",
        u"Windows/Linux/Mac Combined",
        u"Zip distribution for the Windows x86, Linux x86, Macintosh x86 and Macintosh ppc platforms.",
        u"Build",
        u"Start building the distributions.",
        u"Base Name",
        u"Please enter in the base name for your distribution. This name is used to generate the names of directories and archive files. Usually, this is the name of your game, plus a version number, like \"moonlight-1.0\".",
        u"Executable Name",
        u"Please enter a name for the executables in your distribution. This should not include an extension, as that will be added automatically.",
        u"Ignore Extensions",
        u"Please enter a space-separated list of file extensions. Files with these extensions will not be included in the built distributions.",
        u"Documentation Extensions",
        u"Please enter a space separated list of documentation extensions. Files in the base directory with these extensions will have a second copy stored outside of the Macintosh application.",
        u"Scanning...",
        u"Building Windows...",
        u"Building Linux...",
        u"Building Macintosh...",
        u"Building Combined...",
        u"Thank you for choosing Ren'Py.",
        u"The distributions have been built. Be sure to test them before release.\n\nNote that unpacking and repacking the Macintosh, Linux, or Combined distributions on Windows is not supported.\n\nPlease announce your release at the {a=http://lemmasoft.renai.us/forums/}Lemma Soft Forums{/a}, so we can add it to the Ren'Py web site.",
        u"The editor has been set from the RENPY_EDITOR environment variable, and cannot be changed.",
        u"Choose Editor",
        u"Please choose the editor that will be use to edit scripts and display errors. More editors can be downloaded from {a=http://www.renpy.org/wiki/renpy/Editors}the Ren'Py website{/a}.",
        u"Error",
        u"Press enter when done.",
        u"The string cannot be empty. Please enter some text.",
        u"Non-ASCII filenames are not allowed. This is because Zip files cannot reliably represent non-ASCII filenames.",
        u"Processed %d of %d files.",
        u"Welcome!",
        u"New Project",
        u"Please type the name of your new project.",
        u"Something with that name already exists in the projects directory.",
        u"Creating Project",
        u"Please wait while we create the project.",
        u"%s Launcher",
        u"Launcher Options",
        u"Using RENPY_EDITOR",
        u"Change the default text editor.",
        u"Projects Directory",
        u"Select the directory Ren'Py searches for projects.",
        u"Select Project",
        u"%s has been launched.",
        u"Opening game directory:\n%s",
        u"No editor has been selected.",
        u"No files to edit.",
        u"Launching the editor failed.",
        u"Launched editor with %d script files.",
        u"Lint",
        u"Lint in progress.",
        u"Lint complete.",
        u"Deleting persistent data.",
        u"Delete Persistent",
        u"Persistent data has been deleted.",
        u"Choose Projects Directory",
        u"Please choose the directory containing your projects.",
        u"Could not run zenity. The projects directory has been set to the directory immediately above the directory containing Ren'Py.",
        u"Now showing the Ren'Py documentation in your web browser.",
        u"Launch",
        u"Launches the project.",
        u"Edit Script",
        u"Edits the script of the project.",
        u"Game Directory",
        u"Opens the project's game directory.",
        u"Check Script (Lint)",
        u"Checks the script of the project for likely errors.",
        u"Changes the theme used by the project.",
        u"Deletes the persistent data associated with the project.",
        u"Archive Files",
        u"Archives files found in the game and archived directories.",
        u"Build Distributions",
        u"Builds distributions of the project.",
        u"Ren'Py",
        u"Select a project to work with.",
        u"Create a new project.",
        u"Causes the launcher to exit.",
        u"Options",
        u"Change Ren'Py launcher options.",
        u"Ren'Py Help",
        u"Open the Ren'Py documentation in a web browser.",
    ]

