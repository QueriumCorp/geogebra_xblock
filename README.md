Geogebra xBlock
===============
A simple edX xBlock wrapper around the GeoGebra graphing calculator widget. Note that the calculator is subject to GeoGebra's licensing requirements.

Documentation
-------------
This XBlock can be installed like most XBlocks. See the 
[documentation for how to add custom XBlocks to your system](https://edx.readthedocs.io/projects/edx-installing-configuring-and-running/en/latest/configuration/install_xblock.html).

Once you have installed the block and added it to your course's advanced module list, go to [Geogebra](https://geogebra.com/)
and create your desired graph.

**Do not sign into Geogebra.** You cannot export a file if you're signed in. **Resize your window to be small so that 
the viewport of the problem better matches the size of an XBlock on a unit page.** Otherwise you may end up with a 
weird viewport that doesn't show your graph at all.

Open the sidebar and save your graph. Take this file, and upload it to your course in studio under Content->Files and Uploads.

Once uploaded, copy the resulting LMS link. Add the Geogebra XBlock to your desired Unit, and then edit its properties.
Paste the LMS link into the provided field. **Note that you may have to add `http://` or `https://` to the front of the URL
as the studio may not copy it for you.**

Preview the block on the LMS to verify its appearance. You may discover you need to resize, pan, and re-export if the
viewport isn't quite right. Otherwise, you should be good to go!

Further documentation for all Rover source code is now located in [Read The Docs](http://readthedocs.roverbyopenstax.org/)

Developer Notes
-------------
3-June-2020 (McDaniel): Python3 / Juniper.rc3 upgrade changes. These are potentially not backward compatible.
As a precautionary measure I've created a new branch, juniper.rc3, and made this the default repo branch.
