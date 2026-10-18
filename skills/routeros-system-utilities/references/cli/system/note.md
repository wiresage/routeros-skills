# /system/note

> Source: https://manual.mikrotik.com/docs/cli-reference/system/note

Type: Settings Directory

A text that the router shows to administrators at login, for example the router's purpose, contacts or a warning. For examples, see [Note](../../guides/system-information-and-utilities/note.md).

**Arguments**

- `show-at-login` (bool): Show the note after login: in interactive command-line sessions such as SSH or Telnet, right after the banner, and in WinBox. A command run over SSH without an interactive session does not show it. Default: yes.
- `show-at-cli-login` (bool): Also show the note before the Telnet login prompt, to anyone who connects, without authentication; independent of `show-at-login`. SSH does not show the note before login, and MAC Telnet asks for the credentials before it connects. Default: no.
- `note` (string): Text of the note. `\n` starts a new line; `/system/note/edit note` opens the text in the built-in editor. A file named `sys-note.txt` in the root of the file storage replaces the note at the next startup, and the router then removes the file. Default: empty.
