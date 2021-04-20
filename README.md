<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="generator" content="RocketCake">
	<title></title>
	<link rel="stylesheet" type="text/css" href="index_html.css">
</head>
<body>
<div class="textstyle1">
<span class="textstyle2">Module to use a simple stepmotor with RPI &amp; python.</span><span class="textstyle3"><br/><br/>How to use:<br/>- Copy the motors folder to the folder of your python file<br/>- use &quot;from motors.motor import *&quot;<br/>- Create object of type Motor(name). Example: my_motor = Motor(&quot;Funcky motor&quot;)<br/>- Change attributes as desired (or use defaults - see table below)<br/>- use the method init() to initialize desired ports (or defaults) once<br/>- use the method move(steps, direction) to move the motor (see below)<br/><br/></span>  <table id="table_67c5a5c8" cellpadding="3" cellspacing="1" >
	<tr>
		<td width="33%" height="21px" style="vertical-align: top; overflow:hidden; ">    <div id="cell_15ec8179">
      <div class="textstyle1">
        <span class="textstyle3">Attribute</span>
        </div>
      </div>
		</td>
		<td width="33%" height="21px" style="vertical-align: top; overflow:hidden; ">    <div id="cell_5d6e8fc5">
      <div class="textstyle1">
        <span class="textstyle3">Defaults</span>
        </div>
      </div>
		</td>
		<td width="33%" height="21px" style="vertical-align: top; overflow:hidden; ">    <div id="cell_4a8d779a">
      <div class="textstyle1">
        <span class="textstyle3">Description</span>
        </div>
      </div>
		</td>
	</tr>
	<tr>
		<td width="33%" height="96px" style="vertical-align: top; overflow:hidden; ">    <div id="cell_5f0116bc">
      <div class="textstyle1">
        <span class="textstyle3">f_seq</span>
        </div>
      </div>
		</td>
		<td width="33%" height="96px" style="vertical-align: top; overflow:hidden; ">    <div id="cell_3984735a">
      <div class="textstyle1">
        <span class="textstyle3">[<br/>            [1, 1, 0, 0],<br/>            [0, 1, 1, 0],<br/>            [0, 0, 1, 1],<br/>            [1, 0, 0, 1],<br/>            [0, 0, 0, 0]]</span>
        </div>
      </div>
		</td>
		<td width="33%" height="96px" style="vertical-align: top; overflow:hidden; ">    <div id="cell_11b4f6cd">
      <div class="textstyle1">
        <span class="textstyle3">Forward sequence for 1 step.</span>
        </div>
      </div>
		</td>
	</tr>
	<tr>
		<td width="33%" height="96px" style="vertical-align: top; overflow:hidden; ">    <div id="cell_10e32479">
      <div class="textstyle1">
        <span class="textstyle3">b_sec</span>
        </div>
      </div>
		</td>
		<td width="33%" height="96px" style="vertical-align: top; overflow:hidden; ">    <div id="cell_4915d68c">
      <div class="textstyle1">
        <span class="textstyle3">[<br/>            [1, 1, 0, 0],<br/>            [1, 0, 0, 1],<br/>            [0, 0, 1, 1],<br/>            [0, 1, 1, 0],<br/>            [0, 0, 0, 0]]</span>
        </div>
      </div>
		</td>
		<td width="33%" height="96px" style="vertical-align: top; overflow:hidden; ">    <div id="cell_23932c22">
      <div class="textstyle1">
        <span class="textstyle3">Backward sequence for 1 step.</span>
        </div>
      </div>
		</td>
	</tr>
	<tr>
		<td width="33%" height="21px" style="vertical-align: top; overflow:hidden; ">    <div id="cell_3dae042d">
      <div class="textstyle1">
        <span class="textstyle3">used_pins</span>
        </div>
      </div>
		</td>
		<td width="33%" height="21px" style="vertical-align: top; overflow:hidden; ">    <div id="cell_30ba40bc">
      <div class="textstyle1">
        <span class="textstyle3">[22, 23, 24, 25]</span>
        </div>
      </div>
		</td>
		<td width="33%" height="21px" style="vertical-align: top; overflow:hidden; ">    <div id="cell_65b495a2">
      <div class="textstyle1">
        <span class="textstyle3">GPIO BCM numbers</span>
        </div>
      </div>
		</td>
	</tr>
	<tr>
		<td width="33%" height="28px" style="vertical-align: top; overflow:hidden; ">    <div id="cell_64f37254">
      <div class="textstyle1">
        <span class="textstyle3">debug</span>
        </div>
      </div>
		</td>
		<td width="33%" height="28px" style="vertical-align: top; overflow:hidden; ">    <div id="cell_7912be8c">
      <div class="textstyle1">
        <span class="textstyle3">False</span>
        </div>
      </div>
		</td>
		<td width="33%" height="28px" style="vertical-align: top; overflow:hidden; ">    <div id="cell_780a4201">
      <div class="textstyle1">
        <span class="textstyle3">When set to True debug information will be printed</span>
        </div>
      </div>
		</td>
	</tr>
	<tr>
		<td width="33%" height="18px" >
		</td>
		<td width="33%" height="18px" >
		</td>
		<td width="33%" height="18px" >
		</td>
	</tr>
    </table>
  <span class="textstyle3"><br/><br/><br/><br/><br/></span>
  <table id="table_49364a9" cellpadding="3" cellspacing="1" >
	<tr>
		<td width="33%" height="21px" style="vertical-align: top; overflow:hidden; ">    <div id="cell_54a1c552">
      <div class="textstyle1">
        <span class="textstyle3">Method</span>
        </div>
      </div>
		</td>
		<td width="33%" height="21px" style="vertical-align: top; overflow:hidden; ">    <div id="cell_25ee779">
      <div class="textstyle1">
        <span class="textstyle3">Parameters</span>
        </div>
      </div>
		</td>
		<td width="33%" height="21px" style="vertical-align: top; overflow:hidden; ">    <div id="cell_555429bd">
      <div class="textstyle1">
        <span class="textstyle3">Function</span>
        </div>
      </div>
		</td>
	</tr>
	<tr>
		<td width="33%" height="21px" style="vertical-align: top; overflow:hidden; ">    <div id="cell_46617e6a">
      <div class="textstyle1">
        <span class="textstyle3">init()</span>
        </div>
      </div>
		</td>
		<td width="33%" height="21px" style="vertical-align: top; overflow:hidden; ">    <div id="cell_4146eb3e">
      <div class="textstyle1">
        <span class="textstyle3">none</span>
        </div>
      </div>
		</td>
		<td width="33%" height="21px" style="vertical-align: top; overflow:hidden; ">    <div id="cell_7d1752af">
      <div class="textstyle1">
        <span class="textstyle3">Initialize ports</span>
        </div>
      </div>
		</td>
	</tr>
	<tr>
		<td width="33%" height="79px" style="vertical-align: top; overflow:hidden; ">    <div id="cell_1fd9e86b">
      <div class="textstyle1">
        <span class="textstyle3">move(steps, direction)</span>
        </div>
      </div>
		</td>
		<td width="33%" height="79px" style="vertical-align: top; overflow:hidden; ">    <div id="cell_594a0821">
      <div class="textstyle1">
        <span class="textstyle3">steps: int<br/>direction: bool</span>
        </div>
      </div>
		</td>
		<td width="33%" height="79px" style="vertical-align: top; overflow:hidden; ">    <div id="cell_4bfff64d">
      <div class="textstyle1">
        <span class="textstyle3">Moves the number of steps in the set direction<br/>example:<br/>move(8,True) will move 8 steps in forward direction</span>
        </div>
      </div>
		</td>
	</tr>
	<tr>
		<td width="33%" height="28px" style="vertical-align: top; overflow:hidden; ">    <div id="cell_6a5612c4">
      <div class="textstyle1">
        <span class="textstyle3">hello()</span>
        </div>
      </div>
		</td>
		<td width="33%" height="28px" style="vertical-align: top; overflow:hidden; ">    <div id="cell_7a1f4a7c">
      <div class="textstyle1">
        <span class="textstyle3">none</span>
        </div>
      </div>
		</td>
		<td width="33%" height="28px" style="vertical-align: top; overflow:hidden; ">    <div id="cell_365f079f">
      <div class="textstyle1">
        <span class="textstyle3">will print &quot;hello from &lt;motor_name&gt;&quot;</span>
        </div>
      </div>
		</td>
	</tr>
	<tr>
		<td width="33%" height="21px" >
		</td>
		<td width="33%" height="21px" >
		</td>
		<td width="33%" height="21px" >
		</td>
	</tr>
	<tr>
		<td width="33%" height="18px" >
		</td>
		<td width="33%" height="18px" >
		</td>
		<td width="33%" height="18px" >
		</td>
	</tr>
    </table>
  <span class="textstyle3"><br/><br/></span>
  </div>
</body>
</html>
