<?php

/**************************************************************************\
* Viewpart CMSimple plugin 0.01
* http://cmsimple.cycu.org
* Copyright (C) 2013 by Chiaming Yen
* ------------------------------------------------------------------------
*  This program is free software; you can redistribute it and/or 
*  modify it under the terms of the GNU General Public License Version 2
*  as published by the Free Software Foundation; only version 2
*  of the License, no later version. 
* 
*  This program is distributed in the hope that it will be useful,
*  but WITHOUT ANY WARRANTY; without even the implied warranty of
*  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
*  GNU General Public License for more details.
* 
*  You should have received a copy of the GNU General Public License
*  Version 2 along with this program; if not, write to the Free Software
*  Foundation, Inc., 59 Temple Place - Suite 330, Boston,
*  MA  02111-1307, USA. 
\**************************************************************************/

function viewpartMain($file){
// 假如要改為 GET 取得零件名稱 nutcracker.stl
//$file = $_GET["file"];
    $output = <<<EOF
        <style type="text/css">
        body{
            background-color:AntiqueWhite;
        }
        #webgl {
            background-color:white;
            border:solid 1px black;
            width:640px;
            height:480px;
        }
        div.centered{
            display:block;

            width:350px;z-index: 21;
            background-color: MintCream;
            border: 0px solid black;
        }
    </style>
    <script src="jscript/partview/Three.js"></script>
    <script src="jscript/partview/RequestAnimationFrame.js"></script>
    <script src="jscript/partview/objstl.js"></script>
    </head>
    <body>
    <script>
    window.onload = function ()
    {
        load();
EOF;

$output .= "example(\"downloads/".$file."\");";

$output .= <<<EOF
    }
    </script>
    <div id="centered" class="centered">
    </div>
    <div id="webgl" oncontextmenu="return false;">
    </div>
EOF;
    return $output;
}
?>