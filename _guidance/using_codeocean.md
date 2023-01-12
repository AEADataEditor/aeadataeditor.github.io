
The basic thing to know about CO: you cannot have code and data in the same place (it's a really bad idea anyway, ...). So packages are split into "/data" and "/code".

You must have a single (main) file to run. Let's call it "main.do". Right-click on it, and "Set [it] as the file to run".  But you could also use the "run" file to collect various other programs. Start with the first dofile, then copy-paste the rows in "run" to correspond to your other files. Your choice, depending on how you structure your code. The difference will be that when using "main.do", all Stata programs run in a single Stata session. If using "run", they run in independent sessions.

All the Stata paths should use "/", not "\" - also a best practice - makes it work everywhere, including Windows.

All output on CO must​ be written to "/results" (which is defined in "main.do" so one can replace it).

Once run, you see all the results in the right or left panel. 

- Right panel: all previous runs, and the most recent one. 
- Left panel: the most recent one.

What gets published is what's in the left panel (and the data and code). All the other runs, on the right side, are not made public.