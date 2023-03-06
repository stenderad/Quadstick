## text strings

FILE_LIST_HTML_HEADER = """<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
  <meta content="text/html; charset=ISO-8859-1" http-equiv="content-type">
  <title>QuadStick File Selector</title>
</head>
<body>
<div style="text-align: center;">QuadStick File Selector.<br>
</div>
<br>
<div style="text-align: center;">To activate a configuration file, start with a long sip on the side tube.
When the purple leds start flashing, move the joystick right or left to
select the desired file. Press the Lip button to select file.<br>
</div>
<br>
<table style="text-align: center; margin-left: auto; margin-right: auto; " border="1" cellpadding="2" cellspacing="2">
  <tbody>
    <tr>
      <td style="width: 110px; text-align: center;"><span style="font-weight: bold;">LED Pattern</span></td>
      <td style="width: 50px; text-align: center;"><span style="font-weight: bold;">File Number</span></td>
      <td style="width: 150px;"><span style="font-weight: bold;">CSV Filename</span></td>
      <td style="width: 400px;"><span style="font-weight: bold;">Configuration Filename</span></td>
    </tr>
"""

FILE_LIST_COL_0 = """    <tr>
      <td style="width: 110px; text-align: center;">"""
FILE_LIST_COL_1 = """</td>
      <td style="width: 50px; text-align: center;">"""
FILE_LIST_COL_2 = """</td>
      <td style="width: 150px;">"""
FILE_LIST_COL_3 = """</td>
      <td style="width: 400px;">"""
FILE_LIST_COL_4 = """</td>
    </tr>
"""

FILE_LIST_HTML_FOOTER = """  </tbody>
</table>
	<script type="text/javascript">
		window.print();
	</script>
</html>
"""

RED_DOT = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   width="5.011848mm"
   height="5.011848mm"
   viewBox="0 0 5.011848 5.011848"
   version="1.1"
   id="svg8"
   inkscape:version="0.92.0 r15299"
   sodipodi:docname=".../assets/img/red.svg">
  <defs
     id="defs2" />
  <sodipodi:namedview
     id="base"
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1.0"
     inkscape:pageopacity="0.0"
     inkscape:pageshadow="2"
     inkscape:zoom="97.294867"
     inkscape:cx="9.4712081"
     inkscape:cy="9.471209"
     inkscape:document-units="mm"
     inkscape:current-layer="layer1"
     showgrid="false"
     fit-margin-top="0"
     fit-margin-left="0"
     fit-margin-right="0"
     fit-margin-bottom="0"
     inkscape:window-width="3840"
     inkscape:window-height="2066"
     inkscape:window-x="3829"
     inkscape:window-y="-11"
     inkscape:window-maximized="1" />
  <metadata
     id="metadata5">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title></dc:title>
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <g
     inkscape:label="Layer 1"
     inkscape:groupmode="layer"
     id="layer1"
     transform="translate(-30.259026,-46.720856)">
    <circle
       style="fill:#ff0000;fill-opacity:1;stroke-width:0.26458332"
       id="path4487"
       cx="32.76495"
       cy="49.22678"
       r="2.505924" />
  </g>
