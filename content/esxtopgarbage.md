Title: Fix Garbage Output from esxtop (and learn something along the way)
Slug: fix-garbage-output-from-esxtop
Date: 2014-08-28 19:45:48
Tags: esxi, cli, os x
Category: virtualization
Image: /images/osx-set-term.png
Summary: If esxtop looks like a stream of nonsense when you run it, check your emulation mode, then understand what emulation mode is to feel clever the next time this happens.
Status: Draft

I noticed when I accessed my ESXi hosts from my Mac and ran `esxtop`, the output was a stream of seeming garbage like:

```bash
~ # esxtop
no termcap entry for a `xterm-256color' terminal"(PDH-CSV 4.0) (UTC)(0)","\\esxihost.example.org\Memory\Memory Overcommit (1 Minute Avg)","\\esxihost.example.org\Memory\Memory Overcommit (5 Minute Avg)","\\esxihost.example.org\Memory\Memory Overcommit (15 Minute Avg)","\\esxihost.example.org\Physical Cpu Load\Cpu Load (1 Minute Avg)","\\esxihost.example.org\Physical Cpu Load\Cpu Load (5 Minute Avg)"
```

The key is in the first line: `no termcap entry for a 'xterm-256color' terminal`. [Termcap](https://www.gnu.org/software/termutils/manual/termcap-1.3/html_mono/termcap.html) is a utility meant to allow presenting output to terminals of various kinds. The utility essentially has a configuration setting for each popular terminal emulation mode, so that output requiring a more complex layout could be displayed properly. Terminal emulation is a whole other topic in itself, but suffice it to say that todays "terminals" in e.g. OS X, Linux, etc. are imitating a configuration and display borrowed from the screens of old computers, because much of the early standards around how CLI stuff ought to work was decided when these were the systems the utilities ran upon. (xterm, upon which the OS X default xterm-256 is based, imitates the [VAXstation 100](https://en.wikipedia.org/wiki/VAXstation))

<aside markdown="1">
> The quickest solution is to change the terminal emulation mode your terminal uses... but this isn't the best solution.

</aside>

It's done this way because it works, and keeps there's not much necessity to change how this output should work. Having a standard is helpful, because it's actually quite a bit of work to map GUIs to console output, and there's many rather old CLI programs which need to keep portable to newer systems, and still display just fine. However, OS X has chosen the less-common profile xterm-256color, which simply isn't set in the termcap configuration esxtop uses. The quickest solution is to change the terminal emulation mode your terminal uses ("xterm" is a generally good choice). To change this in OS X, select **Preferences** from the **Terminal** menu. Then, select the profile you want to change on the left side of the window (the current profile you're using will already be selected). Finally, select **xterm** from the **Declare terminal as** dropdown menu.

![OS X Terminal Preferences Window](/images/osx-set-term.png)

<aside markdown="1">
It's worth mentioning that setting this does not mean you will not be able to display colors in the terminal - it's rather more complicated than that. Essentially, setting the mode *explicitly* declares the kind of color made the terminal can support. There are other ways color support is detected, but many systems and utilities have other ways of detecting or forcing the display mode.
</aside>

Changing the emulation mode client-side is a simple one-off way to fix it, but this isn't the best solution. As Mathias Ewald correctly points out in his [article on fixing esxtop output](http://www.vxpertise.net/2012/12/esxi-shell-fixing-esxtop-output-via-ssh/), a better approach is to change how the ESXi host perceives your terminal session. You can, as Mathias suggests, simply execute `TERM=xterm esxtop`, which will force the emulation mode for just that run. He also correctly mentions you could also set the [environment variable](https://wiki.archlinux.org/index.php/Environment_Variables) TERM, which decides what terminal mode your session will use: `export TERM=xterm`. There's another, more permanent solution: set the option in .profile, a file in your home directory which is really just a logon script:

```bash
echo "TERM=xterm >> ~/.profile"
```

<aside markdown="1">
> I hope this more lengthy exploration of a one-line fix serves as a reminder that searching out and understanding the underlying problem goes a long way toward most correctly solving it.

</aside>

This works the same way the `export` command does, it simply sets it at a different time. This way, regardless of what mode your connecting terminal emulator is in, you will correctly view ESXi console output in a mode the termcap utility present on the host natively understands. I hope this more lengthy exploration of a one-line fix serves as a reminder that searching out and understanding the underlying problem goes a long way toward most correctly solving it. Until next time, then.
