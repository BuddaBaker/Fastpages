---
keywords: fastai
title: Note Template
comments: true
nb_path: _notebooks/2022-12-1-notetemplate.ipynb
layout: notebook
---

<!--
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: _notebooks/2022-12-1-notetemplate.ipynb
-->

<div class="container" id="notebook-container">
        
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Take-some-additional-notes-that-you-would-like-here-for-3.12-and-3.13.-We-will-be-looking-for-additional-notes-from-the-presentation.">Take some additional notes that you would like here for 3.12 and 3.13. We will be looking for additional notes from the presentation.<a class="anchor-link" href="#Take-some-additional-notes-that-you-would-like-here-for-3.12-and-3.13.-We-will-be-looking-for-additional-notes-from-the-presentation."> </a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>ADDITIONAL NOTES:</p>
<ul>
<li>New parameters and arguments give a different output</li>
<li>You call a function, define it then call it then put in your parameters</li>
<li>Insert values into a function for a certain output</li>
<li>Splice function splits up different parts of a string</li>
<li>Its a pain to rewrite code multiple times rather than defining it as a function</li>
<li>Modularity is needed for large coding projects</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="What-are-procedures?">What are procedures?<a class="anchor-link" href="#What-are-procedures?"> </a></h1><p><strong>Fill in the blanks please:</strong></p>
<p>Procedure:  Methods or functions</p>
<p>Parameters: Input values of a procedure</p>
<p>Arguments: Specify value of values when procedure is called</p>
<p>Modularity: Executing the code multiple times</p>
<p>Procedural Abstraction: Provides a name for a process</p>
<p>What are some other names for procedures?: 
Function</p>
<p>Why are procedures effective?: 
They can repeat a code multiple times without rewriting the entire code again
You can also alter the result without channging the code</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Challenge-1-below:-Add-the-command-that-will-call-the-procedure."><mark>Challenge 1</mark> below: Add the command that will <strong>call</strong> the procedure.<a class="anchor-link" href="#Challenge-1-below:-Add-the-command-that-will-call-the-procedure."> </a></h2>
</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">decimal</span> <span class="o">=</span> <span class="mi">8</span>
<span class="n">binary</span> <span class="o">=</span> <span class="mi">0</span>
<span class="n">ctr</span> <span class="o">=</span> <span class="mi">0</span>
<span class="n">new</span> <span class="o">=</span> <span class="n">decimal</span> 

