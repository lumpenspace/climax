#!/usr/bin/osascript
on run args
  set the clipboard to POSIX file (items of args)
end