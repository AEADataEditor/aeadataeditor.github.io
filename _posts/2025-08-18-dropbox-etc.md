---
title:  "On the Dangers of Online Storage"
date: 2025-08-18
mastodon: 
twitter:
bluesky: 
tags:
  - data editor tips
  - replication packages
  - Dropbox
  - OneDrive
  - Box
---

We see this far too often: When we go to check the deposit that authors submit to us, all the files are there, but somewhere halfway through the process, the replicators hits one, then many files that are empty or ... weird. What's going on?


<!-- more -->

## The Problem

It turns out that online storage solutions, such as Dropbox, OneDrive, and Box (without necessarily limiting ourselves to these), provide a really "convenient" feature: They show you all the thousands of files you have accumulated, including over the 8 years this project has been underway. But they don't want to put 2TB of data on your laptop. So the files you see are NOT really there... they leave placeholders in place. 

What happens when you want to access these files? You double-click on them, and then it takes a bit longer for your Word, Acrobat, or Stata to open the file, because in the background, OneDropBoxDrive is quickly downloading the file for you, as if it had always been there. Sometimes, the application crashes, because OneDropBoxDrive is taking too long, but you try again, and it works. You think "huh, stupid computer"  and go on with your work.

So what happens when you zip up these files? Well, it turns out, in many cases (not entirely clear when), ZIP file creators are perfectly happy to NOT be patient, and simply zip up the placeholders. Which are empty files. 

When you then upload these ZIP files to deposits like the AEA's [Data and Code Repository](https://www.openicpsr.org/openicpsr/search/aea/studies), the system there happily unzips the ZIP file. And perfectly preserves a bunch of empty files.

![Empty files on openICPSR](/images/icpsr-zero-byte-files.png)

The problem is as bad on other repositories, such as the various Dataverses out there, or [Zenodo](https://zenodo.org/).

## The partial Solution

We have added to our ingest scripts a [check for zero-byte files](https://github.com/AEADataEditor/replication-template/blob/master/automations/06_check_duplicates_and_zero_bytes.sh), which will flag these files. But this is relatively new, and not all replicators catch this early on. Leading to frustrating delays for everybody. 

## The Solution

How do YOU (the author) avoid this problem? Two paths:

- You could simply set the project directory to be "always available offline" (or whatever DriveBoxOneDrop may call it). So they gobble up all the storage space they need.  Then, when you ZIP them up, they will all be there. When you are done, you can flip them back to "online only" if you want (until you get back the report from us asking you to fix stuff...) 
- Or, you can simply go to the BoxDriveDropOne website, and download the entire project from there, as a ZIP file, ready to upload. 

> For Dropbox, here's what you do:
> 
> - Go to <https://www.dropbox.com/home>. If you are not logged on there, go to your Dropbox icon in the system tray (Windows, Linux) or menu bar (Mac), and select "Launch Dropbox Website".
> - Navigate to the folder you want to download. You want to see the files in the folder (be "in"  the folder).
> 
> ![Dropbox folder view](/images/dropbox-sample-folder.png)
>
> - Click on the gear icon ⚙️ to the right of the folder name, and select "Download"
> 
> ![Dropbox download menu](/images/dropbox-sample-folder-download.png)


Voilà! You have a ZIP file with all the files in it, ready to upload to your deposit, with no chance at all that some files are missing.[^a]

[^a]: Unless, of course, the files are missing on your DropOneBoxDrive, and the problem is not the software....