</svg>
"""
BLUE_DOT = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   width="5.011848mm"
   height="5.011848mm"
   viewBox="0 0 5.011848 5.011848"
   version="1.1"
   id="svg8"
   inkscape:version="0.92.0 r15299"
   sodipodi:docname=".../assets/img/blue.svg">
  <defs
     id="defs2" />
  <sodipodi:namedview
     id="base"
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1.0"
     inkscape:pageopacity="0.0"
     inkscape:pageshadow="2"
     inkscape:zoom="97.294867"
     inkscape:cx="9.4712081"
     inkscape:cy="9.471209"
     inkscape:document-units="mm"
     inkscape:current-layer="layer1"
     showgrid="false"
     fit-margin-top="0"
     fit-margin-left="0"
     fit-margin-right="0"
     fit-margin-bottom="0"
     inkscape:window-width="3840"
     inkscape:window-height="2066"
     inkscape:window-x="3829"
     inkscape:window-y="-11"
     inkscape:window-maximized="1" />
  <metadata
     id="metadata5">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title></dc:title>
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <g
     inkscape:label="Layer 1"
     inkscape:groupmode="layer"
     id="layer1"
     transform="translate(-30.259026,-46.720856)">
    <circle
       style="fill:#0000ff;fill-opacity:1;stroke-width:0.26458332"
       id="path4487"
       cx="32.76495"
       cy="49.22678"
       r="2.505924" />
  </g>
</svg>
"""
GREY_DOT = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   width="5.011848mm"
   height="5.011848mm"
   viewBox="0 0 5.011848 5.011848"
   version="1.1"
   id="svg8"
   inkscape:version="0.92.0 r15299"
   sodipodi:docname=".../assets/img/grey.svg">
  <defs
     id="defs2" />
  <sodipodi:namedview
     id="base"
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1.0"
     inkscape:pageopacity="0.0"
     inkscape:pageshadow="2"
     inkscape:zoom="97.294867"
     inkscape:cx="9.4712081"
     inkscape:cy="9.471209"
     inkscape:document-units="mm"
     inkscape:current-layer="layer1"
     showgrid="false"
     fit-margin-top="0"
     fit-margin-left="0"
     fit-margin-right="0"
     fit-margin-bottom="0"
     inkscape:window-width="3840"
     inkscape:window-height="2066"
     inkscape:window-x="3829"
     inkscape:window-y="-11"
     inkscape:window-maximized="1" />
  <metadata
     id="metadata5">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title></dc:title>
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <g
     inkscape:label="Layer 1"
     inkscape:groupmode="layer"
     id="layer1"
     transform="translate(-30.259026,-46.720856)">
    <circle
       style="fill:#404040;fill-opacity:1;stroke-width:0.26458332"
       id="path4487"
       cx="32.76495"
       cy="49.22678"
       r="2.505924" />
  </g>
</svg>
"""
PURPLE_DOT = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   width="5.011848mm"
   height="5.011848mm"
   viewBox="0 0 5.011848 5.011848"
   version="1.1"
   id="svg8"
   inkscape:version="0.92.0 r15299"
   sodipodi:docname=".../assets/img/purple.svg">
  <defs
     id="defs2" />
  <sodipodi:namedview
     id="base"
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1.0"
     inkscape:pageopacity="0.0"
     inkscape:pageshadow="2"
     inkscape:zoom="97.294867"
     inkscape:cx="9.4712081"
     inkscape:cy="9.471209"
     inkscape:document-units="mm"
     inkscape:current-layer="layer1"
     showgrid="false"
     fit-margin-top="0"
     fit-margin-left="0"
     fit-margin-right="0"
     fit-margin-bottom="0"
     inkscape:window-width="3840"
     inkscape:window-height="2066"
     inkscape:window-x="3829"
     inkscape:window-y="-11"
     inkscape:window-maximized="1" />
  <metadata
     id="metadata5">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title></dc:title>
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <g
     inkscape:label="Layer 1"
     inkscape:groupmode="layer"
     id="layer1"
     transform="translate(-30.259026,-46.720856)">
    <circle
       style="fill:#ff00ff;fill-opacity:1;stroke-width:0.26458332"
       id="path4487"
       cx="32.76495"
       cy="49.22678"
       r="2.505924" />
  </g>
</svg>
"""

maxPatterns = 35 #(was 33, but this should work)
cols = 5
LED_PATTERN = {}

for i in range(maxPatterns):
   baseColor = "grey"
   if i >=19: baseColor = "blue"
   if i >= 29: baseColor ="red"

   pat = [baseColor for j in range(cols)]
   pat[i % cols] = "purple"

   if((i >= 4 and i < 9) or (i >= 24 and i < 29)): pat[-1] = "purple"
   if((i >= 9 and i < 14) or (i >= 19 and i < 24)): pat[-1] = "blue"
   if((i >= 14 and i < 19) ): pat[-1] = "red "

   LED_PATTERN[i+1] = "".join(['<img src=".../assets/img/' + color + '.svg">' for color in pat]) #keeping 1-indexing support

# LED_PATTERN = { #NO
#     1:  '<img src=".../assets/img/purple.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg">',
#     2:  '<img src=".../assets/img/grey.svg"><img src=".../assets/img/purple.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg">',
#     3:  '<img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/purple.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg">',
#     4:  '<img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/purple.svg"><img src=".../assets/img/grey.svg">',
#     5:  '<img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/purple.svg">',