<span class="k">while</span><span class="p">(</span><span class="n">new</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">):</span>
    <span class="n">binary</span> <span class="o">=</span> <span class="p">((</span><span class="n">new</span><span class="o">%</span><span class="k">2</span>)*(10**ctr)) + binary
    <span class="n">new</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">new</span><span class="o">/</span><span class="mi">2</span><span class="p">)</span>
    <span class="n">ctr</span> <span class="o">+=</span> <span class="mi">1</span>

<span class="c1">#output the result       </span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Binary of&quot;</span><span class="p">,</span> <span class="n">decimal</span><span class="p">,</span> <span class="s2">&quot; is:&quot;</span><span class="p">,</span> <span class="n">binary</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>Binary of 8  is: 1000
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Challenge-2-below:-Complete-the-Min-and-Max-procedure-in-either-JavaScript-and-Python-using-the-instructions-from-the-JavaScript-page.-(JavaScript-will-get-you-a-extra-0.1)"><mark>Challenge 2</mark> below: Complete the Min and Max procedure in either JavaScript and Python using the instructions from the JavaScript page. (JavaScript will get you a extra 0.1)<a class="anchor-link" href="#Challenge-2-below:-Complete-the-Min-and-Max-procedure-in-either-JavaScript-and-Python-using-the-instructions-from-the-JavaScript-page.-(JavaScript-will-get-you-a-extra-0.1)"> </a></h2>
</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">const</span> <span class="n">a</span> <span class="o">=</span> <span class="mi">30</span>
<span class="n">const</span> <span class="n">b</span> <span class="o">=</span> <span class="mi">10</span>
<span class="k">if</span> <span class="p">(</span><span class="n">a</span> <span class="o">&gt;</span> <span class="n">b</span><span class="p">)</span> <span class="p">{</span>
    <span class="n">console</span><span class="o">.</span><span class="n">log</span><span class="p">(</span><span class="s2">&quot;Higher&quot;</span><span class="p">)</span>
<span class="p">}</span> <span class="k">else</span> <span class="p">{</span>
    <span class="n">console</span><span class="o">.</span><span class="n">log</span><span class="p">(</span><span class="s2">&quot;Lower&quot;</span><span class="p">)</span>
<span class="p">}</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>higher
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Homework/Hacks:-For-the-hw,-you-have-two-options,-easy-or-hard.-The-easy-hack-is-for-a-2.7-+-extra-work-for-the-full-3.-The-easy-hack-is-simply-creating-your-own-procedure-with-your-own-creativity.-Since-there-is-a-lot-of-leeway-for-this-one,-you-must-do-additional-work-to-get-a-3.-For-the-hard-hack,-below-is-the-start-to-a-character-to-binary-convertor.-This-is-just-a-template,-but-the-goal-is-to-translate-&quot;APCSP&quot;-into-binary.-You-can-delete-the-existing-code-if-you-want.-The-only-contraint-is-that-you-must-use-a-procedure.-Doing-this-will-get-you-a-3."><mark>Homework/Hacks</mark>: For the hw, you have two options, easy or hard. The easy hack is for a 2.7 + extra work for the full 3. The easy hack is simply creating your own procedure with your own creativity. Since there is a lot of leeway for this one, you must do additional work to get a 3. For the hard hack, below is the start to a character to binary convertor. This is just a template, but the goal is to translate "APCSP" into binary. You can delete the existing code if you want. The only contraint is that you must use a procedure. Doing this will get you a 3.<a class="anchor-link" href="#Homework/Hacks:-For-the-hw,-you-have-two-options,-easy-or-hard.-The-easy-hack-is-for-a-2.7-+-extra-work-for-the-full-3.-The-easy-hack-is-simply-creating-your-own-procedure-with-your-own-creativity.-Since-there-is-a-lot-of-leeway-for-this-one,-you-must-do-additional-work-to-get-a-3.-For-the-hard-hack,-below-is-the-start-to-a-character-to-binary-convertor.-This-is-just-a-template,-but-the-goal-is-to-translate-&quot;APCSP&quot;-into-binary.-You-can-delete-the-existing-code-if-you-want.-The-only-contraint-is-that-you-must-use-a-procedure.-Doing-this-will-get-you-a-3."> </a></h2>
</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">math</span>

<span class="k">def</span> <span class="nf">charToBinary</span><span class="p">(</span><span class="n">x</span><span class="p">):</span>
    <span class="n">l</span><span class="p">,</span><span class="n">m</span> <span class="o">=</span> <span class="p">[],[]</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">x</span><span class="p">:</span>
        <span class="n">l</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">ord</span><span class="p">(</span><span class="n">i</span><span class="p">))</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">l</span><span class="p">:</span>
        <span class="n">m</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">int</span><span class="p">(</span><span class="nb">bin</span><span class="p">(</span><span class="n">i</span><span class="p">[</span><span class="mi">2</span><span class="p">:])))</span>
    <span class="k">return</span> <span class="n">m</span>
<span class="nb">print</span><span class="p">(</span><span class="n">charToBinary</span><span class="p">(</span><span class="s2">&quot;APCSP&quot;</span><span class="p">))</span>
    


<span class="c1"># The output shown below is the output you are supposed to get</span>

<span class="c1">#import math</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_text output_error">
<pre>
<span class="ansi-red-fg">---------------------------------------------------------------------------</span>
<span class="ansi-red-fg">TypeError</span>                                 Traceback (most recent call last)
<span class="ansi-green-intense-fg ansi-bold">/home/prasithchilla/Fastpages/_notebooks/2022-12-1-notetemplate.ipynb Cell 10</span> in <span class="ansi-cyan-fg">&lt;cell line: 10&gt;</span><span class="ansi-blue-fg">()</span>
<span class="ansi-green-intense-fg ansi-bold">      &lt;a href=&#39;vscode-notebook-cell://wsl%2Bubuntu-22.04/home/prasithchilla/Fastpages/_notebooks/2022-12-1-notetemplate.ipynb#X11sdnNjb2RlLXJlbW90ZQ%3D%3D?line=7&#39;&gt;8&lt;/a&gt;</span>         m.append(int(bin(i[2:])))
<span class="ansi-green-intense-fg ansi-bold">      &lt;a href=&#39;vscode-notebook-cell://wsl%2Bubuntu-22.04/home/prasithchilla/Fastpages/_notebooks/2022-12-1-notetemplate.ipynb#X11sdnNjb2RlLXJlbW90ZQ%3D%3D?line=8&#39;&gt;9&lt;/a&gt;</span>     return m
<span class="ansi-green-fg">---&gt; &lt;a href=&#39;vscode-notebook-cell://wsl%2Bubuntu-22.04/home/prasithchilla/Fastpages/_notebooks/2022-12-1-notetemplate.ipynb#X11sdnNjb2RlLXJlbW90ZQ%3D%3D?line=9&#39;&gt;10&lt;/a&gt;</span> print(charToBinary(&#34;APCSP&#34;))

<span class="ansi-green-intense-fg ansi-bold">/home/prasithchilla/Fastpages/_notebooks/2022-12-1-notetemplate.ipynb Cell 10</span> in <span class="ansi-cyan-fg">charToBinary</span><span class="ansi-blue-fg">(x)</span>
<span class="ansi-green-intense-fg ansi-bold">      &lt;a href=&#39;vscode-notebook-cell://wsl%2Bubuntu-22.04/home/prasithchilla/Fastpages/_notebooks/2022-12-1-notetemplate.ipynb#X11sdnNjb2RlLXJlbW90ZQ%3D%3D?line=5&#39;&gt;6&lt;/a&gt;</span>     l.append(ord(i))
<span class="ansi-green-intense-fg ansi-bold">      &lt;a href=&#39;vscode-notebook-cell://wsl%2Bubuntu-22.04/home/prasithchilla/Fastpages/_notebooks/2022-12-1-notetemplate.ipynb#X11sdnNjb2RlLXJlbW90ZQ%3D%3D?line=6&#39;&gt;7&lt;/a&gt;</span> for i in l:
<span class="ansi-green-fg">----&gt; &lt;a href=&#39;vscode-notebook-cell://wsl%2Bubuntu-22.04/home/prasithchilla/Fastpages/_notebooks/2022-12-1-notetemplate.ipynb#X11sdnNjb2RlLXJlbW90ZQ%3D%3D?line=7&#39;&gt;8&lt;/a&gt;</span>     m.append(int(bin(i[2:])))
<span class="ansi-green-intense-fg ansi-bold">      &lt;a href=&#39;vscode-notebook-cell://wsl%2Bubuntu-22.04/home/prasithchilla/Fastpages/_notebooks/2022-12-1-notetemplate.ipynb#X11sdnNjb2RlLXJlbW90ZQ%3D%3D?line=8&#39;&gt;9&lt;/a&gt;</span> return m

<span class="ansi-red-fg">TypeError</span>: &#39;int&#39; object is not subscriptable</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

</div>
 

