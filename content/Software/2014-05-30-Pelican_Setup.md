title: Pelican Setup
tags: pelican, python, config

When Ben — my colleague and friend — spoke about **Pelican**, the framework he uses for his site ([Shrike Systems](http://www.shrike-systems.com)), I got interested. I may had finally found a solution which fulfilled my own needs for Web publishing.

Before starting to use it I had a small test run, to check it satisfied all of my requirements, which are as follow:

### Software requirements - Server
<strong class="fa fa-check"></strong> : Can run on most web hosting services

<strong class="fa fa-check"></strong> : Easy to setup on the web server

<strong class="fa fa-check"></strong> : Secure, with minimal/no maintenance required

The previous requirements are met by the model of publication of **Pelican**, which generates once and for all a set of simple *static* files, which are then stored on the public web server. 

This doesn't require any support on the web hosting service, as the only functionality used is the ability to serve files. Any web server can do that.

It also fixes the problem of maintenance, as there is no dynamic, active content, there is no maintenance required. Same goes for security, the only security issue left are those of breach into the web server and file modifications. No risks either linked to database requests exploitation, nor vulnerabilities in any code being executed to serve the pages — as there is none.

I have already tried different CMS, the latest being **Joomla**. After a week or so of setup I had a basic theme in place, but after spending so much time just for getting everything up, I had lost the interest for writing. At that point I had not yet solved the problem of photo galleries… And then came the security / maintenance follow up which had to be done. In the end, that was way too much overhead for me.

### Software requirements - Client

<strong class="fa fa-check"></strong> : Dependencies to run the framework as minimal as possible, ideally cross-platform

My current main workstation is a MacBook Pro running MacOS X, at work I use Linux and Windows to play once in a while. Who knows what I will be running in five or ten years?

**Pelican** is written in python, in what seems to be a no-nonsense way. This is portable enough for me, and as I also have the sources of the framework itself, which means I can maintain it myself if required.

The web site being independent of the framework comes with the added bonus that if the framework breaks for any reason, I have some leeway, as the site will keep working as-is.

### Content management
<strong class="fa fa-check"></strong> : Content is easy to author

As the content (articles and galleries) are simple text files in directories, in any format among **MarkDown**, **ReStructuredText**, **AsciiDoc** or **HTML**, it is:

 1. Easy to import or export content to / from **Pelican**

 2. Easy to backup

 3. The format can be changed if the content of one specific article is better expressed in any of the supported input format.

Adding tags and metadata is straightforward too, using a simple “key: value” system at the top of each article.

### Photo Galleries
<strong class="fa fa-check"></strong> : Support photo galleries with per photo captions

Here I had to activate a plugin, which was straightforward enough. The only missing feature was caption support per image. I was able to modify the plugin to add this functionality within two days of work, without prior knowledge of **Pelican** and only a (very) limited proficiency of Python.

The last thing I had to do, was a small modification of the theme I chose, to add a nice slideshow view. I used, as recommended by the gallery plugin author, [colorbox](http://www.jacklmoore.com/colorbox/) to do so.

### Fine tuning
After being ensured I could easily and painlessly add the two main kind of content I intend to publish, I spent a bit of time to fine tune features of **Pelican**, in order to organise the generated content in a way which is most convenient.

### Conclusion
The installation – on my workstation – went like a breeze. I spent most of the time choosing a theme, and then tuning the configuration, which was a nice surprise.

All in all, I have spent about 4 days worth of hobby time to setup, choose a theme, customize it and modify the settings to my liking.

So now... All that is left is to write something!