#     6:  '<img src=".../assets/img/purple.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/purple.svg">',
#     7:  '<img src=".../assets/img/grey.svg"><img src=".../assets/img/purple.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/purple.svg">',
#     8:  '<img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/purple.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/purple.svg">',
#     9:  '<img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/purple.svg"><img src=".../assets/img/purple.svg">',

#    10:  '<img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/blue.svg">',
#    11:  '<img src=".../assets/img/purple.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/blue.svg">',
#    12:  '<img src=".../assets/img/grey.svg"><img src=".../assets/img/purple.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/blue.svg">',
#    13:  '<img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/purple.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/blue.svg">',
#    14:  '<img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/purple.svg"><img src=".../assets/img/blue.svg">',

#    15:  '<img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/red.svg">',
#    16:  '<img src=".../assets/img/purple.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/red.svg">',
#    17:  '<img src=".../assets/img/grey.svg"><img src=".../assets/img/purple.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/red.svg">',
#    18:  '<img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/purple.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/red.svg">',
#    19:  '<img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/grey.svg"><img src=".../assets/img/purple.svg"><img src=".../assets/img/red.svg">',

#    20:  '<img src=".../assets/img/blue.svg"><img src=".../assets/img/blue.svg"><img src=".../assets/img/blue.svg"><img src=".../assets/img/blue.svg"><img src=".../assets/img/blue.svg">',
#    21:  '<img src=".../assets/img/purple.svg"><img src=".../assets/img/blue.svg"><img src=".../assets/img/blue.svg"><img src=".../assets/img/blue.svg"><img src=".../assets/img/blue.svg">',
#    22:  '<img src=".../assets/img/blue.svg"><img src=".../assets/img/purple.svg"><img src=".../assets/img/blue.svg"><img src=".../assets/img/blue.svg"><img src=".../assets/img/blue.svg">',
#    23:  '<img src=".../assets/img/blue.svg"><img src=".../assets/img/blue.svg"><img src=".../assets/img/purple.svg"><img src=".../assets/img/blue.svg"><img src=".../assets/img/blue.svg">',
#    24:  '<img src=".../assets/img/blue.svg"><img src=".../assets/img/blue.svg"><img src=".../assets/img/blue.svg"><img src=".../assets/img/purple.svg"><img src=".../assets/img/blue.svg">',

#    25:  '<img src=".../assets/img/blue.svg"><img src=".../assets/img/blue.svg"><img src=".../assets/img/blue.svg"><img src=".../assets/img/blue.svg"><img src=".../assets/img/purple.svg">',
#    26:  '<img src=".../assets/img/purple.svg"><img src=".../assets/img/blue.svg"><img src=".../assets/img/blue.svg"><img src=".../assets/img/blue.svg"><img src=".../assets/img/purple.svg">',
#    27:  '<img src=".../assets/img/blue.svg"><img src=".../assets/img/purple.svg"><img src=".../assets/img/blue.svg"><img src=".../assets/img/blue.svg"><img src=".../assets/img/purple.svg">',
#    28:  '<img src=".../assets/img/blue.svg"><img src=".../assets/img/blue.svg"><img src=".../assets/img/purple.svg"><img src=".../assets/img/blue.svg"><img src=".../assets/img/purple.svg">',
#    29:  '<img src=".../assets/img/blue.svg"><img src=".../assets/img/blue.svg"><img src=".../assets/img/blue.svg"><img src=".../assets/img/purple.svg"><img src=".../assets/img/purple.svg">',
   
#    30:  '<img src=".../assets/img/red.svg"><img src=".../assets/img/red.svg"><img src=".../assets/img/red.svg"><img src=".../assets/img/red.svg"><img src=".../assets/img/purple.svg">', #guessing this is a bug (duplicates here)
#    30:  '<img src=".../assets/img/red.svg"><img src=".../assets/img/red.svg"><img src=".../assets/img/red.svg"><img src=".../assets/img/red.svg"><img src=".../assets/img/purple.svg">',
#    31:  '<img src=".../assets/img/purple.svg"><img src=".../assets/img/red.svg"><img src=".../assets/img/red.svg"><img src=".../assets/img/red.svg"><img src=".../assets/img/red.svg">',
#    32:  '<img src=".../assets/img/red.svg"><img src=".../assets/img/purple.svg"><img src=".../assets/img/red.svg"><img src=".../assets/img/red.svg"><img src=".../assets/img/red.svg">',
# }